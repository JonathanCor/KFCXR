__author__ = 'Jonathan Corvers'

from .animal_welfare import ANIMAL_WELFARE
from .working_conditions import WORKING_CONDITIONS
from .climate_environment import CLIMATE_ENVIRONMENT
from .health import HEALTH
from .local_community import LOCAL_COMMUNITY


MALPRACTICE_CATEGORIES = {
    ANIMAL_WELFARE.reference: ANIMAL_WELFARE,
    WORKING_CONDITIONS.reference: WORKING_CONDITIONS,
    CLIMATE_ENVIRONMENT.reference: CLIMATE_ENVIRONMENT,
    HEALTH.reference: HEALTH,
    LOCAL_COMMUNITY.reference: LOCAL_COMMUNITY,
}

SOURCES = 'Bronnen'

