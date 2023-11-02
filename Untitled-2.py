import csv
data = []
matchingOrders = []


with open('IAS-staff-ID.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row[1])



with open('IAS-records.csv') as csv_file1:
    csv_reader1 = csv.reader(csv_file1, delimiter=',')
    line_count1 = 0
    for row in csv_reader1:
        for x in data:
            if row[2] == x:
               matchingOrders.append(row)
            else:
                pass


def insertBlank():
        
    # field names
    fields = ['Record','Date','DAS ID','Items to purchase','Item Cost Ex VAT','Qty','Total Item Cost','Category','Total Cost']
    
    # data rows of csv file

    
    with open('IAS-matching-ordersy.csv', 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(matchingOrders)

