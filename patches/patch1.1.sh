#!/bin/sh

CURR_VER=1.0
PATCH_VER=1.1

echo "[Update] Patch Version ${PATCH_VER}\n"

ver=$(auth -v | grep -o -E '[0-9]\.[0-9]')

if [ $1 = "-u" ]
then
    if [ $ver = "${CURR_VER}" ]
    then
        patch $PREFIX/bin/auth ./.patchfiles/auth${PATCH_VER}.patch
    else
        echo "[!] Update Failed."
        echo "[!] Patch not compatible with current version."
        echo "[*] Update with appropriate patch."
    fi
elif [ $1 = "-r" ]
then
    if [ $ver = "${PATCH_VER}" ]
    then
        echo "[!] Reverting to previous version."
        patch -R $PREFIX/bin/auth ./.patchfiles/auth${PATCH_VER}.patch
    else
        echo "[!] Error. Failed to revert to previous version."
    fi
else
    echo "[!] Wrong argument."
    echo "[*] -u : update to next version."
    echo "[*] -r : revert to previous version."
fi
