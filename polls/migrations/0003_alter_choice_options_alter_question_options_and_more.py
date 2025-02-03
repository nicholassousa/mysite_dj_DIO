# Generated by Django 5.1.5 on 2025-01-28 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_question_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="choice",
            options={"verbose_name": "resposta", "verbose_name_plural": "respostas"},
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"verbose_name": "Questão", "verbose_name_plural": "Questões"},
        ),
        migrations.AlterField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(max_length=200, verbose_name="resposta da questão"),
        ),
        migrations.AlterField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.question",
                verbose_name="texto da questão",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="pub_date",
            field=models.DateTimeField(verbose_name="data de publicação"),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=200, verbose_name="texto da questão"),
        ),
    ]
