```
╔═══╗              ╓            
║   ║              ║            
╠══╦╝ ╔══╗ ╒══╗ ╔══╣ ╔═╦═╗ ╔══╗ 
║  ╚╗ ╠══╝ ╔══╣ ║  ║ ║ ║ ║ ╠══╝ 
╜   ╙ ╚══╛ ╚══╝ ╚══╝ ╜ ╙ ╙ ╚══╛ 
```

ASCII art I made. CC0, feel free to use.

- [Resources](#resources)

- [ASCII art (Unformatted)](#ascii-art-unformatted)
- [ASCII art (Formatted)](#ascii-art-formatted)
- [Figlet fonts](#figlet-fonts)

Upcoming :
- 🔜 *[Logos (Unformatted)](#logos-unformatted)*
- 🔜 *[Logos (Neofetch)](#logos-neofetch)*
- ⏳ *[Logos (Fastfetch)](#logos-fastfetch)*
- ⏳ *[Cowsays animals](#cowsays-animals)*

## Resources

- Guides
    - [Using ANSI escape codes to format text](https://github.com/Phantomwise/ascii/blob/main/Resources/ANSI-escape-codes.md)
- Reference lists/tables of characters and escape codes (incomplete)
- Scripts to preview ASCII formatted with escape characters in the terminal (made by chatGPT because I suck at coding)
    - [bash version](https://github.com/Phantomwise/ascii/blob/main/Resources/preview-ANSI-formatting.sh)
    - [python version](https://github.com/Phantomwise/ascii/blob/main/Resources/preview-ANSI-formatting.py)

## ASCII art (Unformatted)

Plain text unformatted ASCII banners.

## ASCII art (Formatted)

ASCII banners formatted with ANSI escape characters.

Usable anywhere that supports ASCII with ANSI escape characters.
Ex for ricing :
- `/etc/issue` file *(defines what message is displayed before the tty login prompt)*
- `/etc/issue.net`

To preview the formatted banners in your terminal, you can't just use `cat` on the file because of the escape characters. Instead run this command :
```
printf "%b" "$(cat path-to-file)" 
```
Or you can use this script :
1. Download (this script)[https://github.com/Phantomwise/ascii/blob/main/preview-formatted-ascii.sh]
2. Make it executable
```
chmod +x preview-formatted-ascii.sh
```
3. Run it with the path to the file as an argument  
For example, to preview the file with the Arch Linux banner, download the script and the file containing the banner, then run :
```
bash preview-formatted-ascii.sh arch-tubes-banner-1-formatted
```

## Figlet fonts

Fonts for figlet.

You can see what they look like here :
https://github.com/Phantomwise/ascii/blob/main/figfonts/figfonts-preview.md
Though keep in mind that they'll look better in a terminal than in a code block because you won't see the gaps between the lines.

Figlet is a CLI tool for making ASCII banners. More info here :  
https://github.com/cmatsuoka/figlet

How to use :
1. Install figlet.
2. Download the font file.
3. Put it in `/usr/share/figlet/fonts`.
4. Run `figlet "Your text" -f Font_Name`
    - For the text, make sure to escape special characters like '!' with a backslash.
    - For the font, you don't need to add the extension if the file is in `/usr/share/figlet/fonts`. If the file name has spaces, either rename it to remove the spaces remove them.
    - You can use a font that is not located in `/usr/share/figlet/fonts` if you specify the full path to a font file instead of just a font name.

To show all installed figlet fonts :
```
showfigfonts
```

Other really cool figlet fonts :
https://github.com/xero/figlet-fonts
(Look for the 'example' file linked in the readme to preview all of them at once)

## Logos (Unformatted)

🔜 Not added to the repo yet, I can't remember on which USB stick I put them and I have like a thousand of them -__-

## Logos (Neofetch)

🔜 Not added to the repo yet, I can't remember on which USB stick I put them and I have like a thousand of them -__-

## Logos (Fastfetch)

⏳ Still working on them. Not added yet.

## Cowsays animals

⏳ Not finished. Not added yet, I might have list the files...
