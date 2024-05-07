import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def atik_kontrol(atik):
    geri_donusturulebilir_atiklar = ["kağıt", "karton", "metal", "cam", "plastik"]
    if atik.lower() in geri_donusturulebilir_atiklar:
        return "Bu atık geri dönüştürülebilir."
    else:
        return "Bu atık çöp kutusuna atılmalıdır."

# Discord bot komutları
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")

@bot.command()
async def bye(ctx):
    await ctx.send("Görüşürüz!")

@bot.command()
async def senkimsin(ctx):
    await ctx.send("Ben bir Discord botuyum. Kullanıcılara çeşitli komutlarla yardımcı olmak için buradayım.")

@bot.command()
async def kulturel_ozellik(ctx, sehir):
    if sehir in turkiye_sehirleri:
        await ctx.send(turkiye_sehirleri[sehir])
    else:
        await ctx.send("Üzgünüm, bu şehir hakkında bilgi bulunamadı.")

# Mesaj dinleme fonksiyonu
@bot.event
async def on_message(message):
    if not message.author.bot and "şaka" in message.content.lower():
        saka = random.choice(saka_havuzu)
        await message.channel.send(saka)
    
    await bot.process_commands(message)

# Çöp ayırma işlevselliği
@bot.command()
async def atik_kontrol(ctx, atik):
    geri_donusturulebilir_atiklar = ["kağıt", "karton", "metal", "cam", "plastik"]
    if atik.lower() in geri_donusturulebilir_atiklar:
        await ctx.send("Bu atık geri dönüştürülebilir.")
    else:
        await ctx.send("Bu atık çöp kutusuna atılmalıdır.")



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def geri_donusturulebilir(ctx, malzeme):
    geri_donusturulebilir_malzemeler = ["kağıt", "karton", "metal", "cam", "plastik"]
    if malzeme.lower() in geri_donusturulebilir_malzemeler:
        await ctx.send(f"{malzeme} geri dönüştürülebilir bir malzemedir.")
    else:
        await ctx.send(f"{malzeme} maalesef geri dönüştürülebilir bir malzeme değildir.")

@bot.command()
async def geri_donusum_tips(ctx):
    tips = [
        "Plastik şişeleri kullanmadan önce tekrar doldurun.",
        "Alüminyum ve teneke kutuları geri dönüştürün.",
        "Kağıt ürünleri için geri dönüşüm kutuları kullanın.",
        "Cam şişeleri ve kavanozları temizleyip geri dönüştürün.",
        "Atık pilleri geri dönüşüm kutularına atın.",
        "Eski giysilerinizi geri dönüştürün veya bağışlayın."
    ]
    await ctx.send(random.choice(tips))

@bot.command()
async def geri_donusum_nedir(ctx):
    explanations = [
        "Geri dönüşüm, kullanılmış malzemelerin toplanıp işlenerek yeni ürünlerin üretilmesi sürecidir. Bu süreç, doğal kaynakların korunmasına, enerji tasarrufuna ve atık miktarının azaltılmasına yardımcı olur.",
        "Geri dönüşüm, atıkların işlenerek tekrar kullanılabilir hale getirilmesi işlemidir. Bu sayede kaynaklar daha verimli kullanılır ve çevreye daha az zarar verilir."
    ]
    await ctx.send(random.choice(explanations))


bot.run("")
