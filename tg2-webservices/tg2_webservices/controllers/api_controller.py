
from tg import expose, flash
from tg2_webservices.lib.base import BaseController
from tg2_webservices.model import DBSession, metadata
from tg2_webservices.model.post import Post


class APIController(BaseController):
    @expose('tg2_webservices.templates.api_controller.get')
    def index(self):
        return dict()
