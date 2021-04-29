__author__ = 'Jonathan Corvers'

from django.shortcuts import render


def index(request):
    try:
        language = request.session['language']
    except KeyError:
        request.session['language'] = 'EN'
        language = 'EN'

    if language == 'NL':
        from .text.dutch.index import TITLE, CARD_TITLE_1, CARD_TITLE_2, CARD_TITLE_3, CARD_TITLE_4, CARD_TITLE_5, GREY_CARD
    else:
        from .text.english.index import TITLE, CARD_TITLE_1, CARD_TITLE_2, CARD_TITLE_3, CARD_TITLE_4, CARD_TITLE_5, GREY_CARD

    context = {
        'title': TITLE,
        'card_title_1': CARD_TITLE_1,
        'card_title_2': CARD_TITLE_2,
        'card_title_3': CARD_TITLE_3,
        'card_title_4': CARD_TITLE_4,
        'card_title_5': CARD_TITLE_5,
        'grey_card': GREY_CARD
    }

    return render(request=request, context=context, template_name='consumer/index.html')
