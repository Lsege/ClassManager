# Generated by Django 4.2.2 on 2023-10-05 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0001_initial'),
        ('curso', '0003_remove_curso_nombrecurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='id_materia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='materia.materia'),
            preserve_default=False,
        ),
    ]