# Clean File Sort for Nintendo Switch
## Description
### Summary
Using this python script, a user is able to copy all screenshots (.jpg), recorded video clips (.mp4), or both into a newly created folder. This program is written in Python for its readability and my own personal preference.

### Full Explanation
Upon trying to extract recorded media from the Nintendo Switch, I was surprised to see the folder structure
of an inserted MicroSD card to be organized by Date `\...\Year\Month\Day` despite the naming structure of the files already being named in a datetime format `YYYYMMDDhhmmssss-?` that allows for easy sorting. 

For convenience, this program parses through all subfolders from the parent directory and copies them into a newly designated folder (and current date prepended) in the parent directory. The decision to 'copy' rather than 'move' was in order to prevent potential any file corruption and preserve original files on the Nintendo Switch MicroSD if desired.

This script is able to copy all files from all sub-folders within a parent directory in general, but since it was written specifically Nintendo switch media types, only .jpg and .mp4 files are currently supported. Additional file types can be added easily in the future.


## How To
### Windows Executable

 1. Download the `.zip` file
 2. Navigate to `"main.exe"` executable within.
 3. Run the application.
 4. A command prompt will appear, follow the instructions to proceed.
  
   `Copy/Paste Path of Directory here`
   > Copy/Paste the path to your MicroSD folder
  
   `New Folder Name?`
   >Type the desired name for the new folder containing your media files
  
   `File type?`
   >- Enter 'a' to copy all files
   >- Enter 'b' to copy only screenshots (.jpg)
   >- Enter 'c' to copy only video clips (.mp4)
  
 5. After selection, the program will complete the operation and self-close. 
Copied Files will be found in a newly named folder following the format: "YYYY-MM-DD _FolderName_"
in the parent directory.
