import os, os.path
import json

import platform
import shutil

from django.shortcuts import render
from django.http import HttpResponse
from .. import models
from .. import serializers
from rest_framework import generics
from .backup_conf import *
from .code_based_conf import *
from .restore_conf import *
from .routing_conf import *
from .setting_conf import *
from .routing_conf_ipv6 import *
from .vlan_conf import *
from ..models import Connect, Ip, c_Setting as settings
ip_list = []


#method resource server
def infoprocessor():
	with open("/proc/cpuinfo", "r")  as f:
    		info = f.readlines()
	cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
	for index, item in enumerate(cpuinfo):
    		return ("    " + str(index) + ": " + item)
def loadd():
	with open("/proc/loadavg", "r") as f:
    		a=f.read().strip()
	return a

def uptimes():
	with open("/proc/uptime", "r") as f:
    		uptime = f.read().split(" ")[0].strip()
	uptime = int(float(uptime))
	uptime_hours = uptime // 3600
	uptime_minutes = (uptime % 3600) // 60
	return (str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

def hddtotal():
	total, used, free = shutil.disk_usage("/")
	return total/(2**30)

def hddused():
	total, used, free = shutil.disk_usage("/")
	return used/(2**30)



def hddfree():
	total, used, free = shutil.disk_usage("/")
	return free/(2**30)


def mem1():
	with open("/proc/meminfo", "r") as f:
    		lines = f.readlines()
	return (lines[0].strip())


def mem2():
	with open("/proc/meminfo", "r") as f:
    		lines = f.readlines()
	return (lines[1].strip())

def distribution():
	dist = platform.dist()
	dist = " ".join(x for x in dist)
	return dist




def index(request):
	# if request.method == "GET":
	HDD1=hddtotal()
	HDD2=hddused()
	HDD3=hddfree()
	sys=platform.system()
	Distribution=distribution()
	Node=platform.node()
	arsitek=(platform.architecture()[0])
	Infoprocessor=infoprocessor()
	load_cpu=loadd()
	UpTime=uptimes()
	free=mem1()
	total=mem2()
	count_all = Connect.objects.all().count()
	vendor_all = settings.objects.all().count()
	print (count_all)
	context={'freehdd':HDD3,'usedhdd':HDD2,'totalhdd':HDD1,'distribution':Distribution,'node':Node,'arsitektur':arsitek,'memfree':free,'memtotal':total,'uptime':UpTime,'loadcpu':load_cpu,'infoprocessor':Infoprocessor,'system':sys,'count_all':count_all,'vendor_all':vendor_all}
	return render(request, 'index.html',context)




def verifip(request):
	print ("verifikasi ip")

def ip_validation(request):
	
	if request.method == 'POST':
		if request.is_ajax():
			ip_list_json = request.POST.get('iplist')
			ok_ip_list = []
			print (ip_list_json)
			print ("Checking the connection.....")
			response = os.system("ping -c 3 " + ip_list_json)
			respon_koneksi = " "
			if response == 0 :
				respon_koneksi = ip_list_json+" is connected"
				# print respon_koneksi
			else:
				respon_koneksi = ip_list_json+" is not connected"

			print (respon_koneksi)
			data = {'respon_koneksi': respon_koneksi}
			return HttpResponse(
				json.dumps(data)
			)
	else:
		passes = "nothing"
		return HttpResponse(content_type="application/json")

#def config_static_ipv6(request):
#	return render(request, 'config/routing_static_ipv6.html')

#def config_dynamic_ipv6(request):
#	return render(request, 'config/routing_dynamic_ipv6.html')


def history(request):
	return render(request, 'history.html')

# def read_file_static(request):
# 	if request.method == 'GET':
# 		showCode_dir = os.path.join(settings.MEDIA_ROOT, "showCode/")
# 		print (showCode_dir+'routing_conf.py')
# 		f = open(showCode_dir+'routing_conf.py', 'r')
# 		file_content = f.read()
# 		f.close()
# 		context = {'file_content': file_content}
# 		return render(request, "config/routing_static.html", context)

class LoginInfo(generics.ListCreateAPIView):
	queryset = models.Connect.objects.all()
	serializer_class = serializers.AutonetSerializer

class LoginInfoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Connect.objects.all()
	serializer_class = serializers.AutonetSerializer

class IpInfo(generics.ListCreateAPIView):
	queryset = models.Ip.objects.all()
	serializer_class = serializers.IpAutonetSerializer

class IpInfoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Ip.objects.all()
	serializer_class = serializers.IpAutonetSerializer

class DataInfo(generics.ListCreateAPIView):
	queryset = models.Connect.objects.all()
	serializer_class = serializers.DataAutonetSerializer
