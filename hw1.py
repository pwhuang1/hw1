# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061173.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)


#for row in data:
    #print(row['station_id'],row['TEMP'])
#print(header)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.

target_data = []
target_data_removed = list(filter(lambda item: item['TEMP'] >= '-99.000', data) or filter(lambda item: item['TEMP'] <= '-999.000', data))
data1 = []

#C0A880
target_data1 = list(filter(lambda item: item['station_id'] == 'C0A880', target_data_removed))

for row in target_data1:
    data1.append(row['TEMP'])
    
target_data.append([row['station_id'],max(data1)])

#C0F9A0
data1 = []
target_data2 = list(filter(lambda item: item['station_id'] == 'C0F9A0', target_data_removed))

for row in target_data2:
    data1.append(row['TEMP'])

target_data.append([row['station_id'],max(data1)])

#C0G640
data1 = []
target_data3 = list(filter(lambda item: item['station_id'] == 'C0G640', target_data_removed))

for row in target_data3:
    data1.append(row['TEMP'])

target_data.append([row['station_id'],max(data1)])

#C0R190
data1 = []
target_data4 = list(filter(lambda item: item['station_id'] == 'C0R190', target_data_removed))

for row in target_data4:
    data1.append(row['TEMP'])

target_data.append([row['station_id'],max(data1)])

#C0X260
data1 = []
target_data5 = list(filter(lambda item: item['station_id'] == 'C0X260', target_data_removed))

for row in target_data5:
    data1.append(row['TEMP'])

target_data.append([row['station_id'],max(data1)])


# Retrive ten data points from the beginning.
#target_data = data[:]

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================