__author__ = 'Jonathan Corvers'

from django.http import HttpResponseRedirect
from django.urls import reverse


def set_session_language(request, language):

    request.session['language'] = language
    print(request.session['language'])
    print('cake')

    return HttpResponseRedirect(reverse('fifty_shades_of_kfc:index'))
