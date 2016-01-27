#!/usr/bin/env sh
if [[ "${USER}" == "root" ]]; then
    echo "Do not install as superuser!"
    exit 1
fi

pip3 install --user -r requirements.txt

EXEC=i3-swipe.py
UNIT=i3-swipe.service

# smart detecting user path
DESTDIR=${DESTDIR:-$(echo $PATH | tr ':' '\n' | grep -F "$HOME" | head -1)}
cp -v $EXEC $DESTDIR/$EXEC

if [[ "$(basename $(readlink $(which init)))" == "systemd" ]]; then
    XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-$HOME/.config}
    sed "s|/path/to|$DESTDIR|" $UNIT | tee $XDG_CONFIG_HOME/systemd/user/$UNIT
fi
