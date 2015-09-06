from flask import request

from models import Sentence

from framework.page.protocols import PageBlueprint

page_bp = PageBlueprint('page', __name__, url_prefix='/page', static_folder='pages/static', template_folder='pages/template')
page_debug_bp = PageBlueprint('page_debug', __name__, url_prefix='/page_debug', static_folder='test_pages', template_folder='test_pages')

@page_bp.route('/')
def get_status():
    return page_bp.make_response()


################################################# DEBUG PAGES
@page_debug_bp.route('/')
def debug_main():
    return page_bp.make_response(page='body.html')
