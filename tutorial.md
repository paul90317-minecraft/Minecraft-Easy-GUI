# Tutorial
This part, we look into the code. Take [backpack.yaml](/example/backpack.yaml) for example. 
## Apperence
```yaml
id: backpack
type: drop
block: minecraft:barrel
item:
  id: minecraft:leather_chestplate
  tag: 
    display:
      Name: {text: Backpack, italic: false}
    Unbreakable: true
    HideFlags: 127
    AttributeModifiers: []
    CustomModelData: 54621503
```
* `id` is for tikc mcfunction to recongnize what GUI block it is.
* `type` is `drop` or `spawn_egg`. `drop` means that it summon GUI item when you drop the block on the ground; `spawn_egg` means the item is a spawn_egg.
* `item` is the item of the GUI block, it's in Minecraft item NBT format. The item also show at the buttom of the GUI block when it turn into the GUI block. You can make texture of it by adding `CustomModelData` tag.
## Events
```yaml
load: 'say load'
destroy: 'say destroy'
tick: 'say tick'
```
* `load` is run when the GUI block is spawn and the item (or area cloud effect if the type is `spawn_egg`) haven't be killed, it run by the item. The GUI block have a block (barrel in this example) and an entity (always item_frame). The entity have a tag called `egset`, you can use it to do the data load, for example, you can copy the display name of the item to the custom name of the entity by `/data` command.
    ```yaml
    load: 'data modify entity @e[tag=egset,limit=1] CustomName set from entity @s Item.tag.display.Name'
    ``` 
    If you want load the data of the block use `block ~ ~ ~` to locate the target.
    ```yaml
    load: 'data modify block ~ ~ ~ CustomName set from entity @s Item.tag.display.Name'
    ``` 
* `destroy` is run when the item_frame is summon and the GUI block is haven't be killed. The drop also have a tag `egset`, you can use `entity @e[tag=egset,type=ite,sort=nearest,limit=1]` to locate it. You can use `block ~ ~ ~` to locate the block.
* `tick` is run by the item_frame every tick.
## Slot Behavior
```yaml
slot:
  0..8,18..25:
    type: label
    item:
      id: minecraft:black_stained_glass_pane
  26:
    type: label
    item:
      id: barrier
      tag:
        display:
            Name: {text: Close, color: red, italic: false}
    click: 'say click'
  9..17:
    type: drop
    cond: if
    data: 'eg'
```
`slot` let you design the behavor of each slot. The key `0..8,18..25` means the slot 0~8 and 18~25 have the same behavior.  
The behavor have 3 type, `drop`, `label`, `n_left`
### drop
Drop behavior have 4 condition, `always`, `never`, `if`, `unless`.
* `always` means it always drop the item in that slot.
* `never` means it never drop, you can see it as do nothing.
* `if` means if it meet the specific condition, it drops, for example
    ```yaml
    9..17:
        type: drop
        cond: if
        data: 'display'
    ```
    The item drop if it has `display` tag, it may be the dyed item, renamed item ... 
    ```yaml
    9..17:
        type: drop
        cond: if
        tag: {CustomModelData: 54621503}
    ```
    The item drop if its `CustomModelData` value is 54621503.
* `unless` means unless it meet the specific condition, it drops.
### label
It will show a label in the slot.
```yaml
type: label
item:
    id: barrier
    tag:
        display:
            Name: {text: Close, color: red, italic: false}
click: 'say close'
```
`item` is in NBT Format. `click` is a function, it runs by the item_frame when the label is clicked.
### n_left
```yaml
10:
    type: n_left
    n: 1
```
The item count in the slot can't exceed `n`, or it will drop the extra item.

