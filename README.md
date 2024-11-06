# Win + P for Hyprland

This is a short Python script to control your monitors.

### Installation
Download the python file and make it executable: `sudo chmod +x <you path>/monitor.py`.
Add a bind to your `hyprland.conf` file.

for example:
```
$mainMod = SUPER
bind = $mainMod, P, exec, ~/.config/hypr/tools/monitor.py
```
## App launcher
The default launcher for the script is `tofi`, if you are using wofi or another launcher you can change the following line:
```py
# wofi example
launcher: str = "wofi -i --dmenu"
```

### Screenshots
![monitor_selection](img/monitor_selection.png)

![monitor_operation](img/monitor_operation.png)
