@Rise.command()
async def syntax(ctx, cmd):
    await ctx.message.delete()
    await asyncio.sleep(1)
    print(cmd)
    try:
        with open('Scripts/syntaxs.json', 'r') as f:
            data = json.load(f)
            for i in data[cmd]:
                i1= str(i)
                i2= i1.replace("{", "")
                i3= i2.replace("}", "")
                i4= i3.replace("\', \'", "\'\n\'")
                theSyntax= "```py\n" + cmd + ":\n" + i4 + "\n```"
                await ctx.send(theSyntax, delete_after=15)
                print(theSyntax)
            # await ctx.send(syntaxFull)
    except Exception as e:
        print(str(e))
        await ctx.send("Command Not Found!\nMake sure you use all lowercase", delete_after=15)