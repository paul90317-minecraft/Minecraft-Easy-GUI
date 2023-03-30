kill @s
setblock ~ ~-1 ~ air destroy
execute positioned ~ ~-1 ~ run kill @e[type=item,nbt={Item:{id:"minecraft:<block>",Count:1b}},distance=..1,sort=nearest]
function eg:tile/<id>/spawn_egg
