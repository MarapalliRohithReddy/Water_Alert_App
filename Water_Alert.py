
#Alert for drinking water

import PySimpleGUI as sg
from datetime import datetime
from time import sleep

def my_function():
    layout = [[sg.Text("Take a sip of Water!!!", size=(30, 1),font=('Any 15'))], [sg.Button("OK",font=('Any 10'))] ,[sg.Button("STOP",font=('Any 10'))]]

# Create the window
    window = sg.Window("Water Alert!!", layout)

# Create an event loop
    while True:
        event, values = window.read()
    # End program if user closes window or
    # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break
        elif event == "STOP":
            New_layout = [[sg.Text("Are you sure want to close Application!!!!",font=('Any 15'))], [sg.Button("YES",font=('Any 10'))] ,[sg.Button("NO",font=('Any 10'))]]
            New_window = sg.Window("exit", New_layout)
            while True :
                New_event, values = New_window.read()
                if New_event == "YES" :
                   raise SystemExit
                elif New_event == "NO" or New_event == sg.WIN_CLOSED:
                    break
            New_window.close()
    
    window.close()

"""while datetime.now().minute not in {0, 15, 30, 45}:  # Wait 1 second until we are synced up with the 'every 15 minutes' clock
    sleep(1)
    
my_function()

while True:
    sleep(60*15)  # Wait for 15 minutes
    #sleep(5)  # Wait for 5 seconds
    my_function() """

while True :
    if datetime.now().minute in (0,15,30,45):
        my_function()
        sleep(60)
    sleep(1)