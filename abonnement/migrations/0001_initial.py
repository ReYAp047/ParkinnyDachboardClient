# Generated by Django 3.2 on 2022-09-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Client', models.CharField(default='NomClient', max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Prix_payer', models.FloatField(default=1)),
                ('Date_creation', models.DateField(auto_now_add=True)),
                ('Date_expiration', models.DateField(auto_now_add=True)),
                ('Matricule', models.CharField(max_length=50)),
            ],
        ),
    ]
