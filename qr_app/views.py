from django.shortcuts import render
from .forms import QRCodeForm
from .models import QRCode
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr(request):
    form = QRCodeForm()
    img_url = None
    full_img_url = ''

    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            qr_img = qrcode.make(instance.data)
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            image_file = ContentFile(buffer.getvalue())
            instance.image.save(f'{instance.data}_qr.png', image_file)
            instance.save()

            img_url = instance.image.url
            full_img_url = request.build_absolute_uri(img_url)

    return render(request, 'qr_app/home.html', {
        'form': form,
        'img_url': img_url,
        'full_img_url': full_img_url,
    })
