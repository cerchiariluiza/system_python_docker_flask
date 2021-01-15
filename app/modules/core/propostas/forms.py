import json
from ext.db import db
from flask import url_for
from flask_wtf import FlaskForm,widgets
from wtforms_alchemy import Unique,ModelForm
from wtforms.widgets import ListWidget, RadioInput,CheckboxInput
from modules.core.forms import BaseForm
from modules.core.clientes.models import Clientes
from wtforms import PasswordField, StringField, SubmitField, ValidationError,SelectField,Form,FloatField,DateField
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms import DecimalField, RadioField,FileField,FieldList,FormField,SelectMultipleField, BooleanField,StringField,PasswordField, validators,SelectField,IntegerField,RadioField,HiddenField,TextAreaField
from wtforms.fields.html5 import DateField,EmailField,URLField,IntegerRangeField
from modules.core.messages import *

class PropostasForm(BaseForm):
    Proposta = StringField('Proposta',default=False)
   
    cliente = StringField('Nome do Cliente',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    nome_para_contato = StringField('Nome para contrato',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    email = StringField('Email',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    telefone = StringField('Telefone ',render_kw={'maxlength':'255','type':'number'})
    dia_fechamento = StringField('Dia do Fechamento',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    vigencia_inicial = DateField('Dia da vigência Inicial',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    vigencia_final = DateField('Data da vigência Final',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    dia_vencimento = StringField('Dia do Fechamento',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    prazo_vencimento =  StringField('Prazo do Fechamento',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
