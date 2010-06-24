
from tg import expose, flash
from tg2_webservices.lib.base import BaseController
from tg2_webservices.model import DBSession, metadata
from tg2_webservices.model.post import Post

from datetime import datetime
class APIController(BaseController):
    @expose("json")
    @expose('tg2_webservices.templates.api_controller.get')
    def get(self, post_id):
        """
        We expose just simple json and normal HTML, but we could get deep into
        content types:
        
        @expose('json', exclude_names='d')
        @expose('tg2_webservices.templates.api.get_html',
                content_type='text/html')
                
        @ ^^^^^ notice how we output a different template in those cases?
        
        @expose('tg2_webservices.templates.api.get_xml',
                content_type='text/xml', custom_format='special_xml')
        
        But we know that, wither the dictionary is rendered through a template
        engine, or JSON, that it provides the data required for the view.
        
        """
        post = DBSession.query(Post).filter_by(id = post_id).first()
        
        return dict(post=post, time=datetime.now())
    
