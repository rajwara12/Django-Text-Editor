from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyzer(request):
    uptext = request.POST.get('text','default')
    print(uptext)
    removepunc = request.POST.get('removepunc','off') 
    fullcaps = request.POST.get('fullcaps','off') 
    lowercaps = request.POST.get('lowercaps','off') 
    removeextraspace = request.POST.get('removeextraspace','off') 
    newlineremover = request.POST.get('newlineremover','off') 
    if removepunc=='on':
        analyzed = ""
        punctions = ' .,?@!#$%^&*()_-=+ '
        for char in uptext:
            if char not in punctions:
                analyzed = analyzed + char        
        params={'purpose':'Remove Punctuations', 'analyzed_data':analyzed}
        uptext=analyzed  
         
    if fullcaps=='on':
        analyzed = "" 
        for char in uptext:
            analyzed = analyzed + char.upper()        
        params={'purpose':'Capitalization', 'analyzed_data':analyzed} 
        uptext=analyzed  
    if lowercaps=='on':
        analyzed = "" 
        for char in uptext   :
            analyzed = analyzed + char.lower() 
        params={'purpose':'Lowered All CAPS', 'analyzed_data':analyzed}
        uptext=analyzed  
    if removeextraspace=='on':
        analyzed=""
        for index, char in enumerate(uptext):
            if not (uptext[index]==" " and uptext[index+1]==" "):
                analyzed = analyzed+char 
        params={'purpose':'Remove Extra Spaces', 'analyzed_data':analyzed} 
        uptext=analyzed 
    if newlineremover=='on':
        analyzed=""
        for char in uptext:
            if char !="\n" and char != "\r":
                analyzed=analyzed+char  
        params={'purpose':'Remove New Lines', 'analyzed_data':analyzed}
      
     
    return render(request,'analyzer.html',params)  
                  




























        