__author__ = 'Jonathan Corvers'

from django.http import HttpResponseRedirect
from django.urls import reverse


def set_session_language_in_category(request, category_reference, language):

    request.session['language'] = language
    return HttpResponseRedirect(reverse('fifty_shades_of_kfc:viewCategory', args=(category_reference,)))
