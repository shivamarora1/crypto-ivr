from urllib import response
from flask import (request, url_for, Flask)
from twilio.twiml.voice_response import VoiceResponse
from coin import (coins, init_coins)
from helper import twiml

init_coins()
app = Flask(__name__)


@app.route("/ivr/crypto", methods=['POST'])
def ivr_crypto():
    # Start our TwiML response
    response = VoiceResponse()
    with response.gather(input=1, action=url_for("cryto_price"), method="POST") as g:
        g.say("Welcome to Horus crypto exchange. " +
              "Press 1 for Bitcoin" +
              "Press 2 for Ethereum" +
              "Press 3 for Tether" +
              "Press 4 for Dogecoin" +
              "Press 5 for Solana",)
    return twiml(response)


@app.route("/ivr/crypto-price", methods=['POST'])
def cryto_price():

    coin_selected = request.form['Digits']
    coins_options = {"1": "BTC", "2": "ETH",
                     "3": "USDT", "4": "DOGE",
                     "5": "SOL"}

    if coin_selected in coins_options:
        # get currency and its price
        code = coins_options[coin_selected]

        coin = coins.get(code)
        price = coin.fetch_price()

        response = VoiceResponse()
        response.say(f'Price of {coin.name} is $ {price}.')
        response.hangup()
        return twiml(response)
    else:
        return _redirect_to_welcome()


def _redirect_to_welcome():
    response = VoiceResponse()
    response.say('You have made an invalid selection.')
    response.redirect(url_for("ivr_crypto"))
    return twiml(response)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
