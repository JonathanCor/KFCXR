__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


LOCAL_COMMUNITY = MalpracticeCategory(name='Lokale Gemeenschap', reference='localCommunity')


malpractice = Malpractice(title='Geen ruimte voor lokaal ondernemen',
                          explanation='Multinationals duwen huurprijzen omhoog, waardoor onafhankelijke zaken, '
                                      'die al lijden door COVID richting faillissement geduwd worden.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Geen democratische inspraak',
                          explanation='In een stad met zoveel leegstand, heeft Leuven echt een KFC nodig? '
                                      'Dit is niet gewoon hoe de economie werkt. Dit is een politieke beleidskeuze.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Prachtig historisch centrum?',
                          explanation='Grote ketens verpesten het karakter van een stad, willen we echt dat Leuven er '
                                      'binnenkort uitziet als een Amerikaanse stad?')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Dit is nog maar het begin',
                          explanation='KFC hoopt tussen 2019 en 2025 40 vestigingen te openen in België.')

LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)
