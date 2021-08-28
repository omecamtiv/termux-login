#!/bin/sh

rm $HOME/.zprofile

if [ -f $HOME/.zprofile.bak ]
then
    mv $HOME/.zprofile.bak $HOME/.zprofile
fi

if [ -f $PREFIX/bin/auth ]
then
    rm $PREFIX/bin/auth
fi

if [ -f $PREFIX/etc/passwd ]
then
    rm $PREFIX/etc/passwd
fi

echo "[*] Uninstalled Successfully."
