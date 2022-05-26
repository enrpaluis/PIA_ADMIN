from distutils.command.upload import upload
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
from tabnanny import verbose
from telnetlib import STATUS
from turtle import goto
from xmlrpc.client import _datetime_type
from cv2 import CalibrateDebevec, CascadeClassifier
from django.db import models
from pyparsing import null_debug_action
from requests import delete
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
import random



#Choices


estatus_choice= (
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
)   

dominio_choice= (
    ('Propio', 'Propio'),
    ('Comodato', 'Comodato'),
    ('Otro', 'Otro'),
)

daño_choice= (
    ('Pieza Faltante', 'Pieza Faltante'),
    ('Daño por Accidente', 'Daño por Accidente'),
    ('Daño por Incendio', 'Daño por Incendio'),
    ('No enciende', 'No enciende'),
    ('Otro', 'Otro'),
    ('No encontrado', 'No encontrado'),)



# Create your models here.
class Equipo(models.Model):
    id= models.AutoField(primary_key=True)
    clave=models.CharField(max_length=100,null=True,blank=True)
    equipo=models.CharField(max_length=100, null=True)
    marca=models.CharField(max_length=100, verbose_name='Marca', null=True)
    modelo=models.CharField(max_length=100, verbose_name='Modelo', null=True)
    num_serie=models.CharField(max_length=100, verbose_name='Número de Serie', null=True)
    proveedor=models.CharField(max_length=100, verbose_name='proveedor',null=True)
    ficha_mantenimiento=models.CharField(max_length=100, verbose_name='Ficha de mantenimiento',null=True)
    frecuencia=models.CharField(max_length=100,choices=[ ('Diario', 'Diario'),
    ('Semanal', 'Semanal'),
    ('Mensual', 'Mensual'),
    ('Semestral', 'Semestral'),
    ('Anual', 'Anual'),],verbose_name='Frecuencia',null=True)
    ubicación=models.CharField(max_length=100, verbose_name='ubicación',null=True)
    dominio=models.CharField(choices=dominio_choice, max_length=100, verbose_name='Dominio',null=True)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True,blank=True)
    fecha=models.DateField(auto_now=True)
    def __str__(self):
        fila="# "+ str(self.id)+"-"+"Equipo: "+self.equipo+"-"+" Marca: "+self.marca+" -"+"Clave "+self.modelo+ " Proveedor: "+self.proveedor+"- "+" Ubicación: "+self.ubicación
        return fila

    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Mantenimiento(models.Model):
    id= models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100, verbose_name='Descripción', null=True)
    responsable=models.CharField(max_length=100, verbose_name='Responsable', null=True)
    fecha_inicio=models.DateField(verbose_name='Fecha de inicio', auto_now_add=True)
    problema=models.CharField(choices=daño_choice, max_length=100, verbose_name='Problema',null=True)
    hora=models.TimeField(verbose_name='Hora', auto_now_add=True)
    
    def __str__(self):
        fila="# "+ str(self.id)+"Descripción: "+self.descripcion+"-"+" Responsable: "+self.responsable+" -"
        return fila

    def delete(self,using=None,keep_parents=False):
        super().delete()   

   
class QrCode(models.Model):
   url=models.URLField()
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)