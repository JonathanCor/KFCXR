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
