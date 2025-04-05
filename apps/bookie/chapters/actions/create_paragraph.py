import logging
import lorem

logger = logging.getLogger(__name__)


def create_paragraph() -> str:
    return lorem.paragraph()
