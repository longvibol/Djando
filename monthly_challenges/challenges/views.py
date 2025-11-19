from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges_dict = {
    "jan": "January Challenge d",
    "feb": "February Challenge d",
    "mar": "March Challenge d",
    "apr": "April Challenge",
    "may": "May Challenge",
    "jun": "June Challenge",
    "jul": "July Challenge",
    "aug": "August Challenge",
    "sep": "September Challenge",
    "oct": "October Challenge",
    "nov": "November Challenge",
    "dec": "December Challenge"
}

def monthly_challenges_dict_view(request, month):
    try:
        challenges_text = monthly_challenges_dict[month]
        return HttpResponse(challenges_text)
    except:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenges_response_number(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound("This month is not supported")
    
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)    

# print(forwar_month)
months = list(monthly_challenges_dict.keys())
months1 = list(monthly_challenges_dict.keys())
for i in range(len(months)):
    forward_month = months[i]
    # print(forward_month)
# print(type(forwar_month))

print(months1[0])
print(type(months1))



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