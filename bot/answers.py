'''
File with all buttons and keyboards for bot
'''

# Matkup
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, \
InlineKeyboardButton, InlineKeyboardMarkup


# Format functions
def buttonformcourierstatus(text, txtbtn, call):
    """Format courier change status button"""

    return InlineKeyboardButton(txtbtn.format(status=text),
                                callback_data=call)

class Callbacks:
    """Callbacks"""

    CALLBACKNUMBER = 'changenumber'
    CALLBACKROOM = 'changeroom'

    CALLBACKCOURIERREG = 'courierreg'
    CALLBACKCOURIERCHST = 'courierchst'
    CALLBACKCOURIERPRICE = 'courierprice'

    CALLBACKNEWORDER = 'neworder'
    CALLBACKDELORDER = 'delorder'

    CALLBACKTAKEORDER = 'order-'

class Buttons:
    """Buttons"""

    callbacks = Callbacks()

    PROFILEBTN = "Мой профиль"
    COURIERBTN = "Карьера курьера"
    ORDERSBTN = "Мои заказы"

    COURIERSTARTBTN = "Зарегистрироваться"
    COURIERCHSTBTN = "Изменить статус на: {status}"
    CHANGECOURIERPRICEBTN = "Изменить минимальную цену заказа"

    CHANGEROOMBTN = "Изменить комнату"
    CHANGENUMBERBTN = "Изменить номер"

    NEWORDERBTN = "Создать заказ"
    DELORDERBTN = "Удалить заказ"

    TAKEORDERBTN = "Взять заказ"


    MY_PROFILE = KeyboardButton(PROFILEBTN)
    COURIER = KeyboardButton(COURIERBTN)
    MYORDERS = KeyboardButton(ORDERSBTN)

    EDIT_ROOM = InlineKeyboardButton(CHANGEROOMBTN, callback_data=callbacks.CALLBACKROOM)
    EDIT_NUMBER = InlineKeyboardButton(CHANGENUMBERBTN, callback_data=callbacks.CALLBACKNUMBER)

    COURIER_START = InlineKeyboardButton(COURIERSTARTBTN, \
                                         callback_data=callbacks.CALLBACKCOURIERREG)
    CHANGECOURIERPRICE = InlineKeyboardButton(CHANGECOURIERPRICEBTN, \
                                              callback_data=callbacks.CALLBACKCOURIERPRICE)

    NEWORDER = InlineKeyboardButton(NEWORDERBTN, callback_data=callbacks.CALLBACKNEWORDER)
    DELORDER = InlineKeyboardButton(DELORDERBTN, callback_data=callbacks.CALLBACKDELORDER)

class Answers:
    """Answers"""

    STARTMSG = "Привет, я - бот, созданный @MIKHAN_GO для помощи в доставке еды внутри СУНЦ МГУ.\n\
Зарегистрируйся, и я расскажу, как это работает😁"
    TELEPHONE = "Для начала отправь мне свой номер телефона в формате 8XXXXXXXXXX"
    ROOM = "Отлично! Теперь отправь мне номер комнаты, в которой ты проживаешь"
    ENDREG = "Ты успешно зарегистрировался(-ась)!"

    PROFILE = "*Твой профиль*\n\n*Имя:*  {nick}\n*Номер:*  \
{number}\n*Номер комнаты:*  {room}"
    EDITNUMBER = "Введи новый номер телефона в формате 8XXXXXXXXXX"
    EDITROOM = "Введи новый номер комнаты"
    PROFILEEDITED = "Твой профиль успешно изменен"

    COURIERPROFILE = "*Твой карьерный профиль*\n\n*Имя:*  {nick}\n*Заказ от:* {minrub} ₽\n\
*Всего заработано:*  {coins} ₽\n*Текущий статус:*  {currstatus}"
    COURIERREG = "Ты еще не зарегистрирован(-а) как курьер. Если хочешь начать брать заказы, \
зарегистрируйся по конпке ниже."
    COURIERREGSUCCESS = "Вы успешно зарегистрировались как курьер!"
    COURIERBUSY = "Занят"
    COURIERFREE = "Свободен"
    COURIERMINPRICE = "Введи минимальную цену, от которой ты берешь заказы\nНе более 10000"

    ORDERSMAIN = "*Мои заказы*\n\n"
    NEWORDERCOURIER = "*Новый заказ!*\n\n*ID:* {id}\n*Имя заказчика:* {name}\n*Номер заказчика:* \
{number}\n*Комната для доставки:* {room}\n*Цена:* {price}\n*Комментарий к заказу:* {comment}\n\n"
    ORDERFORMAT = "*ID:* {id}\n*Имя курьера:* {name}\n*Номер курьера:* {number}\n\
*Комната для доставки:* {room}\n*Цена:* {price}\n*Комментарий к заказу:* {comment}\n\n"
    FINDCOURIER = "Ищем курьера"
    ORDERGETPRICE = "Введи цену, которую ты готов заплатить (за заказ, естественно)"
    ORDERGETCOMMENT = "Введи комментарий к заказу"
    ORDERGETID = "Введи ID заказа, который хочешь удалить"
    ORDERSUCCESS = "Заказ успешно создан!"
    ORDERDELSUCCESS = "Заказ успешно удален!"
    LIMITORDERS = "У вас не может быть > 2 заказов одновременно!"
    NOORDERS = "У вас нет текущих заказов"
    COURIERORDERROR = "У заказа уже есть курьер. Для обсуждения \
деталей заказа напишите ему в личные сообщения."
    BADORDER = "У вас нет такого заказа!"
    TAKEORDER = "Взять заказ"

    BADREQUESTREG = "Ты уже зарегистрирован(-а)!"
    DOESNTREG = "Ты еще не зарегистрирован(-а)! Напиши мне /start, чтобы это исправить;)"
    BADREQUEST = "Я не понимаю😢"
    PHONEWRONG = "Неправильный формат ввода!"
    ROOMWRONG = "Неправильный формат ввода!"
    UNCORRECTPRICE = "Неправильный формат цены!"

class Markups:
    """Markups"""

    buttons = Buttons()
    answers = Answers()
    callbacks = Callbacks()

    BASEMARKUP = ReplyKeyboardMarkup(resize_keyboard=True)
    BASEMARKUP.add(buttons.MY_PROFILE, buttons.COURIER, buttons.MYORDERS)

    PROFILEMARKUP = InlineKeyboardMarkup(row_width=1)
    PROFILEMARKUP.add(buttons.EDIT_ROOM, buttons.EDIT_NUMBER)

    COURIERREGMARKUP = InlineKeyboardMarkup(row_width=1)
    COURIERREGMARKUP.add(buttons.COURIER_START)

    COURIERSTATMARKUP = InlineKeyboardMarkup(row_width=1)
    COURIERSTATMARKUP.add(buttons.COURIER_START)

    COURIERBUSYMARKUP = InlineKeyboardMarkup(row_width=1)
    COURIERBUSYMARKUP.add(buttonformcourierstatus( \
        answers.COURIERBUSY, buttons.COURIERCHSTBTN, callbacks.CALLBACKCOURIERCHST), \
                          buttons.CHANGECOURIERPRICE)

    COURIERFREEMARKUP = InlineKeyboardMarkup(row_width=1)
    COURIERFREEMARKUP.add(buttonformcourierstatus( \
        answers.COURIERFREE, buttons.COURIERCHSTBTN, callbacks.CALLBACKCOURIERCHST), \
                          buttons.CHANGECOURIERPRICE)

    ACTORDER = InlineKeyboardMarkup(row_width=1)
    ACTORDER.add(buttons.NEWORDER, buttons.DELORDER)

    EMPTYINL = InlineKeyboardMarkup()
