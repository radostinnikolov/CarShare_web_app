import { html, render, nothing } from "./lib.js";
import { get } from "./api.js";
import { createSubmitHandler } from "./utils.js";
window.addEventListener("load", (event) => {
    const main = document.getElementById('main')


    const pageTemplate = (func) => html`
    <label for="from_city">From where?:</label>
    <select id="from_city" name="from" form="search">
    <option value=>---</option>
    <option value=1>Sofia</option>
    <option value=2>Plovdiv</option>
    <option value=3>Varna</option>
    <option value=4>Burgas</option>
    <option value=5>Ruse</option>
    <option value=6>Veliko Tarnovo</option>
    <option value=7>Stara Zagora</option>
    <option value=8>Blagoevgrad</option>
    </select>

    <br>

    <label for="to_city">To where?:</label>
    <select id="to_city" name="to" form="search">
    <option value=>---</option>
    <option value=1>Sofia</option>
    <option value=2>Plovdiv</option>
    <option value=3>Varna</option>
    <option value=4>Burgas</option>
    <option value=5>Ruse</option>
    <option value=6>Veliko Tarnovo</option>
    <option value=7>Stara Zagora</option>
    <option value=8>Blagoevgrad</option>
    </select>


    <form @submit=${func} id="search">
    <label for="start">Start date:</label>

    <input type="date" id="start" name="date"
       value="${new Date().toISOString().split('T')[0]}"
       min="2022-01-01" max="2024-12-31">
    <input type="submit">
    </form>

    <br>

    <div id="result">

    </div>`


    render(pageTemplate(onSearch), main);


    const resultTemplate = (items) => html`
${!items.length ? html`No transports fit your criteria!` : html`<table class="w3-table-all w3-hoverable w3-large w3-bordered w3-centered">
<tr class="w3-gray">
    <th>From:</th>
    <th>To:</th>
    <th>Driver:</th>
    <th>Date:</th>
    <th>Time:</th>
    <th class="descr">Description:</th>
    <th>Total seats:</th>
    <th>Taken seats:</th>
    <th>Status:</th>
    <th></th>
</tr>
${items.map(item => rowTemplate(item))}</table>`}`


    const rowTemplate = (item) => html`
<tr>
                <td>${item.from_city_name}</td>
                <td>${item.to_city_name}</td>
                <td>
                    <a href="/profile/details/${item.driver_id}">${item.driver_name}</a>
                </td>
                <td>${item.date}</td>
                <td>${item.time}</td>
                <td class="descr">${item.description}</td>
                <td>${item.total_seats}</td>
                <td>${item.passengers_count}</td>
                <td>${item.status}</td>
                <td><a href="/transports/details/${item.id}">Details</a></td>
            </tr>`

    // export async function showSearch(ctx) {

    //     ctx.render(pageTemplate(onSearch))

    async function onSearch(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData);
        const items = await get(`/api/transports/?from=${data.from}&to=${data.to}&date=${data.date}`);
        const parent = document.getElementById('result')
        render(resultTemplate(items), parent)
    }
});



