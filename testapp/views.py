from .models import Question, Choice
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from random import randint
from .compiled.mylib import exportToJson
from datetime import datetime


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


@api_view(["GET"])
def generate_questions(request):
    for i in range(10):
        q = Question(question_text=f"Q{i}",
                     pub_date=datetime.now())
        q.save()
        for i in range(randint(1, 10)):
            c = Choice(question=q, choice_text=f"Choice {i}")
            c.save()
    return Response(status=200)


@api_view(["GET"])
def get_all_qs(request):
    q = ChoiceSerializer(Question.objects.all(), many=True)
    return Response(q.data)


@api_view(["GET"])
def get_everything(request):
    qs = Question.objects.all()
    return Response(exportToJson(qs))

