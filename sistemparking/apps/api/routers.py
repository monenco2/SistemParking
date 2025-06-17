from rest_framework.routers import DefaultRouter
from ..rol.views import *
from ..facturacion.views import *

router = DefaultRouter()

router.register(r'rol', RolViewset, basename='rol')
router.register(r'facturacion', FacturacionViewset, basename='facturacion')
router.register(r'horaparqueo', FacturacionViewset, basename='horaparqueo')
router.register(r'servicio', FacturacionViewset, basename='servicio')
router.register(r'vehiculo', FacturacionViewset, basename='vehiculo')
router.register(r'usuarios', FacturacionViewset, basename='usuarios')

urlpatterns = router.urls