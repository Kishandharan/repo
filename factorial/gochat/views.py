from django.shortcuts import render
from .factorial import fact

# Create your views here.
def ren(request):
    input = 6
    result = fact(input)
    return render(request,"index.html", {"param1":result, "param2":input})
