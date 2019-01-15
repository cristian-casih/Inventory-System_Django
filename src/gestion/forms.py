from django import forms

from .models import Personal


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            "dni",
            "nombre",
            "apellido",
            "fecha_nacimiento",
            "email",
        ]
        labels = {
            "dni": "Dni",
            "nombre": "Sexo",
            "apellido": "Apellido",
            "fecha_nacimiento": "Fecha de Nacimiento",
            "email": "Mail",

        }


    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveeder = email.split("@")
        dominio, extension = proveeder.split(".")

        print(dominio)
        if not dominio == "intel":
            raise forms.ValidationError("Por favor utiliza un mail con dominio @intel")
        return email
