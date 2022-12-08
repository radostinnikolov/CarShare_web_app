from django import forms

from carshare_v2.transports.models import Transport


class CreateTransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['from_city', 'to_city', 'date', 'time', 'description', 'total_seats', 'chatroom_name']
        widgets = {
            'description': forms.Textarea(),
            'date': forms.SelectDateWidget(),
            'time': forms.DateTimeInput()
        }


class EditTransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['from_city', 'to_city', 'date', 'time', 'description', 'total_seats', 'status', 'chatroom_name']
        widgets = {
            'description': forms.Textarea(),
            'date': forms.SelectDateWidget(),
            'time': forms.DateTimeInput()
        }


class DeleteTransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ()
