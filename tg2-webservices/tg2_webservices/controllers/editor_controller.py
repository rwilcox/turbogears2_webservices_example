# -*- coding: utf-8 -*-
"""Create and edit your blog posts here. As in, this is where you populate the data
for your crazy web services experiments"""

from tg import expose, flash
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from repoze.what.predicates import has_permission, in_group
from tgext.crud import CrudRestController

#from dbsprockets.dbmechanic.frameworks.tg2 import DBMechanic
#from dbsprockets.saprovider import SAProvider

from tg2_webservices.lib.base import BaseController
from tg2_webservices.model import DBSession, metadata
from tg2_webservices.model.post import Post

from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller, FormFiller, RecordFiller
from sprox.formbase import AddRecordForm


__all__ = ['ManagePostController']

class ManagePostTable(TableBase):
    __model__ = Post

class ManagePostTableFiller(TableFiller):
    __model__ = Post
    

class ManagePostEditFiller(RecordFiller):
    __model__ = Post

class ManagePostAddForm(AddRecordForm):
    __model__ = Post


class ManagePostsController(CrudRestController):
    """Allows an admin to CRUD artists"""
    
    # The predicate that must be met for all the actions in this controller:
    allow_only = None
    
    model = Post
    table_filler = ManagePostTableFiller(DBSession)
    table = ManagePostTable(DBSession)
    new_form = ManagePostAddForm(DBSession)
    edit_form = ManagePostAddForm(DBSession)
    edit_filler = ManagePostEditFiller(DBSession)
