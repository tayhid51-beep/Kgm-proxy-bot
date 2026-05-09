import logging
from aiogram import Bot, Dispatcher, types, executor

# আপনার দেওয়া তথ্য এখানে সেট করা হয়েছে
API_TOKEN = '8625101863:AAHsUs24lSAhGzedhQgTH21MjMU4OlhkOo8' 
ADMIN_ID = 8696673002

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⚙️ My Account", "💰 Check Balance")
    markup.add("💎 Buy IP", "💳 Deposit Money")
    markup.add("📡 My IP", "📞 Support")
    markup.add("👥 Referral", "📊 Check Data")
    markup.add("🇻🇳 Language")
    await message.reply("✅ Welcome!\n\nনিচের Menu থেকে অপশন সিলেক্ট করুন ⚡", reply_markup=markup)

@dp.message_handler(lambda message: message.text == "💎 Buy IP")
async def buy_ip(message: types.Message):
    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_kb.add(
        types.InlineKeyboardButton("9Proxy (Nice Proxy)", callback_data='9p'),
        types.InlineKeyboardButton("ABC Proxy", callback_data='abc'),
        types.InlineKeyboardButton("ProxySeller", callback_data='ps'),
        types.InlineKeyboardButton("9 Proxy CD Key", callback_data='9cd'),
        types.InlineKeyboardButton("NodeMaven (Recommended)", callback_data='node'),
        types.InlineKeyboardButton("DataImpulse Proxy", callback_data='data')
    )
    await message.reply("🛡 Select a Proxy Provider:", reply_markup=inline_kb)

@dp.message_handler(commands=['admin'], user_id=ADMIN_ID)
async def admin_panel(message: types.Message):
    await message.reply("👑 Hello Admin! আপনি এখান থেকে বট ম্যানেজ করতে পারবেন।")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
