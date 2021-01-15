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


    horas_mes_investigacao =  db.Column(db.String(40))
    horas_mes_ri =  db.Column(db.String(40))
    horas_mes_anal_contra_int =  db.Column(db.String(40))
    horas_mes_consultoria =  db.Column(db.String(40))
    horas_mes_investigacao =  db.Column(db.String(40))
    horas_mes_pentest =  db.Column(db.String(40))

    frequencia_investigacao =  db.Column(db.String(40))
    frequencia_ri =  db.Column(db.String(40))
    frequencia_anal_contra_int =  db.Column(db.String(40))
    frequencia_consultoria =  db.Column(db.String(40))
    frequencia_investigacao =  db.Column(db.String(40))
    frequencia_pentest =  db.Column(db.String(40))

    total_cumulativo_investigacao =  db.Column(db.String(40))
    total_cumulativo_ri =  db.Column(db.String(40))
    total_cumulativo_anal_contra_int =  db.Column(db.String(40))
    total_cumulativo_consultoria =  db.Column(db.String(40))
    total_cumulativo_investigacao =  db.Column(db.String(40))
    total_cumulativo_pentest =  db.Column(db.String(40))
    
    



   
    