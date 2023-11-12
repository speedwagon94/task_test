import asyncio
import re

from aiogram.types import ContentType
from loguru import logger
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import IDFilter, RegexpCommandsFilter, Regexp
import markups as btn
from db import Database
import config

db = Database("1.db")

# Если надо удалить таблицу
# db.drop_table('bookmarks')
db.create_table()
db.create_table_bookmarks()
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"


class Fsm(StatesGroup):
    name = State()
    email = State()
    mob_tel = State()
    user_naber = State()
    add_key_start = State()
    add_key = State()
    get_key = State()
    rm_key = State()


async def result(data, id):
    user_ie = 0
    user_sn = 0
    user_tf = 0
    user_jp = 0
    try:
        if (data["user_naber_1"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_2"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_3"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_4"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_5"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_6"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_7"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_8"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_9"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_10"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_11"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_12"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_13"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_14"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_15"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_16"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_17"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_18"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_19"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_20"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_21"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_22"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_23"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_24"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_25"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_26"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_27"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_28"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_29"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_30"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_31"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_32"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_33"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_34"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_35"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_36"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_37"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_38"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_39"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_40"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_41"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_42"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_43"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_44"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_45"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_46"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_47"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_48"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_49"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_50"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_51"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_52"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_53"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_54"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_55"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_56"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_57"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_58"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_59"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_60"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_61"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_62"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_63"] == 'a'):
            user_jp = user_jp + 1

        if (data["user_naber_64"] == 'a'):
            user_ie = user_ie + 1
        if (data["user_naber_65"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_66"] == 'a'):
            user_sn = user_sn + 1
        if (data["user_naber_67"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_68"] == 'a'):
            user_tf = user_tf + 1
        if (data["user_naber_69"] == 'a'):
            user_jp = user_jp + 1
        if (data["user_naber_70"] == 'a'):
            user_jp = user_jp + 1
    except:
        pass
    if (user_ie > 5):
        user_i = 'E'
    else:
        user_i = 'I'

    if (user_sn > 10):
        user_n = 'S'
    else:
        user_n = 'N'
    if (user_tf > 10):
        user_f = 'T'
    else:
        user_f = 'F'

    if (user_jp > 10):
        user_p = 'J'
    else:
        user_p = 'P'

    user_nnnn = user_i + user_n + user_f + user_p
    sum = user_ie + user_sn + user_tf + user_jp

    if (user_nnnn == 'ESTJ'):
        user_full = 'Тип Администратор: ответственный, надежный для него важны долг, иерархия, порядок практичный, открытый, все у него идет по плану без глупостей и лишних выдумок бесхитростный, исполнительный, цельная натура.  ESTJ.'
    if (user_nnnn == 'ISTJ'):
        user_full = 'Тип Инспектор или Опекун: на первом месте - долг, человек слова, ответственный спокойный, твердый, надежный, логичный, малоэмоциональный семьянин ему свойственны обстоятельность и даже въедливость.'
    if (user_nnnn == 'ISTP'):
        user_full = 'Тип Мастер: субординация - излишняя условность бесстрашие, жажда действий увлечения с оттенком экстремальности умение обращаться с любыми инструментами и механизмами это боевики, наемники им свойственны братские взаимоотношения формальное образование не обязательный вариант для них (часто бросают школу и редко стремятся к высшему образованию).'
    if (user_nnnn == 'ESTP'):
        user_full = 'Тип Маршал или Антрепренер: энергия, игра, неистощимый, искушенный в обращении с людьми остроумие, прагматизм работа в условиях риска и на грани катастрофы поиск острых ощущений преследуют выгоду во взаимоотношениях погоня за Госпожой Удачей, риск.'
    if (user_nnnn == 'INTP'):
        user_full = 'Тип Критик или Архитектор: ценитель мыслей и языка мгновенная оценка ситуации, логичность познание законов природы интеллектуал, несколько высокомерный, интеллигент, философ, математик, теоретик, неистощимый фонтан новых идей чуткий и умный родитель отличается сложным внутренним миром богатство ассоциаций.'
    if (user_nnnn == 'ENTP'):
        user_full = 'Тип Искатель или Изобретатель": применяет интуицию на практике (в изобретениях):, энтузиаст, новатор важна воплощенная идея, а не идея сама по себе приятный собеседник, инициативный в общении нетерпение к банальным, рутинным операциям, хороший педагог любит юмор девиз: "Понимать людей"!'
    if (user_nnnn == 'ENTJ'):
        user_full = 'Тип Предприниматель или Фельдмаршал: руководитель-стратег ориентация на цель логичный эффективность в работе превыше всего хранитель домашнего очага интеллигент требовательный родитель, неутомимый карьера иногда важнее, чем семейное благополучие.'
    if (user_nnnn == 'INTJ'):
        user_full = 'Тип Аналитик или Исследователь: самоуверенный его интересы в будущем авторитет положения или звания не имеет значения теоретик, приверженец "мозгового штурма", жизнь - игра на гигантской шахматной доске дефицит внешней эмоциональности, высокие способности к обучению, независимость, интуиция возможны трудности в мире эмоций и чувств.'
    if (user_nnnn == 'ESFJ'):
        user_full = 'Тип Энтузиаст или Торговец: открытый, практичный, расчетливый, обладает житейской мудростью компанейский, гостеприимный деловой, ответственный, интересы клиента превыше всего общительный.'
    if (user_nnnn == 'ISFJ'):
        user_full = 'Тип Хранитель или Консерватор: спокойный защищает интересы организации, традиции ответственный придерживается связи времен, проявляет интерес к истории все у него по плану заботливый выполнять поручения для него спокойнее, чем руководить хозяин в доме.'
    if (user_nnnn == 'ISFP'):
        user_full = 'Тип Посредник или Художник: успешное художественное творчество, эпикурейский образ жизни острота ощущения текущей минуты высокая чувствительность к оттенкам и полутонам в ощущениях тонкости устной и письменной речи обычно не интересуют свобода, оптимистичность, непокорность, уход от всякого рода ограничений.'
    if (user_nnnn == 'ESFP'):
        user_full = 'Тип Политик или Тамада: оптимизм и теплота избегают одиночества идут по жизни смеясь, жизнь для них - сплошные приключения игнорируют все мрачное щедрость, поддаются соблазнам старший друг для своего ребенка умение вдохновлять людей, приземленность языка наука - дело не для них, они выбирают бизнес, торговлю.'
    if (user_nnnn == 'INFP'):
        user_full = 'Тип Лирик или Романтик: спокойный, идеалист чувство собственного достоинства борется со злом за идеалы добра и справедливости отличается лирическим символизмом это писатель, психолог, архитектор кто угодно, только не бизнесмен способности в изучении языков принцип "Мой дом - моя крепость" уживчивые и покладистые супруги.'
    if (user_nnnn == 'ENFP'):
        user_full = 'Тип Советчик или Журналист: умение влиять на окружающих видит людей насквозь отрывается от реальности в поиске гармонии подмечает все экстраординарное ему свойственны чувствительность, отрицание сухой логики, творчество, энтузиазм, оптимизм, богатая фантазия это торговец, политик, драматург, практический психолог ему присущи экстравагантность, щедрость, иногда избыточная.'
    if (user_nnnn == 'ENFJ'):
        user_full = 'Тип Наставник или Педагог: гуманистический лидер, общительный, внимательный к чувствам других людей, образцовый родитель нетерпеливый по отношению к рутине и монотонной деятельности отличается умением распределить роли в группе.'
    if (user_nnnn == 'INFJ'):
        user_full = 'Тип Гуманист или Предсказатель: радость друзей - радость и для него проницательность и прозорливость успешное самообразование ранимость, не любят споров и конфликтов богатое воображение, поэтичность, любовь к метафорам это психолог, врачеватель, писатель стремится к гармонии человеческих взаимоотношений.'

    text = f"Буквенный код оценки: {user_nnnn}\nВашей оценкой является балл: {sum}/70\n" \
           f"Баллы расширенные: {user_ie} {user_sn} {user_tf} {user_jp} "
    await bot.send_message(id, text)
    await bot.send_message(id, user_full)
    await bot.send_message(id, 'Спасибо! Тестирование закончилось.')
    db.post_result(id, data['name'], data['email'], data['mob_tel'], user_nnnn, user_ie, user_sn, user_tf, user_jp, sum)


####################################ОТМЕНА########################################
@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Выход.\n")
    await state.finish()
    return False

####################################СТАРТ########################################
@dp.message_handler(commands=['start'])
async def admin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, btn.start, parse_mode='html')


####################################АВТОРИЗАЦИЯ########################################
@dp.message_handler(commands=['test'])
async def admin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, btn.text1, parse_mode='html')
    await bot.send_message(message.chat.id, btn.name)
    await Fsm.name.set()


@dp.message_handler(state=Fsm.name)
async def name(message: types.Message, state: FSMContext):
 
    await state.update_data(name=message.text)
    await bot.send_message(message.from_user.id, btn.email)
    await Fsm.email.set()


@dp.message_handler(state=Fsm.email)
async def email(message: types.Message, state: FSMContext):
 
    if not re.findall(pattern, message.text):
        await bot.send_message(message.from_user.id, "Неверный емэйл, попробуйте снова")
        return
    await state.update_data(email=message.text)
    await bot.send_message(message.from_user.id, btn.mob_tel)
    await Fsm.next()
    await state.update_data(state=1)


@dp.message_handler(state=Fsm.mob_tel)
async def mob_tel(message: types.Message, state: FSMContext):
 
    try:
        if len(message.text) == 11 and int(message.text):
            await state.update_data(mob_tel=message.text)
            await bot.send_message(message.from_user.id, btn.ready)
            await bot.send_message(message.from_user.id, btn.user_naber_1, reply_markup=btn.choice)
            await Fsm.next()
            await state.update_data(state=1)
            return
    except:
        pass
    await bot.send_message(message.from_user.id, "Неверный номер, попробуйте снова")
    return


####################################КНОПКИ ОПРОСА########################################
@dp.callback_query_handler(state=Fsm.user_naber)
async def user_naber(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query_id=callback.id)
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    data = await state.get_data(state)
    state_user = data["state"]
    if callback.data == "⏭":
        state_user += 1
        if len(data) - state_user == 2:
            # txt='Вы ответили не на все вопросы! Для коректного теста необходимо ответить на все'
            # await bot.send_message(callback.from_user.id, txt)
            state_user -= 1

    elif callback.data == "⏮":
        if state_user != 1:
            state_user -= 1
    else:
        dic = {f"user_naber_{state_user}": callback.data}
        await state.update_data(dic)
        state_user += 1
        if state_user == 70:
            data = await state.get_data(state)
            await result(data, callback.from_user.id)
            await state.finish()
            return

    await state.update_data(state=state_user)
    txt = btn.__dict__[f"user_naber_{state_user}"]
    try:
        already_answer = data[f"user_naber_{state_user}"]
        txt += f'''
<i>Ваш ответ:{already_answer}
</i>
'''
    except:
        pass
    await bot.send_message(callback.from_user.id, txt, reply_markup=btn.choice, parse_mode='html')

    data = await state.get_data(state)
    logger.info(data)


####################################КЛЮЧИ########################################
@dp.message_handler(commands=['listink13'], state="*")
async def list_key(message: types.Message):
    res = db.list_key(message.from_user.id)
    if not res:
        await bot.send_message(message.from_user.id, btn.list_key_error)
        return
    keys = ''
    for rows in res:
        keys += '`' + rows[0] + '`' + '\n'
    await bot.send_message(message.from_user.id, keys, parse_mode='markdown')

@dp.message_handler(commands=['add'])
async def add_key(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите добавить!")
    await Fsm.add_key_start.set()

@dp.message_handler(state=Fsm.add_key_start)
async def add_key(message: types.Message, state: FSMContext):
    key=message.text
    if db.isMessageExists(key):
        await bot.send_message(message.from_user.id, "Такое название уже занято. Попробуйте другой!")
        return
    await bot.send_message(message.from_user.id, btn.add_key(key), parse_mode='markdown')
    await state.update_data(key=key)
    await Fsm.add_key.set()


@dp.message_handler(state=Fsm.add_key, content_types=ContentType.ANY)
async def add_key2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if not db.add_key(message.from_user.id, data["key"], message.message_id):
        await bot.send_message(message.from_user.id, btn.add_key_error)
        return
    await bot.send_message(message.from_user.id, btn.add_key_successful)
    await state.finish()


@dp.message_handler(commands=['get'])
async def get_key(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите получить!")
    await Fsm.get_key.set()

@dp.message_handler(state=Fsm.get_key)
async def get_key2(message: types.Message, state: FSMContext):
    key = message.text
    res = db.get_key(message.from_user.id, key)
    if not res:
        await bot.send_message(message.from_user.id, btn.get_key_error)
        return
    try:
        await bot.copy_message(message.chat.id, message.from_user.id, res)
    except Exception as ex :
        logger.error(ex)
        await bot.send_message(message.from_user.id, btn.get_key_error2)
    await state.finish()

@dp.message_handler(commands=['rm'])
async def get_key(message: types.Message):
    await bot.send_message(message.from_user.id, "Укажите название закладки, которую хотите удалить!")
    await Fsm.rm_key.set()

@dp.message_handler(state=Fsm.rm_key)
async def get_key2(message: types.Message, state: FSMContext):
    key = message.text
    res = db.remove_key(message.from_user.id, key)
    if not res:
        await bot.send_message(message.from_user.id, btn.remove_key_error)
        return
    await bot.send_message(message.from_user.id, btn.remove_key(key), parse_mode='markdown')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
