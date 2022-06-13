from django import forms

from blog.models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=["nombreApellido", "email", "telefono", "mensaje", ]
        labels={"nombreApellido":"Nombre y Apellido",
                "email":"Correo Electrónico",
                "telefono": "Teléfono",
                "mensaje":"Mensaje",
                }
        widgets={"nombreApellido":forms.TextInput(attrs={'class':'form-control'}),
                "email":forms.TextInput(attrs={'class':'form-control'}),
                "telefono":forms.TextInput(attrs={'class':'form-control'}),
                "mensaje":forms.Textarea(attrs={'class':'form-control'}),
                }        

    #nombreApellido= forms.CharField(max_length=150)
    #email=forms.EmailField(max_length=100, label='Email')
    #telefono= forms.CharField(max_length=100)
    #mensaje= forms.CharField (label='Mensaje', widget= forms.widgets.Textarea)    
