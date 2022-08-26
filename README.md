# 💻 My system setup

## ⁉ What is this?
This is how I set up my system.

I use the [`winget`](https://docs.microsoft.com/en-us/windows/package-manager/winget/) and [`choco`](https://chocolatey.org/) package managers. I use [VS Code](https://code.visualstudio.com/) as my preferred code editor.

I install several Python versions and manage them by using [Python Launcher](https://peps.python.org/pep-0397/).

## 📄 Get configuration

Install git and clone this repo:

```pwsh
winget install --id Git.Git -s winget
git clone https://github.com/mortenengen/mysetup
cd mysetup
```

## 👨‍💻 Basic apps and terminal experience
Install basic apps using winget:

```pwsh
winget import basicwingetapps.json
```

Install font for oh-my-posh:

```pwsh
sudo oh-my-posh font install meslo
```

Open Windows Terminal and edit `settings.json` by pressing `ctrl+shift+,`. Add `profiles.defaults.font.face: "MesloLGM NF"`. Restart terminal.

Edit the profile script:

```
code $PROFILE
```

Add the following line

```pwsh
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\nu4a.omp.json" | Invoke-Expression
```

Reload the profile script:
```pwsh
. $PROFILE
```

## 🐍 Other apps
Install other apps from `winget`:

```pwsh
sudo winget import wingetapps.json
```

Install chocolatey:

```pwsh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Install packages from chocolatey:

```pwsh
choco install chocopackages.config
```

## 👀 VS Code
Install VS Code Extensions:

```pwsh
foreach($line in get-content vscodeextensions.txt) {code --install-extension $($line)}
```

Open VS Code and select the preferred color theme by pressing `ctrl+k ctrl+t`.

Install VS Code Extension Manager

```pwsh
npm install -g vsce
```
