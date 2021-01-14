from wtforms_alchemy import Unique,ModelForm
import json
from flask_wtf import FlaskForm,widgets
from wtforms import HiddenField,BooleanField,FieldList,StringField,MultipleFileField

class BaseForm(FlaskForm,ModelForm):
    ativo = BooleanField('Ativo',default = True)