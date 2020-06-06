from flask import Blueprint, jsonify
from gca.service.CoinService import Coin

coin = Blueprint('coin', __name__, template_folder='templates')


@coin.route('/coins/', methods=['GET'])
def index():
    return Coin().all()


#@coin.route('/test/', methods=['GET'])
#def index():
#    return Coin().get('btc')

