from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    result=None
    if request.method=='POST':
        try: 

            a=int(request.POST.get('NUM1'))
            b=int(request.POST.get('NUM2'))
            op=request.POST.get('op')
            if op == 'add':
                result=a+b
                return redirect('hello',result=result)
            else:
                return render(request,'home.html',{'error': 'Invalid Operator'})
        except ValueError:
            return render(request, 'home.html', {'error': 'Please enter valid numbers.'})
    return render(request,'home.html', {})
def hello(request,result):
    return render(request, 'result.html', {'result':result})
