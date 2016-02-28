import urllib.request
import urllib.parse
import requests
import json
from django.http import JsonResponse


#api/v1/home
def home(request):
		req = requests.get('http://models-api:8000/api/v1/courses/'+course_pk)
		course = json.loads(req.txt)
		data = { 'course' : course }

		return JsonResponse(data, safe=False)


#api/v1/product
def product(request, course_pk = ' '):
		#req = urllib.request.Request('http://models-api:8000/api/v1/courses/'+course_pk)
		course_req = requests.get('http://models-api:8000/api/v1/courses/'+course_pk)
		
		#retrieve tutor primary key
		tutor_pk = course_req.headers.get('tutor')

		#use tutor pk to find associated courses
		tutor_req = requests.get('http://models-api:8000/api/v1/courses/'+ tutor_pk)
		
		#deserialize
		course = json.loads(course.txt)
		tutor = json.loads(tutor_req.txt)

		#aggregate into single JSON object
		data = { 'course' : course, 'tutor' : tutor }


		return JsonResponse(data, safe=False)


