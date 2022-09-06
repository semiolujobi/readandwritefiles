def main():
    import csv

    infile = open ('EmployeePay.csv','r')
   
    csvfile = csv.reader(infile, delimiter=',')
    next (csvfile)
    num = 1 
    print('ID ', 'Employee First Name ', 'Employee Last Name ', 'Salary')
    for record in csvfile:
        empid = record[0]
        empfname = record[1]
        emplname = record[2]
        salary = int(record[3])
        bonus = float(record[4])
        empbonus = salary*bonus
        newsalary = salary+empbonus
        num+=1
        records = [empid,empfname,emplname,newsalary]
        print (records)
main()





