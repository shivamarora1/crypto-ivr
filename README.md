# Horus: Crypto IVR
This IVR will tell you price of some famous crypto currencies. The IVR is based on Twillio voice and fetched crypto price from coin market cap api.
This project is used flask framewok for the webhooks of Twillio incoming calls.

## Steps for local set up of project

1. First clone this repository and cd into it.

``$ git clone git@github.com:TwilioDevEd/ivr-phone-tree-python.git`` <br>
``$ cd ivr-phone-tree-python``

2. Create a new virtual environment.

```python3 venv -m .venv```<br>
```source .venv/bin/activate```

3. Install the dependencies.<br>
```pip install -r requirements.txt```

4. Set coin market api key in **environment variables**.<br>
```COIN_MARKET_KEY```

5. Start the server.<br>
 ```make run```

6. Expose the application to the wider Internet using ngrok.

7. Configure Twilio to call your webhooks
