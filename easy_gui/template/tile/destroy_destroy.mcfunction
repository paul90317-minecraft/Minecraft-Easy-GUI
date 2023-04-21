kill @s
setblock ~ ~ ~ air destroy
kill @e[type=item,nbt={Item:{id:"<block>",Count:1b}},distance=..1,sort=nearest]
function eg:tile/<id>/spawn_egg
