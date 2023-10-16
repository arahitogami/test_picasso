import os
from time import sleep

from app_core import settings
from app_core.celery import app
from myapp.file_type_category import CategoryAndInstrument


def file_choice_processing(file_id: int, category: str, instrument: str):
    """
    Файлы у которых category устновлена other не обрабатываются
    :param file_id: id orm File
    :param category: category from class CategoryAndInstrument
    :param instrument: instrument from class CategoryAndInstrument
    :return:
    """

    match instrument:
        case CategoryAndInstrument.INSTRUMENT_1:
            instrument_1.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_2:
            instrument_2.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_3:
            instrument_3.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_4:
            instrument_4.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_5:
            instrument_5.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_6:
            instrument_6.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_7:
            instrument_7.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_8:
            instrument_8.delay(file_id, category)
        case CategoryAndInstrument.INSTRUMENT_9:
            instrument_9.delay(file_id, category)
        case _:
            pass


def processing_file(file_id, category):
    from myapp.models import File
    file = File.objects.get(pk=file_id)

    with open(os.path.join(settings.MEDIA_ROOT, file.file.path), 'rb') as f:
        content = f.read()

    file.processed = True
    file.save()
    return {"processed": file.processed, "category": category}


"""
Во всех тасках прописать свои способы обработки файла 
вместо функции processing_file. Так как в задании не указано как обрабатывать.
Это пример архитектуры обработками разными инструментами. 
Также указать продолжительность работы тасок и повторение.
"""


@app.task(bind=True)
def instrument_1(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_2(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_3(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_4(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_5(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_6(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_7(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_8(self, file_id, category):
    return processing_file(file_id, category)


@app.task(bind=True)
def instrument_9(self, file_id, category):
    return processing_file(file_id, category)