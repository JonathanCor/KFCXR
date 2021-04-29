__author__ = 'Jonathan Corvers'


class Malpractice:

    counter = 1

    def __init__(self, title, explanation, image_ref=None):
        self.title = title
        self.explanation = explanation
        self.image_ref = image_ref
        self.counter = Malpractice.counter
        Malpractice.counter += 1
