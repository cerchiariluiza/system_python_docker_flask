from flask import url_for
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm,widgets
from sqlalchemy.ext.mutable import MutableList

from modules.core.models import BaseModels

class Clientes(BaseModels):
    exames = db.Column(db.Boolean, default=True)
    nome_completo = db.Column(db.String(255))
    cpf_cnpj = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    rg = db.Column(db.String(40))
    telefone = db.Column(db.String(40))
    endereco =  db.Column(db.String(255))
    cep =  db.Column(db.String(40))
    cidade =  db.Column(db.String(40))
    estado =  db.Column(db.String(40))
    bairro =  db.Column(db.String(40))
    data_nascimento = db.Column(db.DateTime)
    # observacoes = db.Column(db.String(255))
    email = db.Column(db.String(255))

    # # exames = BooleanField('Exames',default=False)
    # nome_completo = StringField('Nome Completo',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    # cpf_cnpj = StringField('CPF/CNPJ',render_kw={'maxlength':'255','type':'number'},validators=[validators.DataRequired()])
    # telefone = StringField('Telefone',render_kw={'maxlength':'255','type':'number'},validators=[validators.DataRequired()])
    # cep = StringField('CEP ',render_kw={'maxlength':'255','type':'number'})
    # endereco = StringField('Endereço',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    # complemento = StringField('Complemento',render_kw={'maxlength':'255'})
    # cidade = StringField('Cidade ',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    # estado = StringField('UF',render_kw={'maxlength':'2'},validators=[validators.DataRequired()])
    # bairro = StringField('Bairro',render_kw={'maxlength':'255'})
    # data_nascimento = DateField("Data nascimento",validators=[validators.DataRequired()])
    # observacoes = FieldList(FieldList(StringField(""),min_entries=2),min_entries=1)
    # observacoes_ = FieldList(FieldList(StringField(""),min_entries=2),min_entries=1)
    # email = EmailField('Email',render_kw={'maxlength':'255','type':'email'},validators=[validators.DataRequired()])
    # valor_pago_exame = DecimalField('Valor Pago',render_kw={'maxlength':'255'})
  
   
    