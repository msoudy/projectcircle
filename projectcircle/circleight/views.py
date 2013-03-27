from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect


def index(request):
	return render_to_response ('circleight/index.html')

# returns an array of 
def getUserPosts(request, username):
	return 1
