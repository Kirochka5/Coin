from flask import Flask
from markupsafe import escape
import random

app = Flask(__name__)

facts = [
    'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',

'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',

'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',

'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',

'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ'
]

coins = ['орел', 'решка']

@app.route("/")
def hello_world():
    return '<a href="/random_fact">Посмотреть случайный факт!</a>'



@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts)}</p>'

@app.route("/<dice>")
def random_dice(dice):
    return f'Вам выпало число {random.randint(1,int(dice))}'

@app.route("/coin")
def random_coin():
    return f'У вас {random.choice(coins)}'

app.run(debug=True)