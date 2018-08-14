# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientID', models.CharField(db_column=b'patientID', max_length=10, primary_key=True, serialize=False, verbose_name=b'Patient ID')),
                ('patientname', models.CharField(db_column=b'patientName', max_length=30, verbose_name=b'Patient Name')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name=b'User Name')),
                ('password', models.CharField(max_length=20, verbose_name=b'Password')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Gender')),
                ('patientactive', models.BooleanField(db_column=b'patientActive', default=True, verbose_name=b'Patient Active')),
                ('email', models.CharField(max_length=30, verbose_name=b'Email Address')),
                ('phone', models.CharField(max_length=10, verbose_name=b'Phone')),
                ('address', models.CharField(max_length=100, verbose_name=b'Address Line')),
                ('city', models.CharField(max_length=30, verbose_name=b'City')),
                ('state', models.CharField(max_length=2, verbose_name=b'State')),
                ('zip', models.CharField(max_length=5, verbose_name=b'Zip Code')),
                ('insprovider', models.CharField(db_column=b'insProvider', max_length=100, verbose_name=b'Insurance Provider')),
                ('insdeductible', models.DecimalField(db_column=b'insDeductible', decimal_places=2, max_digits=6, verbose_name=b'Insurance Deductible')),
                ('inscopay', models.DecimalField(db_column=b'insCopay', decimal_places=2, max_digits=3, verbose_name=b'Insurance Copay')),
                ('inspolicyno', models.CharField(db_column=b'insPolicyNo', max_length=10, verbose_name=b'Insurance Policy No')),
                ('insphone', models.CharField(db_column=b'insPhone', max_length=10, verbose_name=b'Insurance Phone Number')),
            ],
            options={
                'db_table': 'Patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('physicianID', models.CharField(db_column=b'doctorID', max_length=7, primary_key=True, serialize=False, verbose_name=b'Doctor ID')),
                ('physicianLastName', models.CharField(db_column=b'doctorLastName', max_length=30, verbose_name=b'Doctor Last Name')),
                ('physicianFirstName', models.CharField(db_column=b'doctorFirstName', max_length=30, verbose_name=b'Doctor First Name')),
                ('doctorspec', models.CharField(db_column=b'doctorSpec', max_length=30, verbose_name=b'Doctor Specialization')),
                ('physicianPhone', models.CharField(db_column=b'doctorPhone', max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('username', models.CharField(max_length=20, unique=True, verbose_name=b'Username')),
                ('pPassword', models.CharField(db_column=b'password', max_length=20, verbose_name=b'Password')),
            ],
            options={
                'db_table': 'Doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AssignedTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PerformedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('sampleID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sampleDisposition', models.CharField(max_length=20)),
                ('sampleCategory', models.CharField(max_length=20)),
                ('dateReceived', models.DateField()),
                ('dateTestDone', models.DateField()),
                ('patientID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Patient')),
                ('physicianID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Physician')),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('technicianID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('technicianName', models.CharField(max_length=30)),
                ('schedule', models.CharField(max_length=10)),
                ('tPassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('testID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('testRuns', models.IntegerField()),
                ('kindsOfTests', models.CharField(max_length=100)),
                ('testSchedule', models.TimeField(default=b'00:00:00')),
                ('testResult', models.CharField(default=b'Normal', max_length=30)),
                ('equipmentNeeded', models.CharField(default=b'e', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='receivedby',
            name='sampleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Sample'),
        ),
        migrations.AddField(
            model_name='receivedby',
            name='technicianID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Technician'),
        ),
        migrations.AddField(
            model_name='performedby',
            name='technicianID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Technician'),
        ),
        migrations.AddField(
            model_name='performedby',
            name='testID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Test'),
        ),
        migrations.AddField(
            model_name='assignedto',
            name='sampleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Sample'),
        ),
        migrations.AddField(
            model_name='assignedto',
            name='testID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.Test'),
        ),
    ]
