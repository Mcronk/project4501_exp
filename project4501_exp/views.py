import urllib.request
import urllib.parse
import requests
import json
from django.http import HttpResponse, JsonResponse


#Course + Tutor: get information of a list of courses
def courses(request):
	course_req = requests.get('http://models-api:8000/api/v1/course/')
	course_data = json.loads(course_req.text)
	courses_list = []
	for d in course_data:
		course = {}
		course['course_pk'] = d['pk']
		fields = d['fields']
		course['course_name'] = fields['name']
		course['course_description'] = fields['description']
		tutor_pk = fields['tutor']

		user_req = requests.get('http://models-api:8000/api/v1/user/'+str(tutor_pk))
		user_data = json.loads(user_req.text)
		for d in user_data:
			fields = d['fields']
			course['course_tutor'] = fields['name']
		courses_list.append(course)
	#return a list dictionary (each dictionary is a course)
	return JsonResponse(courses_list, safe=False)
	

#Course + Tutor: get information of a course
def course(request, course_pk = ''):
	course_req = requests.get('http://models-api:8000/api/v1/course/'+course_pk)	
	course_data = json.loads(course_req.text)
	for d in course_data:
		fields = d['fields']
		course_name = fields['name']
		course_price = fields['price']
		course_description = fields['description']
		tutor_pk = fields['tutor']
	user_req = requests.get('http://models-api:8000/api/v1/user/'+str(tutor_pk))
	user_data = json.loads(user_req.text)
	for d in user_data:
		fields = d['fields']
		tutor_name = fields['name']
		tutor_description = fields['description']
	return JsonResponse({'course_name':course_name, 'course_price':course_price, 'course_description':course_description,'tutor_name':tutor_name, 'tutor_description':tutor_description}, safe=False)

#User: Create and return token
def createAuth(request, username = '', password = ''):
	auth_req = requests.get('http://models-api:8000/api/v1/createAuth/'+ username + '/' + password)
	token_data = json.loads(auth.text)#should return the auth Token to be put in cookies.
	return JsonResponse({'token_data': token_data}, safe=False)
	
#User:  Check user token and return true or false
def checkAuth(request, token = ''):
	auth_req = requests.get('http://models-api:8000/api/v1/checkAuth/' + str(token))
	auth_resp = json.loads(auth_resp.text)#should basically return true or false.
	return JsonResponse({'auth_resp': auth_resp}, safe=False)
