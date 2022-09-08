#define main function
#import csv function
#set infile to opening and reading steps csv file
#set a counter of month to 1
#define variable of months and make an integer of read figure
#define variable of steps and make an integer of read figure
#create running total of steps
#create a for loop that goes through the records in steps csv file
#create an if else clause where if counter of month is equal to the months variable, then add the steps to running total
#in if clause, calculate the average steps by dividing totalsteps by number of steps 
#else add 1 to the counter if the counter is not equal to months 
#outside the for loop, 




def main():
    import csv
    infile = open ('steps.csv', 'r')
    csvfile = csv.reader(infile, delimiter=',')
    next (csvfile)
    month = 1
    counter = 0 
    totalsteps = 0
    for record in csvfile:
        if int(record[0]) == month:
            #month = int(record[0])
            steps = int(record[1])
            counter = counter+1
            totalsteps = totalsteps+steps
            #avgsteps = int(totalsteps/counter)
            #print (month, avgsteps)
        else:
            avgsteps = float(totalsteps/counter)
            print (month, avgsteps)
            month = int(record[0])   
            monthrecords = str(month)
            stepsrecords = str(avgsteps)
    outfile = open('customer_country.csv','w')
    outfile.write(monthrecords)
    outfile.write(stepsrecords)
main()
#thomas_craig1@baylor.edu