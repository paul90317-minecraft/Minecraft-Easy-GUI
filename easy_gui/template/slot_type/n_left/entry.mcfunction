scoreboard players set @s eg.n 0
execute store result score @s eg.n run data get block ~ ~-1 ~ Items[{Slot:<slot>b}].Count
execute if score @s eg.n matches <n_add_one>.. run function easy_gui:containers/<id>/slot/<slot>/event
