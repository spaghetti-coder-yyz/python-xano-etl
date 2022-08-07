# python-xano-etl

Update your FTP credentials in file: 1-pull-combine.py:

# FTP connection config

ftp = FTP('[FTP host here]')
ftp.login('[FTP username]', '[FTP password]')

# set encoding to utf-8

ftp.encoding = 'latin-1'

# Change to the directory on the FTP server

ftp.cwd('[change FTP directory to files to be downloaded]')
....
