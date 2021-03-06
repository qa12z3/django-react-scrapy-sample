# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('photoUrl', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardDriveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MotherBoardFormFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PciType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PowerSupplyFormFactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RamFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('weight', models.FloatField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('motherBoardFormFactors', models.ManyToManyField(to='components.MotherBoardFormFactor')),
                ('powerSupplyFormFactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.PowerSupplyFormFactor')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='GraphicCard',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('memory', models.IntegerField()),
                ('pcitype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.PciType')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='HardDrive',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('capacity', models.IntegerField()),
                ('hardDriveType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.HardDriveType')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('ramSlots', models.IntegerField()),
                ('maxRam', models.IntegerField()),
                ('formfactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.MotherBoardFormFactor')),
                ('pcitypes', models.ManyToManyField(to='components.PciType')),
                ('ramfrequency', models.ManyToManyField(to='components.RamFrequency')),
                ('ramtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.RamType')),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Socket')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('watts', models.IntegerField()),
                ('modular', models.BooleanField()),
                ('factorForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.PowerSupplyFormFactor')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('frequency', models.FloatField()),
                ('cores', models.IntegerField()),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Socket')),
            ],
            bases=('components.component',),
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('component_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='components.Component')),
                ('capacity', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.RamFrequency')),
                ('ramtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.RamType')),
            ],
            bases=('components.component',),
        ),
        migrations.AddField(
            model_name='component',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.Brand'),
        ),
    ]
