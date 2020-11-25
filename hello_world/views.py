from django.http import HttpResponse
from .models import Pawn
from .models import SplendorGame
from .models import SplendorGameState
from .models import SplendorPlayerState
import decimal


def index(request):
        return HttpResponse("Hello, world")

def read(request):
        pawn = Pawn.objects.last()
        response = HttpResponse(str(pawn.xpos) + ',' + str(pawn.ypos))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response


def pasha(request):
        return HttpResponse("you still found pasha's url")

def write(request):
        myxpos = request.GET['xpos']
        myypos = request.GET['ypos']
        p = Pawn(xpos=decimal.Decimal(myxpos), ypos=decimal.Decimal(myypos))
        p.save()
        return HttpResponse("you saved, go you")

def splendor_write(request):
        game_name = request.GET['game']
        game = SplendorGame.objects.get(name=game_name)
        game_state = SplendorGameState.objects.filter(game=game).last()
        return HttpResponse(game_state)
