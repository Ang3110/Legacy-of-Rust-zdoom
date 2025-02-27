# Legacy-of-Rust-zdoom
This project brings ZDoom-close compatibility and development features to ZDoombased source ports that don't support mbf21, such as Zandronum, LZDoom, ZDoom, but can also work in gzdoom despite having mbf21 support. It translates and adapts the LoR content into the ZDoom ecosystem while keeping it the same. 

## Build Instructions

### Linux
It shouldn't be difficult to build the project. Just make sure you have GNU Make and the zip. 
Most of the time, they come included in all the Linux distributions. 
If they are not installed on your computer, use your package manager to install them.

### Windows
These tools are also available for Windows users. You can search GnuWin32 or Gnu on Windows (GOW): https://github.com/bmatzelle/gow, download and set them up.

1. **Extract the Archive:**
   Download and extract the file to your desired directory.

2. **Open the Terminal:**
   Navigate to the extracted folder where the `Makefile` is located. For instance:
   ```
   cd /path/to/extracted zip file
   ```
   then type
   ```
   make
   ```
   After that your compiled file called `LoR-ZD.pk3` should be located in the dist folder, you can move the pk3 or run from the dist folder directly and run it with one of the following recommended sourceports
   for example:
   ```
   Windows
   lzdoom.exe -iwad C:\path\to\doom2.wad -file C:\path\to\LoR-ZD.pk3 C:\path\to\id1.wad
   
   Linux
   lzdoom -iwad /path/to/doom2.wad -file /path/to/LoR-ZD.pk3 /path/to/id1.wad
   ```
   same applies to zandronum, zdoom and gzdoom as well otherwise a file manager like zdl or doom explorer is recommended, or drag the pk3 and the `id1.wad` to the suggested sourceport's executable with the doom2 iwad in them.

# License Agreement for Legacy of Rust Modding Tools

## Terms and Conditions

### 1. Permissions
- This project is intended for **non-commercial use only**.
- You are allowed to use, modify, and distribute the scripts, code, and templates provided in this repository **for personal or educational purposes** or as part of your own DOOM mods.
- You may modify this project in any way you like, provided that:
  - Any official DOOM code or assets are **not distributed commercially** without proper authorization from id Software/Bethesda.
  - This project has no involvement in or responsibility for any copyright infringement committed by users. It is provided solely as a fun, time-driven hobby project.

### 2. Credits and Attribution
- Proper attribution must be given when using assets or code from this repository.
- Include the following credits in your project:
Legacy of Rust - ZDoom Edition by Angelloproduct Additional contributions and assets by TheAgaures, Mattfrie1, Tarles X, and Xaser.
Original DOOM assets and engine by id Software, Bethesda, Nightdive Studios, and MachineGames.

### 3. Compliance with Bethesda's EULA
- This project is a fan work and is not affiliated with or endorsed by id Software, Bethesda, Nightdive Studios, or MachineGames.
- Users must own a legal copy of `doom2.wad` and `id1.wad` or (`id1-res.wad` if its maps, zmapinfo are removed) to use this project.
- By using this project, you agree to adhere to Bethesda/id Software's End User License Agreement (EULA).

### 4. Updates to This License
- The authors reserve the right to update this license to ensure compliance with legal and community standards.
---
For more information, visit the official [Bethesda EULA](https://bethesda.net/en/document/eula).
