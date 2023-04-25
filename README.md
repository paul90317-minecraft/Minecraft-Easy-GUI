# Easy GUI

## Environment
This repos only use the package `pyyaml`, see `requirements.txt`
```bat
pip install pyyaml
```
### execute
Download release file to run (recommended for user)
```
python ./easy_GUI.zip ./your_container_settings.yaml
```
Or you can just run under this repos (recommended for developer)
```
python ./easy_GUI/ ./your_container_settings.yaml
```
It create `pack.mcmeta` and `data` in root automatically
## Examples
Here are some examples setting files, it's easy to understand.
* drop to summon GUI block (type = `drop`)  
[backpack.yaml](/example/backpack.yaml)  
* spawn egg to summon GUI block (type = `spawn_egg`)  
[scribing_table.yaml](/example/scribing_table.yaml)  
[working_table.yaml](/example/working_table.yaml)  
## Tutorual
[tutorial.md](/tutorial.md)
## License
You can use this tool to generate your datapack.  
You can fork this repos and modify the tool to your version.  
You can do antything with it.  
Credit on me if you use this tool. (let your user know I make this and let more people know the tool).

## Works on PMC
* [upgradable backpack](https://www.planetminecraft.com/data-pack/backpack-1-18-2/)
* [custom craft](https://www.planetminecraft.com/data-pack/better-anvil/)