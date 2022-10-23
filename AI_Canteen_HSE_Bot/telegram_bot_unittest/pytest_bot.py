def test_bot_start(bot, user):

    user.send_command('/start')

    message = user.get_message()

    assert message
    assert message['text'] == '''Здравствуйте, добро пожаловать в наше заведение!

                        Я - ваш бот официант, готовый помочь вам с выбором и заказом😉
                        Вот, что я умею:
                        
                        /menu - меню ресторана🍕
                        /order - сделать заказ📃
                        /rec - если не знаете, что выбрать
                        
                        Если уже знаете, что хотите заказать, то можете просто написать "Я хочу", а дальше свой заказ в формате:
                        
                        блюдо - количество порций,
                        блюдо - количество порций и т.д.
                        
                        подробнее о формате заказа расскажу по команде /order'''


def test_bot_rec(bot, user):

    user.send_command('/rec')

    message = user.get_message()

    assert message
    assert message['text'] == 'Вы желаете плотно поесть или перекусить?'


def test_bot_order(bot, user):

    user.send_command('/order')

    message = user.get_message()

    assert message
    assert message['text'] == 'Начните со слов "Я хочу ", а дальше напишите список блюд, как в примере'


def test_bot_menu(bot, user):

    user.send_command('/menu')

    message = user.get_message()

    assert message
    assert message['text'] == '''Наше меню: 
 
                            -Суши с лососем🐟
                            -Салат с хумусом и фалафелем🥬
                            -Стейк Рибай🥩
                            -Куриные крылышки баффало🍗
                            -кокосовое мороженное🍨
                            -Пироженое Брауни🍫
                            -Хлебные гренки с чесноком🍞
                            -Пицца пепперони🍕
                            -Торт Наполеон🍰
                            
                            
                            Если не знаете, что выбрать нажмите /rec'''