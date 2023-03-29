import yaml
from yaml.loader import SafeLoader
import sys
import os
import json
from os import path

def template(code: str, pattern:dict[str,int|str])->str:
    for k,v in pattern.items():
        code =code.replace(f'<{k}>',str(v))
    return code

def write_code(code :str, filename :str)->None:
    dirname=path.dirname(filename)
    if len(dirname)>0:
        os.makedirs(dirname,exist_ok=True)
    with open(filename,'w')as f:
        f.write(code)

def update_values(new_values:set,filename:str)->None:
    if os.path.isfile(filename):
        with open(filename,'r')as f:
            for item in json.load(f)['values']:
                new_values.add(item)
    write_code(json.dumps({
        "values":list(new_values)
    }),filename)

class Item:
    def __init__(self,data:dict) -> None:
        self.id = data['id']
        self.enchant = data.get('enchant',False)
        self.text = data.get('text','')
        self.color = data.get('color',None)

class Slot:
    LABEL_ENTRY=open(path.join(path.dirname(__file__), 'template/slot_type/label/entry.mcfunction'),'r').read()
    LABEL_EVENT=open(path.join(path.dirname(__file__), 'template/slot_type/label/event.mcfunction'),'r').read()
    N_LEFT_ENTRY=open(path.join(path.dirname(__file__), 'template/slot_type/n_left/entry.mcfunction'),'r').read()
    N_LEFT_EVENT=open(path.join(path.dirname(__file__), 'template/slot_type/n_left/event.mcfunction'),'r').read()
    LABEL_ITEMS={'cookie'}
    @staticmethod
    def codeGen(containerId:str,slot:int,object:dict)->tuple[str,str]:
        slotType=object['type']
        if slotType == 'label':
            item = Item(object['item'])
            click = object.get('click','')
            Slot.LABEL_ITEMS.add(item.id)
            return (
                template(Slot.LABEL_ENTRY,{
                    'slot':slot,
                    'id':containerId
                }),
                template(Slot.LABEL_EVENT,{
                    'slot':slot,
                    'item':item.id,
                    'text':item.text,
                    'color':f',"color":"{item.color}"' if item.color is not None else '',
                    'enchant':',Enchantments:[{id:"minecraft:binding_curse",lvl:1}]' if item.enchant else '',
                    'click':click
                })
            )
        elif slotType == 'n_left':
            n :int = object['n']
            return (
                template(Slot.N_LEFT_ENTRY,{
                    'slot':slot,
                    'id':containerId,
                    'n_add_one':n+1
                }),
                template(Slot.N_LEFT_EVENT,{
                    'slot':slot,
                    'n':n
                })
            )
        else:
            exit(f'error: unknown slot type {slotType}')
            
        

with open(sys.argv[1],'r') as f:
    data:dict = yaml.load(f, Loader=SafeLoader)

containerId=data['id']
entries=''
for slot,object in data['slot'].items():
    entry,event=Slot.codeGen(containerId,slot,object)
    write_code(event,f'data/easy_gui/functions/containers/{containerId}/slot/{slot}/event.mcfunction')
    entries+=entry
container_block=Item(data['entity']['block'])
write_code(template(open(path.join(path.dirname(__file__),'template/tile/tick.mcfunction')).read(),{
    "id":containerId,
    "block":container_block.id
})+entries,
f'data/easy_gui/functions/containers/{containerId}/tick.mcfunction')

write_code(template(open(path.join(path.dirname(__file__),'template/tile/destroy.mcfunction')).read(),{
    "id":containerId,
    "block":container_block.id
}),
f'data/easy_gui/functions/containers/{containerId}/destroy.mcfunction')

write_code(template(open(path.join(path.dirname(__file__),'template/tile/search/item_frame.mcfunction')).read(),{
    "id":containerId
}),
f'data/easy_gui/functions/containers/{containerId}/search/item_frame.mcfunction')

write_code(template(open(path.join(path.dirname(__file__),'template/tile/search/area_effect_cloud.mcfunction')).read(),{
    "id":containerId
}),
f'data/easy_gui/functions/containers/{containerId}/search/area_effect_cloud.mcfunction')

write_code(template(open(path.join(path.dirname(__file__),'template/tile/try_spawn/cancel.mcfunction')).read(),{
    "id":containerId
}),
f'data/easy_gui/functions/containers/{containerId}/try_spawn/cancel.mcfunction')

write_code(template(open(path.join(path.dirname(__file__),'template/tile/try_spawn/check.mcfunction')).read(),{
    "id":containerId
}),
f'data/easy_gui/functions/containers/{containerId}/try_spawn/check.mcfunction')

spawn_egg=Item(data['spawn_egg'])
write_code(template(open(path.join(path.dirname(__file__),'template/tile/spawn_egg.mcfunction')).read(),{
    "id":containerId,
    'spawn_egg':spawn_egg.id,
    'text':spawn_egg.text,
    'color':f',"color":"{spawn_egg.color}"' if spawn_egg.color is not None else '',
    'enchant':',Enchantments:[{id:"minecraft:binding_curse",lvl:1}]' if spawn_egg.enchant else ''
}),
f'data/easy_gui/functions/containers/{containerId}/spawn_egg.mcfunction')

container_item=Item(data['entity']['item'])
write_code(template(open(path.join(path.dirname(__file__),'template/tile/try_spawn/load.mcfunction')).read(),{
    "id":containerId,
    'item':container_item.id,
    'item_text':container_item.text,
    'item_color':f',"color":"{container_item.color}"' if container_item.color is not None else '',
    'item_enchant':',Enchantments:[{id:"minecraft:binding_curse",lvl:1}]' if container_item.enchant else '',
    'block':container_block.id,
    'block_text':container_block.text,
    'block_color':f',"color":"{container_block.color}"' if container_block.color is not None else '',
}),
f'data/easy_gui/functions/containers/{containerId}/try_spawn/load.mcfunction')

update_values(Slot.LABEL_ITEMS,
              'data/easy_gui/tags/items/label.json')

update_values({f"easy_gui:containers/{containerId}/search/item_frame"},
              'data/easy_gui/tags/functions/search/item_frame.json')

update_values({f"easy_gui:containers/{containerId}/search/area_effect_cloud"},
              'data/easy_gui/tags/functions/search/area_effect_cloud.json')

write_code(open(path.join(path.dirname(__file__),'template/game/tick.mcfunction'),'r').read(),
           'data/easy_gui/functions/tick.mcfunction')

write_code(open(path.join(path.dirname(__file__),'template/game/load.mcfunction'),'r').read(),
           'data/easy_gui/functions/load.mcfunction')

if not os.path.exists('pack.mcmeta'):
    write_code(json.dumps({
        "pack":{
            "pack_format":10,
            "description": ""
        }
    }),
    'pack.mcmeta')

update_values({"easy_gui:tick"},
              'data/minecraft/tags/functions/tick.json')

update_values({"easy_gui:load"},
              'data/minecraft/tags/functions/load.json')