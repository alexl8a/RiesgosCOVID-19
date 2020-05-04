from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from wkhtmltopdf.views import PDFTemplateResponse

from data import models


class ResponsePdf(LoginRequiredMixin, View):

    template_name = 'web/response_pdf.html'

    def get(self, request, pk, **kwargs):

        r = get_object_or_404(
            models.Response,
            pk=pk,
            user=request.user,
            enabled=True,
        )

        answers = r.answers.order_by('option')

        data = {
                'response': r,
                'answers': answers
            }

        response = PDFTemplateResponse(request=request,
                                       template=self.template_name,
                                       filename="survey_response.pdf",
                                       context= data,
                                       show_content_in_browser=False,
                                       cmd_options={
                                            'margin-top': 10,
                                            'zoom':1,
                                            'viewport-size' :'1366 x 513',
                                            'javascript-delay':1000,
                                            'footer-center' :'[page]/[topage]',
                                            'no-stop-slow-scripts':True
                                        },
                                    )

        return response

