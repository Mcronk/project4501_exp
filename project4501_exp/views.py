import urllib.request
import urllib.parse
import json
from django.http import JsonResponse


#api/v1/homePageCourse
def homePageCourse(request, class_id, info_id):
		resp_json = {}
		req = urllib.request.Request('CoursePlaceholder.url', class_id = class_id)
		resp_json["course"] = urllib.request.urlopen(req)
		req = urllib.request.Request('infoPlaceholder.url', info_id = info_id)
		resp_json["info"] = urllib.request.urlopen(req)
		print(resp_json)
		return JsonResponse(resp_json)


#api/v1/productPageCourse
def productPageCourse(request, class_id, info_id):
		resp_json = {}
		req = urllib.request.Request('CoursePlaceholder.url', class_id = class_id)
		resp_json["course"] = urllib.request.urlopen(req)
		req = urllib.request.Request('infoPlaceholder.url', info_id = info_id)
		resp_json["info"] = urllib.request.urlopen(req)
		print(resp_json)
		return JsonResponse(resp_json)
