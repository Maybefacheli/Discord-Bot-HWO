import os
import random
import praw
import nextcord
import math
import asyncio
import datetime
import string
import requests

from nextcord.ext import commands 
from dotenv import load_dotenv
from datetime import datetime, date, time, timezone

load_dotenv()
TOKEN = os.getenv('nextcord_TOKEN')
owners = [796400317334945813 , 557333679203024963]
bot = commands.Bot(command_prefix= ['!', "HWO "]  ,help_command=None, case_insensitive=True, owner_ids = set(owners))

# reddit = praw.Reddit(client_id='vTFZ6w_iCbnY5w',
#  client_secret='	YrsWHUthpUf8IFGM3wRc736-fTG0TQ',
#  user_agent='u/bumblebeehour469')

characters = "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z" "1" "2" "3" "4" "5" "6" "7" "8" "9" "0"
true=True
false=False

#def hocus():
	

   
@bot.event 
async def on_ready():
	await bot.change_presence(activity=nextcord.Game('!help'))
	print('------')
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print('Servers connected to:')
	for guild in bot.guilds:
		print(guild.name)
	print('-------------------------------------')
	print("BE PREPARED TO NOT GET ANYTHING DONE")

@bot.event 
async def on_command_error(ctx, error): 
		if isinstance(error, commands.CommandNotFound): 
				msg=ctx
				em = nextcord.Embed(title=f"Error!!!", description=f"Command not found.", color=ctx.author.color) 
				await ctx.send(embed=em)
				await msg.add_reaction(':pirate_flag:')
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome this nextcord server!')

@bot.command("help")
async def help(ctx):
  
	embed = nextcord.Embed(
    color = nextcord.Color.gold(),
    url="https://bit.ly/3AIdW82",
    description="These are the comands this bot can do. All of these commands require the prefix ! or HWO (What you say before the command). Please remember that it is a work in progress. Have fun!\U0001F607 \U0001F609. If you find any issues or have any suggestions, please DM me MaybeFacheli#3932")
		#\U0001F607 is angel emoji \U0001F609 is winking emoji
	embed.set_author(name= ctx.author.display_name)
  
	embed.add_field(name = "------------Simulations Section------------", value="Commnds that have to do with simulating something", inline=False)
	embed.add_field(name="rolldice",value =  'Simulates rolling dice', inline=True)
	embed.add_field(name="passwordgenerator",value='Generate yourself a password between 3-40 characters', inline=True)
  #embed.add_field(name="lottery", value = 'Play the lottery within a certain role', inline=True)
	embed.add_field(name='8ball', value='Ask the 8ball a question', inline=True)
	embed.add_field(name='coinflip', value='Flip a coin', inline=True)
	embed.add_field(name='ask',value='HWO will ask you a question. It\'ll be hard.',inline=True)
  

	embed.add_field(name="----------------🤓Math Section🤓----------------", value="Commands needed for math", inline=False)
	embed.add_field(name="add",value='Add two numbers together', inline=True)
	embed.add_field(name="subract",value='Subtract two numbers', inline=True)
	embed.add_field(name="multiply",value='Multiply two numbers', inline=True)
	embed.add_field(name="divide",value='divide two numbers', inline=True)
  
	embed.add_field(name="------------- Fun Section --------------", value = "Commands that have to do with fun and games", inline = False)
	embed.add_field(name="howcool",value =  'How cool is someone? (Totally not rigged) ', inline=False) 
	embed.add_field(name="hAx", value='hax...', inline=True)
	embed.add_field(name="quote", value='Quote what you just said', inline=True)
	embed.add_field(name= 'rps(rockpaperscissors)',value = "Play rock paper scissors with the bot",inline = True)
	embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
	embed.add_field(name='poke',value = 'poke someones dms by @ing them after the command name.',inline=True)

	embed.add_field(name='------------- technicalities --------------', value='commands for people better than you', inline=False)
	embed.add_field(name='role magic', value='make a new role with a name of your choosing.', inline=True)
	embed.add_field(name='report', value = 'report someone to the mods of a server', inline=True)
	embed.add_field(name='servers', value='lists bots servers', inline=True)



	await ctx.send( embed=embed)
 
@bot.command(name = "up")
async def upembed(ctx):
    embed=nextcord.Embed(title="The Bot Is Up!", url="https://bit.ly/3AIdW82", description=(f'{bot.user.name} is connected to nextcord!'), color=nextcord.Color.blue())
    print(f'{bot.user.name} has connected to nextcord!')
   
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar)
    
    await ctx.send(embed=embed)

@bot.command()
async def servers(ctx):
	for guild in bot.guilds:
		await ctx.send(f'{guild.name}')

@bot.command()
async def ask(ctx):

        _list = [
        'Are the Fachelis the best?', 
        'Are the Fachelis the Best?']

        list1 = random.choice(_list)

        def answer():
            answer = "-1"
            if _list[0] == list1:
                answer = "yes"
            else: 
                answer = "yes"
            return answer

        await ctx.send("What is the answer to this question?")
        await asyncio.sleep(1)
        await ctx.send(list1)
        def check(m): return m.author == ctx.author and m.channel == ctx.channel

        msg = await bot.wait_for('message', check=check, timeout=None)

        if msg.content == answer():
            await ctx.send("good")
        else:
            await ctx.send("ur wrong, u suck") 



@bot.command(name = "role_magic")
@commands.has_permissions(manage_roles=True) #Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
	print(f'the role {name} has been created by {ctx.author}')


@bot.command()
async def poke(ctx, pokeduser: nextcord.Member=None):
	if pokeduser is None:		
			await ctx.send("Incorrect Syntax:\nUsage: `!poke [user]`")
	date_time = (datetime.datetime.now())
	await pokeduser.send("*poke*")
	await asyncio.sleep(2)
	await pokeduser.send(f'you\'ve been poked by {ctx.author}. They used my poke command, try it out by typing !poke @person')
	await ctx.send('poked!')
	
	print(f'{ctx.author} used the poke command against {pokeduser}')


@bot.command()
async def pfp(ctx):
	await ctx.send('you sure? yes or no')


	def check(m): return m.author == ctx.author and m.channel == ctx.channel
	msg = await bot.wait_for('message', check=check, timeout=None)
	yes = 'yes'
	if msg.content == yes:
		await ctx.send('ok, sending now')
		await ctx.send('https://photos.app.goo.gl/aeEP2kw6ZzuJPRbH9')
	else:
		await ctx.send('ok, ur pretty... lame')
		
hated = ['jazzy']



@bot.command(name='whois')
async def whois(ctx, whoisthis):
	whosthis = whoisthis.lower()
	print('0')
	if whosthis == 'facheli':
		print('1 \n ---')
		await ctx.send('just the best. He is my creator.')
	elif whosthis == 'maybefacheli':
		print('2 \n ---')
		await ctx.send('He\'s amazing. He\'s the programer from who I have been birthed. He is occasionally blunt and an idiot too')
	elif whosthis == 'hated':
		print('3\n ---')
		embed=nextcord.embed(
			color = nextcord.color.red(),
			url="https://bit.ly/3AIdW82",
		  description = hated
			)
		embed.set_author(name= ctx.author.display_name)
		embed.add_field(name='hated', value=hated, inline=True)
		await ctx.send(embed=embed)
		print('3.2\n ---')



@bot.command()
async def report(ctx, name, *reason):
	print('reported')
	embed = nextcord.Embed(
		color = nextcord.Color.gold(),
		url="https://bit.ly/3AIdW82",		
		description= 'REPORTED'
	)
	embed.set_author(name=ctx.author.display_name)
	embed.add_field(name=name,value=reason, inline=False)
	
	guild = bot.guilds[0]
	owner = guild.owner
	#owner = int(wner)
	
	await ctx.send(embed=embed)
	print('embed sent')
	


@bot.event 
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    
    if message_id == 916116986344403024:
        guild_id = payload.guild_id
        guild = nextcord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == "watermelon":
            role = nextcord.utils.get(guild.roles, name = 'WaterMelon')
        elif payload.emoji.name == "0492":
            role = nextcord.utils.get(guild.roles, name = 'SCP-049-2')
        elif payload.emoji.name == "096":
            role = nextcord.utils.get(guild.roles, name = 'SCP-096')
        elif payload.emoji.name == "106":
            role = nextcord.utils.get(guild.roles, name = 'SCP-106')
        elif payload.emoji.name == "173":
            role = nextcord.utils.get(guild.roles, name = 'SCP-173')
        elif payload.emoji.name == "682":
            role = nextcord.utils.get(guild.roles, name = 'SCP-682')
        elif payload.emoji.name == "939":
            role = nextcord.utils.get(guild.roles, name = 'SCP-939')
        elif payload.emoji.name == "999":
            role = nextcord.utils.get(guild.roles, name = 'SCP-999')
        elif payload.emoji.name == "Chaos":
            role = nextcord.utils.get(guild.roles, name = 'Chaos Insurgency')
        elif payload.emoji.name == "DClass":
            role = nextcord.utils.get(guild.roles, name = 'D-Class')
        elif payload.emoji.name == "MTF":
            role = nextcord.utils.get(guild.roles, name = 'MTF')
        elif payload.emoji.name == "Scientist":
            role = nextcord.utils.get(guild.roles, name = 'Scientist')

        member = payload.member
        await member.add_roles(role)





@bot.command(name='rps')
async def rps(ctx, selection):
  rock = "rock"
  paper = "paper"
  scissors = "scissors"
  
  types = (rock, paper, scissors)
  botchoice = random.choice(types)
  if selection == rock:
    if botchoice == scissors: 
      await ctx.send ("You win :unamused:")
    elif botchoice == paper:
      await ctx.send("You lose! Middle Fingers Up!:middle_finger::smirk:")
    else:
      await ctx.send("tie")
  
  if selection == paper:
    if botchoice == rock:
      await ctx.send("You win :unamused:")
    elif botchoice == scissors:
      await ctx.send("You lose! Middle Fingers Up!:middle_finger::smirk:")
    else: 
      await ctx.send("tie")
  if selection == scissors:
    if botchoice == paper:
      await ctx.send("You win :unamused:")
    elif botchoice == rock:
      await ctx.send("You lose! 𝓜𝓲𝓭𝓭𝓵𝓮 𝓯𝓲𝓷𝓰𝓮𝓻𝓼 𝓾𝓹!:middle_finger::smirk:")
    else:
      await ctx.send("Great minds think alike")
  await ctx.send(f'Bot chose {botchoice}')


@bot.command(name="howcool", help="How cool is someone?")
async def howcool(ctx, mentioned):
    
    random_number = str(random.randint(80, 100))
    iss = " is "
    cool = "% cool"
    await ctx.send(mentioned + iss + random_number + cool)




@bot.command(name='rolldice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name="quote")
async def block_quote(ctx, *, arg):
    quote_text = 'You said:\n> {}'.format(arg)
    await ctx.send(quote_text)

@bot.command(name='passwordgenerator',
             help='generates you a random password')
async def passwordgen(ctx, number_of_characters: int):
	counter = 1
	if number_of_characters == 0:
		await ctx.send("password")
		await ctx.send("end password")  
	else:
		if number_of_characters >= 40:
			await ctx.send("LOL nice try :smirk: please make a password **under** 40 characters")    
		
		elif number_of_characters <= 4:
			await ctx.send("please make a password with more than 4 characters")
		
		else:
				lower = string.ascii_lowercase
				upper = string.ascii_uppercase
				num = string.digits	
				all = lower + upper + num	
				temp = random.sample(all, number_of_characters)						
				print(f'Temporary password before line 345: \n{temp}')
				password = "".join(temp)
				await ctx.send(password)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@bot.command(name="add", help="add two numbers ")
async def calculator(ctx, a: int, b: int):
  if a or b == 0:
    await ctx.send('Thats easy, you are adding NOTHING')
    return
  else:
    answer = a + b
    await ctx.send(answer )

@bot.command(name="subtract", help="subtract two numbers ")
async def subtract(ctx, a: int, b: int):
	if a or b == 0:
		await ctx.send('Thats easy, you are subtracting NOTHING')
		return
	else:
		answer = a - b
		await ctx.send(answer )

@bot.command(name="multiply", help="  multiply two numbers ")
async def multiply(ctx, a: int, b: int):
	if a or b == 0:
		await ctx.send('Thats easy, you are multiplying NOTHING')
		return
	else:
		answer = a * b
		await ctx.send(answer )

@bot.command(name="divide", help="  divide two numbers ")
async def divide(ctx, a: int, b: int):
	if a  == 0:
		await ctx.send('Its Zero, always has been and always will ')
		return
	elif b == 0:
		await ctx.send('Theres no way...')

	else:
	
	
		answer = a / b
		embed=nextcord.Embed(title=f'{a}/{b}', description=f"{answer}", color=ctx.author.color) 
		await ctx.send(embed=embed )


  


@bot.command(name='Hi', help='replies with random greeting message')
async def ccvv(ctx):
    hi = "hello",
    "good day",
    "greetings",
    "welcome back"

    response = random.choices(hi)
    await ctx.send(response)


@bot.command(name="bye", help="BYE! ")
async def adios(ctx):
    phrases = "*adios*", "good bye", "*auf wiedersehen*", "goodbye, we won't miss you :wink:", "ok"
    await ctx.send(random.choice(phrases))


@bot.command(name='coinflip', help='flips a coin ')
async def coinflip(ctx):
    coin_flip = ('heads', 'tails')
    response = random.choice(coin_flip)
    await ctx.send(response)


@bot.command(name='???', help='IDK?')
async def FR_YT(ctx):
    Lala = (
        'SUB TO FUTURISTIC REALITY ON YOUTUBE. 20 subs before 2022! https://www.youtube.com/channel/UCzg2irv97vDywwgD07LzrnQ '
    )
    response = (Lala)
    await ctx.send(response)


@bot.command(name='8ball', help='ask the 8ball a question ')
async def eight_ball(ctx, *question):
	question=question
	if len(question) == 0:
		await ctx.send('you idiot, you need to ask a question')
		return
	else:	
		answertoquestion = 'no you dum-dum', 'yes, obviously', 'NO! was that a legit question!? :rofl:', 'absolutly'
		response = random.choice(answertoquestion)
		await ctx.send(response)


@bot.command(name='botcool?')
async def _bot(ctx):
    cool = "Am I Cool?" + "Yes, I'm cool"
    await ctx.send(cool)


@bot.command(name='hAx', help=':computer:HaXIng...')
async def HAx(ctx):
    HAx1 = ("Connecting to Server...")
    HAx2 = ("Connected!")
    HAx3 = ("Uploading File: 10%")
    HAx4 = ("Uploading File: 20%")
    HAx5 = ("Uploading File: 30%")
    HAx6 = ("Uploading File: 40%")
    HAx7 = ("Uploading File: 50%")
    HAx8 = ("Uploading File: 60%")
    HAx9 = ("Uploading File: 70%")
    HAx10 = ("Uploading File: 80%")
    HAx11 = ("Uploading File: 90%")
    HAx12 = ("Uploading File: 99%")
    HAx13 = ("File Uploaded!")
    HAx14 = ("Virus Injection Started...")
    HAx15 = ("Virus Injection Complete!")
    await ctx.send(HAx1)
    await ctx.send(HAx2)
    await asyncio.sleep(2)
    await ctx.send(HAx3)
    await asyncio.sleep(2)
    await ctx.send(HAx4)
    await asyncio.sleep(2)
    await ctx.send(HAx5)
    await asyncio.sleep(2)
    await ctx.send(HAx6)
    await asyncio.sleep(2)
    await ctx.send(HAx7)
    await ctx.send(HAx8)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await ctx.send(HAx9)
    await ctx.send(HAx10)
    await asyncio.sleep(2)
    await ctx.send(HAx11)
    await ctx.send(HAx12)
    await ctx.send(HAx13)
    await asyncio.sleep(2)
    await ctx.send(HAx14)
    await asyncio.sleep(2)
    await ctx.send(HAx15)




@bot.command(name= "formatting")
async def formating_embed(ctx):
    embed=nextcord.Embed(
    title="Text Formatting",
        url="https://www.youtube.com/channel/UCzg2irv97vDywwgD07LzrnQ",
        description="Here are some ways to format text",
        color=nextcord.Color.brown())
  
    embed.set_author(name=ctx.author.display_name, url="https://bit.ly/3AIdW82a", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://imgur.com/a/XveUIdx")
    embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
    embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
    embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
    embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
    embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
    embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
    embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
    embed.set_footer(text='Learn more here: https://bit.ly/3kELU7Q')
    await ctx.send(embed=embed)

@bot.command(name='AI')
async def tts(ctx):
	message = await ctx.send('hmm…')
	message_id = message.id
	await message_id.add_reaction('\U0001f44d')


@bot.command(name='date')
async def odate(ctx):
	await ctx.send(datetime.date.now)
@bot.command(name='time')
async def otime(ctx):
	date_=datetime.datetime.now
	await ctx.send(date_)







    
bot.run("ODM5ODY4Nzc2OTA3Mjc2MzA4.YJP6wA.2C3kEgMCAFu6mHFJnubti51fc6Y")
