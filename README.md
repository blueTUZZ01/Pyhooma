# Pyhooma
## The reverse shell tool

Pyhooma - is a easy reverse shell tool maded on python3

- Intuitive interface
- Easy and fast setup

## Features

- Easy file download
- Take screenshots and webcam photo
- After disconnection can delete file to cover your tracks
- Can log shell results into txt file


### Commands
- Shell
- Download
- Screenshot
- Photo
- Disconnect
1. Shell - main command, can execute shell commands on target computer
```shell <command> ``` 

2. Download - for download specified files from target computer
```download <file path>```

3. Screenshot - takes monitor screenshot
```screenshot```

4. Photo - takes webcam photo
```photo```

5. Disconnect - stop conection
```disconnect```
      or
```disconnect_&_delete```
to delete reverse shell file on target computer

Screenshot and webcam photo will be saved in folder "Photo"
Donwloaded files will be saved in folder "Downloads"

## Installation
Pyhooma needs python3 to run.
If you don't installed python3:
```apt install python3```
Else if you have windows - download python on official site 
https://www.python.org/downloads/.
Then after python3 installation, start install and run Pyhooma
```
git clone https://github.com/blueTUZZ01/Pyhooma
cd Pyhooma
python3 PYHOOMA.py -p <port>
```
To build reverse shell file add argument -b
```
python3 PYHOOMA.py -b
```
To setup shell connection, in folder "ReverseSet" redact file "Ip" and "Port".
If you wanna log all shell results add argument -l
```
python3 PYHOOMA.py -p <port> -l
```
After running the file wait while revesre shell will be connected.
If you will find any bugs - contact with me at telegram
@N_B_K_1
