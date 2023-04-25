summon item ~ ~ ~ {Tags:[egno,egset],CustomNameVisible:1b,CustomName:'<text>',Motion:[0.0,0.3,0.0],Item:{Count:1b,id:"<item>",tag:{eg:{is:1b,type:tile,name:<id>}<tag>}}}
<load>
tag @e[sort=nearest,limit=1,type=item,tag=egset] remove egset
kill @s
setblock ~ ~ ~ air destroy
kill @e[type=item,tag=!egno,nbt={Item:{id:"<block>",Count:1b}},distance=..1,sort=nearest]