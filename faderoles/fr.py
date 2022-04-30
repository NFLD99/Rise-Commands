@Rise.command(aliases=['fr'])
async def faderoles(ctx, colours):
    await ctx.message.delete()
    hexStr = colours.replace("#", "0x")
    hexList = hexStr.split(',')
    roles = ctx.guild.roles
    rn = ",".join([str(r.name) for r in roles])
    rnl = rn.split(',')
    del rnl[0]
    roleList = rnl
    i = 0
    for r in roleList:
        roleedit = r
        roletag = discord.utils.get(ctx.guild.roles, name=str(roleedit))
        try:
            if (hexList[0] == "rng"):
                hexToSet = int("%06x" % random.randint(0, 0xFFFFFF), 16)
            else:
                if (len(roleList) != len(hexList)):
                    await ctx.send("Error, Not Enough Colours, Please Enter: " + str(len(roleList)) + " Colours")
                    print(" ")
                else:
                    hexToSet = int(hexList[i], 16)
        except:
            print("except: ")
            print(sys.exc_info())
            await ctx.send("hexToSet except: " + str(sys.exc_info()))
            print(" ")
            break
        print(roletag)
        print("hexToSet: ")
        print(hexToSet)
        print(" ")
        i = i + 1
        try:
            await roletag.edit(colour=hexToSet)
        except:
            print("except: ")
            print(sys.exc_info())
            print(" ")
            await ctx.send("roletag.edit except: " + str(sys.exc_info()))
            break
    await ctx.send("Roles Coloured.")