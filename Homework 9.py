import requests

# response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
# print(type(response.content))
# response = requests.post("https://bank.gov.ua/ua/markets/exchangerates", data = "Test data")
# print(response.text)

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text
response_parse = response_text.split("<td>")
for pars_elem_1 in response_parse:
    if pars_elem_1.startswith('$'):
        for pars_elem_2 in pars_elem_1.split('</td>'):
            if pars_elem_2.startswith('$') and pars_elem_2[1].isdigit():
                print(pars_elem_2)