#i have createe
#aman Shrivastava

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("hello this is amanshrivastvaa")

def navigator(request):
    djtext = request.GET.get('text')
    print(djtext)
    return HttpResponse('''<h1> website navigator </h1> <a href="https://www.geeksforgeeks.org/django-tutorial/"><h2>gfg blog<h2></a>''')

#Check Checkbox Values

def analyze(request):
    djtext = request.GET.get('text','default'),
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    newlineremover = request.GET.get('newlineremover','off')

    #Check Whick checkbox is Open-> removepunc/ uppercase
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"/,-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctations','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    elif uppercase == "on" :
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on" :
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+char
        params = {'purpose': 'newline removed', 'analyzed_text': analyzed }
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error404")