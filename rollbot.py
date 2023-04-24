import discord
import random
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('/roll'): #change your prefix here if you don't want forward slash as the option
        number = message.content.split() #split string into an array
        num = int(number[1]) #get the 2nd array value (first will be 'roll') 
        result = str(random.randint(1,num)) #get a random number between 1 and the users number
        #print(message.author.display_name) 
        #print(result)
        await message.channel.send(str(message.author.display_name + ' rolls ' + result + ' (1-' + str(num) + ')' )) #post to the channel the result
                                       
client.run(<your client token here>)
