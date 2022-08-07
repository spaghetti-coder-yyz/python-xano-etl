from ftplib import FTP
import os
import glob
import pandas as pd

# FTP connection config
ftp = FTP('[FTP host here]')
ftp.login('[FTP username]', '[FTP password]')

# set encoding to utf-8
ftp.encoding = 'latin-1'

# Change to the directory on the FTP server
ftp.cwd('[change FTP directory to files to be downloaded]')

files = ftp.nlst()

ftp = FTP('[FTP host here]')
ftp.login('[FTP username]', '[FTP password]')

# set encoding to utf-8
ftp.encoding = 'latin-1'

# Change to the directory on the FTP server
ftp.cwd('[change FTP directory to files to be downloaded]')

files = ftp.nlst()
# print(files)

# If the file is a CSV, download it
for fileName in files:
    if fileName.endswith('.csv'):
        print(fileName)
        with open(fileName, 'wb') as file:
            retCode = ftp.retrbinary('RETR ' + fileName, file.write)
            file.close()

# Close the FTP connection
ftp.quit()


extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

# Print a finished message
print("Finished")



    