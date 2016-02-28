import urllib.request
import urllib.parse
import requests
import json
from django.http import JsonResponse


#api/v1/home
def home(request):
		req = requests.get('http://models-api:8000/api/v1/course/'+course_pk)
		course = json.loads(req.txt)
		data = { 'course' : course }

		return JsonResponse(data, safe=False)

#api/v1/product
def product(request, course_pk = ''):
		#req = urllib.request.Request('http://models-api:8000/api/v1/courses/'+course_pk)
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



