import flask
import json
from flask import render_template

class PageResponseMaker(object):
    def make_response(self, **kwargs):
        if 'page' in kwargs:
            return render_template(kwargs['page'])
        else:
            return render_template('index.html')

class PageBlueprint(flask.Blueprint):
    def make_response(self, **kwargs):
        response_maker = PageResponseMaker()
        return response_maker.make_response(**kwargs)
