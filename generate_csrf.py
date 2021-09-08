from django.middleware.csrf import get_token

request_csrf_token, csrf_token= get_token(request), get_token(request)

csrf_in_dict = {'csrfmiddlewaretoken': request_csrf_token, 'csrftoken': csrf_token}
