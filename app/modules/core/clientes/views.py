from ext.db import db
import requests,json
from flask_wtf import FlaskForm,widgets
from functools import wraps
from modules.core.clientes.models import Clientes
from modules.core.clientes.forms import ClientesForm
from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []


@roles_accepted('admin','usuario')
def clientes():
    return render_template("clientes/listas.html", lista=Clientes.query.all())
    
@roles_accepted('admin','usuario')
def novo_cliente():
    form = ClientesForm()
    if form.validate_on_submit():
        obj  = Clientes()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        MESSAGES.CADASTRADO_COM_SUCESSO('Cliente')
        return redirect(url_for('core.novo_cliente'))
    return render_template('clientes/form.html',form=form)

@roles_accepted('admin','usuario')
def cliente_edicao(id):
    obj = Clientes.query.filter_by(id=id).first_or_404()
    form = ClientesForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        MESSAGES.ATUALIZADO_COM_SUCESSO('Cliente')
    return render_template('clientes/form.html')





routes.append(dict(rule='clientes/',view_func=clientes, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='cliente/',view_func=novo_cliente, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='cliente/<int:id>',view_func=cliente_edicao, options=dict(methods=['GET','POST'])))