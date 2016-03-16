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
def create_account(request, username = '', password = ''):
	auth_req = requests.post('http://models-api:8000/api/v1/create_account/'+ username + '/' + password)
	token_data = json.loads(token_data.text)#should return the auth Token to be put in cookies.
	return JsonResponse({'token_data': token_data}, safe=False)

#User:  login user with token and return true or false
@csrf_exempt
def login(request):
	if request.method == 'POST':
		info = request.POST.get('data')
		login_req = requests.post('http://models-api:8000/api/v1/authenticator/login/', data = json.dumps(info))
		#login_resp = json.loads(login_resp.text)#should return true if login successful or throw an error
		login_data = json.loads(login_req.text)
		return JsonResponse({'result': login_data}, safe=False)
		return JsonResponse({'login_resp': login_req}, safe=False)
	return JsonResponse({'msg': "use POST"}, safe=False)

#User:  logout user with token and returnf true or false
def logout(request, token = ''):
	logout_req = requests.get('http://models-api:8000/api/v1/authenticator/logout/' + str(token))
	logout_resp = json.loads(logout_resp.text)#should return true if login successful or throw an error
	return JsonResponse({'logout_resp': logout_resp}, safe=False)

#User + Listing:  Check if user is logged in with token.  If true, post listing with token and listing text.
def create_listing(request, token = ''):
	return None
	# checkAuth = requests.post('http://models-api:8000/api/v1/authenticator/login' + str(token))
	# checkAuth_resp = json.loads(checkAuth_resp.text)#should return true if logged in and listing posed successfully.
	# if (checkAuth_resp['status'] == 'sucess') 
	# 	create_listing = requests.post('http://models-api:8000/api/v1/course/', info = info)
	# 	listing_resp = json.loads(listing_resp.text)#should return true if logged in and listing posed successfully.
	# 	return JsonResponse({'listing_resp': listing_resp}, safe=False)
	# else:
	# 	return JsonResponse({'listing_resp': "error"}, safe=False)

#name password email phone description.