# Generated by Django 4.2.3 on 2023-07-19 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]