import logging
#импортируем executor для того, чтобы завести шаблон поведения бота,
# классы Bot и dispatcher для инициализации бота в телеге и класс types для работы с типами данных телеграмма(message, photo etc.)
from aiogram import Bot, Dispatcher, executor, types
import json
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5643560588:AAFsdtDfq2JzmdPB4npE5kYEnq73rIojulQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


kb = ReplyKeyboardMarkup(resize_keyboard=True)

kbi = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

last_message = ''

client_onload = {}

n_elka = 1

answ_ar = ['плотно', 'перекус', 'японская кухня',
           'американская кухня', 'итальянская кухня',
           'японская кухня', 'разное', 'французкая кухня',
           'рыба', 'мясо', 'птица', 'vega', 'да', 'нет']
answ_var = {
    'американская кухня': 'кухня',
    'итальянская кухня': 'кухня',
    'разное': 'кухня',
    'французкая кухня': 'кухня',
    'японская кухня': 'кухня',
    'сытно':'сытность',
    'не сытно': 'сытность',
    'мясо':'мясо',
    'рыба':'мясо',
    'птица':'мясо',
    'vega':'мясо',
    'да': 'сахар',
    'нет':'сахар'
            }

client_answ = {'кухня':'', 'сытность':'', 'мясо': '', 'сахар': ''}

questions = ['Вы желаете плотно поесть или перекусить?',
             'А какую кухню предпочитаете?',
             'Какой вид мяса вы бы хотели поесть?\n\nЕсли вы вегитарианец, выберите Vega',
             'Едите ли вы блюда с сахаром?'
             ]
photos = {
    "Суши с лососем": '365Сливочный_лосось.jpg',
    "Стейк рибай": '217bb0ad4ece0ad526db6763b5526136.jpg',
    "Салат с хумусом и фалафелем": 'fal11-zahod.jpg',
    "торт Наполеон": 'DSCF0760-1.jpg',
    "Куриные крылышки Баффало":'franks_redhot_buffalo_chicken_wings_043-601x601.jpg',
    "Кокосовое мороженное":'domashnee-morojenoe-iz-kokosovogo-moloka_1567669131_9_max.jpg',
    "Хлебные гренки с чесноком": 'grenki-s-chesnokom.jpg',
    "Пироженное Брауни": 'unnamed.jpg',
    "Пицца пепперони": 'p_O.jpg'
}


buttons = [
    ['сытно', 'не сытно'],
    [
    'японская кухня',
    'американская кухня',
    'итальянская кухня',
    'разное',
    'французкая кухня'
    ],
    [
        'рыба',
        'мясо',
        'птица',
        'vega'
    ],
    [
        'да',
        'нет'
    ]
]

elka_ar = [0]

def boot():
    menu = KeyboardButton('/menu')
    order = KeyboardButton('/order')
    rec = KeyboardButton('/rec')
    kb.add(menu)
    kb.add(order)
    kb.add(rec)




@dp.message_handler(commands=['start'])
async def greetings(message:types.Message):
        last_message = message.text
        await message.reply('Здравствуйте, добро пожаловать в наше заведение!\n'
                            '\n'
                            'Я - ваш бот официант, готовый помочь вам с выбором и заказом😉\n'
                            'Вот, что я умею:\n'
                            '\n'
                            '/menu - меню ресторана🍕\n'
                            '/order - сделать заказ📃\n'
                            '/rec - если не знаете, что выбрать\n'
                            '\n'
                            'Если уже знаете, что хотите заказать, то можете просто написать \"Я хочу\", а дальше свой заказ в формате:\n'
                            '\n'
                            'блюдо - количество порций,\n'
                            'блюдо - количество порций и т.д.\n'
                            '\n'
                            'подробнее о формате заказа расскажу по команде /order ', reply_markup=kb)

@dp.message_handler(commands=['menu'])
async def menu(message:types.Message):
    last_message = message.text
    with open('menu', 'r', encoding='utf-8') as file:
        await message.reply('Наше меню: \n \n' + str(file.read()) + '\n\n' + 'Если не знаете, что выбрать нажмите /rec')

@dp.message_handler(commands=['order'])
async def order(message: types.Message):
    with open('order_example.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,'Начните со слов \"Я хочу \", а дальше напишите список блюд, как в примере')

@dp.message_handler(commands=['rec'])
async def menu(message: types.Message):
    kbi = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for k in buttons[elka_ar[0]]:
        kbi.add(KeyboardButton(k))
    await bot.send_message(message.chat.id, 'Вы желаете плотно поесть или перекусить?', reply_markup=kbi)
    '''@dp.message_handler(content_types=['text'])
            async def elka_2(message):
                kbi.add(KeyboardButton('японская кухня'))
                await bot.send_message(message.chat.id, 'А какую кухню предпочитаете?', reply_markup=kbi)'''


elka = 1

def rec_sort(client_d):
    best_var = ''
    score = 0
    max_score = 100000000
    with open('products.json', 'rb') as file:
        content = json.load(file)
    for pro_i in content:
        differ = []
        for k in pro_i.values():
            for j in client_d.values():
                if k!=j:
                    differ.append(k)
        score = len(differ)
        if score < max_score:
            max_score = score
            best_var = pro_i["Название"]
        else:
            continue
    return best_var


@dp.message_handler(content_types=['text'])
async def ordtext(message: types.Message):
    txt = str(message.text).lower()
    if 'я хочу' in txt.lower():
        txt = txt.replace('я хочу ', '')
        txt = txt.replace('я хочу\n', '')
        data = txt.split(',')
        onload = {'id': message.from_user.id, 'блюда': '', 'количество': ''}
        dumb = []
        print(onload)
        with open('orders.json', 'w', encoding='utf-8') as datafile:
            for i in data:
                onld = i.split(' - ')
                onload_copy = onload.copy()
                onload_copy['блюда'] = onld[0].replace('\n', '')
                onload_copy['количество'] = onld[1]
                print(onload)
                dumb.append(onload_copy)
                print(dumb)

            print(dumb)
            json.dump(dumb, datafile, ensure_ascii=False, indent=4)
        await message.reply('Спасибо за заказ!')
    if txt in answ_var:
        client_answ[answ_var[txt]] = txt
        print(client_answ)
        if elka_ar[0] == len(questions)-1:
            result = rec_sort(client_answ)
            print(result)
            elka_ar[0] = 0
            #await bot.send_message(message.chat.id, f'Чтож, спасибо за ответы, рекомендую попробовать {result}')
            with open(photos[result], 'rb') as file:
                await bot.send_photo(message.chat.id, file, caption=f'Чтож, спасибо за ответы, рекомендую попробовать {result}')
        else:
            if elka_ar[0]\
                    != len(buttons)-1:
                kbi = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                for k in buttons[elka_ar[0]+1]:
                    kbi.add(KeyboardButton(k))
                await bot.send_message(message.chat.id, questions[elka_ar[0]+1], reply_markup=kbi)
            else:
                await bot.send_message(message.chat.id, questions[elka_ar[0]+1])
            elka_ar[0] += 1
    #elif txt not in answ_var and not(txt.startswith('я хочу')):
        #await bot.send_message(message.chat.id, 'Извините, я вас не понимаю')

if __name__ == '__main__':
    boot()
    #inl_boot()
    executor.start_polling(dp, skip_updates=True)
