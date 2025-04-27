import os
from pyrogram import Client
from aiohttp import web
from config import API_ID, API_HASH, BOT_TOKEN

# Define routes for aiohttp web server
r = web.RouteTableDef()

@r.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(text='<h3 align="center"><b>I am Alive</b></h3>', content_type='text/html')

async def wsrvr():
    wa = web.Application(client_max_size=30000000)
    wa.add_routes(r)
    return wa

class Bot(Client):
    def __init__(self):
        super().__init__(
            "auto_approve_bot",
            api_id=27227762,
            api_hash=cc9b763a5ebce6e1ed3414c3d805842d,
            bot_token=8166897584:AAEV3orAMB2TRtPLzZH7pC-UBEzgPLpfTBI,
            plugins=dict(root="plugins"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        # Start aiohttp web server
        app = web.AppRunner(await wsrvr())
        await app.setup()
        ba = "0.0.0.0"
        port = int(os.environ.get("PORT", 8080)) or 8080
        await web.TCPSite(app, ba, port).start()
        
        # Start Pyrogram client
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username

        print('Bot Started Powered By @Son_Goku_8')

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')
    
# Run the bot
Bot().run()
