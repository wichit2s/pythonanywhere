from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'pokemon/index.html')

def atimesb(req, fn):
    print(f'ส่ง fn = {fn}')
    if fn == 'integration':
        print(req.body)
        data = {}
        for pair in str(req.body)[2:-1].split('&'):
            try:
                kv = pair.split('=')
                data[kv[0]] = kv[1]
            except: pass
        for k,v in data.items():
            print(k, v)
        return render(req, 'pokemon/index.html', data)
    elif fn == 'differentiate':
        pass
    a = 20
    b = 9
    c = a*b
    return render(req, 'pokemon/index.html', { 
        'a': a, 
        'b': b, 
        'c': c})