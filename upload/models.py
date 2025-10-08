'''데이터베이스 모델을 정의하는 파일. 데이터 베이스 사용하는곳'''

from django.db import models

def pdf_upload_path(instance, filename):
    # media/pdfs/원본파일명
    return f"pdfs/{filename}"

class PDF(models.Model):
    file = models.FileField(upload_to=pdf_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
