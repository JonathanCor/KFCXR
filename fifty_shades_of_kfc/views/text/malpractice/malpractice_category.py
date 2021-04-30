__author__ = 'Jonathan Corvers'


class MalpracticeCategory:

    def __init__(self, name, reference, image_ref=None):
        self.name = name
        self.malpractices = list()
        self._image_ref = image_ref
        self.reference = reference

    def add_malpractice(self, malpractice):
        self.malpractices.append(malpractice)

    @property
    def image_ref(self):
        if self._image_ref:
            return self._image_ref

        if self.reference == 'animalWelfare':
            return 'http://xrchippenham.earth/wp-content/uploads/2020/10/XR-Song-Thrush-2.png'
        elif self.reference == 'workingConditions':
            return 'https://rebellion.global/assets/img/wood-blocks/bee2.svg'
        elif self.reference == 'climateEnvironment':
            return 'https://rebellion.global/assets/img/wood-blocks/hourglass.svg'
        elif self.reference == 'health':
            return 'https://rebellion.global/assets/img/wood-blocks/orchid.svg'
        elif self.reference == 'localCommunity':
            return 'https://rebellion.global/assets/img/wood-blocks/tree.svg'
        else:
            return ''
