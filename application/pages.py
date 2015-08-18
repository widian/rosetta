from flask import request

from models import Sentence

from framework.page.protocols import PageBlueprint

page_bp = PageBlueprint('page', __name__, url_prefix='/page', static_folder='pages/static', template_folder='pages/template')

@page_bp.route('/')
def get_status():
    return page_bp.make_response()

