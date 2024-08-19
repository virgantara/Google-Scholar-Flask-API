from flask import Blueprint, request, jsonify
from controllers import get_list_publication

main_bp = Blueprint('main', __name__)


@main_bp.route('/gs/pub/list', methods=['GET'])
def get_pubs():
    gs_id = request.args.get('gs_id')
    item = get_list_publication(gs_id)
    results = {
        'status' : 200,
        'values' : item
    }
    return jsonify(results)