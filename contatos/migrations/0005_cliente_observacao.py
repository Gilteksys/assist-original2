# Generated by Django 4.2.1 on 2023-05-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_cliente_contato_cliente_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='observacao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
