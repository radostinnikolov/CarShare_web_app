import {html, render, nothing} from "./lib.js";
import {get} from "./api.js";


window.addEventListener("load", (event) => {
    const main = document.getElementById('main')


    const pageTemplate = (func) => html`
        
                    <div class="w3-row w3-section w3-center">
                        <h1>Search for transport:</h1>
                    </div>
                    <form @submit=${func} id="search">
                        <p><label for="from_city">From where?:</label>
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
                            </select></p>


                        <br>
                        <p><label for="to_city">To where?:</label>
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
                            </select></p>

                        <p><label for="start">Start date:</label>

                            <input type="date" id="start" name="date"
                                   value="${new Date().toISOString().split('T')[0]}"
                                   min="2022-01-01" max="2024-12-31"></p>
                        
                        <p><label for="time">Time:</label>
                            <select id="time" name="time" form="search">
                                <option value=>---</option>
                                <option value='00:00:00'>00:00</option>
                                <option value='01:00:00'>01:00</option>
                                <option value='02:00:00'>02:00</option>
                                <option value='03:00:00'>03:00</option>
                                <option value='04:00:00'>04:00</option>
                                <option value='05:00:00'>05:00</option>
                                <option value='06:00:00'>06:00</option>
                                <option value='07:00:00'>07:00</option>
                                <option value='08:00:00'>08:00</option>
                                <option value='09:00:00'>09:00</option>
                                <option value='10:00:00'>10:00</option>
                                <option value='11:00:00'>11:00</option>
                                <option value='12:00:00'>12:00</option>
                                <option value='13:00:00'>13:00</option>
                                <option value='14:00:00'>14:00</option>
                                <option value='15:00:00'>15:00</option>
                                <option value='16:00:00'>16:00</option>
                                <option value='17:00:00'>17:00</option>
                                <option value='18:00:00'>18:00</option>
                                <option value='19:00:00'>19:00</option>
                                <option value='20:00:00'>20:00</option>
                                <option value='21:00:00'>21:00</option>
                                <option value='22:00:00'>22:00</option>
                                <option value='23:00:00'>23:00</option>
                            </select></p>
                        
                        <p><label for="status">Status:</label>
                            <select id="status" name="status" form="search">
                                <option value=>---</option>
                                <option value='ACTIVE'>Active</option>
                                <option value='FINISHED'>Finished</option>
                            </select></p>
                        
                        <div class="w3-row w3-section w3-center">
                            <button class="w3-btn w3-teal">Submit</button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
        <div id="result">
        </div>`


    render(pageTemplate(onSearch), main);


    const resultTemplate = (items) => html`
        ${!items.length ? html`No transports fit your criteria!` : html`
            <table class="w3-table-all w3-large w3-bordered w3-centered w3-gray">
                <tr class="w3-teal">
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
                ${items.map(item => rowTemplate(item))}
            </table>`}`


    const rowTemplate = (item) => html`
        <tr>
            <td>${item.from_city_name}</td>
            <td>${item.to_city_name}</td>
            <td>
                <a href="/profile/details/${item.driver_id}">${item.driver_first_name} ${item.driver_last_name}</a>
            </td>
            <td>${item.date}</td>
            <td>${item.time}</td>
            <td class="descr">${item.description}</td>
            <td>${item.total_seats}</td>
            <td>${item.passengers_count}</td>
            <td>${item.status}</td>
            <td><a class="w3-btn w3-teal" href="/transports/details/${item.id}">Details</a></td>
        </tr>`

    // export async function showSearch(ctx) {

    //     ctx.render(pageTemplate(onSearch))

    async function onSearch(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData);
        const items = await get(`/api/transports/?from=${data.from}&to=${data.to}&date=${data.date}&time=${data.time}&status=${data.status}`);
        const parent = document.getElementById('result')
        render(resultTemplate(items), parent)
    }
});



