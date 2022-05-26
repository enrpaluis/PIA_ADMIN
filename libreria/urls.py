from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from .views import  registro

from django.conf.urls import include
from qr_code import urls as qr_code_urls

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('inventarios',views.inventario,name='inventario'),
    path('ordenes',views.ordenes,name='ordenes'),
    path('pendientes',views.pendientes,name='pendientes'),
    path('inventarios',views.inventario,name='inventario'),
    path('inventarios/crear',views.crear_equipo,name='crear'),
    path('inventarios/editar/<int:id>',views.editar_equipo,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('reportes',views.reportes,name='reportes'),
    path('registro/',views.registro,name="registro",),
    path('detalle/<int:id>',views.detalle,name='detalle'),
    path('scanner/',views.scanner,name='scanner'),
    path('qr_code/', include(qr_code_urls, namespace="qr_code")),
    
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
