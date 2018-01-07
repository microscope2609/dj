
#-*-coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from collections import OrderedDict


def index(request):

	link =OrderedDict([('Home','#'),('Article','#'),('Tutorial','#'),('E-Paper','#'),('Result','#'),('Contact','#')])
	return render_to_response("index.html",{'list':link.items()})


def login(request):
	link =OrderedDict([('Home','home'),('Post','#'),('E-Paper','#'),('Q.O.D.','#'),('Article','#'),('Tutorial','#')])
	return render_to_response("login.html",{'list':link.items()})
	
def user_agent(request):
	link =OrderedDict([('Home','home'),('Post','#'),('E-Paper','#'),('Q.O.D.','#'),('Article','#'),('Tutorial','#')])
	return render_to_response('test.html',{'list':link.items()})