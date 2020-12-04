#Risk Calculator By Ethan Justice

import math
from time import sleep

#Some fun start up stuff
'''
print("Starting Risk Calculator......\n")
sleep(3)
print("Loading.....\n") 
sleep(2)
print("Please wait..\n")
sleep(2)
print("Ready to go!\n")
'''
#Variables
height=0
weight=0
bmi=0.0
bp=[0,0,0,0,0] #[normal,elevated,stage1, stage2, crisis]
familyhist=[0,0,0] #[diabetes,cancer,alzheimers]
age=0
totalRisk=0
inchToMeter=0
sysolicBP=0
diastolicBP=0


#Calculating total height in inches
print("\nPlease tell me your height first in feet then inches\n")
feet=int(input("Feet:"))
inches=int(input("Inches:"))
feet=(feet)*12
totalheight=feet+inches


#Asking for weight and calculating BMI
weight=int(input("\nWhat is your current weight in pounds:"))
inchToMeter=totalheight/39.37
poundToKilo=weight/2.205
bmi=poundToKilo/(inchToMeter*inchToMeter)

if bmi<24.9:
    totalRisk+=0
elif bmi<29.4:
    totalRisk+=30
else:
    totalRisk+=75

#Age Stuff
age=int(input("\nEnter your age in years:"))

if age<30:
    totalRisk+=0
elif age<45:
    totalRisk+=10
elif age<60:
    totalRisk+=20
else:
    totalRisk+=30

#Getting all Blood Pressure Values and combining them
sysolicBP=int(input("\nWhat is your systolic blood pressure:"))
diastolicBP=int(input("\n What is your diastolic blood pressure:"))

if sysolicBP<120 and diastolicBP<80:
    bp=[1]
    totalRisk+=0
elif sysolicBP<129 and diastolicBP<80:
    bp=[2]
    totalRisk+=15
elif sysolicBP<139 or diastolicBP<89:
    bp=[3]
    totalRisk+=30
elif sysolicBP>140 or diastolicBP>90:
    bp=[4]
    totalRisk+=75
else:
    bp=[5]
    totalRisk+=100

#Asking for family history
familyhist=[input("\nHas anyone in your family ever had diabates? Type 'Yes'or 'No':"), input("\nHas anyone in your family ever had any form of cancer? Type 'Yes or 'No':"), input("\nHas anyone in your family ever had alzheimers? Type 'Yes' or 'No':")]

if familyhist[0]=="Yes":
    totalRisk+=10
if familyhist[1]=="Yes":
    totalRisk+=10
if familyhist[2]=="Yes":
    totalRisk+=10

#Calculating Total Risk and Insurability
if totalRisk<=20:
    print("You are at low risk")
elif totalRisk<=50:
    print("You are at moderate risk")
elif totalRisk<=75:
    print("You are at high risk and need to stop eating")
else:
    print("You are uninsurable and need to work out")