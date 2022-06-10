from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="🇺🇿 O'zbekcha",callback_data='uzb'),
	
	 InlineKeyboardButton(text='🇬🇧 English',callback_data='eng')

	],
],
	)
bir = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="📒Loyiha haqida",callback_data='loyiha'),
	
	 InlineKeyboardButton(text="Ro'yxatdan o'tish",callback_data='ruyhat')

	],

    [InlineKeyboardButton(text="Savollar yo'llash",callback_data='savol')

    ],
    ],
	)

bosh = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Loyiha maqsadi",callback_data='loyiha2'),
	
	 InlineKeyboardButton(text="Loyiha vazifasi",callback_data='loyiha3')

	],

    [InlineKeyboardButton(text="O'tkazilish tartibi",callback_data='loyiha4'),
    InlineKeyboardButton(text="Talablar",callback_data='loyiha5')

    ],
    [InlineKeyboardButton(text="Orqaga",callback_data='back1')
    ],
    ],
	)


orqa =  InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Orqaga",callback_data='back2')
	

	],
],
	)
orqa1 =InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Orqaga",callback_data='back3')
	

	],
],
	)



one = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="📒About the project",callback_data='project'),
	
	 InlineKeyboardButton(text="Regestration",callback_data='register')

	],

    [InlineKeyboardButton(text="Send questions",callback_data='question')

    ],
    ],
	)

main = InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Aim of the project",callback_data='project1'),
	
	 InlineKeyboardButton(text="Project task",callback_data='project2')

	],

    [InlineKeyboardButton(text="The order of process",callback_data='project3'),
    InlineKeyboardButton(text="Requirements",callback_data='project4')

    ],
    [InlineKeyboardButton(text="Back",callback_data='orqa3')
    ],

    ],
)


old1=  InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Back",callback_data='orqa1')
	

	],
],
	)
old2 =InlineKeyboardMarkup(

	inline_keyboard=[

	[
	 InlineKeyboardButton(text="Back",callback_data='orqa2')
	],
],
	)
