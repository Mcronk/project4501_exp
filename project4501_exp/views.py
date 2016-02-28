import urllib.request
import urllib.parse
import requests
import json
from django.http import HttpResponse, JsonResponse


#api/v1/home
def home(request):
	req = requests.get('http://models-api:8000/api/v1/course/'+course_pk)
	course = json.loads(req.txt)
	data = { 'course' : course }
	return JsonResponse(data, safe=False)

#Course + Tutor: get information of a list of courses
def courses(request):
	course_req = requests.get('http://models-api:8000/api/v1/course/')
	course_data = json.loads(course_req.text)
	course_list = []
	for d in course_data:
		course = {}
		course['course_pk'] = d['pk']
		fields = d['fields']
		course['course_name'] = fields['name']
		tutor_pk = fields['tutor']

		user_req = requests.get('http://models-api:8000/api/v1/user/'+str(tutor_pk))
		user_data = json.loads(user_req.text)
		for d in user_data:
			fields = d['fields']
			course['course_tutor'] = fields['name']
		course_list.append(course)
	return JsonResponse(course_list, safe=False)
	

#Course + Tutor: get information of a course
def course(request, course_pk = ''):
	course_req = requests.get('http://models-api:8000/api/v1/course/'+course_pk)	
	course_data = json.loads(course_req.text)
	for d in course_data:
		fields = d['fields']
		course_name = fields['name']
		price = fields['price']
		description = fields['description']
		tutor_pk = fields['tutor']
	user_req = requests.get('http://models-api:8000/api/v1/user/'+str(tutor_pk))
	user_data = json.loads(user_req.text)
	for d in user_data:
		fields = d['fields']
		tutor_name = fields['name']
	return JsonResponse({'name':course_name, 'price':price, 'description':description,'tutor':tutor_name}, safe=False)


