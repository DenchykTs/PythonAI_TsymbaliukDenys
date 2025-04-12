# https://t.me/AI_C2221_Denys_Tsymbaliuk_bot
from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

url = "https://uaserials.pro/films/"
r = requests.get(url)
soup = BeautifulSoup(r.text, features = "html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt', "w", encoding = 'utf-8')
for href in soup_list_href:
    print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

# print(links_list)

f = open('info.txt', 'w', encoding = 'utf-8')

exchange_rate_list = []
list_name = []
list_desc = []
list_numbers = [0, 18]

for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text, features = "html.parser")
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film) > 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)

f.close()

command = """/help - список всіх команд
/hello - привітання,
/film - список найновіших фільмів,
/star - зірка,
/RoleTheFilm - обирання фільму,
/rate - курс валют
/most_popular - найпопулярніші фільми
/least_popular - найменшпопулярні фільми"""

def exchange():
    url = "https://bank.gov.ua/ua/markets/exchangerates"
    get_url = requests.get(url)
    exchange_soup = BeautifulSoup(get_url.text, features = "html-parser")
    exchange_soup_liter = exchange_soup.find_all('td', {'data-label': "Код літерний"})
    exchange_soup_count = exchange_soup.find_all('td', {'data-label': "Кількість одиниць валюти"})
    exchange_soup_course = exchange_soup.find_all('td', {'data-label': "Офіційний курс"})

    for line in range(len(exchange_soup_liter)):
        exchange_text = f"{exchange_soup_liter[line].text}\t {exchange_soup_count[line].text} : {exchange_soup_course[line].text}\t"
        exchange_rate_list.append(exchange_text)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def most_popular(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Майнкрафт в кіно"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\n Description: {list_desc[i]}\n Link: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def least_popular(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_name = "Артур"
    found = False
    for i in range(len(list_name)):
        if target_name.lower() in list_name[i].lower():
            text = f"Title: {list_name[i]}\n Description: {list_desc[i]}\n Link: {links_list[i]}"
            await update.message.reply_text(text)
            found = True
            break
    if not found:
        await update.message.reply_text(f"Movie '{target_name}' not found.")

async def random_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    numbers = random.randint(0,18)
    number = f"{list_name[numbers]}\n{list_desc[numbers]}\n{list_name[numbers]}"
    await update.message.reply_text(number)

async def star(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'You are my star! {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{list_name[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    exchange()
    for i in range(len(exchange_rate_list)):
        text = f"{exchange_rate_list[i]}"
        await update.message.reply_text(text)


app = ApplicationBuilder().token("8123978417:AAH_s67C7IC5IUJLFUZ_nRhiJMyppM0AzA8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("star", star))
app.add_handler(CommandHandler("RoleTheFilm", random_film))
app.add_handler(CommandHandler("rate", rate))
app.add_handler(CommandHandler("most_popular", most_popular))
app.add_handler(CommandHandler("least_popular", least_popular))

app.run_polling()