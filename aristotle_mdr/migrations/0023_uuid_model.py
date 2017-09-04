# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-04 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid

from aristotle_mdr.utils.migrations import create_uuid_objects

class Migration(migrations.Migration):

    dependencies = [
        ('aristotle_mdr', '0022_switch_to_concept_relations'),
    ]

    operations = [
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid1, editable=False, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', primary_key=True, serialize=False, unique=True)),
                ('app_label', models.CharField(max_length=256)),
                ('model_name', models.CharField(max_length=256)),
            ],
        ),

        migrations.RunPython(create_uuid_objects('_concept')),
        migrations.RunPython(create_uuid_objects('measure')),
        migrations.RunPython(create_uuid_objects('organization')),
        migrations.RunPython(create_uuid_objects('workgroup')),

        migrations.AlterField(
            model_name='_concept',
            name='uuid',
            field=models.OneToOneField(default=None, editable=False, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', null=True, on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr.UUID'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='uuid',
            field=models.OneToOneField(default=None, editable=False, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', null=True, on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr.UUID'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='uuid',
            field=models.OneToOneField(default=None, editable=False, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', null=True, on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr.UUID'),
        ),
        migrations.AlterField(
            model_name='workgroup',
            name='uuid',
            field=models.OneToOneField(default=None, editable=False, help_text='Universally-unique Identifier. Uses UUID1 as this improves uniqueness and tracking between registries', null=True, on_delete=django.db.models.deletion.CASCADE, to='aristotle_mdr.UUID'),
        ),
    ]
