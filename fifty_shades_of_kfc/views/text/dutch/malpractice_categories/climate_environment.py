__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


CLIMATE_ENVIRONMENT = MalpracticeCategory(name='Klimaat & Milieu', reference='climateEnvironment')


malpractice = Malpractice(title='Greenwashing',
                          explanation='KFC is een dochteronderneming van YUM!. YUM! heeft een rapport gepubliceerd '
                                      'waaruit blijkt dat hun beleid duurzaam genoeg is volgens de criteria van CDP. '
                                      'Belangijk om te weten is echter dat CDP voor het grootste deel gefinancieerd '
                                      'wordt door multinationals. Dit betekent dat deze bedrijven vanuit hun eigen '
                                      'beperkte interessen hun eigen regels bepalen. Deze vorm van zelfregulering '
                                      'kent u ongetwijfeld nog van in de bankindustrie voor de crisis van 2008.',
                          url_ref=['https://www.cdp.net/en/info/finance/europe'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Verpakkingen maken van het regenwoud',
                          explanation='In 2014 werd door een studie van Greenpeace bekend dat KCF verpakkingen '
                                      'gebruikte waarvoor regenwoud moest gekapt worden. Ondertussen beloofde KFC om '
                                      'enkel verantwoorde verpakkingen te gebruiken tegen eind 2020. Er is op dit '
                                      'moment geen bewijs dat KFC dit doel volledig bereikt is.',
                          url_ref=['https://www.greenpeace.org/nl/natuur/4637/wegwerpverpakkingen-van-kfc-vernielen-regenwoud/'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Ook dat nog: het logo van KFC is van in de ruimte te zien',
                          explanation='',
                          image_ref='https://static.standaard.be/Assets/Images_Upload/2006/11/15/kfc.jpg?maxheight=416&maxwidth=568&scale=both',
                          url_ref=['https://www.standaard.be/cnt/dmf15112006_090'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Voeder maken van het regenwoud',
                          explanation='Een derde van de sojaproductie gaat naar het voeden van kippen. Soja is één '
                                      'van de belangrijkste redenen voor ontbossing.',
                          url_ref=['https://ourworldindata.org/soy'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Luchtvervuiling',
                          explanation='Kippenrennen stoten grote hoeveelheden ammoniak en andere stikstofhoudende '
                                      'moleculen uit, dit heeft een negatief effect op de luchtkwaliteit. '
                                      'Ammoniakgas in de atmosfeer ondergaat reacties waarin fijn stof ontstaan '
                                      '(PM2.5), dit fijn stof kan grote afstanden afleggen en wordt geassocieerd met '
                                      'verhoogd risico op longkanker en andere hart- en longziekte gerelateerde '
                                      'overlijdens.',
                          url_ref=['https://www.theguardian.com/environment/2017/jul/25/mega-farms-devastating-effects-go-far-beyond-the-chicken-shed'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Effect op wilde dieren',
                          explanation='De stikstof “fall-out” rond kippenboerderijen kan zodanig hoog zijn dat de '
                                      'stikstofvervuiling de lokale wildpopulatie verandert. Veel gevoelige '
                                      'dierensoorten reageren slecht op hoge stikstofconcentraties en worden dan '
                                      'vervangen door diersoorten die al veel voorkomen. Dit is dus slecht voor de '
                                      'biodiversiteit die noodzakelijk is voor robuuste ecosystemen.',
                          url_ref=['https://www.theguardian.com/environment/2017/jul/25/mega-farms-devastating-effects-go-far-beyond-the-chicken-shed'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Mestoverschot',
                          explanation='Industriële kippenboerderijen produceren een onhoudbare hoeveelheid mest. '
                                      'Deze kippenmest wordt op veel verschillende manieren gebruikt, onder andere '
                                      'als meststof voor landbouw. De "run-off" hiervan veroorzaakt '
                                      'stikstofvervuiling in de bodem en in onze waterwegen.',
                          url_ref=['https://foodprint.org/issues/what-happens-to-animal-waste/'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Klimaatverhitting',
                          explanation='Ons globaal voedselproductiesysteem is een van de voornaamste bijdragers aan '
                                      'de klimaatverhitting. Vleesconsumptie veranderen van runds naar kip werd ooit '
                                      'gezien als een stap in de juiste richting maar wetenschappers trekken nu aan '
                                      'de alarmbel. Wetenschappers waarschuwen ons dat we de vleesindustrie op '
                                      'dezelfde manier moeten zien als de fossiele-brandstoffenindustrie.',
                          url_ref=['https://www.ecowatch.com/beef-chicken-climate-change-impact-2652836402.html'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Landgebruik',
                          explanation='Meer dan 71% van Europese landbouwgrond is gereserveerd voor vlees- en '
                                      'melkproductie, dus het reduceren van vleesproductie is een manier waarop '
                                      'grote verbetering bereikt kan worden.',
                          url_ref=['https://www.greenpeace.org/eu-unit/issues/nature-food/1807/71-eu-farmland-meat-dairy/#:~:text=%23Farming%20%23Food-,Over%2071%25%20of%20EU%20farmland%20dedicated,meat%20and%20dairy%2C%20new%20research&text=Brussels%20%E2%80%93%20At%20least%2071%25%20of,new%20research%20published%20by%20Greenpeace.&text=Researchers%20calculated%20that%20125%20million,graze%20livestock%20or%20produce%20feed.'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)
