kill @s
setblock ~ ~-1 ~ air destroy
execute positioned ~ ~-1 ~ run kill @e[type=item,nbt={Item:{id:"<block>",Count:1b}},distance=..1,sort=nearest]
execute positioned ~ ~-1 ~ run function eg:tile/<id>/spawn_egg
