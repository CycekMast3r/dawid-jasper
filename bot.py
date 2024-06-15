import discord 
from discord.ext import commands
import os
import random
import json
import importlib
from discord import FFmpegPCMAudio
import counter
import openai
import yt_dlp
import asyncio


intents = discord.Intents.default()
intents.message_content = True
openai.api_key = os.getenv("CHATGPT_API")

bot = commands.Bot(command_prefix='&', intents=intents)
miska_counter = counter.miska_counter
images_folder = 'photo'
images = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if file.endswith(('jpg', 'png', 'jpeg', 'gif'))]


quotes = [
    "Tata jest cola???",
    "Osoby zostały wyciszone na 600 minut to minuta- 600 minut to jest minuta",
    "To jest twoje zdanie kolego, moje zdanie jest dokładnie inne",
    "Takie masz zdanie o mnie, takie masz zdanie o mnie",
    "Z Art.2-, artykuł dwu-, Art.25 konstytucji mówi POWTARZAM Art.25 konstytucji mówi: Że wszyscy jesteśmy równi i możemy się wypowiadać się na temat innych osób",
    "Mamy skręt w lewo albo prosto... KURWAAA AJAJAJAJ",
    "O O O O O O O O O O O O O O O O O O O O O O O O O O O O ",
    "TATA, chodź no co tu pisze",
    "Ja nie mam mamy dlatego, że  mamma umarła mi na raka w 2006 roku w stanie krytycznym a wy cały czas pierdolicie, że trzymam mamę w boilerze",
    "A Pan mówi, że nie mam jedynek",
    "O NIEEEE TO JEST KOTOMILER WAMPIR AAAAAA USZY MA JAK NIETOPERZ KOTOMILER WAMPIR",
    "Ale bym pierdolnął tego kotomilera",
    "DAWAJ TO MIĘSKO O O O O O O O",
    "MAM PIĄTY TELEFON W CIĄGU 5 MINUT",
    "8:41 i  05 setnych- katastrofa Smoleński, samolot Boeing rozbił się... O Boże tragedia, masakra",
    "JEEEEEEST KURWA JEEEST 1:0 UTRZYMAJMY TĄ PRZEWAGĘ UTRZYMAJMY TĄ PRZEWAGĘ",
    "Patrzcie widzowie jaka pizza, jaka pizza duża taką będą jadł zaraz z Francji",
    "GAGRI GAGRI GAGRI",
    "To se weź"
]

pickup_lines = [
    "Witam Cię koleżanko jesteś bardzo piękna i ładna, powiedz mi  z jakiej jesteś miejscowości i ile masz lat",
    "Jesteś bardzo piękna koleżanko, zakochałem się w Tobie POWTARZAM KOLEŻANKO zakochałem się w Tobie. Słyszysz? Zakochałem się w Tobie koleżanko",
]

sounds = [
    "1- pokemon",
    "2- how old are you",
    "3- łokieta",
    "4- mój tata",
    "5- niger",
    "6- podryw",
    "7- staruszki",
    "8- tureckie kozy",
    "9 - czarny medyk",
    "10- wylizałbym",
    "11- bomba",
    "12- pozdro",
    "13- kiedysPokemon",
    "14- caluski",
    "15- co cześć kurwo",
    "16- oddział specjalny",
    "17- tata jest cola",
    "18- spokocepcja",
    "19- donejt",
    "20- myszard",
    "21- najlepszegoKasia",
    "22- nie sraj",
    "23- hymn ZSRR",
    "24- heteroseksualny",
    "25- pingwinki",
    "26- zesrał sie",
    "27- xxx",
    "28- uhuhu",
    "29 - Uaga",
    "30- zmontowane",
    "31- boobsy",
    "32- kotomiller",
    "33- shrek",
    "34- RTV RGD",
    "35- ban",
    "36- legia",
    "37- gej",
    "38- Giw mi siekierka",
    "39- jedynki",
    "40- drugi czarny",
    "41- dziub",
    "42- co niedziela",
    "43- ruchal",
    "44- batman",
    "45- Ale miała melony",
    "46 - Ale mają przekurwione jak wejdą na ten serwer",
    "47 - Ale do 23 mam czas",
    "48- Adolf Jasper"
]
images = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    '8.jpg',
    '9.jpg',
    '10.jpg',
    '11.jpg',
    '12.jpg',
    '13.jpg',
    'g1.gif',
    'g2.gif',
    'g3.gif',
    'g4.gif',
    'g5.gif',
    'g6.gif'
]


@bot.event
async def on_ready():
    print('Witam was widzowie z tej strony {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global miska_counter

    if message.author == bot.user:
        return
    
    if message.content.startswith('&dzwieki'):
        await message.channel.send(sounds)

    if message.content.startswith('&cytat'):
        num = random.randint(0, len(quotes)-1)
        await message.channel.send(quotes[num])

    if message.content.startswith('&podryw'):
        num = random.randint(0, len(pickup_lines)-1)
        await message.channel.send(pickup_lines[num])
    
    if message.content.startswith('&cienias'):
        await message.channel.send("Cieniecki to gej widzowie pamiętajcie zostawcie mu łapki w dół powtarzam zostawcie mu łapki w dół")
    
    if message.content.startswith('&hamrokar'):
        await message.channel.send("Dykta ciapa")
    
    if message.content.startswith('&miska'):
        miska_counter += 1
        
        file = open('counter.py', 'w') 
        file.write(f"miska_counter = {miska_counter}")
        file.close()

        if miska_counter == 1:
            await message.channel.send("Miśka była bita: " + str(miska_counter) + " raz")
        else:
            await message.channel.send("Miśka była bita: " + str(miska_counter) + " razy")

        if miska_counter % 10 == 0:
            if message.author.voice:
                channel = message.author.voice.channel
                voice = await channel.connect()
                await message.channel.send(f"Wchodzę na kanał głosowy, bo Miśka była bita {miska_counter} razy! POWTARZAM JA NIE BIJE MOJEGO PSA MIŚKA!")
                source = FFmpegPCMAudio("miska.mp3")
                voice.play(source)

                
                while voice.is_playing():
                    await asyncio.sleep(1)
                await voice.disconnect()
            else:
                await message.channel.send("Kolego musisz być na kanale discord POWTARZAM musisz być na kanale discord spoko ok????")
            
    await bot.process_commands(message)

@bot.command(pass_context = True)
async def rymowanka(msg, user: str = None):
    if user is None:
        user = "Ryszard Wójcik"
    
    rhymes = [
        f"Co niedziela, co niedziela {user} kawał cwela, pije wódkę co niedziela, co niedziela, co niedziela",
        f"Siekiera, motyka, bomba, boiler {user} to transformers. Siekiera, motyka bum cyk cyk uuuuu {user} stary gej"
    ]
    rhyme = random.choice(rhymes)

    await msg.channel.send(rhyme)

@bot.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        await ctx.send("Witam was widzowie na moim strimie")
        sound_choice = random.choice(sounds)
        source = FFmpegPCMAudio("audio/" + sounds[sound_choice] + ".mp3")
        player = voice.play(source)
    else:
        await ctx.send("Kolego musisz być na kanale discord POWTARZAM musisz być na kanale discord spoko ok????")


@bot.command(pass_context = True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ja spadam widzowie, dzięki za liw")
    else:
        await ctx.send("Widzowie nie ma mnie na kanale discord, Ryszard wyłączył mi ruter")

@bot.command(pass_context = True)
async def powiedz(ctx, num: int = None):
    if ctx.voice_client is None:
        await ctx.send("Kolego najpierw kolego muszę dołączyć, POWTARZAM spoko ok?")
        return
    
    if num is None:
        sound_choice = random.choice(sounds)
    else:
        if 1 <= num <= len(sounds):
            sound_choice = sounds[num - 1]
        else:
            await ctx.send(f"Podaj numer od 1 do {len(sounds)}.")
            return
    
    source = FFmpegPCMAudio(f"audio/{sound_choice}.mp3")
    ctx.voice_client.play(source)

@bot.command(pass_context = True)
async def  pause(ctx):
    voice = ctx.voice_client

    if voice.is_playing():
        voice.pause()

@bot.command(pass_context = True)
async def  resume(ctx):
    voice = ctx.voice_client

    if voice.is_paused():
        voice.resume()

@bot.command(pass_context = True)
async def  stop(ctx):
    voice = ctx.voice_client
    
    if voice.is_playing():
        voice.stop()

@bot.command()
async def zdjecie(ctx):
    if not images:
        await ctx.send("Brak kolego jaspera :(")
        return

    image_path = random.choice(images)
    with open(image_path, 'rb') as file:
        await ctx.send(file=discord.File(file, os.path.basename(image_path)))

@bot.command()
async def radio(ctx):
    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)
    ffmpeg_options = {"options": "-vn"}

    try:
        voice_client = await ctx.author.voice.channel.connect()
    except discord.ClientException:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    playlist_url = "https://www.youtube.com/watch?v=ClxLD8fOcHc&list=PLLSYiXjAh1g2SNyJh0XoCR4HwP5djcqSX"
    loop = asyncio.get_event_loop()

    def get_playlist_songs(url):
        info = ytdl.extract_info(url, download=False)
        return info['entries']

    songs = await loop.run_in_executor(None, lambda: get_playlist_songs(playlist_url))

    for song in songs:
        url = song['url']
        title = song['title']
        await ctx.send(f'Teraz wdziowie na bicie: {title}')
        voice_client.play(FFmpegPCMAudio(url, **ffmpeg_options))

        while voice_client.is_playing():
            await asyncio.sleep(1)

    await voice_client.disconnect() 



token = os.getenv("TOKEN")

if token is None:
    raise ValueError("Token Discorda nie jest ustawiony w zmiennych środowiskowych.")

bot.run(token)
