# Generated by Django 3.1 on 2020-11-21 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0002_auto_20201115_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='SplendorGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SplendorGameState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_turn', models.CharField(max_length=30)),
                ('t1_offer_string', models.CharField(max_length=100)),
                ('t2_offer_string', models.CharField(max_length=100)),
                ('t3_offer_string', models.CharField(max_length=100)),
                ('nobles_offer', models.CharField(max_length=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_world.splendorgame')),
            ],
        ),
        migrations.CreateModel(
            name='SplendorPlayerState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('chip_count_string', models.CharField(max_length=6)),
                ('nobles_string', models.CharField(max_length=50)),
                ('reserve_cards_string', models.CharField(max_length=100)),
                ('played_cards_string', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_world.splendorgamestate')),
            ],
        ),
    ]
