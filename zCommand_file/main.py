import aiml
from podrum.console.logger import logger
from podrum.protocol.mcbe.mcbe_player import mcbe_player
import asyncio,os
import config as c
from discord_webhook import DiscordWebhook
from send_command import send_command
from ai import ai_command


class Main:
	
	def __init__(self):
		self.server: object = 'server'
		self.name: str = "zCommand"
		self.description: str = "Adds few commands"
		
	def on_load(self):
	       self.logger: logger = self.server.logger
	       self.server.managers.command_manager.register(send_command(self))
	       self.server.managers.command_manager.register(run_command(self))
	       self.server.managers.command_manager.register(ai_command(self))
	       
