from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


@bot.on_message(filters.command("cstart"))
async def start(client, message):
        await message.reply_text("📲")
        
