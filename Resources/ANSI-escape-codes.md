# ANSI escape codes

- List of codes
    - [Formatting codes](#formatting-codes)
    - [Foreground colors](#foreground-text-colors)
    - [Background colors](#background-colors)
    - [Reset code](#reset-code)
- [Combinations](#combinations)
- [Tips](#tips)
- [Preview formatting in the terminal](#preview-formatting-in-the-terminal)

## Formatting Codes
- `\e[0m`  : Reset / Normal
- `\e[1m`  : Bold or increased intensity
- `\e[2m`  : Faint, decreased intensity (not widely supported)
- `\e[3m`  : Italic (not widely supported)
- `\e[4m`  : Underline
- `\e[5m`  : Slow Blink (less than 150 per minute)
- `\e[6m`  : Rapid Blink (MS-DOS ANSI.SYS; 150+ per minute)
- `\e[7m`  : Image Negative (inverse or reverse; swap foreground and background)
- `\e[8m`  : Conceal (not widely supported)
- `\e[9m`  : Crossed-out (characters legible, but marked for deletion, not widely supported)

## Foreground (Text) Colors
- `\e[30m` : Black
- `\e[31m` : Red
- `\e[32m` : Green
- `\e[33m` : Yellow
- `\e[34m` : Blue
- `\e[35m` : Magenta
- `\e[36m` : Cyan
- `\e[37m` : White
- `\e[90m` : Bright Black (Gray)
- `\e[91m` : Bright Red
- `\e[92m` : Bright Green
- `\e[93m` : Bright Yellow
- `\e[94m` : Bright Blue
- `\e[95m` : Bright Magenta
- `\e[96m` : Bright Cyan
- `\e[97m` : Bright White

## Background Colors
- `\e[40m` : Black
- `\e[41m` : Red
- `\e[42m` : Green
- `\e[43m` : Yellow
- `\e[44m` : Blue
- `\e[45m` : Magenta
- `\e[46m` : Cyan
- `\e[47m` : White
- `\e[100m` : Bright Black (Gray)
- `\e[101m` : Bright Red
- `\e[102m` : Bright Green
- `\e[103m` : Bright Yellow
- `\e[104m` : Bright Blue
- `\e[105m` : Bright Magenta
- `\e[106m` : Bright Cyan
- `\e[107m` : Bright White

## Reset Code
- `\e[0m` : Reset all attributes

## Combinations
To combine formatting and colors, you can use multiple codes separated by semicolons. For example:
- `\e[4;34m` : Underlined blue
- `\e[1;31;103m` : Bold red on yellow background

## Tips

When giving examples, I'll be giving two versions : one with the actual escape characters, and one with the escape characters replaced by tags for readability purposes.

### Reset at the end

Always reset the formatting at the end of your formatted text.  
Otherwise the formatting might continue to apply afterwards, depending on the situation.

❌ Incorrect :  
> **`<Formatting>`** _ASCII art_  
_ASCII art_  
_ASCII art_

❌ Incorrect :
> **`\e[31m`**_ASCII art_  
_ASCII art_  
_ASCII art_

✅ Correct :
> **`<Formatting>`** _ASCII art_  
_ASCII art_  
_ASCII art_ **`<Reset>`**

✅ Correct :
> **`\e[31m`**_ASCII art_  
_ASCII art_  
_ASCII art_**`\e[0m`**

### Reset between sequences

Always reset the formatting before applying another one.

❌ Incorrect :  
> **`<Red FG>`** _red text_ **`<Blue FG>`** _blue text_

> **`\e[31m`**_red text_ **`\e[34m`**_blue text_

✅ Correct :  
> **`<Red FG>`** _red text_ **`<Reset>`** **`<Blue FG>`** _blue text_**`<Reset>`**

> **`\e[31m`**_red text_**`\e[0m`** **`\e[34m`**_blue text_ **`\e[0m`**

### Use single sequences

You can't add the formatting of several sequences of escape characters. You need to put all the formatting in the same sequence of escape characters.

❌ Incorrect :  
> **`<Red FG>`** _red text_ **`<Yellow BG>`** _red text on yellow BG_ **`<Reset>`**

> **`\e[31m`**_red text_ **`\e[43m`**_red text on yellow BG_**`\e[0m`**

✅ Correct :  
> **`<Red FG>`** _red text_ **`<Reset>`** **`<Red FG Blue BG>`** _red text on blue BG_ **`<Reset>`**

> **`\e[31m`**_red text_**`\e[0m`** **`\e[31;43m`**_red text on blue BG_**`\e[0m`**

## Preview formatting in the terminal

To preview the formatted text  in your terminal, you can't just use 'echo' on the code nor `cat` on a file because everything will just be displayed as plain text, including the escape characters.

You have several options.
If you're on Windows or another system without bash, then use the python script.

### Echo

Copy the code and run :
```
echo -e "your formatted text"
```

### Printf

Save the code in a file and run :
```
printf "%b" "$(cat path-to-file)" 
```

### Bash script

1. Save the code in a file
2. Download (this bash script)[https://github.com/Phantomwise/ascii/blob/main/Resources/preview-ANSI-formatting.sh]
3. Make it executable
```
chmod +x preview-formatted-ascii.sh
```
4. Run it with the path to the file as an argument  
```
bash preview-formatted-ascii.sh file-to-preview
```

### Python script

If don't have bash, you can use this python script :
1. Save the code in a file
2. Download (this python script)[https://github.com/Phantomwise/ascii/blob/main/Resources/preview-ANSI-formatting.py]
3. Make it executable
4. Run it with the path to the file as an argument  
```
python preview-formatted-ascii.py file-to-preview
```
