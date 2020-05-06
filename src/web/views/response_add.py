from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views import View

from data import models


class ResponseAdd(LoginRequiredMixin, View):

    template_name = 'web/response_add.html'

    def get(self, request):

        survey = models.Survey.objects.filter(enabled=True).first()

        questions_count = models.Question.objects.filter(
            enabled=True,
            survey=survey,
        ).count()

        questions = models.Question.objects.filter(
            enabled=True,
            survey=survey,
        )

        questions_per_page = int(questions_count / 3)

        questions1 = questions[:questions_per_page]
        questions2 = questions[questions_per_page:questions_per_page * 2]
        questions3 = questions[questions_per_page * 2:]

        return render(request, self.template_name, {
            'survey': survey,
            'questions1': questions1,
            'questions2': questions2,
            'questions3': questions3,
        })

    def post(self, request):

        survey = models.Survey.objects.filter(enabled=True).first()

        response = models.Response()

        response.survey = survey

        response.user = request.user

        response.facility = 1

        response.risk_result_i = 0

        response.risk_result_v = 0

        response.expired_on = timezone.now() + timedelta(hours=72)

        response.completion_date = timezone.now()

        response.enabled = True

        response.save()

        for field in request.POST:            

            if field == 'csrfmiddlewaretoken' or field == 'facility':
                continue            

            field_split = field.split('-')            

            question_type = int(field_split[0])

            value = int(field_split[1])

            if question_type == models.Question.SINGLE_OPTION:                

                option_id = int(request.POST.get(field))                

                option = models.Option.objects.get(id=option_id)

                answer = models.Answer()

                answer.response = response

                answer.option = option

                answer.answer_value = option.text

                answer.risk_result_i = option.risk_value_infection

                response.risk_result_i += option.risk_value_infection

                answer.risk_result_v = option.risk_value_vulnerability

                response.risk_result_v += option.risk_value_vulnerability

                answer.save()

            elif question_type == models.Question.SELECT_MULTIPLE:

                option_id = value

                option = models.Option.objects.get(id=option_id)                

                answer = models.Answer()

                answer.response = response

                answer.option = option

                answer.answer_value = option.text

                answer.risk_result_i = option.risk_value_infection

                response.risk_result_i += option.risk_value_infection

                answer.risk_result_v = option.risk_value_vulnerability

                response.risk_result_v += option.risk_value_vulnerability

                answer.save()

            elif question_type == models.Question.NUMBER:

                question_id = value

                option = models.Option.objects.filter(
                    question__id=question_id
                ).first()

                answer = models.Answer()

                answer.response = response

                answer.option = option

                answer.answer_value = float(request.POST.get(field))

                answer.risk_result_i = option.risk_value_infection

                answer.risk_result_v = option.risk_value_vulnerability

                answer.save()

            elif question_type == models.Question.TEXT:

                question_id = value

                option = models.Option.objects.filter(
                    question__id=question_id
                ).first()

                answer = models.Answer()

                answer.response = response

                answer.option = option

                answer.answer_value = float(request.POST.get(field))

                answer.risk_result_i = option.risk_value_infection

                answer.risk_result_v = option.risk_value_vulnerability

                answer.save()

            response.save()

            messages.success(request,
                _('Gracias por haber contestado esta encuesta, te será informado en breve si tu acceso es otorgado.')
            )

        return render(request, self.template_name)
