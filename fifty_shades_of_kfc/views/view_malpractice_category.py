__author__ = 'Jonathan Corvers'

from django.shortcuts import render


def view_malpractice_category(request, category_reference):

    try:
        language = request.session['language']
    except KeyError:
        request.session['language'] = 'EN'
        language = 'EN'

    if language == 'NL':
        from .text.dutch.malpractice_categories import MALPRACTICE_CATEGORIES
        from .text.dutch.index import TITLE
    else:
        from .text.english.malpractice_categories import MALPRACTICE_CATEGORIES
        from .text.english.index import TITLE

    other_categories = set()
    current_category = None
    for reference, category in MALPRACTICE_CATEGORIES.items():
        if reference == category_reference:
            current_category = category
        else:
            other_categories.add(category)

    context = {
        'current_category': current_category,
        'other_categories': other_categories,
        'title': TITLE,
    }

    return render(request=request, context=context, template_name='consumer/malpractice_category.html')
