__author__ = 'Jonathan Corvers'

from fifty_shades_of_kfc.views.text.malpractice import MalpracticeCategory, Malpractice


WORKING_CONDITIONS = MalpracticeCategory(name='Working Conditions', reference='workingConditions')


malpractice = Malpractice(title='Poor labour practices are systemic, get unionized!',
                          explanation='These injustices are not the acts of a few bad apples. '
                                      'Working for KFC means working for a multinational where the balance of power '
                                      'between shareholders and individual employees is extremely unequal. '
                                      'If you need a job at KFC, make sure to get unionized.')

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='In 2012, KFC got fined for child labour in Australia',
                          explanation='If they are this careless with child labour in an industrialized nation, '
                                      'what does their global supply chain look like?',
                          url_ref=['https://thewest.com.au/news/wa/kfc-fined-over-child-labour-ng-ya-285294'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='Work at KFC, be forced to poison your community',
                          explanation='Check out this report of Auckland KFC employees protesting being forced '
                                      'to sell expired food to their community.',
                          url_ref=['https://www.stuff.co.nz/business/119908028/kfc-workers-say-they-were-bullied-for-telling-managers-not-to-sell-expired-chicken'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC doesn\'t take care of its employees when the going gets tough',
                          explanation='In 2018 KFC had some delivery issues. The higher-ups were responsible '
                                      'for the supply chain, '
                                      'yet the local employees took the hit in the form of lost wages.',
                          url_ref=['https://www.cornwalllive.com/news/local-news/angry-kfc-workers-say-not-1235512'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)


malpractice = Malpractice(title='KFC has no shame in discriminating against workers with disabilities',
                          explanation='Only after public outcry and union organizing '
                                      'did KFC reinstate workers who were unfairly let go.',
                          url_ref=['https://www.nzherald.co.nz/nz/kfc-calls-back-disabled-staff/6DPE42EYBYFZ7FN3HICXKGLXY4/',
                                   'https://www.tvnz.co.nz/content/tvnz/onenews/story/2013/09/01/kfc-s-new-employment-policy-unfair-and-unjust-labour.html?utm_variant=taboola_visible_1'])

WORKING_CONDITIONS.add_malpractice(malpractice=malpractice)
