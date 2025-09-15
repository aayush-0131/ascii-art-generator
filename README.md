# 🐍 ASCII Art Generator

A simple, command-line Python script that converts any image into text-based ASCII art. This was a small project built to practice image manipulation with the Pillow library.

## 🖼️ Demo Output

,:;**?%%%%%***+*???***************%SSSS###SSSSS#SSSSSSS%%%%%%????????******???????******************
,,;**?%%%%%***+*???***************SSSSSSS#SSSSSSSSS%%%%%???????*********+********************+++++++
::;??%%%%%%**++*******************S%%SSSSSSSSSSSS%%%????********++++*+++++++++++++++++++++;;;;;;::::
::+%%%%%%%%**++*******************%%%%SSSSSSSSSSS%%??***++++++++*???+;;;;;;::::::::,,,,,,,,,,,,,,,,,
::;??%%%%%%**+;*******************%%%%%SS#SSSSS%%?***+;;::::,:*%%%%?,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,:**?%%%%%*++;+******************?%%%%SS##SSS%%??**+:,,..,:+%%%???:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,:+*??%%%?*++;+******************?%%SSSSS#####@####S???**?%%%????+,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,:+**?%%%?++;;+******************?SS##SS#S####@#S#@#S#SSSS%%%???+,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,:+**?%%%?++;;+******************?S##SSSSSS#S#@##S@#S%SS%%%%%%%+,,,,,,,,,,,,,,,,,,,,,,,,,,,,::::::;
,,:+**?%%%?*++;+******************%S#S**?%SSSSS#SS####%#S%%%%S%%;,,,,,,,,,,:::::::;;;;;;++++++++++++
,,:+**?%%%%*++;+*****************?%%SS%??#@@###S%S###S%S%%%%?%S?;;;;;;+++++++++++++++++++++*********
,,:+**?%%%%**+;+****************?%SSSS#SS######@#S##SS####S%%*?*++++++++++**********************????
,,:+*?%%%%%?*++*****************%S####SS%########S#SS?#######S%?*++++**********??*******?????????%%?
,,:+?%%SSS%%?++*****************%SSSSS##########@##S%?%######%%%?********????????????????%%%?%%%%%%%
::;?%SSS##S%?*+*??????**********%%S######SS#####@@##SSSSSSSS%%#%??***????????%%??????%%%%%%%%%%SSSSS
:;+%S#####S%%*+*????????********%%SS####SSSSS##SS#@#S%SSSSSS%%SS??????%%%????%%%%%%%%%%%%%%%SSSSSSSS
+*%S#######%%**??????????*******?%%SS#SSS%%%SSSS%S#S%%S%?%S##%%%??????%%%%%%%%%%%SSSSSSSSSSSSSSSSS##
%SS########S%?*?????????????*%??%%%%SS##SS%%%%SSS##S%%%%?%SSSSS???????%%SSSS%%%SSSSSSSSSSS##########
SSSS#####@#S%?*?????????????%SSSS%%%%SSS#SSS%%%%%SS%%???%SSSS%?*****???%%%%%%%SSSS##################
SSS#####@@#SS???%???%%%?????%SSSSS#######S##SSS%%%???%%%S%%%%?**************?????%%SSS##############
SS####@@@@@SS%?%%%%%%%%%%%%??%?%SSS##@@###@#######S#S#SSSS%SS%?**+++****************????????%%%%%%%%
SS##@@@@@@@#S%%%%%%%%%%%SS%?*+*%SSSS#@##@@#@@@@@@@@@@@##SSS%%%%S%?+++*******************************
SSS########SS%%%SSSSSSS%%%?%?+?SSSSSS#@@@@@@@#@@@@@@@###SSSS%S##??*++++++***************************
S##########SSS%SSSS%%%?????%?+%SSSSSSSS#@@@@@@@@@@@@@@##SS%%%S@@%?**???*+*%??????**************?????
##@@@@@@@@@#SSSSS%%???*****%**SSSSSSSSSS#@#@@@@@@@@@@##SSSSS#@#%?*?%?S%?%%?????%%????%%%%???????????
@@@@@@@@@@##SSS%%???*******%*?SSSSSSSS#SS####@@@#######SSSS###%?***??SS%%%%*%%?%SS%%%%%%%SS%?%%%%??%
###SSSSSS%%%????***+++++++*%**%SSSSSSS###S#@#######@######SSS%??**?*%SSSS%%?%%%%%SSS##S%%SS%%%%SS%%%
%%%???????******+++********%??%SSSSSSS####S#@@@######@###SS#S%?**?*+%SSSSSSSSSS%SSSS###SS%%%%%?%SSS%
%?????%???***????????????%%%S%SSSSSS#SS###S#@####@@@@######SSSS%+%?+*SSSSS%S##SSSS##@###SS%%%SS%SSSS
????%%%%%??????????***?*?SS%%#SSSSSSS#SS##SS@@@#@@@@@#####SSSSS?*%?+*SSSSS%####SSS#######SS###S%SSS#
???***??????***********?%%SS%S#SSSSSS#SS###SS@##@#@@@@#####SSS?*???%%%##SS################@@#S%#@@#S
????*****???????*****+;?%%SSSSS#SS####SS###SS#@@@@@#@#####S#S%%%SSS%SS##############@@@#@@@#SS#@####
%%%%%%%%%%%%%?????**?%?%%SSSSSSS#S#####S####S#@@@###@######SS#SSS%%%S####@#####@@@@@@@@#@###S#@SS#@@
##############SSS+;*??%%%SS##S#########S####S#@@@@@@########SSS%%%%S####@@@@@@@@@@@@@#####@##@##@@SS
%%%SSSSSSSSSSSSS%**SSSS%%%SS########@@#S####SS@@@@@@######S%%%???%%%??%@@@@@@@@@@@@@####@@@@@@@@@###
?%%%%%%%%%%%%%S%?%%###############@@@@@########@@@@#####SS%%???%%SSSS?S@@@@@#@@#########@@@@@@@@@@#@


## ✨ Features

- Converts common image formats (JPG, PNG) into ASCII art.
- Resizes the image to fit standard terminal widths.
- Uses a character palette to represent pixel brightness.
- Simple, single-file script with minimal dependencies.

## 🚀 Setup and Installation

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/aayush-0131/ascii-art-generator.git](https://github.com/YourUsername/ascii-art-generator.git)
    cd ascii-art-generator
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependency:**
    ```bash
    pip install Pillow
    ```

## ⚙️ Usage

1.  Place an image file (e.g., `my_image.jpg`) into the project directory.

2.  Open `generator.py` and change the `path` variable on line 20 to match your image's filename.

3.  Run the script:
    ```bash
    python3 generator.py
    ```
    The ASCII art will be printed directly to your terminal.
