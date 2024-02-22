from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from company.forms import EmpForm, TeamForm
from company.models import Emp, Team

def EmpView(request):
    if request.method == "GET":
        FormOfEmp = EmpForm()
    elif request.method == "POST":
        FormOfEmp = EmpForm(request.POST)
        if FormOfEmp.is_valid():
            team=Team.objects.filter(pk=request.POST["team"])[0]
            emp = Emp.objects.create(
                emp_name=FormOfEmp.cleaned_data["emp_name"],
                salary=FormOfEmp.cleaned_data["salary"],
                title=FormOfEmp.cleaned_data["title"],
                team_id=FormOfEmp.cleaned_data["team"]
            )
          
    else:
        FormOfEmp = EmpForm()
        
    return render(request, 'company/CreateEmp.html', {'form': FormOfEmp})


# def TeamView(request):
#     if request.method == "POST":
#         form = TeamForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Team created successfully!")  
#     else:
#         form = TeamForm()
#     return render(request, 'company/CreateTeam.html', {'form': form})


class TeamView(View):
    def get(self, request):
        form = TeamForm()
        return render(request, 'company/CreateTeam.html', {'form': form})

    def post(self, request):
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Team created successfully!")
        return render(request, 'company/CreateTeam.html', {'form': form})

