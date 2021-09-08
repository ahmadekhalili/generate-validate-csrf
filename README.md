# generate-validate-csrf

for activing csrf validation change DEFAULT_AUTHENTICATION_CLASSES in settings to CustomSessionAuthentication. example:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'app1.custom_authentication.CustomSessionAuthentication',
    ),
    ...
    }
	
generate_csrf.py:
request_csrf_token should be in request body. example: <input type="hidden" name="csrfmiddlewaretoken" value={{ request_csrf_token }}>
csrftoken should be in rquest header. example: "csrftoken=put csrf_token value"

validate_csrf.py:
enforce_csrf method compare two csrf sended and if matched return None else raise proper error message. you can disable csrf validation by return None in first of enforce_csrf method.
validating of csrfs sended to enforce_csrf method will done automatically by CustomSessionAuthentication when user is login but for unauthenticated users you should use handy in signin and signup. example:

username, password = 'user1', '123'
CustomSessionAuthentication().enforce_csrf(request)
login(request, user)