import discord
from discord.ext import commands
import keep_alive
import json
import random

with open('setting.json',mode='r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix=['Bot','!','+']) 


bot.remove_command('help') 

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot", description="你可以標記我跟我聊天，或是標記後用以下關鍵字：", color=0xeee657)
    embed.set_author(name="by Hung Kao") 
    embed.add_field(name="比大小 要比的對象", value="跟指定對象玩比大小遊戲", inline=False)
    embed.add_field(name="幫我決定or抽 +你想要的選項，各選項需空白間隔", value="抽選功能", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 決鬥(ctx, *,arg):
  user_input = [str(n) for n in arg.split()]
  user_name = ctx.message.author.mention
  enemy_name = user_input[0]
  user_life = 3500
  enemy_life = 3500
  flag = 0

  if len(user_input) == 3 :   	 
        await ctx.send(f'{user_name} 對 {enemy_name} 大喊：「{user_input[2]}！」')

 
  while user_life * enemy_life > 0 :

  	    if user_life > 0 and flag % 2 == 0 :
  	       user_move = random.choice(["開槍射擊","打雷","普","普","普"])
  	       away = random.choice(["中","中","中","中","閃避"])
  	       awayway = random.choice(["嚇得抱頭蹲下","踩到香蕉皮滑倒意外","大喊一聲Ahoy之後"])
  	       flag = flag + 1 

  	       if user_move == "開槍射擊" and away == "中" :
           	   user_damage = random.randint(900,1500)
           	   enemy_life = enemy_life - user_damage
           	   await ctx.send(f'{user_name} 開槍射擊，命中 {enemy_name} 造成{user_damage}點傷害')

  	       elif user_move == "開槍射擊" and away == "閃避" :
        	   await ctx.send(f'{user_name} 開槍射擊，但是 {enemy_name} {awayway}閃開了')

  	       elif user_move == "打雷" and away == "中" :
        	   user_damage = random.randint(1200,2000)
        	   enemy_life = enemy_life - user_damage
        	   await ctx.send(f'{user_name} 閉上眼祈禱，突然一道落雷命中 {enemy_name} 造成{user_damage}點傷害')

  	       elif user_move == "打雷" and away == "閃避" :
        	   await ctx.send(f'{user_name} 閉上眼祈禱，但是信仰不足完全沒有效果')

  	       elif user_move == "普" and away == "中" :
        	   user_damage = random.randint(100,200)
        	   enemy_life = enemy_life - user_damage
        	   await ctx.send(f'{user_name} 攻擊，命中 {enemy_name} 造成{user_damage}點傷害')

  	       elif user_move == "普" and away == "閃避" :
        	   await ctx.send(f'{user_name} 攻擊，但是 {enemy_name} {awayway}閃開了')


  	    elif user_life > 0 and flag % 2 != 0 :
  	       enemy_move = random.choice(["開槍射擊","打雷","普","普","普"])
  	       away = random.choice(["中","中","中","中","閃避"])
  	       awayway = random.choice(["嚇得抱頭蹲下","踩到香蕉皮滑倒意外","大喊一聲Ahoy之後"])
  	       flag = flag + 1

  	       if enemy_move == "開槍射擊" and away == "中" :
        	   enemy_damage = random.randint(900,1500)
        	   user_life = user_life - enemy_damage
        	   await ctx.send(f'{enemy_name} 開槍射擊，命中 {user_name} 造成{enemy_damage}點傷害') 

  	       elif enemy_move == "開槍射擊" and away == "閃避" :
        	   await ctx.send(f'{enemy_name} 開槍射擊，但是 {user_name} {awayway}閃開了')

  	       elif enemy_move == "打雷" and away == "中" :
        	   enemy_damage = random.randint(1200,2000)
        	   user_life = user_life - enemy_damage
        	   await ctx.send(f'{enemy_name} 閉上眼祈禱，突然一道落雷命中 {user_name} 造成{enemy_damage}點傷害')

  	       elif enemy_move == "打雷" and away == "閃避" :
        	   await ctx.send(f'{enemy_name} 閉上眼祈禱，但是信仰不足完全沒有效果')

  	       elif enemy_move == "普" and away == "中" :
        	   enemy_damage = random.randint(100,200)
        	   user_life = user_life - enemy_damage
        	   await ctx.send(f'{enemy_name} 攻擊，命中 {user_name} 造成{enemy_damage}點傷害')

  	       elif enemy_move == "普" and away == "閃避" :
        	   await ctx.send(f'{enemy_name} 攻擊，但是 {user_name} {awayway}閃開了')

  else:
  	    if enemy_life <= 0 :
  	    	await ctx.send(f'{enemy_name} 倒下了，{user_name} 還有{user_life}點血量')

  	    elif user_life <= 0 :
  	    	await ctx.send(f'{user_name} 倒下了，{enemy_name} 還有{enemy_life}點血量')



@bot.event 
async def on_ready():
   print(">>Bot is online<<")

@bot.event

async def on_message(msg):


    elif '對吧' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['沒錯','不對喔!'])        
        await msg.channel.send(f'{response} {msg.author.mention}')


    elif '對不對' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['沒錯!','不對喔!',])      
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '知道' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['是的!'])  
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '是不是' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['是!','不對喔!'])    
        await msg.channel.send(f'{response} {msg.author.mention}')


    elif '是' in msg.content and jdata['ID'] in msg.content and '嗎' in msg.content and msg.author != bot.user:
        response = random.choice(['是!','不對喔!'])       
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '是' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['是!','不對喔!',])  
        await msg.channel.send(f'{response} {msg.author.mention}')


    elif '可以' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['可以!','不可以!'])  
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '能' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['能!','不能!'])   
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '好嗎' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['好!','不好!'])  
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '好不好' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['好!','不好!'])
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '會不會' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['會!','不會']) 
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '會有' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['會!','不會'])
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '有' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['沒有!','有'])
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif '會什麼' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['請輸入+help'])
        await msg.channel.send(f'{response}')

    elif '會' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
        response = random.choice(['會!','不會~']) 
        await msg.channel.send(f'{response} {msg.author.mention}')

    elif jdata['ID'] in msg.content and '幫我決定' in msg.content and msg.author != bot.user:
           txt = [str(n) for n in msg.content.split()]
           listnum = len(txt)
         #  await msg.channel.send(f'有{listnum}個選擇')
           result = random.randint(1,listnum)
         #  await msg.channel.send(f'我選第{result}個')
           x = txt[result] 
           await msg.channel.send(f'我決定是{x}了，{msg.author.mention}!')

    elif '幫' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['好呀!','不要!'])
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '陪' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['好!','不要!'])    
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '來' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['不要!','好']) 
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '要' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['好!','不要!']) 
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '晚安' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['祝你有個好夢!']) 
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '午安' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['睡個午覺吧!']) 
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '早安' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['早安!'])
         await msg.channel.send(f'{response} {msg.author.mention}')

    elif '你好' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['你好!'])
         await msg.channel.send(f'{response} {msg.author.mention}')


    elif '嗨' in msg.content and jdata['ID'] in msg.content and msg.author != bot.user:
         response = random.choice(['嗨!'])
         await msg.channel.send(f'{response} {msg.author.mention}')


    elif jdata['ID'] in msg.content and '抽' in msg.content and msg.author != bot.user:
           txt = [str(n) for n in msg.content.split()]
           listnum = len(txt) -1
         #  await msg.channel.send(f'有{listnum}個選擇')
           result = random.randint(2,listnum)
         #  await msg.channel.send(f'我選第{result}個')
           x = txt[result] 
           await msg.channel.send(f'我決定是{x}了，{msg.author.mention}!')


    elif jdata['ID'] in msg.content and 'dice' in msg.content and msg.author != bot.user:
           player = random.randint(1,6)
           await msg.channel.send(f'{msg.author.mention}擲出了{str(player)}點!')


    elif jdata['ID'] in msg.content and '比大小' in msg.content and msg.author != bot.user:
           player = random.randint(1,87)
           txt = [str(n) for n in msg.content.split()]
           x = random.randint(1,87)
           y = txt[2]
           if player > x :
               await msg.channel.send(f'{msg.author.mention}擲出了{str(player)}點，{y}擲出了{str(x)}點，{msg.author.mention}贏了! ') 
           elif player < x :                       
               await msg.channel.send(f'{msg.author.mention}擲出了{str(player)}點，{y}擲出了{str(x)}點，{y}贏了! ')
           elif player == x :                       
               await msg.channel.send(f'{msg.author.mention}擲出了{str(player)}點，{y}擲出了{str(x)}點，平手')


    await bot.process_commands(msg)

    


keep_alive.keep_alive()
bot.run(jdata['TOKEN'])
