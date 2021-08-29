# Termux Login Utility

This program enables a login feature on starting Termux app.  
The credentials provided are hashed using `bcrypt` and stored in a file as user password pair.  
Currently `zsh` shell is supported.  

### How to install

```zsh
# Clone the repo...
git clone https://github.com/omecamtiv/termux-login.git

# Open termux-login folder...
cd termux-login

# Run install.sh
sh ./install.sh
```

### How to uninstall
```zsh
# Run uninstall.sh from termux-login folder...
cd termux-login
sh ./uninstall.sh
```

### FAQs
1. **How to change credentials?**  
Just run `auth -p` to change credentials.

2. **I forgot password, now I can't open Termux. What to do?**  
This is a serious problem. You have to launch Termux in Failsafe mode and delete the `passwd` file inside `etc` folder. After that restart Termux in normal mode.
3. How to update Termux Login Utility?  
Refer to [Updating Termux Login Utility](./UPDATING.md).  
