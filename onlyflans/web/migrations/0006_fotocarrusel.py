# Generated by Django 5.0.6 on 2024-06-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_contactform_customer_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoCarrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('static_url', models.CharField(max_length=50)),
            ],
        ),
    ]