__author__ = 'Jonathan Corvers'

from django.http import HttpResponseRedirect
from django.urls import reverse


def set_session_language(request, language):

    request.session['language'] = language

    return HttpResponseRedirect(reverse('main_page:index'))
