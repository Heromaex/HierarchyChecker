'''
discord.py role hierarchy checker by Heromaex#3945 
language: Python
'''

'''
Needed arguments:
- user (the person that needs to be higher)
- target (the person that needs to be lower)
it will only return True, if the given user objects highest role is higher than the targets highest role! Otherwise it will return False.
'''

import discord

def role_hierarchy(ctx, user:discord.Member, target:discord.Member):
    roledict = {}
    guildroles = ctx.guild.roles # gets all roles of the server
    for i in range(len(guildroles)):
        roledict[guildroles[i]] = str(i) # saves every role as a number in a dictionary
    highest_roles = (user.roles[-1],target.roles[-1]) # gets the users and targets highest roles
    if int(roledict[highest_roles[0]]) > int(roledict[highest_roles[1]]):
        return True
    else:
        return False