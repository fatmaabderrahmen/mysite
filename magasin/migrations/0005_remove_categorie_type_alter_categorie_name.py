# Generated by Django 5.0.2 on 2024-02-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_categorie_type_alter_categorie_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='type',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(default='Alimentaire', max_length=50),
        ),
    ]