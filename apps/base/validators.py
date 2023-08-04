import magic
from django.core.exceptions import ValidationError

def validate_pdf_file(file):
    valid_mime_types = ['application/pdf']
    file_mime_type = magic.from_buffer(file.read(2048), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Tipo de archivo inválido. Suba un archivo PDF válido.', code = 'invalid_file_type')