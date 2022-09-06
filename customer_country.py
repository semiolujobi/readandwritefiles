def main():
    import csv

    infile = open ('customers.csv','r')
   
    csvfile = csv.reader(infile, delimiter=',')

    next (csvfile)
    num = 1
    outfile = open ('customer_country.csv','w')
    csvwriter = csv.writer(outfile, delimiter =',')
    header = ['Full Name', 'Country']
    csvwriter.writerow(header)
    for record in csvfile:
        full_name = record[1] + ' ' + record [2]
        country = ' '+ record[4]
        num += 1
        records = [full_name, country]
        csvwriter.writerow(records)
    print ('We have read', num, 'records in this file')
        
    outfile.close()       
main()