# pyxcel
Compile relevant data from a larger excel file, into a smaller, precise file


# Required Modules

- pandas
- xlrd
- openpyxl 3.0.4 (version 3.0.5 has an error with appending to existing excel file)
- xlsxwriter
- xlwt

# Functionality
## Forms Handler
Extract relevant information from a larger excel document, and collate into a new document

## Divider
Make individual files from a larger master file, based on given indentifier.

## Migrator
Collate data from multiple individual files into a single master file, with a given format, to prepare migration

## Aminipy
Cross reference call list with member data to identify administrator and relevant information.

## Apendinator
Collate data from multiple org specific files into a collective Master File

### Validator
Validates data in the currently handled file, and performs some corrective measures.

### Logger
Logs out any occurances of bad data in the batch of files handled by Appendinator, and where these data points are located.