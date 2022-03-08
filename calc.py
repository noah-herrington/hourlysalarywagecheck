import os, re, sys, itertools, json, requests, base64, linecache, time, requests, webbrowser, bs4, time, pyautogui, pyperclip, urllib3, pprint, shutil, platform, subprocess
from pickletools import float8, int4

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    cls()

paygrade = str(input("Are you salaried or hourly? Type S or H to continue. "))
if paygrade == "S":
    salaryrate = float(input("How much do you make yearly? "))
    hours = float(input("How many hours do you work in a week? "))
    salaryhourlyrate = salaryrate/52/hours
    overtimethreshhold = 40
    print("You make approximately " + (str(salaryhourlyrate)) + " per hour.")
    hourlypaycheck = (salaryhourlyrate*(1.5)*(hours-overtimethreshhold) + (salaryhourlyrate*overtimethreshhold))
    print("If you were hourly, you would make approximately " + str(hourlypaycheck) + " per paycheck, leading to")
    print("approximately " + str(hourlypaycheck * 52) + " per year")
    quit()
elif paygrade == "H":
    overtimethreshhold = 40
    hours = float(input("How many hours did you work this week? "))
if hours >= overtimethreshhold:
    overtime = (hours-overtimethreshhold)
    hours = (hours-overtime)
    print("Hours used overtime: " + str(overtime))
    print("Total hours: " + str(hours+overtime))
else:
    overtime = 0
    print("No overtime")
    print("Total hours: " + str(hours))
# calculates hourly before tax
payrate = abs(float(input("How much do you get paid an hour? ")))
overtimepay = overtime * (1.5*payrate)
normalpay = hours * payrate
fullpay = float(normalpay+overtimepay)
print("Estimated weekly pay: " + str(fullpay))
frequency = abs(float(input("How many weeks is your pay period? ")))
periodtotal = (frequency*fullpay)
print("Estimated period paycheck: " + (str(periodtotal)))
salary = (hours+overtime)*payrate*52
print("\n")
print("Estimated salary is: " + str(salary) + " per year")
overtimeyearly = fullpay*52
print("Estimated annual income, paid hourly: " + str(overtimeyearly))
if overtimeyearly > salary:
    print("\n")
    print("Sorry dude, you're getting less money salaried than you would if you were paid hourly")
    print("You're losing out on " + str(overtimeyearly-salary) + " every year")
elif overtimeyearly < salary:
    print("You're making more money than you would be making salaried, go you!")
    quit()
