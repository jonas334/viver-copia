from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario
from apps.tienda.models import Producto

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
 
class UsuarioForm(forms.ModelForm):
    """ Formulario de Registro de un Usuario en la base de datos

    Variables:

        - password1:    Contraseña
        - password2:    Verificación de la contraseña

    """
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'required': 'required',
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'required': 'required',
                }                
            )
        }

    def clean_password2(self):
        """ Validación de Contraseña

        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.

        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AdminForm(UsuarioForm):
    class Meta:
        model = Usuario
        fields = ('email','cc','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'cc': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'C.C',
                    'required': 'required',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'required': 'required',
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                    'required': 'required',
                }                
            )
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','descripcion','precio','cantidad', 'imagen', 'categoria_id')
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre',
                    'required': 'required',
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripcion',
                    'required': 'required',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Precio',
                    'required': 'required',
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'placeholder': 'Cantidad',
                    'required': 'required',
                }                
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'Imagen',
                }                
            ),
            'categoria_id': forms.Select(
                attrs = {
                    'placeholer': 'Categoria',
                    'required': 'required',
                }                
            ),
        }