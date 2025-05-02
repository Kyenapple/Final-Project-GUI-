# mo7 Final Project Update
# author - Kye Church
# Created 2025-04-24, Updated 2025-05-01 (klc)
# This GUI application will help workers keep track of a running number of bolts torqued 
# AI ASSISTANCE WAS USED AND IS ANNOTATED 

# psuedo code
# import tkinter
# create top level window for area selection
# select area
# loop for repeat engine selection
# close windows
# give total bolts and number of engines


# import tkinter/ create top window
import tkinter as tk
from tkinter import Toplevel

# Create variables (global, used throughout the entire code)
TOTALBOLTS = 0
yourArea = ""
shiftTotals = {}

# Start engine counts with specific bolt amounts for each engine type in each area 
engineCount = {
    "camsAndGears": {"LYM0000": 34, "JD70000": 34, "ZNL0000": 42},
    "frontHousing": {"LYM0000": 22, "JD70000": 22, "ZNL0000": 30},
    "rearHousing": {"LYM0000": 36, "JD70000": 36, "ZNL0000": 38},
}

# Create area selection window that pops up
def areaSelectionWindow(root):
    # Opens area selection window
    areaWindow = Toplevel(root)
    areaWindow.title("Area Selection")

    # Copilot used to add columnspan for longer text box! Title label for user to select area. Using grid structure
    tk.Label(areaWindow, text="Please select your area: ").grid(row=0, column=0, columnspan=3)

    # connect all names with code names
    areas = {
        "Cams and Gears Install": "camsAndGears",
        "Front Housing Install": "frontHousing",
        "Rear Housing Install": "rearHousing"
    }

    # format grid and button placement 
    counter = 0
    for label, area in areas.items():
        # when button is pressed it uses selectedArea to find correct information needed
        tk.Button(areaWindow, text=label, command=lambda a=area: selectArea(a, areaWindow, root)).grid(row=1, column= counter)
        # step up counter 
        counter += 1

# user area selection/ opens selection window
# USED COPILOT/ how to destroy/close a window... self explanitory after I looked it up
def selectArea(area, window, root):
    global yourArea
    # set yourArea as selected area
    yourArea = area
    # Closes window after selection has been made 
    window.destroy()

    # print out users selected area to ensure correct area was chossen
    print(f"You selected area: {yourArea}")
    engineSelectionWindow(root)

# opens new selection window
def engineSelectionWindow(root):
    # opens engine selection window,,, for repeat engine selection
    engineWindow = Toplevel(root)
    # opens another window with this title "" 
    engineWindow.title("Please select one of the three engine types!")
    tk.Label(engineWindow, text="Please select one of the three engine types!").grid(row=0, column=0)

    # set new counter for button at start of loop
    counter = 0

    # arrange buttons in {name} {# of bolts} for ease of use sarts loop
    for engineName, bolts in engineCount[yourArea].items():
        buttonName = f"{engineName} ({bolts} bolts)"
        tk.Button(engineWindow, text=buttonName, command=lambda e=engineName: addEngine(e, root)).grid(row=1, column=counter)
        # add a step counter to ensure theres a new colomn each new button added 
        counter +=1 
    # Make an end shift button that allows users to stop inputting engines and gain their totals
    tk.Button(engineWindow, text="End Of Shift", command=lambda: endShift(engineWindow, root)).grid(row=2, column=1)

# used to add to bolt torque count when engine is added
def addEngine(engineName, root):
    global TOTALBOLTS, shiftTotals
    # user check for engine in shift Totals, if not
    if engineName not in shiftTotals:
        shiftTotals[engineName] = 0
    # increase engine count by 1 each selected button
    shiftTotals[engineName] += 1

    # adds bolt count from selected engine
    TOTALBOLTS += engineCount[yourArea][engineName]

    # COPILOT USED TO CONFIGURE THIS. updates total label to new total 
    totalLabel.config(text=f"Total number of bolts torqued this shift: {TOTALBOLTS}")
    print(f"You completed a(n) {engineName} : {shiftTotals[engineName]} times this shift")
    
# allows employee to stop entering engines and stop their day
def endShift(window, root):
    # closes engine selection window
    window.destroy()

    # opens new window for summary// title
    summaryWindow = Toplevel(root)
    summaryWindow.title("Your summary for today: ")

    # initial value for summary
    summary = ""
    # loop for finding correct counts and totals using string
    for engineName, count in shiftTotals.items():
        totalBolts = count * engineCount[yourArea][engineName]
        summary += f"{engineName}: {count} times ({totalBolts} bolts torqued)"
    # adds all bolts for final bolt torque count
    summary += f"Total bolts torqued today: {TOTALBOLTS}"

    # UTILIZED COPILOT TO ASSIST WITH A CLOSING STATEMENT SUMMARY AND CLOSE BUTTON
    tk.Label(summaryWindow, text=summary,justify="left").pack(padx=20, pady=10)
    tk.Button(summaryWindow, text="Close", command=summaryWindow.destroy).pack(pady=10)

# Main loop setup// main window// title
root = tk.Tk()
root.title("Welcome to your Bolt Torque Counter for the 3500 Short Line!")


# COPILOT USED to assist with creating a label for total bolts displayed in the main window
totalLabel = tk.Label(root, text="Total bolts torqued today = 0")
totalLabel.pack()

# Opens main loop window first 
areaSelectionWindow(root)
# start main loop
root.mainloop()
           
    

   
