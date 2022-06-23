from django import forms

from blog.models import Contacto, BlogModel

listatipo = [("Público","Público"),
             ("Privado","Privado"),]

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


class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields= fields = ["titulo", "sub_titulo", "cuerpo", "visible","image"]
        labels={"image":"Imagen",}
        widgets={"visible":forms.Select(attrs={'required': True}, choices=listatipo),}  
 
