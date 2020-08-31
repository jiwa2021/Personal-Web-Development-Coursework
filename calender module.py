import calendar

#(calendar.month(2020, 7, 4, 1))  #year, month, date column width, number of lines per week.

X = input("What time of calender would you like to see(Days_of_the_week, Month, Year): ")

yearx = int(input("Enter Year: "))
monthx = int(input("Enter Month: "))
clmwidth = int(input("Enter Column Width: "))
lpw = int(input("Number of Lines per Week: "))


if X == "Days_of_the_week":
    print(calendar.month(yearx, monthx, clmwidth, lpw))
elif X == "Month":
    print(calendar.monthcalendar(yearx, monthx))
else: 
    print(calendar.calendar(yearx))


    
