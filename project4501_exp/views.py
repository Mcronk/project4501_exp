import urllib.request
import urllib.parse
import requests
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
	return JsonResponse({'result': course_data['work']})
	req = json.loads(course_req)
	return JsonResponse({'result': req})

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
@csrf_exempt
def create_account(request):
	auth_req = requests.post('http://models-api:8000/api/v1/create_account/'+ username + '/' + password)
	token_data = json.loads(token_data.text)#should return the auth Token to be put in cookies.
	return JsonResponse({'token_data': token_data}, safe=False)
	if request.method == 'POST':
		data = request.POST
		if not data:
    		return _error_response(request, "Failed.  No data received")
		response = requests.post('http://models-api:8000/api/v1/user/', data = data)
		response_data = json.loads(response.text)
		return JsonResponse({'result': response_data}, safe=False)
    return _error_response(request, "Failed.  Use post")

#User:  login user with token and return true or false
@csrf_exempt
def login(request):
	if request.method == 'POST':
		data = request.POST
		if not data:
			return JsonResponse({'fail': "no POST data received"}, safe=False)
		response = requests.post('http://models-api:8000/api/v1/authenticator/login/', data = data)
		#login_resp = json.loads(login_resp.text)#should return true if login successful or throw an error
		response_data = json.loads(response.text)
		return JsonResponse({'result': response_data}, safe=False)
		#return JsonResponse({'login_resp': login_req}, safe=False)
    return _error_response(request, "Failed.  Use post")

#User:  logout user with token and return true or false
def logout(request):
	if request.method == 'POST':
		data = request.POST
		if not data:
			return JsonResponse({'fail': "no POST data received"}, safe=False)
		response = requests.post('http://models-api:8000/api/v1/authenticator/logout/', data = data)
		response_data = json.loads(response.text)
		return JsonResponse({'result': response_data}, safe=False)
    return _error_response(request, "Failed.  Use post")


#User + course:  Check if user is logged in with token.  If true, post listing with token and listing text.
def create_listing(request):
	#check if user is authenticated correctly
	
	if request.method == 'POST':
		data = request.POST
		if not data:
			return JsonResponse({'fail': "no POST data received"}, safe=False)
		response = requests.post('http://models-api:8000/api/v1/course/', data = data)
		response_data = json.loads(response.text)
		return JsonResponse({'result': response_data}, safe=False)
    return _error_response(request, "Failed.  Use post")
	

def _error_response(request, error_msg):
    return JsonResponse({'work': False, 'msg': error_msg}, safe=False)

def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'work': True, 'resp': resp}, safe=False)
    else:
        return JsonResponse({'work': True})