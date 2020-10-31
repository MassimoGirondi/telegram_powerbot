# Telegram powerbot

A Telegram bot to manage the power cycle of a remote server.

## Use scenario

- You are away from your home and want to access to the files on your server or on your computer
- Damn! The computer is turned off.
- Send `\wake` to the bot, running on a cheap Raspberry Pi (-like) board and turn on the computer

## Installation
- Clone the repository
- Configure the settings in `config.py`
- Change `run.sh` to respect your path
- Add `@reboot path/run.sh` to your crontab
- Enjoy

# Prerequsites

- The server must support Wake On Lan and it has to be enabled in the BIOS
- The `ssh` should be set to run without password (set the public key in the server).
- The user on the remote server needs to be in the `sudoers` and have the permissions to run the sudo commands without password.

## User restrictions

You may not want to give anyone the possibility to turn on your server.
Set your telegram ID in the configuration to limit which users can run commands.

## License

This software is distributed under the GNU GPL v3 license. See LICENSE.

(C) 2020 Massimo Girondi
