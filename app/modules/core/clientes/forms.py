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

class ClientesForm(BaseForm):
    exames = BooleanField('Exames',default=False)
    nome_completo = StringField('Nome Completo',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    cpf_cnpj = StringField('CPF/CNPJ',render_kw={'maxlength':'255','type':'number'},validators=[validators.DataRequired()])
    telefone = StringField('Telefone',render_kw={'maxlength':'255','type':'number'},validators=[validators.DataRequired()])
    cep = StringField('CEP ',render_kw={'maxlength':'255','type':'number'})
    endereco = StringField('Endereço',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    complemento = StringField('Complemento',render_kw={'maxlength':'255'})
    cidade = StringField('Cidade ',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    estado = StringField('UF',render_kw={'maxlength':'2'},validators=[validators.DataRequired()])
    bairro = StringField('Bairro',render_kw={'maxlength':'255'})
    data_nascimento = DateField("Data nascimento",validators=[validators.DataRequired()])
    observacoes = FieldList(FieldList(StringField(""),min_entries=2),min_entries=1)
    observacoes_ = FieldList(FieldList(StringField(""),min_entries=2),min_entries=1)
    email = EmailField('Email',render_kw={'maxlength':'255','type':'email'},validators=[validators.DataRequired()])
    valor_pago_exame = DecimalField('Valor Pago',render_kw={'maxlength':'255'})