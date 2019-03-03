from django.shortcuts import render

# Create your views here.

def chanjong(request):
   
    return render(request, 'chanjong.html')

def chanjong2(request):
    
    a1 =  float(request.POST['a1']     )
    b1 =  int(request.POST['b1'] )
    a2 =  float(request.POST['a2']     )
    b2 =   int(request.POST['b2'] )
    a3 =  float(request.POST['a3']     )
    b3 =   int(request.POST['b3'] )
    a4 =   float(request.POST['a4']    )
    b4 =   int(request.POST['b4'] )
    a5 =   float(request.POST['a5']    )  
    b5 =   int(request.POST['b5'] )
    a6 =   float(request.POST['a6']    )  
    b6 =   int(request.POST['b6'] )
    a7 =   float(request.POST['a7']    )
    b7 =   int(request.POST['b7'] )
    a8 =   float(request.POST['a8']    )
    b8 =   int(request.POST['b8'] )

    total = a1*b1 + a2*b2 + a3*b3 + a4*b4 + a5*b5 + a6*b6 + a7*b7 + a8*b8
    hours = b1+b2+b3+b4+b5+b6+b7+b8
    result = total/hours
    result = round(result, 2)
    return render(request, 'chanjong2.html', {'result':result})