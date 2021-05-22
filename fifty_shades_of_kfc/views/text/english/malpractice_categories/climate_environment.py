__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


CLIMATE_ENVIRONMENT = MalpracticeCategory(name='Climate & Environment', reference='climateEnvironment')


malpractice = Malpractice(title='Greenwashing',
                          explanation='KFC is a subsidiary of Yum!, Yum! issues a sustainability report to CDP which '
                                      'is of course, you guessed it, funded by multinationals! Companies setting '
                                      'their own rules and then check themselves. This is called self-regulation and '
                                      'you may know it as standard practice in the banking industry before 2008.',
                          url_ref=['https://www.cdp.net/en/info/finance/europe'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Turning the rainforest into packaging',
                          explanation='In 2014 Greenpeace found that KFC turned the Amazon rainforest into fast food '
                                      'packaging. KFC recently committed to using more responsible packaging by the '
                                      'end of 2020. We found no report available that proves '
                                      'they have achieved that goal.',
                          url_ref=['https://www.greenpeace.org/nl/natuur/4637/wegwerpverpakkingen-van-kfc-vernielen-regenwoud/'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Fun fact: the KFC logo can be seen from space',
                          explanation='',
                          image_ref='https://static.standaard.be/Assets/Images_Upload/2006/11/15/kfc.jpg?maxheight=416&maxwidth=568&scale=both',
                          url_ref=['https://www.standaard.be/cnt/dmf15112006_090'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Turning the rainforest into unsustainable animal feed',
                          explanation='A third of world soy production goes to feeding chickens, soy being an important reason for deforestation.',
                          url_ref=['https://ourworldindata.org/soy'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)
