__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


WORKING_CONDITIONS = MalpracticeCategory(name='Werkomstandigheden', reference='workingConditions')


malpractice = Malpractice(title='Sluit je aan bij een vakbond!',
                          explanation='Onrechtvaardigheden op de werkvloer van KFC zijn niet het gevolg van een paar '
                                      'rotte appels. Dergelijke slechte werkomstandigheden zijn een structureel '
                                      'probleem want KFC is een multinational waar het machtsevenwicht tussen '
                                      'aandeelhouders en individuele werknemers extreem ongelijk is. Met andere '
                                      'woorden: zorg dat je bij een vakbond aangesloten bent!')

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='In 2012, kreeg KFC een boete voor kinderarbeid in Australië',
                          explanation='In 2012 kreeg KFC in Australië een boete voor kinderarbeid. Als KFC zo '
                                      'onachtzaam omgaat met kinderarbeid in een geïndustrialiseerd land, wil je dan '
                                      'nog weten hoe hun bevoorradingsketen eruit ziet?',
                          url_ref=['https://thewest.com.au/news/wa/kfc-fined-over-child-labour-ng-ya-285294'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Werk voor KFC, word verplicht om je buren te vergiftigen',
                          explanation='Werknemers van KFC Auckland protesteerden omdat ze geforceerd werden om '
                                      'vervallen producten te verkopen.',
                          url_ref=['https://www.stuff.co.nz/business/119908028/kfc-workers-say-they-were-bullied-for-telling-managers-not-to-sell-expired-chicken'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC geeft niet om werknemers',
                          explanation='In 2018 waren er bij KFC problemen met de bevoorrading. De kaderleden waren '
                                      'verantwoordelijk voor de bevoorradingsketen, maar het waren de lokale '
                                      'werknemers die in de vorm van loonsverlagingen voor de kosten moesten '
                                      'opdraaien.',
                          url_ref=['https://www.cornwalllive.com/news/local-news/angry-kfc-workers-say-not-1235512'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC discrimieert schaamteloos werknemers met een handicap',
                          explanation='Er waren publieke protesten en een vakbond nodig om ervoor te zorgen dat '
                                      'werknemers, die op die grond ontslagen waren, terug aan het werk konden.',
                          url_ref=['https://www.nzherald.co.nz/nz/kfc-calls-back-disabled-staff/6DPE42EYBYFZ7FN3HICXKGLXY4/',
                                   'https://www.tvnz.co.nz/content/tvnz/onenews/story/2013/09/01/kfc-s-new-employment-policy-unfair-and-unjust-labour.html?utm_variant=taboola_visible_1'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)

