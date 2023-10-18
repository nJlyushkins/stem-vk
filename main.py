import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token="b38692f39ecaa16c600bcdb020ae4be656d11f411ba680e236c68f5fbf9a8bcb1363e024f00218809b46b"

# Клавиатура после курса
keyboard_ater_cource = VkKeyboard(inline = True)
keyboard_ater_cource.add_openlink_button('Записаться самому через мой класс',link="https://vk.com/coistem?w=app6094020_-113376999")
keyboard_ater_cource.add_line()
keyboard_ater_cource.add_button('Связаться с менеджером', color = VkKeyboardColor.PRIMARY)
keyboard_ater_cource.add_line()
keyboard_ater_cource.add_button('Вернуться к занятиям')
keyboard_ater_cource.add_line()
keyboard_ater_cource.add_button('Вернуться в основное меню')
keyboard_ater_cource.add_line()
keyboard_ater_cource.add_button('У меня больше нет вопросов')


# Клавиатура после контактов
keyboard_ater = VkKeyboard(one_time = True)
keyboard_ater.add_button('Вернуться в основное меню', color = VkKeyboardColor.PRIMARY)
keyboard_ater.add_line()
keyboard_ater.add_button('Больше нет вопросов')

# Клавиатура для связи с менеджером
keyboard_contact_meneger = VkKeyboard(inline = True)
keyboard_contact_meneger.add_button('Да, хочу связаться с менеджером',color = VkKeyboardColor.POSITIVE)
keyboard_ater_cource.add_line()
keyboard_ater_cource.add_button('Вернуться в основное меню')

keyboard_user_meneger = VkKeyboard(one_time = True)
keyboard_user_meneger.add_button('Спасибо, вы ответили на мой вопрос')

# Клавиатура "С чат-ботом или с менеджером"
keyboard_meneger = VkKeyboard(one_time = True)
keyboard_meneger.add_button('Хотите что-то узнать')
keyboard_meneger.add_line()
keyboard_meneger.add_button('Связаться с менеджером')

# Клавиатура "Начать"
keyboard_begin = VkKeyboard(one_time = True)
keyboard_begin.add_button('Начать', color = VkKeyboardColor.PRIMARY)

# Клавиатура "Что вы хотели узнать?"
keyboard_chapter = VkKeyboard(inline = True)
keyboard_chapter.add_openlink_button('Записаться самому через мой класс',link="https://vk.com/coistem?w=app6094020_-113376999")
keyboard_chapter.add_line()
keyboard_chapter.add_button('Направления и цены')
keyboard_chapter.add_line()
keyboard_chapter.add_button('Подробнее о центре')
keyboard_chapter.add_line()
keyboard_chapter.add_button('Связаться с менеджером')

# Клавиатура с курсами
keyboard_cource = VkKeyboard(one_time = True)
keyboard_cource.add_button('Программирование', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_line()
keyboard_cource.add_button('Робототехника', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_button('WEB-разработка', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_line()
keyboard_cource.add_button('Компьютерная графика', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_button('Компьютерная грамотность', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_line()
keyboard_cource.add_button('Инженерные проекты', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_line()
keyboard_cource.add_button('Школа дронов АЭРОСТЕМ', color = VkKeyboardColor.PRIMARY)
keyboard_cource.add_line()
keyboard_cource.add_button('Вернуться назад')

keyboard_cource_programming = VkKeyboard(inline = True)
keyboard_cource_programming.add_button('Python', color = VkKeyboardColor.PRIMARY)
keyboard_cource_programming.add_button('Construct 2', color = VkKeyboardColor.PRIMARY)
keyboard_cource_programming.add_line()
keyboard_cource_programming.add_button('Java', color = VkKeyboardColor.PRIMARY)
keyboard_cource_programming.add_button('C#', color = VkKeyboardColor.PRIMARY)
keyboard_cource_programming.add_button('Scratch', color = VkKeyboardColor.PRIMARY)
keyboard_cource_programming.add_line()
keyboard_cource_programming.add_button('Вернуться к направлениям')
keyboard_cource_programming.add_line()
keyboard_cource_programming.add_button('Вернуться в основное меню')

def get_name(uid: int) -> str:
    data = authorize.method("users.get", {"user_ids": uid})[0]
    return "{}".format(data["first_name"])

def get_fullname(uid: int) -> str:
    data = authorize.method("users.get", {"user_ids": uid})[0]
    return "{} {}".format(data["first_name"], data["last_name"])

def write_message(sender, message):# Функция для ответа на сообщения
    authorize.method('messages.send', {'user_id' : sender, 'message' : message, 'random_id': get_random_id()})

def write_message_image_video(sender, message, attachments):# Функция для ответа на сообщения с картинкой
    authorize.method('messages.send', {'user_id' : sender, 'message' : message, 'random_id': get_random_id(), 'attachment': attachments}) # 'attachment': ','.join(attachments)

def write_message_keyboard(sender, message, keyboard):# Функция для ответа на сообщения с клавиатурой
    authorize.method('messages.send', {'user_id' : sender, 'message' : message, 'random_id': get_random_id(), 'keyboard': keyboard.get_keyboard()})

def write_message_image_video_keyboard(sender, message, attachments, keyboard):
    authorize.method('messages.send', {'user_id': sender, 'message' : message, 'random_id': get_random_id(), 'attacnment': attachments, 'keyboard': keyboard})

def get_msg(user,name_user, msg):
    if msg == 'начать' or msg == 'привет' or msg == 'приветик' or msg == 'здравствуйте' or msg == 'старт' or msg == 'здравствуйте!' or msg == 'привет!':
        write_message_image_video(user,
                                  f'Привет, {name_user}&#128522;\n Я новый чат-бот центра образовательных инициатив СТЕМ&#10071; \n&#128521;',
                                  "photo-221332906_457239058")
        write_message_keyboard(user, 'Нажмите на кнопку ниже, чтобы выбрать действие&#10067;', keyboard_meneger)

    elif msg == 'связаться с менеджером' or msg == "да, хочу связаться с менеджером":
        write_message(user,
                      'Вы можете связаться с менеджером по номеру +79136280398\n\n Или Вы можете оставить свой номер телефона, чтобы наш менеджер связался с Вами.\nДля этого кликните по ссылке: https://forms.gle/iziTzCZfXGmrLrw4A')
        write_message(user, f'С Вами был чат-бот СТЕМ&#128526;\n До скорой встречи, {name_user}!')
        write_message_keyboard(user, 'Чтобы снова начать общение, нажмите "Начать"', keyboard_begin)

    elif msg == 'хотите что-то узнать':
        write_message_keyboard(user,
                               f'\n{name_user}, что бы Вы хотели узнать?',
                               keyboard_chapter)

    # ---------------курсы и направления----------------
    elif msg == 'направления и цены' or msg == 'вернуться к направлениям' or msg == 'вернуться к занятиям':
        write_message_keyboard(user,
                               'Ребята в возрасте от 6 до 18 лет могут начать обучение на одном или нескольких курсах с учетом начального уровня подготовки.\n\nПро какое направление Вы хотите узнать подробнее?',
                               keyboard_cource)

    elif msg == 'программирование':
        write_message_keyboard(user,
                               'Отличный выбор! Мы учим программировать на многих языках:)\nЧто Вас интересует?',
                               keyboard_cource_programming)

    elif msg == 'python':
        write_message_image_video(user,
                                  '&#128013; Программирование Python &#128013;\n\nPython - язык программирования общего назначения c автоматическим управлением памятью для повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.\n\n&#128204; Программирование для ребят от 12 до 17 лет. \n&#128204; Занятия 1 раз в неделю по 1.5 часа.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 3200 рублей.',
                                  'photo-113376999_457244872')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'java':
        write_message_image_video(user,
                                  '&#128421; Программирование Java &#128421;\n\nJava - язык программирования общего назначения. Приложения на языке Java разрабатываются под большинство современных систем, что делает язык универсальным для изучения. Программы, написанные на Java, состоят из «блоков», что сокращает время разработки, а также делает код более читаемым и удобным для модификации.\n\n&#128204; Программирование для ребят от 12 до 16 лет. \n&#128204; Занятия 1 раз в неделю по 1.5 часа.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 3200 рублей.',
                                  'photo-113376999_457244931')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'scratch':
        write_message_image_video(user,
                                  '&#11088; Программирование Scrath &#11088;\n\nScratch - это среда программирования, состоящая из блоков, созданная для детей и подростков, предоставляющая визуальный интерфейс для создания игр и анимаций. Одним из главных достоинств среды программирования Scratch является доступность и понятность абсолютно всем. Не требует навыков программирования, поэтому начать создавать собственные проекты можно практически с первого занятия.\n\n&#128204; Программирование для детей от 8 лет. \n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457245054')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'c#':
        write_message_image_video(user,
                                  '&#128194; Программирование C# &#128194;\n\nС# - один из самых распространённых языков программирования. Широко используется для разработки программного обеспечения. Область его применения включает создание операционных систем, разнообразных прикладных программ, драйверов устройств, приложений для встраиваемых систем, высокопроизводительных серверов, а также игр.\n\n&#128204; Программирование для ребят от 12 до 16 лет. \n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 3200 рублей.',
                                  'photo-113376999_457245014')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'construct 2':
        write_message_image_video(user,
                                  '&#127918; Программирование Construct 2 &#127918;\n\nЧто такое Construct? Это конструктор двумерных игр. Платформа обладает собственным физическим движком, что позволяет создавать более продвинутые игры. Чтобы работать в Construct не нужны специальные знания о языках программирования и даже какой-либо опыт в игростроении.\n\n&#128204; Программирование для ребят от 8 до 14 лет. \n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457243268')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'компьютерная грамотность':
        write_message_image_video(user,
                                  '&#128187; Компьютерная грамотность &#128187;\n\nВ рамках учебного направления ребята знакомятся с компьютером, изучают возможности ввода информации, программы Microsoft Office.\n\n&#128204; Компьютерная грамотность для ребят 7-14 лет.\n&#128204; Занятия 1 раз в неделю по 1.5 часа.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_435236535')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'web-разработка':
        write_message_image_video(user,
                                  '&#127760; WEB-разработка &#127760;\n\nWeb-разработка - процесс создания веб-сайта или веб-приложения.\n\n&#128204; Сайтостроение на HTML CSS для ребят от 12 до 17 лет.\n&#128204; Занятия 1 раз в неделю по 1.5 часа.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457244295')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'инженерные проекты':
        write_message_image_video(user,
                                  '&#9881; Инженерные проекты &#9881;\n\nПрактические занятия помогают не только лучше понять материал, но и попробовать сделать что-то своими руками! На занятиях у нас ребята учатся работать с датчиками движения, изучают основы физики и математики, а также учатся систематически мыслить.\n\n&#128204; Физика для ребят 8-12 лет.\n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457244988')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'робототехника':
        write_message_image_video(user,
                                  '&#129302; Робототехника &#129302;\n\n&#11088; Робототехника WeDo 2.0. Робототехника для учеников младших классов. \nLego Education WeDo – это интуитивно понятная образовательная робототехника, которая позволяет конструировать интерактивные модели из Lego. Собирать модели и приводить их в движение – что может быть увлекательнее для начинающих робототехников?\nРобототехника для детей от 6 до 10 лет.\n\n&#11088; Робототехника EV3\nLEGO Mindstorms — конструктор (набор сопрягаемых деталей и электронных блоков) для создания программируемого робота. В процессе конструирования ребята используют датчики звука, цвета, касания, и множество других сенсоров, которые позволяют программировать действительно уникального робота, выполняющего интересные задачи. Перевозка грузов от точки до точки, балансирование по линии, движение по цвету – и множество других возможностей на программирование робота!\nРобототехника для детей от 9 до 14 лет.\n\n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457244287')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'компьютерная графика':
        write_message_image_video(user,
                                  '&#128194; Компьютерная графика &#128194;\n\nРебята учатся работать с растровыми изображениями в среде Adobe Photoshop. Создают собственные графические иллюстрации, обрабатывают и улучшают фотографии, накладывают эффекты и учатся создавать собственные кисти для рисования.\n\n&#128204; Компьютерная графика для ребят 10-16 лет. \n&#128204; Занятия 1 раз в неделю.\n&#128204; Учебная группа формируется с учетом возраста, первоначального уровня. Соблюдается индивидуальный подход к каждому ребенку. Обычно коллектив составляет 5-10 человек.\n\n&#128176;Стоимость абонемента на месяц - 2800 рублей.',
                                  'photo-113376999_457244932')
        write_message_keyboard(user,
                               'Вы можете связаться с менеджером, чтобы задать дополнительные вопросы и записаться на первое занятие.',
                               keyboard_ater_cource)

    elif msg == 'вернуться назад' or msg == 'вернуться в основное меню' or msg == 'назад' or msg == 'да':
        write_message_keyboard(user, f'{name_user}, что бы Вы хотели узнать?', keyboard_chapter)

    # ------------Школа дронов----------
    elif msg == 'школа дронов аэростем':
        write_message_image_video(user,
                                  '&#128165;Обучение в школе дронов "Аэро СТЕМ" идёт полным ходом!\n\nМы продолжаем набор ребят 7-11 классов. \n&#9881;В рамках образовательных модулей ребята научатся:\n&#128204;управлять БПЛА\n&#128204;работать с платами и микросхемами\n&#128204;программировать на языке Python\n\n Участники приобретут новые знания и навыки программирования, пайки, сборки, настройки и управления БПЛА, которые пригодятся в будущем.\nПолученные компетенции позволят школьникам быть успешными как в it-сфере, так и в любой иной деятельности. \n\n&#128176;Стоимость обучения: БЕСПЛАТНО. \n Проект реализуется при поддержке Фонда президентских грантов.\n\n Регистрация по форме: https://forms.gle/yG51dMDTanxtcCAi6 \n\n Дополнительная информация по телефонам:\n8-913-628-03-98\n8-913-153-14-14',
                                  'photo-113376999_457245129')
        write_message_keyboard(user, 'Выберите один из вариантов', keyboard_ater)

    elif msg == 'подробнее о центре':
        write_message(user,
                      'Мы центр образовательных инициатив СТЕМ! Помогаем детям войти в мир информационных технологий 😉'
                      '\nНаш сайт: https://www.coistem.com/'
                      '\nМы находимся: '
                      '\n\n&#128204; г. Омск, ИТ-парк, Проспект Комарова, дом 21, корпус 1, офис 109'
                      '\nПосмотреть на карте: https://go.2gis.com/byyrm'
                      '\n\n&#128204; г. Омск, Академия искусств, Рабочая 14-я, 67а, 2 этаж'
                      '\nПосмотреть на карте: https://go.2gis.com/pb257')
        write_message_keyboard(user, 'Выберите один из вариантов', keyboard_ater)

    elif msg == 'больше нет вопросов' or msg == 'у меня больше нет вопросов':
        write_message(user,
                      f'Рад, что смог Вам помочь! \n\nБуду рад, если Вы оставите отзыв о моей работе&#128579;\nДля этого кликните по ссылке: https://forms.gle/jf13gMB99hYhFShz9')
        write_message_keyboard(user,
                               f'С Вами был чат-бот СТЕМ&#128526;\n До скорой встречи, {name_user}!\n\nЧтобы снова начать общение, нажмите "Начать"',
                               keyboard_begin)
    else:
        fail_msg = msg
        write_message_keyboard(user,
                               'Я вас не понимаю! :(\nПопробуйте ещё раз или мы можем отправить Ваше сообщение менеджеру, чтобы он связался с Вами',
                               keyboard_contact_meneger)


authorize = vk_api.VkApi(token = token)

for event in VkLongPoll(authorize).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
        user_name = get_name(user_id)
        get_msg(user_id,user_name,text)