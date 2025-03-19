import requests
from bs4 import BeautifulSoup

amazon_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'DNT': '1',
    'Connection': 'keep-alive'
}

cookie = {
    'aws-target-data':'%7B%22support%22%3A%221%22%7D',
    'aws-target-visitor-id':'1742274122917-718629.42_0',
    'regStatus':'pre-register',
    'AMCV_7742037254C95E840A4C98A6%40AdobeOrg':'1585540135%7CMCIDTS%7C20166%7CMCMID%7C61349907400594365133999107933293868224%7CMCAAMLH-1742878922%7C11%7CMCAAMB-1742878922%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1742281323s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0',
    'session-id':'135-5794392-1819110',
    'session-id-time':'2082787201l',
    'i18n-prefs':'USD',
    'sp-cdn':'L5Z9:KR',
    'skin':'noskin',
    'ubid-main':'131-7340786-9475353',
    'session-token':'96KHUlnml49kWKPvRDhPiTgDGrYt4k7cAwfveRVlmDqSYV9kIRtq4WMhAIHhuTR0OsvkTgfp7ZlS0Q2+fDwpZQz9f4o97oFRZHBxxq3XvkFoWLG3sH5X3YE2W0QgdN9cYutPkwKm17OVA3td/O6n1vw/4h16/yd4SMEhWjY75skIMpCWXUStNjkGqwIVPm+Rx7dlh0yFsZfF0ACSoTxpWnLRz4FI0nvauuxvNG+zn0hl3fS6JQkVy7ImmyPDBJ1S0zVoBluLjkEHjfEWHTytwJNy8KoWrxV/bPQpWATMVAPmyAk1Of62wy3dUJCMOgTUL7uagSse3ju6t12ean5gOzhNQyNs2qOW',
    'csm-hit':'tb:s-GV223XGNKT8MSN6XEGKV|1742399608726&t:1742399609684&adb:adblk_no'
}

r = requests.get('https://www.amazon.com/s?k=monitor&crid=1G9WSO12N4B55&sprefix=monit%2Caps%2C265&ref=nb_sb_noss_2', headers=amazon_header, cookies=cookie)


soup = BeautifulSoup(r.content, 'html')
print(soup)

# print(r.content)
# print(r.status_code)