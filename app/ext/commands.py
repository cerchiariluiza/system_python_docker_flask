import click,time
from flask import Flask
from .db import db
from flask_security.utils import encrypt_password,url_for_security
from modules.core.auth.models import User,Role

def init_app(app:Flask):
    
    @app.cli.command()
    def initdb():
        db.create_all()

    @app.cli.command()
    def less():
        with click.progressbar(range(0,20),label='CALCULO MAROTO') as bar:
            for x in bar:
                bar.update(x)
                time.sleep(x)

    @app.cli.command()
    def admindb():
        db.create_all()
        if db.session.query(User).filter_by(username='master').count() == 0:
            usuario = User(username='master', email='master@rmcontact.com.br', password=encrypt_password('Password@1'))
            db.session.add(usuario)
            click.echo(click.style('USUARIO CRIADO', blink=True, bold=True,fg='green'))
            click.echo(click.style('USUARIO {0} SENHA {1}'.format('master','Password@1'), blink=True, bold=True))
            db.session.commit()
       


