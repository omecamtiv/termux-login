#!/bin/sh

# Installing dependencies. 

pkg install python -y
pip install bcrypt

# Copying necessary scripts.

cp ./script.py $PREFIX/bin/auth

chmod +x $PREFIX/bin/auth

# Configuring zsh shell for script.
if [ -f $HOME/.zprofile ]
then
    cp $HOME/.zprofile $HOME/.zprofile.bak
fi

echo "auth" >> $HOME/.zprofile

echo "[*] Successfully Install."
echo "[*] Restart Termux."
