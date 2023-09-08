#printing calender of a given year using CALENDER build-in module
import calendar
y = int(input("Enter the year: "))
# m = 1
x = "CALENDER".center(100)
print(x)
cal = calendar.TextCalendar(calendar.SUNDAY)    #An instance of Text calender class is created and calender. Sunday means thatb you want to start displaying the calender from sunday
i = 1
while(i<=12):
    cal.prmonth(y,i)
    i += 1
#prmonth is a function of the class that prints the calender for given month and year
