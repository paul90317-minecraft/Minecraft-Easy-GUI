summon item ~ ~1 ~ {Motion:[0.0,0.3,0.0],Item:{id:"minecraft:cookie",Count:1b,tag:{eg:{is:1b,type:label}}},Tags:[egno]}
scoreboard players remove @s eg.n <n>
execute store result block ~ ~ ~ Items[{Slot:<slot>b}].Count byte 1 run scoreboard players get @s eg.n 
execute positioned ~ ~1 ~ run data modify entity @e[type=item,sort=nearest,limit=1,nbt={Item:{tag:{eg:{is:1b,type:label}}}}] Item set from block ~ ~ ~ Items[{Slot:<slot>b}]
data modify block ~ ~ ~ Items[{Slot:<slot>b}].Count set value <n>
playsound block.dispenser.dispense ambient @a ~ ~ ~