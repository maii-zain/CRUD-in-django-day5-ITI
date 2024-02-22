from rest_framework import serializers
from company.models import Emp, Team

class EmployeeSerializerTeam(serializers.ModelSerializer):
    
   class Meta:
        model=Emp
        fields="__all__"


class TeamSerializer(serializers.ModelSerializer):
    manager=EmployeeSerializerTeam()
    class Meta:
        model = Team
        fields = "__all__"

class EmpSerializer(serializers.ModelSerializer):
     team=TeamSerializer()
     class Meta:
        model=Emp
        fields="__all__"



        

