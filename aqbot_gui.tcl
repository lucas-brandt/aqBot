#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 800x600+1038+241
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3188 1743
    wm minsize $top 232 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "aqBot"
    vTcl:DefineAlias "$top" "main" vTcl:Toplevel:WidgetProc "" 1
    message $top.mes38 \
        -background {#d9d9d9} -font $::vTcl(fonts,vTcl:font9,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {aqBot v1.0} -width 378 
    vTcl:DefineAlias "$top.mes38" "title" vTcl:WidgetProc "main" 1
    button $top.but39 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Open Adventure Quest} 
    vTcl:DefineAlias "$top.but39" "openAQ" vTcl:WidgetProc "main" 1
    button $top.but40 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Open Adventure Quest (G)} 
    vTcl:DefineAlias "$top.but40" "openAQG" vTcl:WidgetProc "main" 1
    message $top.mes41 \
        -background {#d9d9d9} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text {Stat Modification} -width 225 
    vTcl:DefineAlias "$top.mes41" "stats" vTcl:WidgetProc "main" 1
    message $top.cpd42 \
        -background {#d9d9d9} -font $::vTcl(fonts,vTcl:font10,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -text Automation -width 225 
    vTcl:DefineAlias "$top.cpd42" "auto" vTcl:WidgetProc "main" 1
    button $top.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Kill Opponent} 
    vTcl:DefineAlias "$top.but44" "kill" vTcl:WidgetProc "main" 1
    button $top.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Infinite HP/SP/MP} 
    vTcl:DefineAlias "$top.but45" "infinite" vTcl:WidgetProc "main" 1
    button $top.but46 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Refill MP} 
    vTcl:DefineAlias "$top.but46" "refillMP" vTcl:WidgetProc "main" 1
    button $top.but47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Refill SP} 
    vTcl:DefineAlias "$top.but47" "refillSP" vTcl:WidgetProc "main" 1
    button $top.but48 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Refill HP} 
    vTcl:DefineAlias "$top.but48" "refillHP" vTcl:WidgetProc "main" 1
    button $top.but49 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Set Heath to 0} 
    vTcl:DefineAlias "$top.but49" "setZero" vTcl:WidgetProc "main" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.mes38 \
        -in $top -x 210 -y -100 -width 378 -relwidth 0 -height 272 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but39 \
        -in $top -x 60 -y 110 -width 300 -anchor nw -bordermode ignore 
    place $top.but40 \
        -in $top -x 460 -y 110 -width 300 -anchor nw -bordermode ignore 
    place $top.mes41 \
        -in $top -x 100 -y 200 -width 225 -relwidth 0 -height 110 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.cpd42 \
        -in $top -x 500 -y 200 -width 225 -height 110 -anchor nw \
        -bordermode inside 
    place $top.but44 \
        -in $top -x 510 -y 300 -width 210 -anchor nw -bordermode ignore 
    place $top.but45 \
        -in $top -x 510 -y 380 -width 210 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 130 -y 300 -width 170 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 130 -y 380 -width 170 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 130 -y 460 -width 170 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 130 -y 540 -width 170 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top37
