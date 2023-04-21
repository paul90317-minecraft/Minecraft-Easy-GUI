summon item ~ ~1 ~ {Motion:[0.0,0.3,0.0],Item:{id:"minecraft:cookie",Count:1b,tag:{eg:{is:1b,type:label}}},Tags:[egno]}
execute positioned ~ ~1 ~ run data modify entity @e[type=item,sort=nearest,limit=1,nbt={Item:{tag:{eg:{is:1b,type:label}}}}] Item set from block ~ ~-1 ~ Items[{Slot:<slot>b}]
item replace block ~ ~ ~ container.<slot> with air
playsound block.dispenser.dispense ambient @a ~ ~ ~