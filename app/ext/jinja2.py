from flask import Blueprint, Flask,render_template
import json
import datetime
import dateutil

def global_vars_templates(app:Flask):
    @app.context_processor
    def variaveis_globais():
        return dict(
                APP=app.config['APP'].upper(),
                now = datetime.datetime.now() ,
        )

    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, fmt=None):
        date = dateutil.parser.parse(date)
        native = date.replace(tzinfo=None)
        format='%d/%m/%Y, %H:%M:%S'
        return native.strftime(format)

    @app.template_filter('js_load')
    def _jinja2_filter_json_loads(data):
        return json.loads(data)