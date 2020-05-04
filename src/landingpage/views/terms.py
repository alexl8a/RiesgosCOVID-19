import os

from django.conf import settings
from django.http import FileResponse
from django.views import View


class Terms(View):

    def get(self, request):

        pdf_path = os.path.join(
            settings.BASE_DIR,
            'landingpage/templates/landingpage/terms.pdf'
        )

        pdf_bytes = open(pdf_path, 'rb')

        return FileResponse(pdf_bytes, filename='Terms.pdf', content_type='application/pdf')
