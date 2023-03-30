scoreboard players set @s eg.temp 0
execute unless block ~ ~ ~ air run scoreboard players set @s eg.temp 1
execute unless block ~ ~-1 ~ <block> run scoreboard players set @s eg.temp 1
execute if score @s eg.temp matches 1 run function eg:tile/<id>/destroy
