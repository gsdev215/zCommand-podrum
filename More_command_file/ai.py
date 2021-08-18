import aiml,os

path: str = os.path.join(os.getcwd(), "plugins")
BRAIN_FILE=path+"/more_command/brain.dump"

k = aiml.Kernel()

class ai_command:
    def __init__(self, plugin: object) -> None:
        self.plugin: object = plugin
        self.name: str = "ai"
        self.description: str = "Ai bot to talk "
        print("Loading from brain file: Brain.dump. please wait Estimated time 20 sec")
        k.loadBrain(BRAIN_FILE)
    
    def execute(self, args: list, sender: object) -> None:

        if len(args) > 0:

            if not hasattr(sender, "username"):
                res= k.respond(' '.join(args))
                sender.send_message(f"[ai] {res}")

            else:
                res= k.respond(f"{' '.join(args)}")

                sender.server.broadcast_message(f"[ai] {res}")

        else:

            sender.send_message("/ai <message: message>")

