@Rise.command()
async def updaterise(ctx):
    await ctx.message.edit(content="Updating...")
    os.system("/home/updateRise.sh")
    await ctx.message.edit(content="Done, Restarting server")
    await ctx.message.delete()
    time.sleep(5)
    os.system("reboot")
    