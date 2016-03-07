from django.shortcuts import render
from .conekta import new_charge


def home(request):
	if request.method == "POST":
		print "entre a post"
		card = {
			'number' : request.POST['number'],
			'exp_month' : request.POST['month'],
			'exp_year' : request.POST['year'],
			'cvc' : request.POST['cvc'],
		}
		print card
		charge = new_charge(card)
		print charge.status
		return redirect('/congrats')

	return render(request,'main/index.html')

	# def post(self, request, *arg, **kwargs):
	# 	card = {
	# 		'number' : request.POST['number'],
	# 		'exp_month' : request.POST['month'],
	# 		'exp_year' : request.POST['year'],
	# 		'cvc' : request.POST['cvc'],
	# 	}
	# 	charge = new_charge(card)
	# 	print charge.status
	# 	return redirect('/congrats')