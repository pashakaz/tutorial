# Generated by Django 3.1 on 2020-11-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pawn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xpos', models.DecimalField(decimal_places=3, max_digits=3)),
                ('ypos', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
        ),
    ]
