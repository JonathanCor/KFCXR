__author__ = 'Jonathan Corvers'


class Malpractice:

    counter = 1

    def __init__(self, title, explanation, image_ref=None, url_ref=None):
        self.title = title
        self.explanation = explanation
        self.image_ref = image_ref
        self.counter = Malpractice.counter
        self.url_ref = url_ref
        Malpractice.counter += 1
