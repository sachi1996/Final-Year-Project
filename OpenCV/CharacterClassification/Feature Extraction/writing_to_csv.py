import csv
from zoning import BigZoneDensity
from MinDistanceFeatures import BigMinDistance
from csv import writer


distance_features = BigMinDistance
zone_features = BigZoneDensity

CombineFeatures = []

for i in range(len(BigZoneDensity)):
    arr = BigZoneDensity[i]
    for j in range(len(BigMinDistance[0])):
        arr.append(BigMinDistance[i][j])
    CombineFeatures.append(arr)

print(CombineFeatures)


# Combine Features Storing
image_set = CombineFeatures

fields = ['target_names', 'zone_1',
                          'zone_2',
                          'zone_3',
                          'zone_4',
                          'zone_5',
                          'zone_6',
                          'zone_7',
                          'zone_8',
                          'zone_9',
                          'zone_10',
                          'zone_11',
                          'zone_12',
                          'zone_13',
                          'zone_14',
                          'zone_15',
                          'zone_16',
                          'left_distance',
                          'right_distance',
                          'up_distance',
                          'down_distance','target']

# data rows of csv file
rows = []

for i in range(len(image_set)):
    features = image_set[i]
    row = ['m',
           features[0],
           features[1],
           features[2],
           features[3],
           features[4],
           features[5],
           features[6],
           features[7],
           features[8],
           features[9],
           features[10],
           features[11],
           features[12],
           features[13],
           features[14],
           features[15],
           features[16],
           features[17],
           features[18],
           features[19],
           13]
    rows.append(row)

#####################################################################################################

# name of csv file

filename = "E:/Python/OpenCV/CharacterClassification/CSV Files/min_and_zone_features.csv"


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


