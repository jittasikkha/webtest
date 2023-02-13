from django import forms
from .models import File , Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name' , 'role', 'province' , 'email']
        labels = {
            'name': ('ชื่อ-สกุล') , 'role' : ('โปรดระบุ') , 'province' : ('จังหวัด')
        }
        error_messages = {
            'name': {
                'required': ("กรุณากรอก ชื่อ"),
            }, 
             'province': {
                'required': ("กรุณาระบุ จังหวัด"),
            },
            'email': {
                'required': ("กรุณากรอก Email "),
            },
        }

