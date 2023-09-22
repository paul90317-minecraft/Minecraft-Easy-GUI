def parse_jsontext(data:dict|str)->str:
    if isinstance(data,str):
        return data
    if len(data)==0:
        return '{"text":""}'
    ret='{'
    for k,v in data.items():
        if isinstance(v,str):
            ret+=f'"{k}":"{v}",'
        elif isinstance(v,bool):
            ret+=f'"{k}":{str(v).lower()},'
        else:
            ret+=f'"{k}":{v},'
    return ret[:-1]+'}'

def parse_lore(lore:list)->list[str]:
    ret=[]
    for item in lore:
        ret.append(parse_jsontext(item)+',')
    return ret

def parse(data:dict) -> None:
    """
    {Name:{...},Lore:[{...},...]} --> {Name:'{...}',Lore:['{...}',...]}
    """
    if 'Name' in data:
        data['Name']=parse_jsontext(data['Name'])
    else:
        data['Name']='{"text":""}'       
    data["Lore"]= parse_lore(data.get('Lore',[]))
