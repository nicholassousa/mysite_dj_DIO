import pytest

from polls.models import Question
from django.utils import timezone


@pytest.mark.django_db
def test_question_was_published_recently_success():
    # given
    question_text = "Qual a sua cor favorita?"
    pub_date = timezone.now()
    active = True
    
    # when
    question = Question.objects.create(question_text=question_text, pub_date=pub_date, active=active)
    
    # then
    assert question.was_published_recently() is True

@pytest.mark.django_db
def test_question_was_published_recently_fail():
    # given
    question_text = "Qual a sua cor favorita?"
    pub_date = timezone.now() - timezone.timedelta(days=2)
    active = True
    
    # when
    question = Question.objects.create(question_text=question_text, pub_date=pub_date, active=active)
    
    # then
    assert question.was_published_recently() is False
