import logging

from programarena import api

LOGGER = logging.getLogger(__name__)

app = api.create_app()
