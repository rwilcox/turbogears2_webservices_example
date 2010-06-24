
from tg import expose, flash
from tg2_webservices.lib.base import BaseController
from tg2_webservices.model import DBSession, metadata
from tg2_webservices.model.post import Post


class APIController(BaseController):
    @expose('tg2_webservices.templates.api_controller.get')
    def get(self, post_id):
        post = DBSession.query(Post).filter_by(id = post_id).first()
        
        return dict(post=post)
    
