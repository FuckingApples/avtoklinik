from http import HTTPStatus

from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(_):
    return HttpResponse(status=HTTPStatus.NO_CONTENT)
