# Readme

ASCII art I made. CC0, feel free to use.

- 🔜 *[Logos (Unformatted)](#logos-unformatted)*
- 🔜 *[Logos (Neofetch)](#logos-neofetch)*
- ⏳ *[Logos (Fastfetch)](#logos-fastfetch)*
- ✅ [Banners (Unformatted)](#banners-unformatted)
- ✅ [Banners (/etc/issue)](#banners-etcissue)
- 🚧 [Figlet fonts](#figlet-fonts)
- ⏳ *[Cowsays animals](#cowsays-animals)*

## Logos (Unformatted)

🔜 Done but not added to the repo yet.

## Logos (Neofetch)

🔜 Done but not added to the repo yet.

## Logos (Fastfetch)

⏳ Still working on them. Not added yet.

## Banners (Unformatted)

Plain text ASCII banners.

## Banners (/etc/issue)

Formatted banners for the /etc/issue file.

This file defines what message is displayed before the tty login prompt and you can make it show colored ASCII art :)  
https://www.man7.org/linux/man-pages/man5/issue.5.html

## Figlet fonts

Fonts for figlet.

Figlet is a CLI tool for making ASCII banners. More info here :  
https://github.com/cmatsuoka/figlet

- 🚧 **tubes** : I'm trying to modify my /etc/issue banner into a full figlet font so I can use it to print something else than "archlinux" 😅
    - ✅ Done: lowercase letters, basic punctuation .,;:!'"_-+*
    - 🚧 WIP: uppercase letters
    - ⏳ Missing for now: extended punctuation, special characters*

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

## Cowsays animals

🚧 WIP. Not added to the repo yet.
