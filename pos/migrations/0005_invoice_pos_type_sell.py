# Generated by Django 3.2.8 on 2023-02-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_invoice_pos_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_pos',
            name='type_sell',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
