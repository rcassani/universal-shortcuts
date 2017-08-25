:; # Linux part
:; ps -e | grep -E 'unity-panel'        > /dev/null && gvfs-open 'file/red_panda.avi'
:; ps -e | grep -E 'aqua'               > /dev/null && open 'file/red_panda.avi'
:; ps -e | grep -E '^.* cinnamon$'      > /dev/null && gvfs-open 'file/red_panda.avi'
:; ps -e | grep -E '^.* kded4$'         > /dev/null &&  'file/red_panda.avi'
:; ps -e | grep -E '^.* xfce4-session$' > /dev/null &&  'file/red_panda.avi'
:; ps -e | grep -E '^.* lxsession$'     > /dev/null &&  'file/red_panda.avi'
:; ps -e | grep -E '^.* mate-panel$'    > /dev/null &&  'file/red_panda.avi'
:; exit

:: # Windows part
@ECHO OFF
cd "file"
start "" "red_panda.avi"
EXIT
