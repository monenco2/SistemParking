from rest_framework.routers import DefaultRouter
from ..rol.views import *
from ..facturacion.views import *
from ..usuarios.views import *
from ..vehiculo.views import *
from ..servicio.views import *
from ..horaparqueo.views import *
from ..pagofinal.views import *

router = DefaultRouter()

router.register(r'rol', RolViewset, basename='rol')
router.register(r'facturacion', FacturacionViewset, basename='facturacion')
router.register(r'horaparqueo', HoraparqueoViewset, basename='horaparqueo')
router.register(r'servicio', ServicioViewset, basename='servicio')
router.register(r'vehiculo', VehiculoViewset, basename='vehiculo')
router.register(r'usuarios', UsuariosViewset, basename='usuarios')
router.register(r'pagofinal', pagofinalViewset, basename='pagofinal')

urlpatterns = router.urls