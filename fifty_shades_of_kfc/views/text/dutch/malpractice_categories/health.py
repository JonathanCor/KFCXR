__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


HEALTH = MalpracticeCategory(name='Gezondheid', reference='health')


malpractice = Malpractice(title='KFC exists to maximize profit, not to maximize nutrition',
                          explanation='KFC heeft als doel om zijn eigen winst te maximaliseren. '
                                      'Maar je kan dan zeggen: \'Mag ik dan geen guilty pleasure hebben, af en toe '
                                      'eens ongezond eten?\' Natuurlijk wel, dat mag iedereen. Maar een bedrijf als '
                                      'KFC heeft niet als doel om aan deze occasionele guilty pleasure tegemoet te '
                                      'komen. Het wil dat je deze zin zo vaak mogelijk ervaart door jou te '
                                      'bombarderen met gerichte reclame, en door kinderen te lokken met speelgoed. '
                                      'Het voedsel is bewust verslavend, bij voorkeur voor een zo jong mogelijk '
                                      'publiek, om zo snel mogelijk zoveel mogelijk winst te maken, zonder oog te '
                                      'hebben voor de negatieve gezondheids- en milieu-impact.')

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Lege calorieën',
                          explanation='Junkfood zoals dat van KFC is ongezond, en bevat grote hoeveelheden calorieën '
                                      'aan suiker en vet.'
                                      'Junkfood heeft amper voedingswaarde, met zeer weinig vezels, '
                                      'vitamines en mineralen. Deze onvoedzame caloriën zijn een van de oorzaken van '
                                      'een wereldwijde obesitas-epidemie, ook wel \'Globesity\' genoemd door de '
                                      'Wereldgezondheidsorganisatie. Het verband tussen obesitas en junkfood is '
                                      'complex, de epidemische proporties van obesitas wereldwijd, als gevolg van een '
                                      'ongezond dieet leidt to andere gezondheidsrisico\'s en ziektes: '
                                      'hart- en vaatziekten, beroertes, hoge bloeddruk, diabetes, sommige kankers, '
                                      'galblaasaandoeningen, galstenen, osteoarthritis, jicht, ademproblemen '
                                      '(slaapapneu en astma)...',
                          url_ref=['https://www.who.int/activities/controlling-the-global-obesity-epidemic'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Slecht voor de huid',
                          explanation='Junkfood zoals dat van KFC verhoogt het risico op acne.',
                          url_ref=['https://www.healthline.com/nutrition/foods-that-cause-acne#TOC_TITLE_HDR_4'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Gefrituurd voedsel maakt je ziek',
                          explanation='Gefrituurd voedsel eten staat in verband met talrijke risico\'s op ziekte: '
                                      'onder andere hart- en vaatziekten, diabetes en obesitas',
                          url_ref=['https://pubmed.ncbi.nlm.nih.gov/26457715/'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Geraffineerd zout',
                          explanation='Fastfood bevat veel geraffineerde zouten (zoals keukenzout natriumchloride en '
                                      'smaakversterkers als natriumfosfaat en natriumglutamaat). '
                                      'Die zorgen voor een hoge bloeddruk (hypertensie), een grote risicofactor voor '
                                      'beroertes en andere hart- en vaatziekten.',
                          url_ref=['https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7318881/'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Azen op de kwetsbaren',
                          explanation='KFC maakt misbruik van lager opgeleiden en mensen die niet gewapend zijn met de '
                                      'kennis om door hun marketing-trucs te zien.',
                          url_ref=['https://www.researchgate.net/profile/Gabrielle-Jenkin/publication/315782915_Individuals_the_Environment_or_Inequalities_Industry_and_Public_Health_Framing_of_Obesity_and_its_Presence_in_New_Zealand_Government_Policy_on_Food_and_Nutrition/links/58e46e37aca272d62977a3e4/Individuals-the-Environment-or-Inequalities-Industry-and-Public-Health-Framing-of-Obesity-and-its-Presence-in-New-Zealand-Government-Policy-on-Food-and-Nutrition.pdf'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Kinderen op weg zetten voor levenslange slechte gezondheid',
                          explanation='KFC, net als andere fastfood-ketens, richt zich met zijn marketing specifiek op '
                                      'kinderen met zogenaamde "kindermenu\'s". Doorheen hun leven hebben kinderen met'
                                      ' ongezond gewicht twee keer zoveel risico op het ontwikkelen van een handicap '
                                      'en een kortere levensverwachting.',
                          url_ref=['https://www.cambridge.org/core/journals/public-health-nutrition/article/nutritional-quality-of-food-items-on-fastfood-kids-menus-comparisons-across-countries-and-companies/0FB4348EA7B9827C6B4F0AF18ACE4219'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Lakse voedselveiligheid',
                          explanation='Onderstaande video toont een schrijnend geval van gebrek aan hygiëne. '
                                      'De drang om winst te maximaliseren zorgt voor laksheid op allerlei andere '
                                      'domeinen. Een voorbeeld van wat het gevolg kan zijn voor voedselveiligheid.',
                          url_ref=['https://www.dailymail.co.uk/news/article-4908614/Video-shows-KFC-workers-expose-house-practices.html'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Antibioticaresistentie',
                          explanation='KFC gebruikt een enorme hoeveelheid antibiotica tijdens de groei van hun '
                                      'kippen, tot 21,32 milligram/kg, wat dan uiteindelijk terechtkomt in de '
                                      'menselijke voedselketen en bijdraagt aan de toename van antibioticaresistente '
                                      'bacteriën.',
                          url_ref=['https://www.dailymail.co.uk/news/article-4908614/Video-shows-KFC-workers-expose-house-practices.html'])

HEALTH.add_malpractice(malpractice=malpractice)
