# Generated by Django 3.0.5 on 2020-06-22 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200622_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cause',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Cause'),
            preserve_default=False,
        ),
    ]
