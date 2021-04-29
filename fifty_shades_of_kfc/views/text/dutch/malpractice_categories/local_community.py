__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


LOCAL_COMMUNITY = MalpracticeCategory(name='Lokale Gemeenschap', reference='localCommunity')

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
              'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
              'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse ' \
              'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa ' \
              'qui officia deserunt mollit anim id est laborum'

image_ref = 'https://images1.persgroep.net/rcs/PwH31Whvtd2oskLgaeQcrSHRY8Y/diocontent/176393540/_fitwidth/763?appId=' \
            '93a17a8fd81db0de025c8abd1cca1279&quality=0.8'

for counter in range(10):

    malpractice = Malpractice(title='Probleem ' + str(counter+1),
                              explanation=lorem_ipsum,
                              image_ref=image_ref)

    LOCAL_COMMUNITY.add_malpractice(malpractice=malpractice)
