from django.shortcuts import redirect

class RootMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class SesionIniciada(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
        
class AdministradorMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_administrador:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class TecnicoMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_tecnico_hardware:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')