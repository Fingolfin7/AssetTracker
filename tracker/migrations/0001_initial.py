# Generated by Django 3.2.9 on 2022-11-02 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('office', models.CharField(choices=[('Harare', 'Harare'), ('Bulawayo', 'Bulawayo'), ('Mutare', 'Mutare')], max_length=100, null=True)),
                ('isManager', models.BooleanField(default=False)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.department')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_qrent', models.BooleanField(default=False)),
                ('brand_model', models.CharField(max_length=100, null=True)),
                ('serial_number', models.CharField(max_length=100, null=True, unique=True)),
                ('processor', models.CharField(max_length=100, null=True)),
                ('ram', models.IntegerField(null=True)),
                ('ram_type', models.CharField(max_length=100, null=True)),
                ('max_ram', models.IntegerField()),
                ('storage', models.IntegerField()),
                ('operating_system', models.CharField(max_length=100, null=True)),
                ('antivirus', models.CharField(max_length=100, null=True)),
                ('condition', models.CharField(blank=True, choices=[('Good', 'Good'), ('Functional (with issues)', 'Functional (with issues)'), ('Non-Functional', 'Non-Functional')], default='Good', max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.employee')),
            ],
        ),
    ]
