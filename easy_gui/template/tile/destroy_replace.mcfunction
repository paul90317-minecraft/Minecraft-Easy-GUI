kill @s
setblock ~ ~-1 ~ air replace
execute positioned ~ ~-1 ~ run function eg:tile/<id>/spawn_egg
