import pytest
from flask import Flask,template_rendered,url_for
from factory import create_app
from flask_security.utils import login_user,hash_password,verify_password
from modules.core.auth.models import User,Role
from ext.db import db 
from ext.config import config
from sqlalchemy import event
from flask_login import user_logged_in,user_logged_out,user_unauthorized,logout_user,login_user
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def client(app):
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    db.drop_all()
    db.create_all()
    yield testing_client 
    ctx.pop()
    

@pytest.fixture
def test_provedor():
    return  { 
        'pos_pago':True,
        'nome_razao_social': 'TESTE 150',
        'cpf_cnpj':'00001', 
        'contato':'00001', 
        'email' : 'aaa@gmail.com' ,
        'credito':'0.00',
        
        'url_prov-0-ativo':True,
        'url_prov-0-url':'http://teste.com',
        'url_prov-0-disparo':True,
        'url_prov-0-method':'post',
        
        'url_prov-0-url_provedor-0-ativo':True,
        'url_prov-0-url_provedor-0-nome':'teste',
        'url_prov-0-url_provedor-0-obrigatorio':False,
        'url_prov-0-url_provedor-0-ordem':'1',
        'url_prov-0-url_provedor-0-tipo':'textarea',

        'url_prov-0-url_provedor-1-ativo':True,
        'url_prov-0-url_provedor-1-nome':'Content-Type',
        'url_prov-0-url_provedor-1-padrao':'padrao',
        'url_prov-0-url_provedor-1-ordem':'1',
        'url_prov-0-url_provedor-1-tipo':'header',

        'url_prov-0-url_provedor-1-opcoes-0-0':'usuario',
        'url_prov-0-url_provedor-1-opcoes-0-1':'1234',
        'url_prov-0-url_provedor-1-opcoes-0-2':'TESTE DESCRICAO',

        'url_prov-0-url_provedor-2-ativo':True,
        'url_prov-0-url_provedor-2-nome':'teste4',
        'url_prov-0-url_provedor-2-ordem':'1',
        'url_prov-0-url_provedor-2-tipo':'textarea',

        'url_prov-0-url_provedor-3-ativo':True,
        'url_prov-0-url_provedor-3-nome':'teste5',
        'url_prov-0-url_provedor-3-ordem':'1',
        'url_prov-0-url_provedor-3-tipo':'select',

        'url_prov-0-url_provedor-3-opcoes-0-0':'1',
        'url_prov-0-url_provedor-3-opcoes-0-1':'VALOR 01',
        'url_prov-0-url_provedor-3-opcoes-0-2':'DESCRICAO 01',
    }


@pytest.fixture
def create_user(client):
    pwd = hash_password('11')
    user  = User(**{ 'active':True,'username':'teste','email':'teste@teste.com.br','password':pwd})
    role = Role(**{'name':'admin','description':'admin'})
    db.session.add(user)
    db.session.commit()
    db.session.add(role)
    user.roles.append(role)
    db.session.commit()
    data = dict(email=user.username, password='11')
    response = client.post(
        '/login?next=/',
        data=data,
        follow_redirects=True)
    return user

@pytest.fixture
def app():
    return create_app("test")

