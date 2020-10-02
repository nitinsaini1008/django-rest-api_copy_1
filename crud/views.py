from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from .models import About
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import AboutForm
@method_decorator(csrf_exempt,name='dispatch')
class Apiclass(View):
	def get(self,request,*args,**kwargs):
		data=request.body
		try:
			js_obj=json.loads(data)
			print(js_obj)
			if 'id' in js_obj:
				d=js_obj['id']
				try:
					emp=About.objects.get(id=d)
					data=serialize('json',[emp,])
					data=json.loads(data)
					ans=[]
					for i in data:
						t=i['fields']
						ans.append(t)
					ans=json.dumps(ans)
					return HttpResponse(ans,content_type='application/json')
				except:
					json_data=json.dumps({'msg':'incorrect id'})
					return HttpResponse(json_data,content_type='application/json')
			else:
				emp=About.objects.all()
				data=serialize('json',emp)
				data=json.loads(data)
				ans=[]
				for i in data:
					t=i['fields']
					ans.append(t)
				ans=json.dumps(ans)
				return HttpResponse(ans,content_type='application/json')
		except:
			json_data=json.dumps({'msg':'not in proper formate'})
			return HttpResponse(json_data,content_type='application/json')
	def post(self,request,*args,**kwargs):
		data=request.body
		try:
			js_obj=json.loads(data)
			f=AboutForm(js_obj)
			if f.is_valid():
				f.save(commit=True)
				json_data=json.dumps({'msg':'saved success'})
				return HttpResponse(json_data,content_type='application/json')
			else:
				data=json.dumps(f.errors)
				return HttpResponse(data,content_type='application/json')
		except:
			json_data=json.dumps({'msg':'not in proper formate'})
			return HttpResponse(json_data,content_type='application/json')
	def put(self,request,*args,**kwargs):
		data=request.body
		try:
			js_obj=json.loads(data)
			if 'id' not in js_obj:
				json_data=json.dumps({'msg':'required id'})
				return HttpResponse(json_data,content_type='application/json')
			else:
				try:
					emp=About.objects.get(id=js_obj['id'])
					obj_data={
						'name':emp.name,
						'sub':emp.sub,
						'num':emp.num
					}
					obj_data.update(js_obj['fields'])
					f=AboutForm(obj_data,instance=emp)
					if f.is_valid():
						f.save(commit=True)
						json_data=json.dumps({'msg':'update success'})
						return HttpResponse(json_data,content_type='application/json')
					else:

						json_data=json.dumps({'msg':'invalid fields is given'})
						return HttpResponse(json_data,content_type='application/json')
				except:
					json_data=json.dumps({'msg':'invalid id'})
					return HttpResponse(json_data,content_type='application/json')
		except:
			json_data=json.dumps({'msg':'not in proper formate'})
			return HttpResponse(json_data,content_type='application/json')

	def delete(self,request,*args,**kwargs):
		data=request.body
		try:
			js_obj=json.loads(data)
			try:
				emp=About.objects.get(id=js_obj['id'])
				a,b=emp.delete()
				if a==1:
					json_data=json.dumps({'msg':'delete success'})
					return HttpResponse(json_data,content_type='application/json')
				else:
					json_data=json.dumps({'msg':'unable to delete'})
					return HttpResponse(json_data,content_type='application/json')
			except:
				json_data=json.dumps({'msg':'required a valid id'})
				return HttpResponse(json_data,content_type='application/json')
		except:
			json_data=json.dumps({'msg':'not in proper formate'})
			return HttpResponse(json_data,content_type='application/json')

