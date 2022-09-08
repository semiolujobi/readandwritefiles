import csv
def main():
    
    monthslist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    infile = open ('steps.csv', 'r')
    csvfile = csv.reader(infile, delimiter=',')
    next (csvfile)

    outfile = open('avg_steps.csv','w')

    month = 1
    counter = 0 
    totalsteps = 0
    outfile.write('Month, Average Steps' +'\n')
    for record in csvfile:
        if int(record[0]) == month:
            
            steps = int(record[1])
            counter = counter+1
            totalsteps += steps
            
        else:
            avgsteps = float(format(totalsteps/counter, '.2f'))
            monthrecords = str(month)
            stepsrecords = str(avgsteps)
            
            outfile.write(monthslist[month-1]+', ')
            outfile.write(str(avgsteps) + '\n')
            counter = 1
            totalsteps = int(record[1])
            month = int(record[0])  
            
            
    avgsteps = float(format(totalsteps/counter, '.2f'))
    monthrecords = str(month)
    outfile.write(monthslist[int(monthrecords)-1]+', ')
    outfile.write(str(avgsteps))
    
main()
