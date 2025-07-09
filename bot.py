import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import random

# Load .env file only if it exists (for local development)
if os.path.exists("token.env"):
    load_dotenv("token.env")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   help_command=None,
                   case_insensitive=True)

@bot.event
async def on_ready():
    print(f"🟢 {bot.user.name} has connected to Discord!")

class_specs_by_role = {
    "dps": [
        "Mage - Fire 🔥", "Mage - Frost ❄️", "Mage - Arcane 🌀",
        "Hunter - Beast Mastery 🐺", "Hunter - Marksmanship 🎯", "Hunter - Survival 🏹",
        "Warlock - Affliction 🕷️", "Warlock - Demonology 👹", "Warlock - Destruction 🔥",
        "Rogue - Assassination 🗡️", "Rogue - Combat 💥", "Rogue - Subtlety 🎭",
        "Priest - Shadow 🌑", "Monk - Windwalker 🐉",
        "Druid - Balance 🌙", "Druid - Feral 🐾",
        "Warrior - Arms 💪", "Warrior - Fury 🔥",
        "Death Knight - Frost ❄️", "Death Knight - Unholy ☠️",
        "Paladin - Retribution ⚔️", "Shaman - Elemental ⚡", "Shaman - Enhancement 🔨"
    ],
    "ranged": [
        "Mage - Fire 🔥", "Mage - Frost ❄️", "Mage - Arcane 🌀",
        "Hunter - Beast Mastery 🐺", "Hunter - Marksmanship 🎯", "Hunter - Survival 🏹",
        "Warlock - Affliction 🕷️", "Warlock - Demonology 👹", "Warlock - Destruction 🔥",
        "Priest - Shadow 🌑", "Druid - Balance 🌙", "Shaman - Elemental ⚡"
    ],
    "melee": [
        "Monk - Windwalker 🐉", "Druid - Feral 🐾",
        "Warrior - Arms 💪", "Warrior - Fury 🔥",
        "Death Knight - Frost ❄️", "Death Knight - Unholy ☠️",
        "Paladin - Retribution ⚔️", "Shaman - Enhancement 🔨",
        "Rogue - Assassination 🗡️", "Rogue - Combat 💥", "Rogue - Subtlety 🎭"
    ],
    "healer": [
        "Priest - Discipline ✨", "Priest - Holy ⛪",
        "Monk - Mistweaver 🌸",
        "Druid - Restoration 🌿",
        "Shaman - Restoration 💧",
        "Paladin - Holy ✝️"
    ],
    "tank": [
        "Monk - Brewmaster 🍺",
        "Druid - Guardian 🦁",
        "Warrior - Protection 🛡️",
        "Death Knight - Blood 💀",
        "Paladin - Protection 🛡️"
    ]
}

@bot.command()
async def chooseclass(ctx, role: str = None):
    # Fallback to full list if role is missing or invalid
    role = role.lower() if role else "all"
    
    if role in class_specs_by_role:
        options = class_specs_by_role[role]
        chosen = random.choice(options)
        await ctx.send(f"Your chosen {role} spec is: **{chosen}**")
    elif role == "all":
        # Flatten all lists into one master list
        all_specs = [spec for specs in class_specs_by_role.values() for spec in specs]
        chosen = random.choice(all_specs)
        await ctx.send(f"Your randomly chosen spec is: **{chosen}**")
    else:
        valid_roles = ", ".join(class_specs_by_role.keys()) + ", all"
        await ctx.send(f"Invalid role. Try one of: {valid_roles}")

@bot.command()
async def classhelp(ctx):
    help_text = (
        "**Welcome to the Pandaria Spec Picker!** 🐉\n\n"
        "Use `!chooseclass <role>` to get a random spec based on role.\n"
        "**Available roles:**\n"
        "- `dps` – Includes all damage dealers (melee & ranged)\n"
        "- `ranged` – Caster & ranged DPS specs\n"
        "- `melee` – Up-close combat DPS specs\n"
        "- `healer` – Healing classes and specs\n"
        "- `tank` – Specs specialized for defense and damage absorption\n"
        "- `all` – Pulls from every class and spec\n\n"
        "For example: `!chooseclass dps` or `!chooseclass tank`\n"
        "let me decide your fate."
    )
    await ctx.send(help_text)

# Run the bot
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN not found in environment variables")