from django.shortcuts import render
from .models import Team
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import TeamSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

def details(request):
    teamlist=Team.objects.all()
    print(teamlist)
    return render(request, 'details.html', {'teams' : teamlist}  )



def team_view(request, team_id):
    teamlist=list(Team.objects.all())
    for team in teamlist:
        if team.team_id == team_id :
            break
    else:
        return HttpResponse("Error 404 : No Such page Exists. ") 
    return render(request, 'team_view.html', {'Team' : team})



@api_view(['GET','POST'])
def details_page(request):
    
    if request.method == 'GET' :
        teams=Team.objects.all()
        serializer= TeamSerializer(teams, many=True)
        return Response (serializer.data )

    elif request.method == 'POST':
        serializer=TeamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, team__id):
    try:
        team=Team.objects.get(team_id=team__id)

    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=TeamSerializer(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer=TeamSerializer(team, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    