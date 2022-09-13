from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text') 
    

    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    removeline = request.POST.get('removeline','off')
    removespace = request.POST.get('removespace','off')
    charcount = request.POST.get('charcount','off')

    if removepunc=='on':
        analyzed_text = ''
        punctuation_marks = string.punctuation

        for char in djtext:
            if char not in punctuation_marks and char not in '\n':
                analyzed_text += char
        djtext=analyzed_text
    

    
    if uppercase=='on':
        analyzed_text = ''
        analyzed_text+=djtext.upper()
        djtext=analyzed_text
    

    
    if removespace=='on':
        analyzed_text = ''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed_text += char
        djtext=analyzed_text        
    

    
    if removeline=='on':
        analyzed_text = ''
        for char in djtext:
            if char!='\n' and char!='\r' :
                analyzed_text += char
        djtext=analyzed_text
    
    
    if charcount=='on':
        analyzed_text = ''
        count=0
        for char in djtext:
            count+=1
        analyzed_text = 'the number of characters are: ' + str(count)
    
    return render(request,'analyze.html',{"analyzed_text":analyzed_text})

