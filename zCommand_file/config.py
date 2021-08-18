import json,os

prefix = "."
token ="NzYwODIxODg3MjE0ODEzMTg2.X3RomQ.DrA3dKUyakrZrXLFIjfM9MGJMuM"
webhooks = "https://discord.com/api/webhooks/876028894766043177/88Ngbu1786hImFZNyKq4IGHD70Lzxssgku_0T0KmVmPGBkquxMeEEKiStnn8SZGhiuLK"
path: str = os.path.join(os.getcwd(), "plugins")

def json_open():
	file = f"{path}/more_command/input.json"
	with open(file,"r") as f:
		n = json.load(f)
	return n
	
def json_dump(n:str=None):
	file = Path(f"plugins/more_command/input.json")
	with open(file,"w") as f:
		json.dump(n,f)