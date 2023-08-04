import mysql.connector
import datetime
from tabulate import tabulate


db=input("Enter name of your database :")


mydb=mysql.connector.connect(host='localhost',user='tarunrajsingh',password="tarun123")
mycursor=mydb.cursor()

sql="create database if not exists %s"% (db,)
mycursor.execute(sql)
print("database created successfully..")
mycursor=mydb.cursor()
mycursor.execute("use "+db)

tablename=input("Name of table to be created:")
query="create table if not exists " +tablename+ " \
(empno int primary key,\
name char(40) not null,\
job varchar(15),\
basicsalary float,\
DA float,\
HRA float,\
grosssalary float,\
Tax float,\
netsalary float)"
print("Table  "+tablename+"  created successfully...")
mycursor.execute(query)



while True:
    print('\n\n\n')
    print("*"*156)
    print('\t\t\t\t\t\tMAIN MENU')
    print("*"*156)
    print('\t\t\t\t1. Adding Employee Record')
    print('\t\t\t\t2. for Displaying record of all the Employee')
    print('\t\t\t\t3. for Displaying record of particular Employee')
    print('\t\t\t\t4. for Deleting record of all the Employee')
    print('\t\t\t\t5. for Deleting record of particular Employee')
    print('\t\t\t\t6. for modification of records Employee')
    print('\t\t\t\t7. for Deleting entire database')
    print('\t\t\t\t8. for Dispalying payroll')
    print('\t\t\t\t9. for Displaying salary slip of the employees')
    print('\t\t\t\t10.for Displaying salary slip of a particular employee')
    print('\t\t\t\t11.for Exit')
    print("Enter choice..",end=" ")
    choice=int(input())
    if choice==1:
        try:
            print("Enter employee information... ")
            mempno=int(input("Enter employee no: "))
            mname=input("Enter employee name: ")
            mjob=input("Enter employee job: ")
            mbasicsalary=float(input("Enter basic salary: "))
            if mjob=="MANAGER":
                mDA=mbasicsalary*0.45
                mHRA=mbasicsalary*0.30
                mTax=mbasicsalary*0.15
            elif mjob=="OFFICER":
                mDA=mbasicsalary*0.5
                mHRA=mbasicsalary*0.35
                mTax=mbasicsalary*0.2
            else:
                mDA=mbasicsalary*0.4
                mHRA=mbasicsalary*0.25
                mTax=mbasicsalary*0.1
            mgrosssalary=mbasicsalary+mDA+mHRA
            mnetsalary=mgrosssalary-mTax
            rec=(mempno,mname,mjob,mbasicsalary,mDA,mHRA,mgrosssalary,mTax,mnetsalary)
            query="insert into  "+tablename+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
            mycursor.execute(query,rec)
            mydb.commit()
            print("Records added successfully..")
        except Exception as e:
            print("somthing went wrong",e)
   
        
    elif choice==2:
        try:
            query="select * from "+tablename
            mycursor.execute(query)
            #print query
            print(tabulate(mycursor, headers=['Empno','Name','Job','Basicsalary','DA','HRA','Grosssalary','Tax','Netsalary'],tablefmt="fancy_grid"))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
            print(rec)'''
        except:
            print("something went wrong")





    elif choice==3:
        try:
            en=input("enter empno..: ")
            query=' select * from ' +tablename+ ' where empno= '+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of employee no..:"+en)
            print(myrecord)
            #print(tabulate(myrecord, headers=['Empno','Name','Job','Basic salary','DA','HRA','grosssalary','tax','Net salary']))

            c=mycursor.rowcount
            if c==-1:
                print("nothing to display")
           
        except Exception as e:
            print("something went wrong",e)




    elif choice==4:
        try:
            x=int(input("Do you want to delete all the records if YES press 1 and for NO press 2...:="))
            if x==1:
                query="delete from "+tablename
                mycursor.execute(query)
                print("ALL THE RECORDS ARE DELETED")
            else:
                print("okk for not deleted")
        except Exception as e:
             print("something went wrong")





    elif choice==5:
        try:
            en=input("Enter Employee no. of the record to be deleted...")
            query="delete from "+tablename+" where empno="+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("Deletion done")
            else:
                print("Employee no",en,"not found")
        except Exception as e:
             print("something went wrong")



    elif choice==6:
        try:
            en=input("Enter employee no. of the records to be modified..:")
            query='select * from '+tablename+' where empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print("Empno  "+en+"  does not exist")
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasicsalary=myrecord[3]
                print('empno         :',myrecord[0])
                print('name          :',myrecord[1])
                print('job           :',myrecord[2])
                print('basicsalary   :',myrecord[3])
                print('DA            :',myrecord[4])
                print('HRA           :',myrecord[5])
                print('grosssalary   :',myrecord[6])
                print('Tax           :',myrecord[7])
                print('Netsalary     :',myrecord[8])
                print('_______________________')
                print("Type value to modify below or just press Enter for no change")
                x=input("Enter name..:")
                if len(x)>0:
                    mname=x
                x=input("Enter job..:")
                if len(x)>0:
                    mjob=x
                x=input("Enter basicsalary..:")
                if len(x)>0:
                    mbasicsalary=float(x)
                query='update '+tablename+' set name='+"'"+mname+"'"+','+'job='+"'"+mjob+"'"+','+'basicsalary='+"'"+str(mbasicsalary)+"'"+' where empno='+en
                mycursor.execute(query)
                mydb.commit()
                print("Record modified")
        except Exception as e:
              print("something went wrong",e)

          
    elif choice==7:
        print("DO YOU WANT TO DELETE YOUR DATABASE :YES/NO")
        x=int(input("enter your confirmination by pressing 1 for yes 2 for no....:-"))
        if x==1:
            query='drop database '+db
            mycursor.execute(query)
            mydb.commit()
            print("your database is deleted now")
            break
        else:
            print("okk not deleted")
        


    elif choice==8:
        try:
            query=' select * from ' +tablename
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print(95*'*')
            print('Employee payroll'.center(90))
            print(95*'*')
            now=datetime.datetime.now()
            print("Current Date and Time:",end=' ')
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            print()
            print(95*'*')
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                  %('Empno','Name','job','Basic','DA','HRA','Gross','Tax','Net'))
            print(95*'-')
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
            print(95*'-')
        except Exception as e:
            print('something went wrong',e)


    elif choice==9:
        try:
            query=' select * from '+tablename
            mycursor.execute(query)
            now= datetime.datetime.now()
            print("\t\t\t\tSALARY SLIP")
            print('-'*95)
            print("Current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=['Empno','Name','Job','Basic salary','DA','HRA','Grosssalary','Tax','Net salary']))


            #for rec in myrecords:
             #   print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
            
        except Exception as e:
            print("Something went wrong",e)
            

    elif choice==10:
        try:
            en=input("Enter employee number whose pay slip you want to retrieve:")
            query ='select * from '+tablename+' where empno= '+en
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n\t\t\t\tSALARY SLIP")
            print("current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(tabulate(mycursor, headers=['Empno','Name','Job','Basic salary','DA','HRA','Grosssalary','Tax','Net salary']))

        except Exception as e:
            print("Something went wrong",e)



                
    elif choice==11:
        break
    else:
        print("wrong choice")
                                                                                
