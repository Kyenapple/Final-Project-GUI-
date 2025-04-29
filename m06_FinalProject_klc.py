# mo6 Final Project Update
# author - Kye Church
# Created 2025-04-24, Updated 2025-04-28 (klc)
# This GUI application will help workers keep track of a running number of bolts torqued 
# THIS IS A MESS RIGHT NOW EVERYTHING IS OUT OF ORDER// ALL OVER THE PLACE
# AI ASSISTANCE WAS USED and is properly annotated

# psuedo code
# import tkinter
# create top level window for area selection
# allow user to select area, delete window after selected
# start of torque count
    # user selects an engine to begin counting torques
    # torques are counted with each engine added

# import tkinter/ create top window
import tkinter as tk
from tkinter import Toplevel

# Create area selection window that pops up on top level
def areaSelectionWindow():
    # "Open area selection window."
    areaWindow = Toplevel()
    areaWindow.title("Area Selection")

    # Title label for user to select area. Using grid structure
    tk.Label(areaWindow, text="Please select your area: ").grid(row=0, column=0)

    # Create three buttons for three different areas
    # did research on how to use Lambda? I believe this would work best for this code?
    tk.Button(areaWindow, text="Cams and Gears Install", command=lambda: selectAreaOne(areaWindow)).grid(row=1, column=0)
    tk.Button(areaWindow, text="Front Housing Install", command=lambda: selectAreaTwo(areaWindow)).grid(row=1, column=1)
    tk.Button(areaWindow, text="Rear Housing Install", command=lambda: selectAreaThree(areaWindow)).grid(row=1, column=2)

# Set total bolts at 0 before counting
TOTALBOLTS = 0

# Start engine counts with specific bolt amounts for each engine type in each area 
engineCount = {
    "camsAndGears": {"LYM0000": 34, "JD70000": 34, "ZNL0000": 42},
    "frontHousing": {"LYM0000": 22, "JD70000": 22, "ZNL0000": 30},
    "rearHousing": {"LYM0000": 36, "JD70000": 36, "ZNL0000": 38},
}

# Set user area as an open string
yourArea = ""

# user select area pop up.
# USED COPILOT/ how to destroy/close a window... self explanitory after I looked it up
def selectArea(area, window):
    "Select area/ close window"
    global yourArea
    # set yourArea as selected area
    yourArea = area
    window.destroy()

    # print out users selected area to ensure correct area was chossen
    print(f"You selected area: {yourArea}")

# start of the main pop up. Add title
root = tk.Tk()
root.title("Bolt Torque Counter for 3500 Short Line")

# Insert total number of bolts torqued so far, 0 to start out. 
totalLabel = tk.Label(root, text="Total number of bolts torqed today: 0")
totalLabel

# Start main loop! yay! 
root.mainloop()


    
   
