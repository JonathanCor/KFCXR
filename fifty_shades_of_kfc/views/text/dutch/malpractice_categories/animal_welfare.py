__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


ANIMAL_WELFARE = MalpracticeCategory(name='Dierenwelzijn', reference='animalWelfare')


malpractice = Malpractice(title='21 volgroeide kippen per 1m²',
                          explanation='In meer dan 80 procent van de gevallen propt KFC 21 volgroeide kippen op één '
                                      'vierkante meter. Probeer u dat even voor te stellen.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC kippen zien nooit de zon',
                          explanation='De helft van de kippen zien in hun korte leven niet één keer het zonlicht.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Pijnlijke infecties',
                          explanation='1 op 3 KFC-kippen lijdt aan pijnlijke infecties.',
                          url_ref=['https://joop.bnnvara.nl/nieuws/kfc-geeft-toe-een-derde-van-de-kippen-lijdt-aan-pijnlijke-ontstekingen'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Plofkippen',
                          explanation='KFC forceert hun kuikens om op 30 dagen tijd tot een monstreuze kip van 1,8 '
                                      'kilo te groeien. '
                                      'Dit veroorzaakt veel lijden voor de kippen.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Grote kippenren betekent grote verantwoordelijkheid',
                          explanation='Per jaar doodt KFC ongeveer een miljard kippen. Dit toont hoe groot hun '
                                      'verantwoordelijkheid voor dierenwelzijn is.',
                          url_ref=['https://ifakfcbucketcouldtalk.weebly.com/if-a-bucket-of-kfc-could-talk-blog'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)
