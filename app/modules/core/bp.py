import uuid
from datetime import datetime
from flask import Blueprint, Flask, Response, render_template,session, request, jsonify,redirect,url_for,flash,g,session
from flask_security import login_required
from flask_login import fresh_login_required
from modules.core.auth.views import routes as routes_auth
from modules.core.clientes.views import routes as routes_clientes
from modules.core.produtos.views import routes as routes_produtos
from modules.core.propostas.views import routes as routes_propostas
from modules.tasks.teste2 import test2

bp = Blueprint('core', __name__,template_folder='templates')

@bp.before_request
@login_required
def before_request():
    pass


@bp.route('/' ,methods=['GET'])
def home():
    return render_template('index.html')


def init_app(app:Flask, url_prefix=''):
    routers = ( routes_auth  + routes_clientes + routes_produtos + routes_propostas )
    for r in routers:
        bp.add_url_rule(r['rule'],endpoint=r.get('endpoint', None),view_func=r['view_func'],**r.get('options', {}))
    app.register_blueprint(bp,url_prefix=url_prefix)
    