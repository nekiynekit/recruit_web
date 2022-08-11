from django.shortcuts import render
from recruit_test.settings import TEMPLATES

import os


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
        template_dir = TEMPLATES[0]['DIRS'][0]
        address = os.path.join(template_dir, 'hello_page.html')
        
        return render(request, address, context=content)