import json
from ext.db import db
from flask import url_for
from flask_wtf import FlaskForm,widgets
from wtforms_alchemy import Unique,ModelForm
from wtforms.widgets import ListWidget, RadioInput,CheckboxInput
from modules.core.forms import BaseForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators,SelectMultipleField,SelectField,IntegerField,RadioField,HiddenField,TextAreaField
from modules.core.produtos.models import Produtos
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms import DecimalField, RadioField,FileField,FieldList,FormField,SelectMultipleField, BooleanField,StringField,PasswordField, validators,SelectField,IntegerField,RadioField,HiddenField,TextAreaField
from wtforms.fields.html5 import DateField,EmailField,URLField,IntegerRangeField
from modules.core.messages import *

class ProdutosForm(BaseForm):
    id =  StringField('Id',render_kw={'maxlength':'125'},validators=[Unique(Produtos.id,message=ITEM_JA_CADASTRADO.format('Bagaça')),validators.DataRequired()])
    nome = StringField('Nome',render_kw={'maxlength':'125'},validators=[Unique(Produtos.nome,message=ITEM_JA_CADASTRADO.format('Bagaça')),validators.DataRequired()])
    segmento = SelectField('Segmento',choices=[('',''),('atacado','Atacado'),('varejo','Varejo')],validators=[validators.DataRequired()],coerce=str) 
    setor = SelectField('Setor',choices=[('',''),('industria','Industria'),('financeiro','Financeiro')],validators=[validators.DataRequired()],coerce=str) 
 