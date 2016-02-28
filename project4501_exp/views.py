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
		
		tutor_pk = course_req.headers.get('tutor')

		tutor_req = requests.get('http://models-api:8000/api/v1/courses/'+ tutor_pk)
		
		course = json.loads(course.txt)
		tutor = json.loads(tutor_req.txt)

		data = { 'course' : course, 'tutor' : tutor }

		#deserialize
		courses = 

		return JsonResponse(data, safe=False)

		#request course via pk
		#recieve pk and all course stuff.
		# parse out tutor PK and then get tutor
		# throw into one json object and return.  


