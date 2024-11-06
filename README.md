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

### Sccrenshots
<img scr="img/monitor_selection.png" alt="monitor_selection">

<img scr="img/monitor_operation.png" alt="monitor_operation">
