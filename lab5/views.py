from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from company.models import Emp, Team
from lab5.serializers import EmpSerializer, TeamSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#CRUD uning class based
class EmployeeAPIView(APIView):
    def get(self, request):
        employees = Emp.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            employees = Emp.objects.all()
            My_Emps = EmpSerializer(employees, many=True)
            return Response({"employees": My_Emps.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk): 
        
        employee_instance = Emp.objects.get(id=pk)  
        serializer = EmpSerializer(employee_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
      
        employee_instance = Emp.objects.get(pk=pk)
        employee_instance.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class TeamViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
