
class CategoryAndInstrument:
    CATEGORY_TEXT = "text"
    CATEGORY_IMAGE = "image"
    CATEGORY_VIDEO = "video"
    CATEGORY_AUDIO = "audio"
    CATEGORY_DATA_FILES = "data"
    CATEGORY_ARCHIVE = "archive"
    CATEGORY_EXECUTABLE = "executable"
    CATEGORY_OTHER = "other"

    """ 
    Здесь указаны псевдо инструменты которыми будут обрабатываться файлы в celery
    """
    INSTRUMENT_1 = "1"
    INSTRUMENT_2 = "2"
    INSTRUMENT_3 = "3"
    INSTRUMENT_4 = "4"
    INSTRUMENT_5 = "5"
    INSTRUMENT_6 = "6"
    INSTRUMENT_7 = "7"
    INSTRUMENT_8 = "8"
    INSTRUMENT_9 = "9"

    EXTENSION_AND_CATEGORY = {
        # CATEGORY_TEXT
        "doc": (CATEGORY_TEXT, INSTRUMENT_1),
        "docx": (CATEGORY_TEXT, INSTRUMENT_1),
        "dot": (CATEGORY_TEXT, INSTRUMENT_1),
        "dotx": (CATEGORY_TEXT, INSTRUMENT_1),
        "html": (CATEGORY_TEXT, INSTRUMENT_2),
        "htm": (CATEGORY_TEXT, INSTRUMENT_2),
        "rtf": (CATEGORY_TEXT, INSTRUMENT_2),
        "txt": (CATEGORY_TEXT, INSTRUMENT_2),
        "odt": (CATEGORY_TEXT, INSTRUMENT_1),
        "pdf": (CATEGORY_TEXT, INSTRUMENT_1),

        # CATEGORY_IMAGE
        "png": (CATEGORY_IMAGE, INSTRUMENT_4),
        "jpeg": (CATEGORY_IMAGE, INSTRUMENT_4),
        "tiff": (CATEGORY_IMAGE, INSTRUMENT_4),
        "webp": (CATEGORY_IMAGE, INSTRUMENT_4),
        "gif": (CATEGORY_IMAGE, INSTRUMENT_4),
        "svg": (CATEGORY_IMAGE, INSTRUMENT_5),
        "eps": (CATEGORY_IMAGE, INSTRUMENT_5),
        "ai": (CATEGORY_IMAGE, INSTRUMENT_5),
        "cdr": (CATEGORY_IMAGE, INSTRUMENT_5),

        # CATEGORY_VIDEO
        "3gp": (CATEGORY_VIDEO, INSTRUMENT_6),
        "asf": (CATEGORY_VIDEO, INSTRUMENT_6),
        "avi": (CATEGORY_VIDEO, INSTRUMENT_6),
        "flv": (CATEGORY_VIDEO, INSTRUMENT_6),
        "mov": (CATEGORY_VIDEO, INSTRUMENT_6),
        "mp4": (CATEGORY_VIDEO, INSTRUMENT_6),

        # CATEGORY_AUDIO
        "wav": (CATEGORY_AUDIO, INSTRUMENT_7),
        "aiff": (CATEGORY_AUDIO, INSTRUMENT_7),
        "raw": (CATEGORY_AUDIO, INSTRUMENT_7),
        "ape": (CATEGORY_AUDIO, INSTRUMENT_7),
        "flac": (CATEGORY_AUDIO, INSTRUMENT_7),
        "mp3": (CATEGORY_AUDIO, INSTRUMENT_7),
        "aac": (CATEGORY_AUDIO, INSTRUMENT_7),
        "ogg": (CATEGORY_AUDIO, INSTRUMENT_7),
        "wma": (CATEGORY_AUDIO, INSTRUMENT_7),


        # CATEGORY_DATA_FILES
        "csv": (CATEGORY_DATA_FILES, INSTRUMENT_3),
        "xml": (CATEGORY_DATA_FILES, INSTRUMENT_2),
        "xls": (CATEGORY_DATA_FILES, INSTRUMENT_3),
        "xlsx": (CATEGORY_DATA_FILES, INSTRUMENT_3),

        # CATEGORY_ARCHIVE
        "zip": (CATEGORY_DATA_FILES, INSTRUMENT_8),
        "rar": (CATEGORY_DATA_FILES, INSTRUMENT_8),
        "arc": (CATEGORY_DATA_FILES, INSTRUMENT_8),
        "arj": (CATEGORY_DATA_FILES, INSTRUMENT_8),
        'jar': (CATEGORY_DATA_FILES, INSTRUMENT_8),
        "tar": (CATEGORY_DATA_FILES, INSTRUMENT_8),

        # CATEGORY_EXECUTABLE
        "exe": (CATEGORY_EXECUTABLE, INSTRUMENT_9)

    }


def file_param_processing(file_extension: str) -> (str, str):
    param = CategoryAndInstrument
    category, instrument = param.EXTENSION_AND_CATEGORY.get(
        file_extension.lower(), (param.CATEGORY_OTHER, '')
    )
    return category, instrument

