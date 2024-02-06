import pandas as pd
import discord
import asyncio
from discord.ui import Select , View
from discord.ext import commands
import tracemalloc
import random as rand
from token import bottoken
tracemalloc.start()

bot_token = bottoken()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    # bot load here
    print('bot ready')
    print('---------')



@client.command()
async def create_family(interaction):
    select = Select(
        placeholder='(Y/N)',
        options=[
            discord.SelectOption(label="Yes", description="Accept"),
            discord.SelectOption(label="No", description="Decline")
        ])
    view = View()
    view.add_item(select)

    select.callback = my_callback
    await interaction.send('So you would like to generate a new family. This will overwrite any existing family.', view=view)


async def my_callback(interaction):
    if interaction.data['values'][0] == 'Yes':
        await interaction.response.send_message('Great! Please provide the name for the new family:')
        try:
            text_input = await client.wait_for(
                'message',
                check=lambda message: message.author == interaction.user,
                timeout=60
            )
            await interaction.followup.send(f'You are the proud leader of the: {text_input.content} family')
            family_name = text_input.content
            user = interaction.user.id
            username = interaction.user.discriminator

            family = pd.read_csv('family.csv')
            if family.size == 0:
                familyid = 1
            else:
                familyid = family.familyid.max() + 1

            f_l = [family_name, familyid, username, user, 0, 0, 0, 0, 'keywords']

            select_follow_up = Select(
                placeholder='Many of the great families have storied lineages tracing their way back to the very founding of Veloria. What stories are told of your family?',
                options=[
                    discord.SelectOption(value='1', description="We are rising stars with no history",
                                         label="Stronger Starting Characters - 5"),
                    discord.SelectOption(value='2', description="We played an important role in the founding of the senate",
                                         label="Stronger Political Influence - 3"),
                    discord.SelectOption(value='3', description="We are as old as Veloria herself",
                                         label="Stronger Estates - 4"),
                    discord.SelectOption(value='4', description="Our name is steeped in mystery and strange stories",
                                         label="Stronger Societies - 4")
                ])
            view_follow_up = View()
            view_follow_up.add_item(select_follow_up)
            select_follow_up.callback = my_callback_2
            select_follow_up.message = await interaction.followup.send('Please choose an option:', view=view_follow_up)
        except asyncio.TimeoutError:
            await interaction.response.edit_message(content='Timeout: You did not provide the text input in time.')
    else:
        await interaction.response.edit_message(content='You declined to create a new family.')

async def my_callback_2(interaction):
    selected_option = interaction.data['values'][0]
    if selected_option == '1':
        num_fam = 5
        num_estates = 3
        resource_multi = 0.6
    elif selected_option == '2':
        num_fam = 3
        num_estates = 5
        resource_multi = 1.2
    elif selected_option == '3':
        num_fam = 2
        num_estates = 6
        resource_multi = 1.5
    elif selected_option == '4':
        num_fam = 4
        num_estates = 4
        resource_multi = 0.9
    await interaction.response.send_message(f'Now we must decide some information on each of your characters and estates you have {num_fam} family members and {num_estates} estates.')
    #for i in range(1, num_fam + 1):  # Adjusted the range to include the last index
    #    await create_family_member(interaction, i)
    in_var = 0
    while in_var < num_estates:  # Adjusted the range to include the last index
        print(in_var,num_estates)
        await interaction.followup.send(f'Family Member {in_var}')
        await create_estates(interaction, in_var)
        in_var=+1

async def create_family_member(interaction, index):
    await interaction.followup.send(f'Family Member {index}')
    try:
        text_input = await client.wait_for(
            'message',
            check=lambda message: message.author == interaction.user,
            timeout=60
            )
        print(text_input.content)
    except asyncio.TimeoutError:
        await interaction.response.edit_message(content='Timeout: You did not provide the text input in time.')
    #await interaction.followup.send_message(num_fam,num_estates,resource_multi)
        
async def create_estates(interaction, index):
    try:
        text_input = await client.wait_for(
            'message',
            check=lambda message: message.author == interaction.user,
            timeout=60
            )
        char_name = text_input.content
    except asyncio.TimeoutError:
        await interaction.followup.send(content='Timeout: You did not provide the text input in time.')
        
    df_ev = pd.read_csv('events.csv')
    df_found = df_ev[df_ev['eventname']=='Founding_Event'].reset_index()
    n_re = df_found.shape[0]-1
    df_q1 = df_found.iloc[rand.randint(0,n_re)]

    await interaction.followup.send_message('Please answer with 1,2,3 or 4')
    await interaction.followup.send_message('Please answer with 1,2,3 or 4')


    try:
        text_input = await client.wait_for(
            'message',
            check=lambda message: message.author == interaction.user,
            timeout=60
            )
        char_name = text_input.content
    except asyncio.TimeoutError:
        await interaction.followup.send(content='Timeout: You did not provide the text input in time.')



    #   select_q1 = Select(
    #           placeholder=df_q1['eventdescription'],
    #           options=[
    #               discord.SelectOption(value='1', description="Option_1",
    #                                    label=df_q1['Option_1']),
    #               discord.SelectOption(value='2', description="Option_2",
    #                                    label=df_q1['Option_2']),
    #               discord.SelectOption(value='3', description="Option_3",
    #                                    label=df_q1['Option_3']),
    #               discord.SelectOption(value='4', description="Option_4",
    #                                    label=df_q1['Option_4'])                                                                                  
    #           ])
    #   view_follow_up = View()
    #   view_follow_up.add_item(select_q1)
    #   select_q1.callback = my_callback_2
    #   select_q1.message = await interaction.followup.send('Please choose an option:', view=view_follow_up)
    #   try:
    #       text_input = await client.wait_for(
    #           'select_option',
    #           check=lambda message: message.author == interaction.user,
    #           timeout=60
    #           )
    #       print(text_input.content)
    #   except asyncio.TimeoutError:
    #       await interaction.response.edit_message(content='Timeout: You did not provide the text input in time.')
    #await interaction.followup.send_message(num_fam,num_estates,resource_multi)










client.run(bot_token)