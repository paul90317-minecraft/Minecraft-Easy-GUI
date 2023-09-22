scoreboard players set @s eg.temp 0
execute unless block ~ ~ ~ #eg:air run scoreboard players set @s eg.temp 1
scoreboard players set @s eg.n 0
execute at @e[type=item, distance=..1] run scoreboard players add @s eg.n 1
scoreboard players set @s[scores={eg.n=2..}] eg.temp 1
execute if score @s eg.temp matches 1 run tag @s add egno
execute if score @s eg.temp matches 0 run function eg:tile/<id>/try_spawn/load