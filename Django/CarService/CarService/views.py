from django.http import HttpResponse
from django.shortcuts import render
def control(request):
    if request.method == 'GET':
        context = {}
        context['hello'] = 'hello world'
        return render(request,'NotFound.html',context)
    else:
        if request.method == "POST":
            forward = request.POST.get('forward')
            return HttpResponse(forward)