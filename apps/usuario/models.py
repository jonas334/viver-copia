from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def _create_user(self, email, nombres, apellidos, password, is_root, is_superuser):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')

        user = self.model(
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos =apellidos,
            is_root=is_root,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,email,nombres,apellidos, password = None):
        return self._create_user(email, nombres, apellidos, password, False, False)

    def create_superuser(self,email,nombres,apellidos, password = None):
        return self._create_user(email, nombres, apellidos, password, True, True)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Correo Electrónico', max_length=254,unique = True)
    cc = models.IntegerField('C.C', unique=True, blank = True, null = True)
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True)
    is_root = models.BooleanField(default = False)
    is_administrador = models.BooleanField(default = False)
    is_tecnico_hardware = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}'

    @property
    def is_staff(self):
        return self.is_root

class TokenEmail(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100)
    fecha_actual = models.FloatField()
    fecha_limite = models.FloatField()
    email = models.CharField(max_length=254)

    class Meta:
        verbose_name = 'Token Email'
        verbose_name_plural = 'Tokens Email'

    def __str__(self):
        return str(self.id)
