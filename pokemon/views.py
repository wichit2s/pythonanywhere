from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'pokemon/index.html')

def atimesb(req, fn):
    print(f'ส่ง fn = {fn}')
    if fn == 'integration':
        print(req.body)
    elif fn == 'differentiate':
        pass
    a = 20
    b = 9
    c = a*b
    return render(req, 'pokemon/index.html', { 'a': a, 'b': b, 'c': c})