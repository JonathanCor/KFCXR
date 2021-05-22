__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


ANIMAL_WELFARE = MalpracticeCategory(name='Animal Welfare', reference='animalWelfare')


malpractice = Malpractice(title='21 Fully grown chickens into 1m²',
                          explanation='In more than 80 procent of the cases, KFC squeezes twenty-one fully grown '
                                      'chickens into a single square meter, try to imagine that for a moment.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC Chickens never see the sun',
                          explanation='Half of KFC chickens don\'t see the sun a single time in their entire short '
                                      'life.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='painful infections',
                          explanation='1 in 3 KFC chickens suffers from painful infections.',
                          url_ref=['https://joop.bnnvara.nl/nieuws/kfc-geeft-toe-een-derde-van-de-kippen-lijdt-aan-pijnlijke-ontstekingen'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Broiler chickens',
                          explanation='In 30 days, a chick is forced to grow to a monstrous 1.8kg. '
                                      'These chickens have been selectively bred to grow that fast. '
                                      'This causes a great deal of suffering to the animals.',
                          url_ref=['https://kfc.nl/kfc-jaarlijks-voortgangsverslag-over-kippenwelzijn.pdf'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Big chicken coop means big responsibility',
                          explanation='Per year, KFC kills about 1 billion chickens (record of 2014). '
                                      'That is, they have an outsized responsability in animal welfare.',
                          url_ref=['https://ifakfcbucketcouldtalk.weebly.com/if-a-bucket-of-kfc-could-talk-blog'])

ANIMAL_WELFARE.add_malpractice(malpractice=malpractice)
