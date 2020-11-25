from django.contrib import admin

from .models import Pawn
from .models import SplendorGame
from .models import SplendorGameState
from .models import SplendorPlayerState

# Register your models here.

admin.site.register(Pawn)
admin.site.register(SplendorGame)
admin.site.register(SplendorGameState)
admin.site.register(SplendorPlayerState)
