from django.db import models

# Create your models here.

class Pawn(models.Model):
    xpos = models.DecimalField(decimal_places=3,max_digits=30)
    ypos = models.DecimalField(decimal_places=3,max_digits=30)

# Splendor model objects

class SplendorGame(models.Model):
    name = models.CharField(max_length=100)

class SplendorGameState(models.Model):
    game_turn = models.CharField(max_length=30)
    game = models.ForeignKey(SplendorGame, on_delete=models.CASCADE)
    t1_offer_string = models.CharField(max_length=100)
    t2_offer_string = models.CharField(max_length=100)
    t3_offer_string = models.CharField(max_length=100)
    nobles_offer = models.CharField(max_length=100)

class SplendorPlayerState(models.Model):
    state = models.ForeignKey(SplendorGameState, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    chip_count_string = models.CharField(max_length=6)
    nobles_string = models.CharField(max_length=50)
    reserve_cards_string = models.CharField(max_length=100)
    played_cards_string = models.CharField(max_length=100)

