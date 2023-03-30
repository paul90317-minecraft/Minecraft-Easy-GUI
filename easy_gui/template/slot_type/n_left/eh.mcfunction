summon item ~ ~ ~ {Motion:[0.0,0.3,0.0],Item:{id:"minecraft:cookie",Count:1b,tag:{eg:{is:1b,type:label}}}}
scoreboard players remove @s eg.n <n>
execute store result block ~ ~-1 ~ Items[{Slot:<slot>b}].Count byte 1 run scoreboard players get @s eg.n 
data modify entity @e[type=item,sort=nearest,limit=1,nbt={Item:{tag:{eg:{is:1b,type:label}}}}] Item set from block ~ ~-1 ~ Items[{Slot:<slot>b}]
data modify block ~ ~-1 ~ Items[{Slot:<slot>b}].Count set value <n>
playsound block.dispenser.dispense ambient @a ~ ~ ~