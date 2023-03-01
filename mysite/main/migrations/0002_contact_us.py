# Generated by Django 4.1.7 on 2023-02-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Contact_Us name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact_Us email')),
                ('subject', models.CharField(max_length=50, verbose_name='Contact_Us subject')),
                ('about', models.TextField(verbose_name='Contact_Us about')),
            ],
            options={
                'verbose_name': 'Contact_Us',
                'verbose_name_plural': 'Contacts_Us',
            },
        ),
    ]