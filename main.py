import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# List of fish
fish_info = {
    'Bass': 'A common fish that prefers freshwater.',
    'Trout': 'A cold-water fish known for its delicate flavor.',
    'Salmon': 'A popular game fish, known for its migration...',
}

# Fishing tips
fishing_tips = [
    'Fish during early morning for the best catch.',
    'Use the right bait for different types of fish.',
    'Keep your fishing spot a secret to avoid crowded areas.',
]

# Logging catches
catches = []

# Command to get fish info
@bot.command()
async def fish(ctx, fish_name: str):
    info = fish_info.get(fish_name.title(), 'Fish not found.')
    await ctx.send(info)

# Command to get fishing tips
@bot.command()
async def tips(ctx):
    tips_message = '\n'.join(fishing_tips)
    await ctx.send(f'Tips for fishing:\n{tips_message}')

# Command to log a catch
@bot.command()
async def catch(ctx, fish_name: str):
    catches.append(fish_name)
    await ctx.send(f'Logged your catch: {fish_name}')

# Command to show leaderboard
@bot.command()
async def leaderboard(ctx):
    # Placeholder for leaderboard functionality
    await ctx.send('Leaderboard feature coming soon!')

# Running the bot
@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

# Start the bot with your token
bot.run('YOUR_BOT_TOKEN')
