from django.shortcuts import render

from recruit_test.settings import TEMPLATES


def hello(request):
    if request.method == 'GET': 
        
        name = request.GET.get('name', 'незнакомец')
        message = request.GET.get('message', 'Хочешь мне что-то сказать?')
        hello_message = f'Hello {name}!'
        welcome_message = f'{message}'
        
        content = {
            'hello_message': hello_message,
            'welcome_message': welcome_message,
        }
        address = "{}/hello_page.html".format(TEMPLATES[0]['DIRS'][0])
        
        return render(request, address, context=content)