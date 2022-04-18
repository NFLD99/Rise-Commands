@Rise.command(aliases=['switchrpc'])
async def srpc(ctx, name):
    await ctx.message.delete()
    os.getcwd()
    cwd = os.getcwd()
    print("Current working directory: {0}".format(cwd))
    try:
        with open(cwd+"/Rpc/"+name+".json", 'r') as file:
            contents = file.read()
            print(contents)
        with open(cwd+"/Misc/richpresence.json", 'w') as cfgsf:
            cfgsf.write(contents)
    except:
        await ctx.send('Error:'+ sys.exc_info()[0])
    await ctx.send('Rpc Updated.')