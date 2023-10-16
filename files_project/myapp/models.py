import os
import uuid

from django.db import models
from rest_framework.exceptions import ValidationError

from app_core import settings
from myapp.file_type_category import file_param_processing, \
    CategoryAndInstrument
from myapp.tasks import file_choice_processing


def upload_to(instance, filename):
    # Получаем расширение файла
    extension = os.path.splitext(filename)[1][1:]
    if not extension:
        raise ValidationError('The file does not have an extension')

    category, _ = file_param_processing(extension)

    if category is CategoryAndInstrument.CATEGORY_OTHER:
        pass
        # FIXME Если необходимо игнорировать другие файлы, то выдать ошибку снизу
        # raise ValidationError(
        #     'This file type is not supported. Please send another file.'
        # )

    file_name = str(uuid.uuid4())
    file_path = 'files/{0}/{1}.{2}'.format(category, file_name, extension)

    # Проверяем, существует ли уже файл с таким именем. Шанс 1 к 1 трлн
    while os.path.exists(os.path.join(settings.MEDIA_ROOT, file_path)):
        file_name = str(uuid.uuid4())
        file_path = 'files/{0}/{1}.{2}'.format(category, file_name, extension)

    return file_path


def validate_file_size(value):
    filesize = value.size
    # TODO можно указать ограничения на размер в зависимоти от катеогрии файла
    if filesize > 10 * 1024 * 1024:  # 10MB
        raise ValidationError(
            "The maximum file size that can be downloaded is 10MB")
    else:
        return value


class File(models.Model):
    file = models.FileField(
        upload_to=upload_to,
        validators=[validate_file_size]
    )
    file_name = models.CharField(null=True, max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        extension = None
        if not self.id:
            self.file_name = self.file.name
            extension = os.path.splitext(self.file_name)[1][1:]
        super(File, self).save(*args, **kwargs)
        if extension:
            file_choice_processing(
                self.id, *file_param_processing(extension)
            )
