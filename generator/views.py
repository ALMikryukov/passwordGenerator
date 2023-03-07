from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def test(request):
    return  render(request, 'test.html')

def test_2(request):
    return render(request ,  'test_2.html')