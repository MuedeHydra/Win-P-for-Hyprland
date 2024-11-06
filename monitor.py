#!/usr/bin/env python3

import os

launcher: str = "tofi"  # or "wofi -i --dmenu"


class Monitors():
    def __init__(self, name) -> None:
        self.name = name
        # print(f"from class {name}")

    def init_monitors(self, conf_list: list) -> None:
        # conf_list: list = conf.split("\n")
        # print(conf_list)

        if (conf_list[len(conf_list)-3]).strip("\t") == "disabled: true":
            self.disabled = True
        else:
            self.disabled = False

        resulution: str = conf_list[-1].split(" ")[1][:-3]
        self.resulution = resulution
        # print(resulution)


def format_selection(selection):
    string: str = ""
    for i in selection:
        string += i
        string += "\n"
    string = string.strip("\n")
    return string


def mirror_selection(mirror) -> str:
    monitors_menu.remove(mirror)
    if len(monitors_menu) == 1:
        return monitors_menu[0]
    else:
        comand: str = f"echo -e '{format_selection(monitors_menu)}' | {launcher}"
        mirror_screen = os.popen(comand).read().strip("\n")
        return mirror_screen


def position(monitor, pos) -> str:
    if pos == "right" or pos == "down":
        monitor = "eDP-1"
    resulution = monitors[monitor].resulution
    li = resulution.split("x")
    li[1] = li[1].split("@")[0]
    high = li[1]
    wide = li[0]

    if pos == "top":
        return f"0x-{high}"
    elif pos == "left":
        return f"-{wide}x0"
    elif pos == "down":
        return f"0x{high}"
    elif pos == "right":
        return f"{wide}x0"
    else:
        return "0x0"


if __name__ == '__main__':
    # read conf
    conf = os.popen("hyprctl monitors all").read().strip("\n").split("\n\n")

    # init
    monitors = {}
    for i in conf:
        i = i.split("\n")
        il = i[0].split(" ")
        monitors[il[1]] = Monitors(il[1])
        monitors[il[1]].init_monitors(i)

    monitors_menu = []
    for i in monitors:
        monitors_menu.append(i)

    comand: str = f"echo -e '{format_selection(monitors)}' | {launcher}"
    monitorinput = os.popen(comand).read().strip("\n")

    if monitorinput == "":
        exit(1)

    # print(monitors[monitorinput].resulution)

    action: list = ["expand right", "expand left", "expand bottom", "expand top", "expand center", "mirror"]
    if not monitors[monitorinput].disabled:
        action.append("off")

    comand: str = f"echo -e '{format_selection(action)}' | {launcher}"
    actioninput = os.popen(comand).read().strip("\n")
    if actioninput == "":
        exit(1)

    if actioninput == "off":
        os.popen(f"hyprctl keyword monitor {monitorinput}, disable")
    elif actioninput == "mirror":
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, auto, 1, mirror, {mirror_selection(monitorinput)}'")
    elif actioninput == "expand right":
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, {position(monitorinput, "right")}, 1'")
    elif actioninput == "expand left":
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, {position(monitorinput, "left")}, 1'")
    elif actioninput == "expand bottom":
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, {position(monitorinput, "down")}, 1'")
    elif actioninput == "expand top":
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, {position(monitorinput, "top")}, 1'")
    else:  # center
        os.popen(f"hyprctl keyword monitor '{monitorinput}, {monitors[monitorinput].resulution}, 0x0'")
