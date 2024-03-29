import csv
from ChainCode import BigChainCode
from csv import writer

chaincode_features = BigChainCode

# Combine Features Storing
image_set = chaincode_features

fields = ['target_names', 'direction1',
                          'direction2',
                          'direction3',
                          'direction4',
                          'direction5',
                          'direction6',
                          'direction7',
                          'direction8',
                          'target']

# data rows of csv file
rows = []

for i in range(len(image_set)):
    features = image_set[i]
    row = ['F',
           features[0],
           features[1],
           features[2],
           features[3],
           features[4],
           features[5],
           features[6],
           features[7],
           6]
    rows.append(row)

#####################################################################################################

# name of csv file

filename = "F:/Python/OpenCV/CharacterClassification/CSV Files/chainCode.csv"


def append_list_as_row(filename, list_of_elem):
    # Open file in append mode
    with open(filename, 'a+', newline='') as csvfile:
        # Create a writer object from csv module
        csvwriter = csv.writer(csvfile)
        # Add field names
        # csvwriter.writerow(fields)
        # Add contents of list as last row in the csv file
        csvwriter.writerows(list_of_elem)


append_list_as_row(filename, rows)


