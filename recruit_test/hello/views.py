from django.shortcuts import render


def hello(request):
    if request.method == 'GET': 
        
        name = request.GET.get('name')
        message = request.GET.get('message')
        hello_message = f'Hello {name}!'
        welcome_message = f'{message}!'
        
        content = {
            'hello_message': hello_message,
            'welcome_message': welcome_message,
        }
        
        return render(request, 'hello_page.html', context=content)