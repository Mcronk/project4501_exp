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
	course = course_data['resp']
	
	
	return _success_response(request, course_data['resp'])

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
	# data = request.POST
	# auth_req = requests.post('http://models-api:8000/api/v1/user/')
	# token_data = json.loads(token_data.text)#should return the auth Token to be put in cookies.
	# return JsonResponse({'token_data': token_data}, safe=False)
	if request.method == 'POST':
		data = request.POST
		if not data:
			return _error_response(request, "Failed.  No data received")
		# try:
		# 	data['grade'] = 0
		# except:
		# 	return _error_response(request, "Failed!")
		response = requests.post('http://models-api:8000/api/v1/user/', data = data)
		response_data = json.loads(response.text)
		return JsonResponse({'result': response_data}, safe=False)
	return _error_response(request, "Failed. Use post")

#User:  login user with token and return true or false
@csrf_exempt
def login(request):
	if request.method == 'POST':
		data = request.POST
		if not data:
			return JsonResponse({'fail': "no POST data received"}, safe=False)
		response = requests.post('http://models-api:8000/api/v1/authenticator/login/', data = data)
		#login_resp = json.loads(login_resp.text)#should return true if login successful or throw an error
		resp_data = json.loads(response.text)
		if not resp_data or not resp_data['work']:
		  	# couldn't log them in, send them back to login page with error
			return _error_response(request, resp_data['msg'])
		return _success_response(request, {'authenticator': resp_data['resp']['authenticator']})
		#return JsonResponse({'login_resp': login_req}, safe=False)
	return _error_response(request, "Failed. Use post")

#User:  logout user with token and return true or false
@csrf_exempt
def logout(request):
	if request.method == 'POST':
		data = request.POST
		if not data:
			return JsonResponse({'fail': "no POST data received"}, safe=False)
		response = requests.post('http://models-api:8000/api/v1/authenticator/logout/', data = data)
		resp_data = json.loads(response.text)
		if not resp_data or not resp_data['work']:
			return _error_response(request, resp_data['msg'])
		return _success_response(request)
	return _error_response(request, "Failed. Use post")


#User + course:  Check if user is logged in with token.  If true, post listing with token and listing text.
@csrf_exempt
def create_course(request):
	#receive authenticator
	#send authenticator
	#get user_pk or false back
	#package user_pk with course 
	#give back response I will get the UserID

	if request.method == 'POST':
		post_data = request.POST
		data = dict(post_data.dict())
		if not data:
			return _error_response("no POST data received")
		#get authenticator
		authenticator = data['authenticator']
		data_auth={'authenticator':authenticator}
		#send authenticator
		response = requests.post('http://models-api:8000/api/v1/authenticator/check/', data = data_auth)
		resp_data = json.loads(response.text)
		if not resp_data or not resp_data['work']:
			return _error_response(request, resp_data['msg'])
		#get user_pk
		tutor_pk = resp_data['resp']['tutor']
		# if (username == "false")
		# 	return _error_response(request, "Failed. Authenticator does not match username")
		# listing = request.POST
		del data['authenticator']
		data['tutor'] = tutor_pk
		data['popularity'] = 0
		course_resp = requests.post('http://models-api:8000/api/v1/course/', data = data)
		resp_data = json.loads(course_resp.text)
		if not resp_data or not resp_data['work']:
			return _error_response(request, resp_data['msg'])
		return _success_response(request, {'course_pk': resp_data['resp']['course_pk']})
	return _error_response(request, "Failed. Use post")
	

def _error_response(request, error_msg):
	return JsonResponse({'work': False, 'msg': error_msg}, safe=False)

def _success_response(request, resp=None):
	if resp:
		return JsonResponse({'work': True, 'resp': resp}, safe=False)
	else:
		return JsonResponse({'work': True})