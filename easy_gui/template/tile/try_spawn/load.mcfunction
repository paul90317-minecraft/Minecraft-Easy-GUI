kill @s
setblock ~ ~ ~ <block>[facing=up]{CustomName:'{"text":"<block_text>"<block_color>,"italic":false}'} destroy
summon item_frame ~ ~ ~ {Tags:[eg.<id>],Facing:1b,Item:{id:"<item>",Count:1b,tag:{display:{Name:'{"text":"<item_text>"<item_color>,"italic":false}'}<item_enchant><item_tag>,HideFlags:1}},Invulnerable:1b,Fixed:1b,Invisible:1b}