# pyxcel
Compile relevant data from a larger excel file, into a smaller, precise file

# Installation and Setup

## Python (and VSCode)
Install Python from https://www.python.org/downloads/

Or install the newest Python Interpreter through VSCode, available at: https://code.visualstudio.com/download
Once VScode is installed you can find the Python Interpreter via the extensions tab in the left hand menu, by searching for "Python" (authored by Microsoft).

## Git
When python is installed you will need to install Git, if it is not already installed:
https://github.com/git-guides/install-git

## Pyxcel and dependencies
With Git installed, it is recommended to use Git Bash or Git Powershell, navigate to the folder where you want to install Pyxcel and clone the repo into it.

For example:

#### Step 1:
Create a folder named IMS Import, open it, and right click to open Git Bash here

#### Step 2:
Clone the repo into this folder with the following command in Git Bash
```
git clone https://github.com/kristhaj/pyxcel.git
```
#### Step 3:
Navigate into the cloned folder:
```
cd pyxcel
```
and install the required packages, listed below, by entering the following command:

```
pip install -r requirements.txt
```


# Required Packages

- pandas
- xlrd
- openpyxl 3.0.4 (version 3.0.5 and newer has an error with appending sheets to an existing excel file)
- xlsxwriter
- xlwt


# Functionality
## Forms Handler
Extract relevant information from a larger excel document, and collate into a new document

## Divider
Make individual files from a larger master file, based on given indentifier.

## Migrator
Collate data from multiple individual files into a single master file, with a given format, to prepare migration

## Adminipy
Cross reference call list with member data to identify administrator and relevant information.

## Appendinator
Collate data from multiple org specific files into a collective Master File

### Validator
Validates data in the currently handled file, and performs some corrective measures.

### Logger
Logs out any occurances of bad data in the batch of files handled by Appendinator, and where these data points are located.


# Usage

## File Structure

In order to keep track of all your files, and to make it easier to update the launch.json configurations, you can follow the below suggested file structure:

![2022-06-27-15-19-06](https://user-images.githubusercontent.com/9265818/175952666-74eee10c-0fa4-40ef-ab8d-dbf6b5f5be05.png)


Here all the different Modules have their own folder, with _appendage_ being used as the folder for Appendinator, and _KA_ being used as the folder for DivideFile.

In each folder the individual files are structured by federation and batch number to easily find back to in case of import issues.

NOTE: In case you decide upon a different file structure the launch.json config needs to be updated accordingly.

## Apendinator (IMS Import processing)

The easiest way to use as of now is to run via the debug mode in VSCode

Select the Debug tab in the left hand menu, select Appendinator as the configuration to run an simply hit the run-button

![2022-06-27-15-11-35](https://user-images.githubusercontent.com/9265818/175949709-5f5418bc-808b-4870-a1d0-c1f76f97de21.gif)


All the necessary congifurations are done made in the launch.json file, as described below and in the file with comments

![2022-06-27-14-46-58](https://user-images.githubusercontent.com/9265818/175949164-99dec2b5-22cb-454f-a0e9-b27ca629405e.png)


- data_dir: Folder with all member and club data to be imported

- target_path: File path and name of the resulting file, that is written after the script has run

- format_path: IMS Template to format the data by NOTE: the sheet and column names must be exact matches to the files in data_dir

- kao_dir: Folder with output data, if files have undergone KA import and need to be matched for PersonID

- kao_meta: Folder with meta data from the KA import, such as OrgID of club and Gren

- is_post_ka: set to true if batch is done with KA import and personIDs are available or already set

- is_productless: set to true if batch is comprised of clubs with no product data

All of the file paths need only the relative path, ie where the file is in relation to the _pyxcel_ folder.

## Divider (KA Import Formatting)

This script can be run the same way as Apendindinator, via the Debug mode in VSCode:

![2022-06-27-15-12-12](https://user-images.githubusercontent.com/9265818/175949838-969ed7ba-ec5a-429a-a194-5ec15bded061.gif)


All the necessary congifurations are done made in the launch.json file, as described below and in the file with comments

![2022-06-27-14-57-19](https://user-images.githubusercontent.com/9265818/175949306-f594bbfb-8ce3-484c-b507-ebb8b24e34bf.png)

- data: Master File outputted from Apendinator to be used for KA import

- ka_template:  File Path to the KA Import Template

- target_path: Path to the output folder, and name prefix of KA import files.


All of the file paths need only the relative path, ie where the file is in relation to the _pyxcel_ folder.
