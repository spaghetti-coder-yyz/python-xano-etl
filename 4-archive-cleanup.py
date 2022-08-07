import shutil
import os
import datetime


# Create new directory inside of archive folder /archive named as datetime
datestring = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S");
print (datestring);
newdir = 'archive/'+datestring
os.mkdir('archive/'+datestring);

# Move the combined CSV file to the archive folder
original_combinedcsv = 'combined_csv.csv'
target_combinedcsv = newdir + "/" + original_combinedcsv


if os.path.exists(original_combinedcsv):
    shutil.move(original_combinedcsv, target_combinedcsv)
    print("CSV File moved successfully")
else:
    print("CSV File not found!")

# Move the combined JSON file to the archive folder
original_dealsjson = 'deals.json'
target_dealsjson = newdir + "/" + original_dealsjson


if os.path.exists(original_dealsjson):
    shutil.move(original_dealsjson, target_dealsjson)
    print("JSON File moved successfully")
else:
    print("JSON File not found!")


# delete all .csv files
for file in os.listdir("."):
    if file.endswith(".csv"):
        os.remove(file)
        print("Deleted: " + file)

