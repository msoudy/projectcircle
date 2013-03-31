from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect


def index(request):
	# return circleight mates array of 8 users with pics
	# return interests array of 8 with pics
	# events array of 8 with pics
	return render_to_response ('circleight/index.html')

# returns an array of 
def getUserPosts(request, username):
	return 1
