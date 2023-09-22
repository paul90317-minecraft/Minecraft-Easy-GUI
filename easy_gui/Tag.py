
def parse_list_to_str(data:list)->str:
    if len(data)==0:
        return '[]'
    ret='['
    for item in data:
        if isinstance(item,list):
            ret+=parse_list_to_str(item)+','
        elif isinstance(item,dict):
            ret+=parse_dict_to_str(item)+','
        elif isinstance(item,str):
            ret+=f'"{item}",'
        elif isinstance(item,bool):
            ret+=f"{str(item).lower()},"
        else:
            ret+=item+','
    return ret[:-1]+']'

def parse_dict_to_str(data:dict)->str:
    if len(data)==0:
        return '{}'
    ret='{'
    for k,v in data.items():
        if isinstance(v,list):
            ret+=f"'{k}':{parse_list_to_str(v)},"
        elif isinstance(v,dict):
            ret+=f"'{k}':{parse_dict_to_str(v)},"
        elif isinstance(v,str):
            ret+=f"'{k}':'{v}',"
        elif isinstance(v,bool):
            ret+=f"'{k}':{str(v).lower()},"
        else:
            ret+=f"'{k}':{v},"
    return ret[:-1]+'}'

def parse(data:dict)->str:
    """
    {a:'1',b:2,c:False} -> 'a':'1','b':'2','c':false
    """
    ret=''
    for k,v in data.items():
        if isinstance(v,list):
            ret+=f",'{k}':{parse_list_to_str(v)}"
        elif isinstance(v,dict):
            ret+=f",'{k}':{parse_dict_to_str(v)}"
        elif isinstance(v,str):
            ret+=f",'{k}':'{v}'"
        elif isinstance(v,bool):
            ret+=f",'{k}':{str(v).lower()}"
        else:
            ret+=f",'{k}':{v}"
    return ret[1:]