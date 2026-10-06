# Project Setup

#### NOTE:
Do all of this in the root directory of the project (I am using the terminal inside of VS Code, if you have any issues setting up the project let me know)

#### NOTE:
Will need to have python installed on computer (version 3.12+) (if you don't just google "python install")

#### NOTE:
Will only be able to run clash royale games on windows computers.

If you do not have any laptops or pc's running windows, you will need to work on other parts of the project.

If you only have a windows pc at your house, consider downloading AnyDesk or other similar apps to let you work on your pc remotely from your laptop.

## Development Environment Setup Steps

Clone our repository:
```bash
# over https
https://github.com/DrewAMSD/clash_royale_ai.git

# using ssh
git@github.com:DrewAMSD/clash_royale_ai.git
```

If you are working entirely in a terminal:
```bash
# move into the root of our project directory
cd clash_royale_ai
```
Otherwise: Open this project folder in your code editor (I am using VS Code), and then use the built in terminal provided by the IDE.

### Once inside of the project's root directory:

Create virtual environment to install and save our project dependencies
```bash
python3 -m venv ./venv
```

Activate our virtual environment (do this every time you open the project) (to deactivate it, just type "deactivate" into terminal)
```bash
# Windows:
.\venv\Scripts\activate.bat

# Linux/MacOs:
source ./venv/bin/activate
```


Install our project dependencies (python packages we will be using)
```bash
pip install -r requirements.txt
```


To run any of our python files (remember to stay in root directory of project)
```bash
python3 -m src.<directory-name>.<file-name>
# examples
python3 -m src.model.model
python3 -m src.game.screen_manager
python3 -m src.constants
```

#### NOTE: 

Do not include the ".py" in the file name, the "-m" flag is running our project as a collection of modules with the "src" directory being our entry point(which automatically assumes the files we are calling to be in the ".py" format).

This allows us to import from our python files in other locations(or "modules") in the src directory via:
```bash
from src.<path>.<to>.<module> import <python classes, methods, and/or variables>
```

That's also why there are "\_\_init\_\_.py" files in each directory, which tells the python interpreter that the directory is a module in our project.


## Installing Clash Royale onto our Windows Computers

Visit this link:
```bash
https://play.google.com/store/apps/details?id=com.supercell.clashroyale
```
OR: Search into browser "clash royale windows pc install", and follow steps from first link.

This will download a setup script for installing the google play app if you do not already have it. If you already have google play installed it will open up the google play store to the Clash Royale app, where you can just select to download.

After google play is installed, simply search for Clash Royale in the app search bar, and download the first app result.

## Running our Project with Clash Royale Open:

Preferrably, try to align your clash royale window with the top left of your screen when running the app, please ask me for help if you have issues aligning the ScreenManager with your clash window setup (example below) 

<img width="1919" height="1079" alt="Screenshot 2026-03-04 110557" src="https://github.com/user-attachments/assets/9449d37e-f8f9-4b8d-8738-300a9bce24c8" />

It is important to keep your app aligned in the same position because then you can pass the same initial parameters to the ScreenManager everytime you run the app .

You will need to pass the pixel coordinates of the top-left corner of your clash royale window + its size to the ScreenManager (bottom-right coordinate minus top-left coordinate)]. I may try to automate this later, but for now this will be required for each device's setup (unless you can replicate my setup). Please make sure to record these values outside of the project so you do not have to repeatedly measure it.

Can see my parameters to the ScreenManager in the code snippet above.
