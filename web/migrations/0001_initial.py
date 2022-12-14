# Generated by Django 3.2.16 on 2022-11-09 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_identifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=130)),
                ('age', models.BooleanField(null=True)),
                ('proband', models.CharField(max_length=100)),
                ('affected_relatives', models.CharField(max_length=100)),
                ('tumor', models.CharField(max_length=100)),
                ('sequencer', models.CharField(max_length=100)),
                ('g_nomenclature', models.CharField(max_length=100)),
                ('pathogenecity_code', models.CharField(max_length=100)),
                ('evidence_codes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='variant_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_protein', models.CharField(max_length=100)),
                ('c_nomenclature', models.CharField(max_length=100)),
                ('g_nomenclature', models.ForeignKey(db_column='g_nomenclature', on_delete=django.db.models.deletion.CASCADE, to='web.patient_identifier')),
            ],
        ),
    ]
