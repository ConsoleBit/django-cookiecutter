from django.http import JsonResponse
from django.shortcuts import render

{% if cookiecutter.api == "y" or cookiecutter.api == "Y" %}
from rest_framework import status
{% else %}
from django.shortcuts import render
{% endif %}

def handler404(request, exception):
	{% if cookiecutter.api == "y" or cookiecutter.api == "Y" %}
    data = {
        'errors': {'not_found': 'This URL does not exist'},
        'status': False,
        'status_code': status.HTTP_404_NOT_FOUND

    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    {% else %}
    return render(request, '404.html')
	{% endif %}



def handler500(request):
	{% if cookiecutter.api == "y" or cookiecutter.api == "Y" %}
    data = {
        'error': {'server_error': 'Server Error (500)'},
        'status': False,
        'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    {% else %}
    return render(request, '500.html')
    {% endif %}