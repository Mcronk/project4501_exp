import urllib.request
import urllib.parse
import json
from django.http import JsonResponse


#api/v1/home
def home(request):
		resp_json = {}
		#req = urllib.request.Request('CoursePlaceholder.url', class_id = class_id)
		#resp_json["course"] = urllib.request.urlopen(req)
		#req = urllib.request.Request('infoPlaceholder.url', info_id = info_id)
		resp_json["info"] = "test"
		print(resp_json)
		return JsonResponse(resp_json)


#api/v1/product
def product(request, course_pk = ' '):
		req = urllib.request.Request('http://models-api:8000/api/v1/courses/'+course_pk)
		resp_json = urllib.request.urlopen(req).read().decode('utf-8')
		resp = json.loads(resp_json)
		return JsonResponse(resp, safe=False)
