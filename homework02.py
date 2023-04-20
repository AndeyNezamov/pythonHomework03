def Fruits():
    fruit =['Абрикос', 'Авара', 'Авокадо', 'Азимина', 'Айва', 'Акебия', 'Аки', 'Алыча', 'Ананас', 'Апельсин', 'Араза', 'Арбуз', 'Архат', 'Асаи',
             'Бабако', 'Баиль', 'Бакупари', 'Банан', 'Барбарис', 'Билимби', 'Боярышник', 'Боярышник мексиканский', 'Бромелия пингвин', 'Брусника', 'Бунхозия серебристая', 'Бузина черная',
             'Вампи', 'Вишня', 'Вишня войлочная', 'Виноград', 'Виноград Кишмиш', 'Воаванга', 'Восковница красная',
             'Гандария', 'Гарциния индийская', 'Гарциния Ливингстона', 'Гарциния Прейна', 'Генипа американская', 'Гетеромелес', 'Гилоцереус коста-риканский', 'Гилоцереус крупноцветковый', 'Годжи (ягоды)', 'Голубика' , 'Голубиная слива', 'Гранадилла', 'Гранат', 'Гревия азиатская', 'Грейпфрут', 'Грумичама', 'Груша', 'Гуава', 'Гуава земляничная', 'Гуайява', 'Гуанабана (Сметанное яблоко)', 'Гуарана',
             'Давидсония', 'Дакриодес съедобный', 'Дереза китайская (ягода)', 'Джаботикаба', 'Джамбоза', 'Джамболан', 'Джамбу', 'Джекфрут', 'Довиалис кафрский', 'Дуриан', 'Дынная груша', 'Дыня',
             'Ежевика',
             'Жаботикаба', 'Жердела', 'Жимолость',
             'Звёздчатое яблоко', 'Земляника', 'Земляничное дерево красное', 'Земляничное дерево крупноплодное', 'Земляничное дерево Менциса', 'Земклуника', 'Зизифус (Унаби)',
             'Икако', 'Илама', 'Имбу', 'Инга съедобная', 'Инжир', 'Инжирный персик', 'Ирга', 'Ирга азиатская', 'Ирга канадская', 'Ирга круглолистная', 'Испанский лайм',
             'Каимито (каинито)', 'Каламондин (Цитрофортунелла)', 'Калина', 'Каму-каму', 'Канистель', 'Канталупа (растение)', 'Капулин', 'Карамбола', 'Кариокар бразильский', 'Карисса', 'Карисса каранда', 'Карисса крупноцветковая', 'Кассаба', 'Кафир-лайм', 'Квини', 'Кепель', 'Кешью', 'Кивано', 'Киви', 'Кизил обыкновенный', 'Китайская клубника (восковница красная)', 'Клементин', 'Клюква', 'Клубника', 'Княженика', 'Кокколоба ягодоносная', 'Кокона', 'Кокос', 'Конфетное дерево', 'Корлан', 'Костяника', 'Красника', 'Криптокария белая', 'Крыжовник', 'Ксимения американская', 'Кудрания триостренная', 'Кумкват', 'Купуасу',
             'Лайм', 'Лангсат', ' Лардизабала', ' Лимон', ' Лимонник', ' Китайский Личи', ' Логановая ягода', ' Лонган', ' Лукума', ' Лума остроконечная', 
             'Маболо', 'Магический фрукт', 'Малайское яблоко', 'Малина', 'Малина майсорская', 'Малина пурпурноплодная', 'Малина черная', 'Манго', 'Манго индийское', 'Манго пахучее', 'Мангостин', 'Мандарин', 'Мандарин уншиу', 'Маракуйя', 'Маранг', 'Мараскиновая вишня', 'Марула (Склерокария эфиопская)', 'Минеола', 'Мирциария сомнительная', 'Можжевельник', 'Момбин жёлтый', 'Момбин пурпурный', 'Момордика кохинхинская', 'Мора', 'Морошка', 'Мунтингия', 'Мушмула', 'Мушмула германская', 'Мушмула японская'
             'Нансе', 'Наранхилья', 'Нектарин', 'Нойна', 'Нони', 
             'Облепиха', 'Оливки', 'Опунция',
             'Пальма тукум', 'Пальмировая пальма', 'Пальчиковый лайм', 'Пандан полезный', 'Панданус (кьюра)', 'Папайя', 'Папеда ежеиглистая', 'Пассифлора нежнейшая', 'Пепино', 'Переския шиповатая', 'Персик', 'Питахайя', 'Питецеллобиум сладкий', 'Питомба', 'Платония', 'Плумкот', 'Помело', 'Померанец', 'Пулазан', 'Пурума цекропиелистная',
             'Рамбутан', 'Рангпур', 'Родомирт войлочный', 'Роллиния слизистая', 'Рука Будды', 'Рябина красная',
             'Салак (змеиный фрукт)', 'Саламандровое дерево', 'Санберри (самбери)', 'Сантол', 'Саподилла', 'Сапота', 'Сахарное яблоко', 'Свити', 'Сереноа', 'Сизигиум масляный', 'Сизигиум метельчатый', 'Сизигиум сердцевидный', 'Сизигиум южный', 'Сикана душистая', 'Слоновое яблоко', 'Слива', 'Сметанное яблоко', 'Смородина белая', 'Смородина красная', 'Смородина черная', 'Страстоцвет лавролистный', 'Страстоцвет съедобный', 'Страстоцвет четырёхгранный', 'Страстоцвет язычковый', 'Стрихнос колючий', 'Суринамская вишня',
             'Тамарилло', 'Тамаринд', 'Танжело', 'Танжерин', 'Терн', 'Терминалия Фердинанда', 'Толокнянка обыкновенная (медвежье ушко)',
             'Угни (Уньи)', 
             'Фалса', 'Фейхоа', 'Ферония (Деревянное яблоко)', 'Физалис', 'Физалис перуанский', 'Фикус', 'Фикус кистевидный', 'Фикус священный', 'Филлантус кислый', 'Финик', 'Финик королевский', 'Финики Мазафати',
             'Хурма', 'Хурма виргинская', 'Хурма королек',
             'Цабр', 'Цитрон', 
             'Черёмуха виргинская', 'Чемпедак', 'Черимойя', 'Черешня', 'Черноплодная рябина', 'Черника', 'Чилибуха (Рвотный орех)', 'Чупа-чупа', 
             'Шелковица', 'Шефердия серебристая', 'Шиповник', 
             'Юдзу',
             'Яблоко', 'Яблоки Антоновка', 'Яблоки Айдаред', 'Яблоки Богатырь', 'Яблоки Белый налив', 'Яблоки Гала', 'Яблоки Голден', 'Яблоки Гренни Смит', 'Яблоня Грушовка Московская', 'Яблоня Коричное полосатое', 'Яблоня Мельба', 'Яблоки Фуджи', 'Яблоко Семеренко', 'Яблоня Слава Победителям', 'Яблоки Штрифель', 'Ягода лох', 'Японский лимон (Юзу)']
    firstLetter = input('Введите первую букву: ').upper()[0]
    for i in fruit:
        if i[0] == firstLetter:
            print(i , end=" * ")
Fruits()