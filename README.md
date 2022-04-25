# Horus🐴: Crypto IVR
This IVR🤙 will tell you price of some famous crypto currencies💰. The IVR is based on [Twillio](https://www.twilio.com/docs/voice) voice and fetched crypto price from [coin market cap api](https://coinmarketcap.com/api/).
This project is used flask framewok for the webhooks of Twillio incoming calls.

## Working
1. Call to the number that you get from **twillio**.
2. **IVR** will tell you all the **crypto currencies** available and ask you to make a selection.
3. According to the selection e.g. 1 for **Bitcoin**, IVR connected web app will fetch the real time prize of crypto currency.
4. IVR will tell/ say the price of selected **crypto currency**.
5. If user make invalid selection then IVR will revert it back to the **main menu**.

## Steps for local set up of project

1. First clone this repository and cd into it.

``$ git clone git@github.com:shivamarora1/crypto-ivr.git`` <br>
``$ cd crypto-ivr``

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



#### Python constructs used
1. **requests** to make http request.
2. **objects** and **classes**.
