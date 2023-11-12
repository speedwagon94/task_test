import re

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from db import Database
import markups as btn
import gerchikov_test as btn1
from gerchikov_test import question_max_answers, process_answers

db = Database("1.db")

db.create_table_gerchikov_results()
db.create_table_bookmarks()
db.create_table()
bot = Bot(token="")
dp = Dispatcher(bot, storage=MemoryStorage())
pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"


class Fsm(StatesGroup):
    name = State()
    position = State()
    email = State()
    mob_tel = State()
    user_naber = State()
    gerchikov = State()
    add_key_start = State()
    add_key = State()
    get_key = State()
    rm_key = State()

# Подсчет очков
user_pr = 0
user_pa = 0
user_ho = 0
user_lu = 0
user_in = 0

# Словаь для выбранных ответов
selected_answers = {}


async def ger_result(data, id):
    """
    Оценивает результаты теста Герчикова, определяет преобладающий тип личности и отправляет сообщение пользователю.
    Также сохраняет результаты в базу данных.

    Parameters:
    - data (dict): Словарь с данными пользователя.
    - id (int): Идентификатор чата пользователя.

    Global Variables:
    - user_pr (int): Текущий балл для черты личности 'pr' (точность).
    - user_pa (int): Текущий балл для черты личности 'pa' (страсть).
    - user_ho (int): Текущий балл для черты личности 'ho' (честность).
    - user_lu (int): Текущий балл для черты личности 'lu' (лояльность).
    - user_in (int): Текущий балл для черты личности 'in' (честность).

    Returns:
    - None
    """
    global user_pr, user_pa, user_ho, user_lu, user_in

    variables = {
        'Инструментальный тип (ИН)': user_in,
        'Профессиональный тип (ПР)': user_pr,
        'Патриотический тип (ПА)': user_pa,
        'Хозяйский тип (ХО)': user_ho,
        'Люмпенизированный (ЛЮ)': user_lu,
    }

    max_variable = max(variables, key=variables.get)

    text = f"Количество баллов: ИН:{user_in}, ПР:{user_pr}, ПА:{user_pa}, ХО:{user_ho}, ЛЮ:{user_lu}\nВаш тип: {max_variable} {variables[max_variable]}"
    await bot.send_message(id, text)

    # Сохраняем результаты в базу данных
    db.ger_post_result(id, data['name'], data['email'], data['mob_tel'], data['position'], user_in, user_pr, user_ho,
                       user_lu, user_pa)


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


@dp.message_handler(commands=['gerchikov'])
async def gerchikov_handler(message: types.Message, state: FSMContext):
    """
    Обработчик команды /gerchikov. Инициирует процесс тестирования Герчикова.

    Parameters:
    - message (types.Message): Объект сообщения пользователя.
    - state (FSMContext): Объект для работы с машиной состояний.

    Returns:
    - None
    """
    await bot.send_message(message.chat.id, btn.name)
    await Fsm.name.set()
    # Устанавливает состояние флага. Чтобы в дальнейшем понять какой тест был выбран.
    # Флаги используются для отслеживания состояния пользователя в ходе взаимодействия с ботом.
    await state.update_data(is_gerchikov=True)
    await state.update_data(is_test=False)


@dp.message_handler(commands=['test'])
async def admin(message: types.Message, state: FSMContext):
    """
    Обработчик команды /test. Инициирует процесс обычного тестирования.

    Parameters:
    - message (types.Message): Объект сообщения пользователя.
    - state (FSMContext): Объект для работы с машиной состояний.

    Returns:
    - None
    """
    await bot.send_message(message.chat.id, btn.text1, parse_mode='html')
    await bot.send_message(message.chat.id, btn.name)
    await Fsm.name.set()
    # Устанавливает состояние флага. Чтобы в дальнейшем понять какой тест был выбран.
    # Флаги используются для отслеживания состояния пользователя в ходе взаимодействия с ботом.
    await state.update_data(is_test=True)
    await state.update_data(is_gerchikov=False)


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
    await Fsm.mob_tel.set()
    await state.update_data(state=1)


@dp.message_handler(state=Fsm.mob_tel)
async def mob_tel(message: types.Message, state: FSMContext):
    """
    Обработчик ввода номера телефона.

    Parameters:
    - message (types.Message): Объект сообщения пользователя.
    - state (FSMContext): Объект для работы с машиной состояний.

    Returns:
    - None
    """
    data = await state.get_data()
    is_gerchikov = data.get('is_gerchikov', False)
    is_test = data.get('is_test', False)

    try:
        # Проверяем, что введенный текст - число и имеет длину 11 символов
        if len(message.text) == 11 and int(message.text):
            await state.update_data(mob_tel=message.text)

            # В зависимости от текущего состояния (тест Герчикова или обычный тест) переходим к следующему шагу
            # Для этого мы устанавливали флаги, которые перенаправляют пользователя дальше
            if is_gerchikov:
                await bot.send_message(message.from_user.id, btn1.position)
                await Fsm.position.set()
                await state.update_data(state=1)
            elif is_test:
                await bot.send_message(message.from_user.id, btn.ready)
                await bot.send_message(message.from_user.id, btn.user_naber_1, reply_markup=btn.choice)
                await Fsm.user_naber.set()
                await state.update_data(state=1)
            return
    except ValueError:
        pass

    # Если введенный номер неверен, отправляем сообщение с просьбой ввести снова
    await bot.send_message(message.from_user.id, "Неверный номер, попробуйте снова")
    return

# Должность
@dp.message_handler(state=Fsm.position)
async def position(message: types.Message, state: FSMContext):
    await state.update_data(position=message.text)
    await bot.send_message(message.from_user.id, btn1.q1, reply_markup=btn1.choice)
    await Fsm.gerchikov.set()


@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Выход.\n")
    await state.finish()
    return False


@dp.message_handler(commands=['start'])
async def admin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, btn.start, parse_mode='html')


@dp.callback_query_handler(state=Fsm.gerchikov)
async def gerchikov(callback: types.CallbackQuery, state: FSMContext):
    """
    Обработчик ответов пользователя в ходе тестирования по методике Герчикова.

    Parameters:
    - callback (types.CallbackQuery): Объект коллбека с данными об ответе пользователя.
    - state (FSMContext): Объект для работы с машиной состояний.

    Returns:
    - None
    """
    global user_pr, user_pa, user_ho, user_lu, user_in

    # Отвечаем на коллбек, чтобы избежать повторного нажатия
    await bot.answer_callback_query(callback_query_id=callback.id)

    # Удаляем предыдущее сообщение с вопросом
    await bot.delete_message(callback.from_user.id, callback.message.message_id)

    # Получаем текущее состояние пользователя
    state_user = await state.get_data()
    state_user = state_user.get("state", 1)

    # Формируем имя текущего вопроса
    current_question = f"q{state_user}"

    # Обработка ответа пользователя
    if callback.data in ["1", "2", "3", "4", "5", "6"]:
        max_answers = question_max_answers.get(current_question, 1)

        if current_question not in selected_answers:
            selected_answers[current_question] = {callback.data}
        else:
            if len(selected_answers[current_question]) < max_answers:
                selected_answers[current_question].add(callback.data)
            else:
                # Ограничиваем количество выбранных ответов для текущего вопроса
                await bot.send_message(callback.from_user.id,
                                       f"Максимальное количество ответов для этого вопроса: {max_answers}. Выберите правильное количество ответов.")

    # Обработка перехода к предыдущему вопросу
    if callback.data == "⏮":
        if state_user != 1:
            state_user -= 1

    # Обработка перехода к следующему вопросу
    if "⏭" in callback.data:
        if f"q{state_user}" in selected_answers:
            answers_q = ",".join(selected_answers.get(f"q{state_user}", set()))
            user_pr, user_pa, user_ho, user_lu, user_in = process_answers(f"q{state_user}", answers_q, user_pr, user_pa,
                                                                          user_ho, user_lu, user_in)

            print(
                f"Для вопроса q{state_user} получены следующие значения: user_pr={user_pr}, user_pa={user_pa}, user_ho={user_ho}, user_lu={user_lu}, user_in={user_in}")

            state_user += 1
            if state_user == 24:
                data = await state.get_data()
                await ger_result(data, callback.from_user.id)
                await state.finish()
                return
            await state.update_data(state=state_user)
            txt = btn1.__dict__[f"q{state_user}"]
            await bot.send_message(callback.from_user.id, txt, reply_markup=btn1.choice, parse_mode='html')
        else:
            await bot.send_message(callback.from_user.id,
                                   "Пожалуйста, выберите хотя бы один ответ перед переходом к следующему вопросу.")
    else:
        txt = btn1.__dict__[f"q{state_user}"]
        try:
            already_answers = selected_answers.get(f"q{state_user}", set())
            if already_answers:
                txt += f'''
<i>Ваши ответы: {', '.join(already_answers)}
</i>
'''
        except:
            pass
        await bot.send_message(callback.from_user.id, txt, reply_markup=btn1.choice, parse_mode='html')



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
    key = message.text
    if db.isMessageExists(key):
        await bot.send_message(message.from_user.id, "Такое название уже занято. Попробуйте другой!")
        return
    await bot.send_message(message.from_user.id, btn.add_key(key), parse_mode='markdown')
    await state.update_data(key=key)
    await Fsm.add_key.set()


@dp.message_handler(state=Fsm.add_key, content_types=types.ContentType.ANY)
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
    except Exception as ex:
        # logger.error(ex)
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
