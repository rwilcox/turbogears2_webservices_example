# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tg2_webservices.model import DeclarativeBase, metadata, DBSession


class Post(DeclarativeBase):
    __tablename__ = 'post'
    
    id = Column(u'id', Integer(), primary_key=True)
    title = Column('title', Unicode(255), nullable=False)
    summary = Column( 'summary', Unicode(512) )
    body_text = Column('body_text', Text(), nullable=False)
