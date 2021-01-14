from flask import url_for
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm,widgets
from sqlalchemy.ext.mutable import MutableList
from modules.core.models import BaseModels


class Produtos(BaseModels):
    id = db.Column(db.String(125), primary_key=True)
    nome = db.Column(db.String(125))
  

 

   
    