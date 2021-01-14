from ext.db import db
import requests,json
from flask_wtf import FlaskForm,widgets
from functools import wraps
from modules.core.propostas.models import Propostas
from modules.core.propostas.forms import PropostasForm
from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []

@roles_accepted('admin','listagem_produtos')
def propostas():
    return render_template("propostas/listas.html", lista=Propostas.query.all())
    
@roles_accepted('admin')
def nova_proposta():
    form = PropostasForm()
    if form.validate_on_submit():
        obj  = Propostas()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        MESSAGES.CADASTRADO_COM_SUCESSO('Propostas')
        return redirect(url_for('core.nova_proposta'))
    return render_template('propostas/form.html',form=form)

@roles_accepted('admin','estagiario')
def proposta_edicao(id):
    obj = Proposta.query.filter_by(id=id).first_or_404()
    form = PropostaForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        MESSAGES.ATUALIZADO_COM_SUCESSO('Proposta')
    return render_template('proposta/form.html')

routes.append(dict(rule='propostas/',view_func=propostas, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='propostas/',view_func=nova_proposta, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='propostas/<int:id>',view_func=proposta_edicao, options=dict(methods=['GET','POST'])))