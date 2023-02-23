# Generated by Django 3.2.8 on 2023-02-19 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_employee_salary'),
        ('pos', '0006_auto_20230219_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet_pos',
            name='employee_close',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_close', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='wallet_pos',
            name='payment_form',
            field=models.CharField(default='', max_length=50),
        ),
    ]