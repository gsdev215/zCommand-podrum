from discord_webhook import DiscordWebhook
import config as c

class send_command:
    def __init__(self, plugin: object) -> None:
        self.plugin: object = plugin
        self.name: str = "send"
        self.description: str = "Sends the message thought webhook"
    
    def execute(self, args: list, sender: object) -> None:
        if len(args) > 0:
            if not hasattr(sender, "username"):
                n = c.json_open()
                #k = n["webhook"]
                webhook = DiscordWebhook(url=n["webhook"], content=f"[Server]{' '.join(args)}")
                response = webhook.execute()
            else:
                n = c.json_open()
                k = n["webhook"]
                webhook = DiscordWebhook(url=k, content=f"[{sender.username}] {' '.join(args)}")
                response = webhook.execute()
                #sender.server.broadcast_message(f"[{sender.username}] {' '.join(args)}")
        else:
            sender.send_message("/send <message: message>")
