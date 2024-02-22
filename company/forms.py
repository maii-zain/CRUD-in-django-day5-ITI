from django import forms
from company.models import Team

class EmpForm(forms.Form):
    emp_name = forms.CharField(max_length=50)
    salary = forms.IntegerField()  
    title = forms.CharField(max_length=50)
    team = forms.ChoiceField(choices=[(team.id, team.name) for team in Team.objects.all()])
    
    
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'manager']