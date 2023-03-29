scoreboard players set @s eg.temp 0
execute unless block ~ ~ ~ air run scoreboard players set @s eg.temp 1
execute unless block ~ ~1 ~ air run scoreboard players set @s eg.temp 1
execute if score @s eg.temp matches 1 run function easy_gui:containers/<id>/try_spawn/cancel
execute if score @s eg.temp matches 0 run function easy_gui:containers/<id>/try_spawn/load