# Generated by Django 5.1.3 on 2024-11-16 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pekerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SesiLayanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('harga', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pemesanan', models.DateField()),
                ('kode_diskon', models.CharField(blank=True, max_length=100, null=True)),
                ('total_pembayaran', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metode_pembayaran', models.CharField(max_length=50)),
                ('sesi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jasa.sesilayanan')),
            ],
        ),
        migrations.CreateModel(
            name='Subkategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jasa.kategori')),
            ],
        ),
        migrations.AddField(
            model_name='sesilayanan',
            name='subkategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jasa.subkategori'),
        ),
    ]