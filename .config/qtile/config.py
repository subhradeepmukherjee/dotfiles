import os
import re
import socket
import subprocess
import psutil
from libqtile import hook
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget.image import Image




#Variables

mod = "mod4"
terminal = guess_terminal("alacritty")
browser = "firefox"
dmenu = "dmenu_run"
rofi_drun = "rofi -show drun"
rofi_window = "rofi -show run"
thunar = "thunar"




#KEYBINDINGS

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),





    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    




    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    



    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),



    # Launch Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    


    # Launch Browser
    Key([mod, "shift"], "b", lazy.spawn(browser), desc = "Launch browser"),


    # Launch Dmenu
     Key([mod], "d", lazy.spawn(dmenu), desc = "Launch Dmenu"),


    #Lauch rofi drun
     Key([mod], "m", lazy.spawn(rofi_drun), desc = "Launch Rofi drun"),



    #Launch rofi window_run
     Key([mod, "shift"], "m", lazy.spawn(rofi_window), desc = "Launch Rofi window run"),
    

    #Launch Thunar
    Key([mod, "shift"], "t", lazy.spawn(thunar), desc = "Launch Thunar file manager"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

]



# GROUPS

groups = []

group_names = ["1", "2", "3", "4", "5",]
group_labels = ["Code</>", "WWW", "Term ", "BSP", "MAX"]
group_layouts = ["monadtall", "monadtall", "monadtall", "bsp", "max"]


for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

    for i in groups:
       keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


#Layout

#layout_monadtall
layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "#ff0000",
    "border_normal": "#00ff00",
}

#layout_max
layout_theme_max = {
    "border_width": 3,
    "margin": 5,
    "border_focus": "#ffd7ff",
    "border_normal": "0f111b",
}


#layout bsp
layout_theme_bsp = {
    "border_width": 3,
    "margin": 8,
    "border_on_single": False,
    "border_normal": "#afff00",
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_theme_max),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme_bsp),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# COLORS FOR THE BAR
colors = [
    ["#ecf0c1", "#ecf0c1"],  # ACTIVE WORKSPACES 0
    ["#686f9a", "#686f9a"],  # INACTIVE WORKSPACES 1
    ["#16172d", "#16172d"],  # background lighter 2
    ["#e33400", "#e33400"],  # red 3
    ["#5ccc96", "#5ccc96"],  # green 4
    ["#b3a1e6", "#b3a1e6"],  # yellow 5
    ["#00a3cc", "#00a3cc"],  # blue 6
    ["#f2ce00", "#f2ce00"],  # magenta 7
    ["#7a5ccc", "#7a5ccc"],  # cyan 8
    ["#686f9a", "#686f9a"],  # white 9
    ["#f0f1ce", "#f0f1ce"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#1b1c36", "#1b1c36"],  # super cyan12
    ["#0f111b", "#0f111b"],  # super blue 13
    ["#0e131a", "#0e131a"],  # super dark background 14
]


widget_defaults = dict(
    font="UbuntuMono Nerd 14",
    fontsize=17,
    padding=4,
    background = colors[14]

)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 3,
                    padding = 1,
                    foreground = colors[12],
                    background = colors[12]
                    ),
                
                widget.Image(
                    filename = '~/.config/qtile/icons/python.png',
                    scale = 'False',
                    margin_x = 8,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(dmenu)}
                    ),


                widget.GroupBox(
                     padding = 5,
                     borderwidth = 3,
                     active = colors[4],
                     inactive = colors[3],
                     disable_drag = True,
                     rounded = True,
                     margin_y = 3,
                     margin_x = 2,
                     padding_y = 5,
                     padding_x = 4,
                    #hide_unused" = True,
                     highlight_color = colors[1],
                     highlight_method = "block",
                     this_current_screen_border = colors[1],
                     this_screen_border = colors [1],
                     other_current_screen_border = colors[2],
                     other_screen_border = colors[2],
                     foreground = colors[8],
                     background = colors[12],
                    ),


                widget.Prompt(),
                widget.WindowName(),

               

                widget.Memory(
                    background = "#00af00",
                    ),

                widget.Sep(
                        linewidth = 3,
                        padding = 4,
                        size_percent = 100,
                        #foreground = colors[12],
                        background = "#ffffff",
                        ),
                

                widget.Net(
                    background = colors[8],
                    interface = 'enp0s3',
                    ),

                widget.Sep(
                        linewidth = 3,
                        padding = 4,
                        size_percent = 100,
                        #foreground = colors[9],
                        background = "#ffffff",
                        ),
                

                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                
                

                widget.Clock(
                    background = colors[6],
                    format="%d-%m-%Y %a %I:%M %p",
                     ),


                widget.Sep(
                        linewidth = 3,
                        padding = 4,
                        size_percent = 100,
                        #foreground = colors[12],
                        background = "#ffffff",
                        ),

                

                widget.QuickExit(
                    background = colors[3],
                    default_text = '[Log/Shut]',
                    countdown_format='[{}]',
                    ),

               
                
               
            ],
            34,
            margin=[0, 0, 2, 0],
            opacity= 1.0,
            
        ),

        bottom=bar.Gap(3),
        left=bar.Gap(5),
        right=bar.Gap(5),
        




        #Wallpaper
        wallpaper="/home/notoriousdev/.config/qtile/wall/qtilebest.jpg",
        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
