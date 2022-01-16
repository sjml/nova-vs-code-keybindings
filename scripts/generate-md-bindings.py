import os
import json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

BINDINGS_FILE = os.path.join(
    "..",
    "VS Code Keybindings.novaextension",
    "KeyBindings",
    "VS Code Keybindings.json"
)

with open(BINDINGS_FILE, "r") as bf:
    bindings_data = json.load(bf)

bindings = []
for top_level_key, binding_list in bindings_data.items():
    if top_level_key != "menuItems":
        # not sure what other entries there will be, but stick with just this for now
        continue
    for binding_name, data in binding_list.items():
        if "shortcut" not in data:
            bindings.append((binding_name, "*[Removed]*"))
            continue
        shortcut = data["shortcut"]
        shortcut = shortcut.replace("cmd", "⌘")
        shortcut = shortcut.replace("shift", "⇧")
        shortcut = shortcut.replace("alt", "⌥")
        shortcut = shortcut.replace("ctrl", "⌃")
        splits = shortcut.split("-")
        splits = [s.capitalize() for s in splits]
        shortcut = "-".join(splits)
        bindings.append((binding_name, shortcut))

max_binding_name = max(len(bd[0]) for bd in bindings)
max_shortcut = max(len(bd[1]) for bd in bindings)

# accounting for formatting
max_binding_name += 4

output = ""
output += f"| {'Menu Item':<{max_binding_name}} | {'Binding':<{max_shortcut}} |\n"
output += f"|{'-'*(max_binding_name+2)}|{'-'*(max_shortcut+2)}|\n"

for bd in bindings:
    bn = f"**{bd[0]}**"
    output += f"| {bn:<{max_binding_name}} | {bd[1]:<{max_shortcut}} |\n"

print(output)
