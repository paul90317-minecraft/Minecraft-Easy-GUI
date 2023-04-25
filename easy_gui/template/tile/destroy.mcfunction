summon item ~ ~ ~ {Tags:[egset],CustomNameVisible:1b,CustomName:'<text>',Motion:[0.0,0.3,0.0],Item:{Count:1b,id:"<spawn_egg>",tag:{EntityTag:{id:"minecraft:area_effect_cloud",Tags:[eg.<id>]}<tag>}}}
<load>
tag @e[sort=nearest,limit=1,type=item,tag=egset] remove egset
kill @s
setblock ~ ~ ~ air destroy
kill @e[type=item,nbt={Item:{id:"<block>",Count:1b}},distance=..1,sort=nearest]