import logging

from jiosaavn.bot import Bot

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

@Bot.on_callback_query(filters.regex('^home$'))
@Bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def start_handler(client: Bot, message: Message | CallbackQuery):
    ##### Mention user
    last_name = f' {message.from_user.last_name}' if message.from_user.last_name else ''
    mention = f"[{message.from_user.first_name}{last_name}](tg://user?id={message.from_user.id})"
    text = (
        f"**⛩️ Hello {mention},**\n\n"
        "<blockquote>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʀɪsʜᴜ ᴍᴜsɪᴄ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ! ᴛʜɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇᴀʀᴄʜ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs, ᴘʟᴀʏʟɪsᴛs, ᴀʟʙᴜᴍs, ᴀɴᴅ ᴀʀᴛɪsᴛs ᴅɪʀᴇᴄᴛʟʏ .</blockquote>\n\n"
        "**❍ ━━━━━━━⸙ Feature ⸙━━━━━━ ❍**\n"
        "**┣⪼𖨠 sᴇᴀʀᴄʜ ғᴏʀ sᴏɴɢs, ᴀʟʙᴜᴍs, \n┃ ᴘʟᴀʏʟɪsᴛs**\n"
        "**┣⪼𖨠 ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ \n┃ ᴛʀᴀᴄᴋs ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ**\n"
        "**┣⪼𖨠 ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ**\n**❍ ━━━━━━━━⸙ ♡ ⸙━━━━━━━━ ❍**\n\n"
        "** ⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆ :** [ ꯭꯭↬꯭ᬃ꯭ ⃪꯭ ꯭⁢⁣⁤⁣⁣⁢⁣⁤⁢⁤⁣⁢⁤⁣⁤᪳᪳🇷꯭𝚰𝛅꯭꯭ʜ꯭֟፝፝֟ᴜ ꯭꯭༗꯭»꯭݅݅݅݅𓆪 ](https://t.me/ur_rishu_143)"
    )

    buttons = [[
        InlineKeyboardButton('˹ ❍ᴡɴᴇꝛ ˼', url='https://t.me/Rishu1286'),
        InlineKeyboardButton('˹ ᴧʙᴏᴜᴛ ˼', callback_data='about')
    ], [
        InlineKeyboardButton('˹ ʜᴇʟᴘ ˼', callback_data='help'),
        InlineKeyboardButton('˹ ᴍᴏᴅᴇ ˼ ', callback_data='settings')
        ]
]
    
    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True, disable_web_page_preview=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

@Bot.on_callback_query(filters.regex('^help$'))
@Bot.on_message(filters.command('help') & filters.private & filters.incoming)
async def help_handler(client: Bot, message: Message | CallbackQuery):
    text = (
        "<blockquote>⌬ IT'Տ ᐯᗴᖇY ՏIᗰᑭᒪᗴ TO ᑌՏᗴ ᗰᗴ! 😉</blockquote>\n\n"
        "**⌬ sᴛᴀʀᴛ ʙʏ ᴄᴏɴғɪɢᴜʀɪɴɢ ʏᴏᴜʀ ᴘʀᴇғᴇʀᴇɴᴄᴇs ᴜsɪɴɢ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ. **\n"
        "**⌬ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀ sᴏɴɢ, ᴘʟᴀʏʟɪsᴛ, ᴀʟʙᴜᴍ, ᴏʀ ᴀʀᴛɪsᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ .**\n"
        "**⌬ ɪ'ʟʟ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇsᴛ ᴀɴᴅ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴛʜᴇ ʀᴇsᴜʟᴛs!**\n\n"
        "<blockquote>⌬ ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀɴᴅ ᴇɴɪᴏʏ ᴛʜᴇ ᴍᴜsɪᴄ !</blockquote>"
    )

    buttons = [[
        InlineKeyboardButton('˹ ʜᴏᴍᴇ ˼ ', callback_data='home'),
        InlineKeyboardButton('˹ ᴄʟᴏsᴇ ˼', callback_data='close')
    ]]

    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex('^about$'))
@Bot.on_message(filters.command('about') & filters.private & filters.incoming)
async def about(client: Bot, message: Message|CallbackQuery):
    me = await client.get_me()

    text = (
        f"**🤖 Bot Name:** {me.mention()}\n\n"
        "**📝 Language:** [Python 3](https://www.python.org/)\n\n"
        "**🧰 Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n\n"
        "**👨‍💻 Developer:** [Rishu](https://t.me/rishu1286)\n\n"
        "**📢 Updates Channel:** [Rishu bots ](https://t.me/ur_rishu_143)\n\n"
        
    )

    buttons = [[
        
        InlineKeyboardButton('˹ ʜᴏᴍᴇ ˼', callback_data='home'),
        InlineKeyboardButton('˹ ᴄʟᴏsᴇ ˼', callback_data='close')
    ]]
    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

@Bot.on_callback_query(filters.regex('^close$'))
async def close_cb(client: Bot, callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
