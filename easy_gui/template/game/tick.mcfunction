execute as @e[type=area_effect_cloud] at @s run function #eg:search/area_effect_cloud
execute as @e[type=item,nbt={OnGround:1b,Item:{tag:{eg:{is:1b}},Count:1b}},tag=!egno] at @s run function #eg:search/item
execute as @e[type=glow_item_frame] at @s run function #eg:search/glow_item_frame
clear @a #eg:label{eg:{is:1b,type:label}}
kill @e[type=item,nbt={Item:{tag:{eg:{is:1b,type:label}}}}]
