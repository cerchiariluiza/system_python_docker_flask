from flask import url_for
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm,widgets
from sqlalchemy.ext.mutable import MutableList
from modules.core.models import BaseModels

class Propostas(BaseModels):
    id = db.Column(db.Integer, primary_key=True)
    proposta = db.Column(db.String(125), nullable=False)
    cliente = db.Column(db.String(125))
    nome_para_contato = db.Column(db.String(125))
    email = db.Column(db.String(125),nullable=False)
    telefone = db.Column(db.String(100))
    dia_fechamento = db.Column(db.Integer)
    vigencia_inicial = db.Column(db.Date)
    vigencia_final = db.Column(db.Date)
    dia_vencimento = db.Column(db.Integer)
    prazo_vencimento =  db.Column(db.String(40))



   
    