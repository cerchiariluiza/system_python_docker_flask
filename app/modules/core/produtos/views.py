from ext.db import db
import requests,json
from flask_wtf import FlaskForm,widgets
from functools import wraps
from modules.core.produtos.models import Produtos
from modules.core.produtos.forms import ProdutosForm
from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []

@roles_accepted('admin','listagem_produtos')
def produtos():
    return render_template("produtos/listas.html", lista=Produtos.query.all())
    
@roles_accepted('admin')
def novo_produto():
    form = ProdutosForm()
    if form.validate_on_submit():
        obj  = Produtos()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        MESSAGES.CADASTRADO_COM_SUCESSO('Produto')
        return redirect(url_for('core.novo_produto'))
    return render_template('produtos/form.html',form=form)

@roles_accepted('admin','estagiario')
def produto_edicao(id):
    obj = Produtos.query.filter_by(id=id).first_or_404()
    form = ProdutosForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        MESSAGES.ATUALIZADO_COM_SUCESSO('Produto')
    return render_template('produtos/form.html', form=form)

routes.append(dict(rule='produtos/',view_func=produtos, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='produto/',view_func=novo_produto, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='produto/<int:id>',view_func=produto_edicao, options=dict(methods=['GET','POST'])))