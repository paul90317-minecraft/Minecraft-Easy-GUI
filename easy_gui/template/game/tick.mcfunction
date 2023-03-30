clear @a #eg:label{eg:{is:1b,type:label}}
kill @e[type=item,nbt={Item:{tag:{eg:{is:1b,type:label}}}}]
execute as @e[type=area_effect_cloud] at @s run function #eg:search/area_effect_cloud
execute as @e[type=item_frame] at @s run function #eg:search/item_frame
