from os import getenv

API_ID = getenv("API_ID","14050586")
API_HASH = getenv("API_HASH","42a60d9c657b106370c79bb0a8ac560c")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_COMMANDS = (
    ("start", "侖 sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ 侖"),
    ("settings", "侖 ᴏᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢ 侖"),
    ("help", "侖 ɢᴇᴛ ʙᴏᴛ ʜᴇʟᴘ 侖"),
    ("about", "侖 ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ 侖"),
)

DATABASE_URL = getenv("DATABASE_URL", None)
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "80"))
