from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import datetime

# Create your views here.


@api_view(['GET'])
def getUsers(request):
	emails = User.objects.filter(interviwer=False).values_list('email', flat=True)
	return Response({"emails": emails}, status.HTTP_200_OK)
    

@api_view(['GET'])
def getUpcommingInterviews(request):
	interview_list = []
	time = datetime.datetime.now()
	for interview in Interviews:
		if interview.interview_from > time:
			interview_list.append(interview)
	return Response({"data": interview_list}, status.HTTP_200_OK)


@api_view(['POST'])
def createInterview(request):
	emails = request.data.get("emails")
