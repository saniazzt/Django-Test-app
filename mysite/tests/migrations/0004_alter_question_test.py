# Generated by Django 4.2.5 on 2023-09-30 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_remove_choice_votes_remove_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
    ]
