from os import environ

API_ID = int(environ.get("API_ID", "27227762"))
API_HASH = environ.get("API_HASH", "cc9b763a5ebce6e1ed3414c3d805842d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8166897584:AAEV3orAMB2TRtPLzZH7pC-UBEzgPLpfTBI")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "2401269280"))
ADMINS = int(environ.get("ADMINS", "7456563475"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", ""))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
