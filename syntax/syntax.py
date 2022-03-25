@Rise.command(aliases=['betterhelp', 'bhelp'])
async def syntax(ctx, cmd):
    await ctx.message.delete()
    await asyncio.sleep(1)
    print(cmd)
    try:
        data = urllib.request.urlopen("https://raw.githubusercontent.com/NFLD99/Rise-Commands/main/syntax/cmdSyntaxList.json").read()
        output = json.loads(data)
        for i in output[cmd.lower()]:
            i1 = str(i).replace("{", "").replace("}", "").replace("\', \'", "\'\n\'")
            theSyntax = f"```py\n{cmd}:\n{i1}\n```"
            await ctx.send(theSyntax, delete_after=15)
            print(theSyntax)
        # await ctx.send(syntaxFull)
    except Exception as e:
        print(str(e))
        await ctx.send(f"Command `{cmd}` not found!", delete_after=15)
