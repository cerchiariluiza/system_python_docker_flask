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
    telefone = db.Column(db.Integer)
    diaFechamento = db.Column(db.Integer)
    vigenciaInicial = db.Column(db.Date)
    vigenciaFinal = db.Column(db.Date)
    diaVencimento = db.Column(db.Integer)
    prazoVencimento =  db.Column(db.String(40))



   
    