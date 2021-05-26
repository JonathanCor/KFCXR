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


malpractice = Malpractice(title='Air pollution',
                          explanation='Chicken sheds emit high levels of ammonia and other nitrogen, that will '
                                      'adversely affect air quality. Ammonia gas in the atmosphere will react to form '
                                      'fine particles (PM2.5) which can travel long distances and are considered to be '
                                      'associated with elevated risk of lung-cancer and cardiopulmonary mortality.',
                          url_ref=['https://www.theguardian.com/environment/2017/jul/25/mega-farms-devastating-effects-go-far-beyond-the-chicken-shed'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Effects on wildlife',
                          explanation='The nitrogen “fall-out” surrounding chicken factories can be so high that the '
                                      'nitrogen pollution changes the local wildlife. Many vulnerable species react '
                                      'badly to nitrogen excesses and often make place for often common species to '
                                      'thrive, thus negatively impacting our biodiversity.',
                          url_ref=['https://www.theguardian.com/environment/2017/jul/25/mega-farms-devastating-effects-go-far-beyond-the-chicken-shed'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Manure surplus',
                          explanation='Industrial chicken farms produce an unsustainable amount of manure. This '
                                      'chicken poop is used in various ways, including as fertilizer on our fields. '
                                      'The run-off from this is known to cause much nitrogen pollution on our land '
                                      'and in our waterways.',
                          url_ref=['https://foodprint.org/issues/what-happens-to-animal-waste/'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Climate change',
                          explanation='Our global food production system is one of the main drivers of climate change.'
                                      ' Changing meat consumption from beef to chicken was once considered a step in '
                                      'the right direction but is now warned against by scientists. Scientists warn '
                                      'we should regard the meat industry in a similar way as the fossil fuel '
                                      'industry.',
                          url_ref=['https://www.ecowatch.com/beef-chicken-climate-change-impact-2652836402.html'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Land use',
                          explanation='Over 71% of European farmland is dedicated to meat and diary production, '
                                      'so reducing meat consumption will significantly impact land-use in Europe.',
                          url_ref=['https://www.greenpeace.org/eu-unit/issues/nature-food/1807/71-eu-farmland-meat-dairy/#:~:text=%23Farming%20%23Food-,Over%2071%25%20of%20EU%20farmland%20dedicated,meat%20and%20dairy%2C%20new%20research&text=Brussels%20%E2%80%93%20At%20least%2071%25%20of,new%20research%20published%20by%20Greenpeace.&text=Researchers%20calculated%20that%20125%20million,graze%20livestock%20or%20produce%20feed.'])

CLIMATE_ENVIRONMENT.add_malpractice(malpractice=malpractice)
