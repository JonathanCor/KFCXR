__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


HEALTH = MalpracticeCategory(name='Health', reference='health')


malpractice = Malpractice(title='KFC exists to maximize profit, not to maximize nutrition',
                          explanation='You may think after reading these health related critiques: "Sure, ok, but '
                                      'sometimes I want to eat unhealthy food." That\'s okay, we all do, that\'s not '
                                      'the point. KFC doesn\'t have satisfying our cravings as its mission. It wants '
                                      'to maximize profits, by increasing how often you feel those cravings by smart '
                                      'advertising, encouraging these cravings in our children and luring them in with'
                                      ' toys. The food is intentionally addictive, getting people addicted preferrably '
                                      'as young as possible and profiting off of them, while offsetting the negative '
                                      'health consequences on broader society.')

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Empty calories',
                          explanation='Junk food such as KFC is unhealthy, '
                                      'as it contains high calories from sugar and fat. These “empty” calories are one'
                                      ' of the causes of a worldwide obesity epidemic, called “Globesity” by the World'
                                      ' Health Organisation. Although the link of obesity and junk food such as KFC is'
                                      ' complex, the epidemic proportions of obesity worldwide through unhealthy diet '
                                      'causes dozens of other health risks & diseases: hearth disease, stroke, high '
                                      'blood pressure, diabetes, some cancers, gallbladder disease, gallstones, '
                                      'osteoarthritis, gout, breathing problems (such as sleep apnea and asthma)…',
                          url_ref=['https://www.who.int/activities/controlling-the-global-obesity-epidemic'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Bad for your skin',
                          explanation='Eating junk food such as KFC increases your risk for developing acne '
                                      'and an acne outbreak.',
                          url_ref=['https://www.healthline.com/nutrition/foods-that-cause-acne#TOC_TITLE_HDR_4'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Deep fried food will make you sick',
                          explanation='Eating deep fried food is associated with a myriad of disease risks: '
                                      'cardiovascular disease, diabetes and obesity to name just a few.',
                          url_ref=['https://pubmed.ncbi.nlm.nih.gov/26457715/'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Refined salts',
                          explanation='Fast food is high in refined salts (such as table salt Sodium Choride and the '
                                      'flavor enhancers Sodium Phosphate and Sodium Glutamate) which cause high blood '
                                      'pressure (hypertension), a big risk factor for stroke and other cardiovascular '
                                      'disease.',
                          url_ref=['https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7318881/'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Preying on the vulnerable',
                          explanation='KFC preys on those who are less educated and lack the knowledge to see through '
                                      'marketing ploys.',
                          url_ref=['https://www.researchgate.net/profile/Gabrielle-Jenkin/publication/315782915_Individuals_the_Environment_or_Inequalities_Industry_and_Public_Health_Framing_of_Obesity_and_its_Presence_in_New_Zealand_Government_Policy_on_Food_and_Nutrition/links/58e46e37aca272d62977a3e4/Individuals-the-Environment-or-Inequalities-Industry-and-Public-Health-Framing-of-Obesity-and-its-Presence-in-New-Zealand-Government-Policy-on-Food-and-Nutrition.pdf'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Setting children up for life-long poor health',
                          explanation='KFC, like other fast-food chains, targets children by marketing specifically to'
                                      ' them with so-called "kids\' menus". "Over the lifespan children of unhealthy '
                                      'weights are twice as likely to have a disability and a '
                                      'shorter life expectancy."',
                          url_ref=['https://www.cambridge.org/core/journals/public-health-nutrition/article/nutritional-quality-of-food-items-on-fastfood-kids-menus-comparisons-across-countries-and-companies/0FB4348EA7B9827C6B4F0AF18ACE4219'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Carelessness with food safety',
                          explanation='All of us have seen pushes to cut corners and maximize profit. '
                                      'The video makes painfully clear what this means for food safety.',
                          url_ref=['https://www.dailymail.co.uk/news/article-4908614/Video-shows-KFC-workers-expose-house-practices.html'])

HEALTH.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Antibiotics resistence',
                          explanation='KFC uses a huge amount of antibiotics during the growth of their chickens, '
                                      'up to 21.32 mg/kg, which then enters the human food change and contributes to '
                                      'the creation of antibiotic resistent bacteria.',
                          url_ref=['https://kfc-uk-brand.s3.eu-west-1.amazonaws.com/drupal/production/2020-08/KFC_Annual_Chicken-Welfare-Report-2020.pdf'])

HEALTH.add_malpractice(malpractice=malpractice)
