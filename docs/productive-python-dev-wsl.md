# A Productive Python development environment on Windows

## System Requirements for WSL2

- Windows 10, version 2004. [See which version of Windows 10 you have.](https://support.microsoft.com/en-us/windows/see-which-version-of-windows-10-you-have-12d35019-4da9-0cb1-ba47-f8b031b712ad)
- A CPU that supports [Hyper-V](https://en.wikipedia.org/wiki/Hyper-V).

## Enable WSL

1. Find **Windows Powershell** in the start menu. Right click and Run As Administrator
2. Run the following commands one by one to enable necessary Windows features.
   ```pwsh
   Enable-WindowsOptionalFeature -Online -FeatureName:Microsoft-Hyper-V -All
   Enable-WindowsOptionalFeature -Online -FeatureName:VirtualMachinePlatform
   Enable-WindowsOptionalFeature -Online -FeatureName:Microsoft-Windows-Subsystem-Linux
   ```
   > :bulb: Any errors you encounter might mean that your system does not meet the system requirements for WSL2.
3. Restart Windows for the changes to take effect


**Make WSL2 the default version of WSL**
1. Open the Command Prompt from the start menu.
2. Run the following:
   ```
   wsl --set-default-version 2
   ```

## Download a distro for WSL
1. Download [Ubuntu from the Microsoft Store](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab) or another distro of your choice
2. After the download is complete, open WSL Terminal from the start menu
3. You will be asked to set a username and a password for your linux user. Keep the username simple (e.g. `dmarakom`) and DO NOT forget your password.

## Install the new Windows Terminal
1. Download [Windows Terminal from the Microsoft Store](https://aka.ms/terminal)
2. (Optional) Pin the Windows Terminal to your taskbar for quick access

#### Configure terminal tabs to default to Ubuntu
1. Open the **Windows Terminal**.
2. Press `Ctrl + ,` to open the terminal's `settings.json` file.
3. Find the guid value of the "Ubuntu" profile (around line 49, e.g. `{2c4de342-38b7-51cf-b940-2309a097f518}`) and copy it to clipboard.
4. Find the *defaultProfile* setting (around line 11), and paste the value from step 2, replacing the current value.
   > :bulb:  Pay attention to not mess up the syntax of the `settings.json` file. [Learn more about JSON files](https://learnxinyminutes.com/docs/json/).
5. Save and close `settings.json`

**Windows Terminal Tips**
- Feel free to play around with the other settings. For instance, you might want to change *copyOnSelect* to true.
- Like Visual Studio Code, the Windows Terminal employs a command palette that you can open with `Ctrl + Shift + P`

#### Configure the terminal to start at your linux home directory
By default the starting directory for your linux terminal is your windows home directory (e.g. `C:\Users\dmarakom`). This can be confusing if you are used to having `~` as your starting directory. Here is how to configure Windows Terminal so that the starting directory matches `~`.

1. Open **Windows Terminal**. On the Ubuntu shell, type the following:
   ```
   explorer.exe ~
   ```
2. A **Windows Explorer** window will open, displaying the files from your Ubuntu home directory. Press `Ctrl + L`, then `Ctrl + C` to copy the directory path to clipboard. The path will look something like this: `\\wsl$\Ubuntu\home\dmarakom`
3. Go back to the **Windows Terminal** window. Press `Ctrl + ,` to open the `settings.json` file.
4. In the list of profiles, find the profile named "Ubuntu". Add a `startingDirectory` setting to the "Ubuntu" profile as shown below. Paste the directory path from step 2 as the value.
    ```jsonc
    {
        "guid": "{2c4de342-38b7-51cf-b940-2309a097f518}",
        "hidden": false,
        "name": "Ubuntu",
        "startingDirectory": "//wsl$/Ubuntu/home/dmarakom",   // Add this line. Make sure it ends with a comma.
        "source": "Windows.Terminal.Wsl"
    }
    ```
   - You must replace backslashes (`\`) with forward slashes (`/`) in the `startingDirectory` path, like this:
        |||
        |--------|-------------------------------|
        | Before | `\\wsl$\Ubuntu\home\dmarakom` |
        | After  | `//wsl$/Ubuntu/home/dmarakom` |



5. Save and close `settings.json`.
6. Verify that the change works by opening a new terminal tab and checking that the working directory matches `~`

## Set up an ergonomic linux environment

- [ ] [Enable passwordless sudo for your user](https://phpraxis.wordpress.com/2016/09/27/enable-sudo-without-password-in-ubuntudebian/) (Optional)
- [ ] Update your packages and install the bare necessities
    ```
    sudo apt update
    sudo apt -y upgrade
    sudo apt -y install autojump build-essential curl git htop make unzip wget
    ```
- [ ] Configure git
    ```
    # Name and email used in your commits
    git config --global user.name "Dimitris Marakomihelakis"
    git config --global user.email dmarakom@gmail.com

    # A couple of recommended settings
    git config --global core.editor nano
    git config --global core.autocrlf input
    git config --global push.default current
    ```
- [ ] [Add an SSH key for your GitHub account](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html)
    1. Generate a public-private key pair and save it under ~/.ssh/
        ```
        ssh-keygen -f ~/.ssh/github -t rsa -N ""
        ```
    2. Copy public key to the windows clipboard
        ```
        clip.exe < ~/.ssh/github.pub
        ```
    3. Add the key on [your GitHub account settings](https://github.com/settings/ssh/new)
        - **Title:** My Ubuntu WSL key
        - **Key**: Press `Ctrl + V` to paste your key
- [ ] [Replace bash with zsh](https://www.addictivetips.com/ubuntu-linux-tips/switch-from-bash-to-zsh-on-linux/)
    1. Install zsh and set it as the default shell
        ```
        sudo apt install -y zsh zsh-doc
        chsh -s $(which zsh)
        ```
    2. Install ohmyzsh
        ```
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
        ```
        > :bulb: If you get a "Could not resolve host" error message for curl, it is probably caused by [this WSL2 issue](https://github.com/microsoft/WSL/issues/4285).
        > Run the following commands to work around the issue.
        > ```
        > sudo -s tee /etc/wsl.conf <<EOT
        > [network]
        > generateResolvConf = false
        > EOT
        >
        > test -f /etc/resolv.conf && sudo rm /etc/resolv.conf
        >
        > sudo -s tee /etc/resolv.conf <<EOT
        > nameserver 1.1.1.1
        > EOT
        > ```
    3. Edit `.zshrc` to activate a decent theme and set of plugins
        ```
        sed -i ~/.zshrc -e 's/ZSH_THEME=.*/ZSH_THEME="geoffgarside"/'
        sed -i ~/.zshrc -e 's/plugins=.*/plugins=(zsh-navigation-tools safe-paste autojump pyenv)/'
        ```

## Install and manage Python versions with pyenv

1. Install build dependencies for python
   ```
   sudo apt -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
   ```
2. Install pyenv. This step assumes that you have replaced bash with zsh as described above
    ```
    curl https://pyenv.run | zsh
    exec $SHELL
    ```
   > Pyenv should already be activated because we enabled the pyenv zsh plugin in a previous step
3. Install python 2 and 3 through pyenv -- and set python3 as the default
    ```
    pyenv install 2.7.18
    pyenv install 3.8.6 && pyenv global 3.8.6
    ```

## Start hacking

Download and install [Visual Studio Code](https://code.visualstudio.com/) on Windows.

Create a directory for your projects on the linux side. I recommend a directory with a short memorable path, such as `~/src`.
```
mkdir -p "~/src"
cd $_
```

Now clone a python project into your project directory and open it in VSCode. The Remote-WSL extension will activate in VSCode and you can edit your code and use the terminal as if VSCode was running on the linux side.

```
git clone git@github.com:dmarakom6/eratosthenis_sieve.git
code ./eratosthenis_sieve
```

**Recommended VSCode extensions**

Python specific:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Debugger and external tooling support
- [MagicPython](https://marketplace.visualstudio.com/items?itemName=magicstack.MagicPython): Improved syntax highlighting
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance): Improved intellisense for python codebases
  - Newer alternative to [Visual Studio Intellisense](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent): Smarter cursor placement when you press enter
- [PyInit](https://marketplace.visualstudio.com/items?itemName=DiogoNolasco.pyinit): Convenient command to generate `__init__.py` for modules

General purpose:
- [Terminal](https://marketplace.visualstudio.com/items?itemName=formulahendry.terminal): Toggle integrated terminal with a status bar button
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare): Pair programming over the internet
- Theme: [Alloy Theme](https://marketplace.visualstudio.com/items?itemName=officerhalf.alloy-theme)
- Icon Theme: [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
