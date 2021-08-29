# Updating Termux Login Utility

Updating **Termux Login Utility** is pretty straight forward.  
The patches are present in `./patches` folder. 
Patches should be applied in sequential manner.  

### Detailed steps to update:
1. First `git pull` the updated repo from within `termux-login` folder.  
2. Run the appropriate patch script inside `./patches` folder.  
```zsh
sh ./patch<version-no>.sh -u
```
3. To revert the patch run the same script with `-r` argument instead of `-u`.
