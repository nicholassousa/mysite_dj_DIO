import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("texto da questão",max_length=200) # Questão de tamanho maximo = 200 caracteres
    pub_date = models.DateTimeField("data de publicação") # mostra data de publicação
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = ("Questão")
        verbose_name_plural = ("Questões")

    # ajuste para poder retornar o enunciado da questão
    def __str__(self):
        return self.question_text

    # ajuste para poder retornar questão recentemente postada
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="texto da questão") # diz qual pergunta está resposta pertence
    # e no on_delete = models.CASCADE serve para deletar a resposta caso a questão seja apagada
    choice_text = models.CharField("resposta da questão", max_length=200)
    votes = models.IntegerField(default=0)

    # ajuste para poder retornar a resposta
    class Meta:
        verbose_name = ("resposta")
        verbose_name_plural = ("respostas")

    # ajuste para poder retornar a resposta
    def __str__(self):
        return f"{self.question.id}: {self.choice_text}"

    
