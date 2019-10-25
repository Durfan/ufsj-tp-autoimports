from django.shortcuts import render

def index(request):
	return render(request, 'automoney/index.html')
