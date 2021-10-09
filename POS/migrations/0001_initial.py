# Generated by Django 3.2.5 on 2021-10-09 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Bill_number', models.IntegerField(primary_key=True, serialize=False)),
                ('Bill_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=120, null=True, verbose_name='Customer Name')),
                ('sub_total', models.IntegerField()),
                ('balance', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('invoice_type', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Cash', 'Cash'), ('Debit', 'Debit')], default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Billinsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_number', models.IntegerField()),
                ('Bill_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('sub_total', models.IntegerField()),
                ('last_updated', models.DateField()),
                ('paid', models.BooleanField()),
                ('invoice_type', models.CharField(max_length=100)),
                ('vehicle_number', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('product_id_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_code', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price')),
                ('order_level', models.IntegerField(blank=True, default=0, null=True, verbose_name='Pre Order Level')),
            ],
        ),
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=100)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='POS.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Billing_Detail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('vehicle_number', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=0, null=True)),
                ('total', models.IntegerField()),
                ('Bill_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='POS.bill')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='POS.product')),
            ],
        ),
    ]
