summon item ~ ~ ~ {Motion:[0.0,0.3,0.0],Item:{id:"minecraft:cookie",Count:1b,tag:{eg:{is:1b,type:label}}}}
data modify entity @e[type=item,sort=nearest,limit=1,nbt={Item:{tag:{eg:{is:1b,type:label}}}}] Item set from block ~ ~-1 ~ Items[{Slot:<slot>b}]
item replace block ~ ~-1 ~ container.<slot> with <item>{eg:{is:1b,type:label},display:{Name:'{"text": "<text>","italic":false<color>}'}} 1
playsound block.dispenser.dispense ambient @a ~ ~ ~
<click>