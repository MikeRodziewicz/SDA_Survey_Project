# Generated by Django 3.0.10 on 2020-11-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_newscategory_newstags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formularz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
