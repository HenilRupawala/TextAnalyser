from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ''
        for char in djtext:
            if char not in punctuations:
                analysed += char
        params = {'purpose':"Removed Punctuations", 'analysed_text':analysed}
        djtext = analysed

    if capfirst == 'on':
        analysed = djtext.capitalize()
        params = {'purpose': "Capitalize first letter", 'analysed_text': analysed}
        djtext = analysed

    if newlineremove == 'on':
        analysed = ''
        for char in djtext:
            if (char != '\n' and char != '\r'):
                analysed += char
        params = {'purpose': "New line remover", 'analysed_text': analysed}
        djtext = analysed

    if spaceremove == 'on':
        analysed = ''
        for index,char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analysed += char
        params = {'purpose': "Space remover", 'analysed_text': analysed}
        djtext = analysed

    if charcount == 'on':
        analysed = 'Total character in the string is ',len(djtext)
        params = {'purpose': "Character count", 'analysed_text': analysed}

    if (removepunc != 'on' and capfirst != 'on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on'):
        return HttpResponse('Please select the operation.')

    return render(request, 'analyse.html', params)