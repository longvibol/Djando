from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("January Challenge")

def monthly_challenges(request, month):
    challenge_text = None
    if month == "jan":
        challenge_text = "January Challenge"
    elif month == "feb":
        challenge_text = "February Challenge"
    elif month == "mar":
        challenge_text = "March Challenge"
    elif month == "apr":
        challenge_text = "April Challenge"
    elif month == "may":
        challenge_text = "May Challenge"    
    elif month == "jun":
        challenge_text = "June Challenge"
    elif month == "jul":
        challenge_text = "July Challenge"
    elif month == "aug":
        challenge_text = "August Challenge"
    elif month == "sep":
        challenge_text = "September Challenge"  
    elif month == "oct":
        challenge_text = "October Challenge"
    elif month == "nov":
        challenge_text = "November Challenge"
    elif month == "dec":
        challenge_text = "December Challenge"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)