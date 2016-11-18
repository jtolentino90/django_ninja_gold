from django.shortcuts import render, redirect
from random import randint

def index(request):
	try:
		request.session['gold']
	except:
		request.session['gold'] = 0
	try:
		request.session['comments']
	except:
		request.session['comments'] = [{'comment': 'Wecome to Ninja Gold'}]
	return render(request, "ninja_gold/index.html")

def process_gold(request):
	print(request.method)
	print(request.POST['building'])

	data = {
		'cave':randint(10,20),
		'farm': randint(10,15),
		'casino': randint(-50,50),
		'house': randint(5,10)
	}
	try:
		request.POST['building']
		request.session['gold'] += data[request.POST['building']]
		if data[request.POST['building']] > 0:
			style  = 'gained'
		else:
			style = 'lost'
		request.session['comments'].append({'comment':"You entered the {} and {} {} gold.".format(request.POST['building'], style, data[request.POST['building']])})
	except:
		print 'fail'
	return redirect('/')

def reset(request):
	print(request.method)
	request.session.pop('gold')
	request.session.pop('comments')
	return redirect('/')
