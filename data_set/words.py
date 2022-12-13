TRIGGERS = {'микола', 'оля', 'поля', 'валя', 'хоча', 'ольга', 'коля', 'миколай', 'скажи', 'будь ласка', 'підскажи',
            'включи', 'слава', 'ще', 'зроби', 'розкажи'}

ON_WORDS = ['включи', 'включає', '', '', '']
OFF_WORDS = ['вимкни', 'виключи', 'вимкнули']

data_set = {

    'увімкне увімкну увімкнув увімкне включи включу включає світло': 'send_to_arduino на',
    'вимкни вимкнули вимкнув вимкну світло': 'send_to_arduino на',

    'яка погода на вулиці': 'weather зараз подивлюся',
    'яка погода': 'weather зараз скажу',
    'що там на вулиці': 'weather можеш сам подивитися, но зараз скажу',
    'скільки градусів': 'weather боїшся замерзнути?',


    'ютуб': 'browser_y що вже йдеш дивитися?',



    'бібліотеку ігор': 'open_s хвилинку',


    'голосніше': 'volume_p  ок',
    'тихо': 'volume_mute   добре',
    'тихіше': 'volume_m   ага',


    'йди спи': 'offBot солодких снів',
    'до побачення': 'offBot сподіваюсь ще вернешся',
    'солодких снів': 'offBot так рано?',


    # 'хто такий вадим': 'passive вадим тупа скотина алкоголік лицтий',
    'прикол': 'passive ти пив ти сам пив ти шо алкоголік ти тупа скотина',
    'будь здоров': 'passive пий на здорвлі',
    # 'міша прийшов з пивом': 'passive фу алкоголіки',
    'прийшов міша': 'passive знову цей безхатько прийшов пити пиво',
    'як справи': 'passive було краще доки не запитав',
    'що робиш': 'passive роблю твоє життя кращим',
    'здоров': 'passive здоровіших бачив',
    'україні': 'passive героям слава!',
    'нації': 'passive смерть ворогам',
    'україна': 'passive поняд усе',
    'де рускій воєнний корабель': 'passive пішов нахуй',
    'рускій воєнний корабель': 'passive иди нахуй',
    'приїхав олег іванович': 'passive та ви замахали, знову до понеділка запой',

    # 'запиши напиши пиши перше запише': 'writers',
    'знайди': 'open_tabs зачекай',

    'включив включає включи пісню': 'play_music добре',

    'рекоменд порекомендуй порекомендує фільм': 'recommended_film шукаю',

    'покаже карту': 'open_map_alarm ок',

    'хочу купити': 'buy шукаю найнижчі ціни'
}
