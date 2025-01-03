# Generated by Django 5.1.4 on 2024-12-29 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('core', '0002_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flete',
            name='nombre',
        ),
        migrations.AddField(
            model_name='flete',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fletes', to='core.user'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paquete', to='cliente.usuario'),
        ),
    ]
