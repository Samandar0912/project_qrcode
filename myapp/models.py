import os
from django.conf import settings
from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import qrcode
from django.contrib.staticfiles import finders

class Sertificate(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism Familya")
    serya = models.CharField(max_length=50, verbose_name='Seriya')
    code = models.ImageField(upload_to='code/', blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + str(self.id) + "/"

    def save(self, *args, **kwargs):
        # Sertifikat uchun shablon rasmni ochish
        template_path = finders.find('img/sertificat.jpg')
        if not template_path:
            print("Error: Template image not found.")
            return
        
        try:
            template = Image.open(template_path)
        except Exception as e:
            print(f"Error opening template image: {e}")
            return

        # QR kod yaratish
        qr_img = qrcode.make(f"Jizpi IT-Park tomonidan {self.name} uchun berilgan")
        qr_offset = Image.new('RGB', qr_img.size, 'white')
        qr_offset.paste(qr_img)

        # QR kodni sertifikat shabloniga joylashtirish
        template.paste(qr_offset, (760, 1700))  # (50, 50) - joylashish koordinatalari

        # Sertifikat ma'lumotlarini shablon rasmga yozish
        draw = ImageDraw.Draw(template)
        font_path = finders.find('fonts/Roboto.ttf')
        if not font_path:
            print("Error: Font file not found.")
            return
        
        try:
            name_font = ImageFont.truetype(font_path, 120)
        
        except IOError as e:
            print(f"Error loading font: {e}")
            return

        # Matn joylashish koordinatalari
        name_position = (970, 730)
  

        draw.text(name_position, self.name, fill='black', font=name_font)
     

        # Yangi rasmni saqlash
        file_name = f"{self.id}_{self.name}_certificate.png"
        with BytesIO() as stream:
            template.save(stream, 'PNG')
            stream.seek(0)
            self.code.save(file_name, File(stream), save=False)

        super().save(*args, **kwargs)
