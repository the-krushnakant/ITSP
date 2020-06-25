from rest_framework import serializers
from .models import Team 

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['team_id', 'team_name', 'member1', 'member2', 'member3', 'member4']
        