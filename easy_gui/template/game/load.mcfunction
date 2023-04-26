scoreboard objectives add eg.n dummy
scoreboard objectives add eg.temp dummy
tellraw @a ["The following blocks is made by ",{"text": "Easy GUI V3","color": "light_purple","clickEvent": {"action": "open_url","value": "https://github.com/paul90317/Minecraft-Easy-GUI"},"bold": true,"hoverEvent": {"action": "show_text","value": "GitHub"}}]
function #eg:made_by