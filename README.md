# YOU CLI tool

Simple tool to get help right in linux shell with YouChat bot.

## Installation

### Install the tool

```bash
$> pip3 install -r requirements.txt
$> sudo ln -s $pwd/main.py /usr/local/bin/howto 
``` 

### Set an API key

Get the key on [betterAPI](https://api.betterapi.net/) for YouChat
```bash
$> mkdir -p ~/.config/you
$> echo {YOUR_KEY} > ~/.config/you/betterapi
```

### Test it

```bash
$> howto get last n lines of the file 
```