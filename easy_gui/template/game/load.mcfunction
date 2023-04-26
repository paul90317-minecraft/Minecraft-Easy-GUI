scoreboard objectives add eg.n dummy
scoreboard objectives add eg.temp dummy
tellraw @a ["The following blocks is powered by ",{"text": "Easy GUI","color": "light_purple","clickEvent": {"action": "open_url","value": "https://github.com/paul90317/Minecraft-Easy-GUI"},"bold": true,"hoverEvent": {"action": "show_text","value": "website"}}]
function #eg:powered_by