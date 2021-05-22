__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


LOCAL_COMMUNITY = MalpracticeCategory(name='Local Community', reference='localCommunity')


malpractice = Malpractice(title='No room for local businesses',
                          explanation='Multinational companies like KFC drive up rent prices, pushing independent '
                                      'businesses already suffering from COVID towards bankruptcy.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='No democratic input',
                          explanation='With so many vacant buildings, is a KFC really what we need? '
                                      'It\'s not just how the economy works. These are policy decisions.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Beautiful historical city center?',
                          explanation='Big chains destroy the character of a city, '
                                      'do we want Leuven to look like any American town?')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='This is just the beginning',
                          explanation='Between 2019 and 2025, KCF wants to open 40 restaurants in Belgium.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)
