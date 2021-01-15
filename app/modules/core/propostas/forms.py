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
    proposta = StringField('Número da Proposta')
    cliente = StringField('Cliente',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    keywords = StringField('Palavras chave', render_kw={"placeholder": "Adicone uma tag "})
    nome_para_contato = StringField('Nome para contato',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    email = StringField('Email',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    telefone = StringField('Telefone ',render_kw={'maxlength':'255'})
    dia_fechamento = SelectField('Dia do fechamento', choices=[('selecione','Selecione'),('15','15'),('30','30')],validators=[validators.DataRequired()],coerce=str) 
    vigencia_inicial = DateField('Dia da vigência Inicial',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    vigencia_final = DateField('Data da vigência Final',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])
    dia_vencimento = SelectField('Dia do vencimento',choices=[('15','15'),('30','30')],validators=[validators.DataRequired()] ,coerce=str)
    prazo_vencimento =  StringField('Prazo do Fechamento',render_kw={'maxlength':'255'},validators=[validators.DataRequired()])


    #investigacao
    horas_mes_investigacao = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_investigacao = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Trimestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_investigacao =StringField('',render_kw={'maxlength':'255','type':'number'})

    #Análise de malware
    horas_mes_anal_malware = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_anal_malware = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Trimestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_anal_malware =StringField('',render_kw={'maxlength':'255','type':'number'})

    #Análise de contra inteligencia
    horas_mes_anal_contra_int = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_anal_contra_int = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Trimestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_anal_contra_int =StringField('',render_kw={'maxlength':'255','type':'number'})

    #pentest
    horas_mes_pentest = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_pentest = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Trimestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_pentest =StringField('',render_kw={'maxlength':'255','type':'number'})

    # ri
    horas_mes_ri = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_ri = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Trimestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_ri =StringField('',render_kw={'maxlength':'255','type':'number'})

    
    #treinamento
    horas_mes_treinamento = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_treinamento = SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Ttreinamentomestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_treinamento =StringField('',render_kw={'maxlength':'255','type':'number'})

    #consultoria
    horas_mes_consultoria = StringField('',render_kw={'maxlength':'255','type':'number'})
    frequencia_consultoria= SelectField('',choices=[('mensal','Mensal'),('bimestral','Bimestral'),('trimestral','Ttreinamentomestral'),('semestral','Semestral')],validators=[validators.DataRequired()] ,coerce=str)
    total_cumulativo_consultoria =StringField('',render_kw={'maxlength':'255','type':'number'})