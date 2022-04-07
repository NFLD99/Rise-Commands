@Rise.command()
async def rebootlinux(ctx):
    await ctx.message.edit(content="Restarting Server", delete_after=15)
    os.system("reboot")