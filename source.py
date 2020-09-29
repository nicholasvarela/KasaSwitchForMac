import asyncio
import PySimpleGUI as sg
from kasa import SmartPlug

sg.theme("DarkTeal9")
p = SmartPlug("192.168.0.10") # hard coded for the testing

async def status(): #gets the inital status of light swtich on start

    await p.update()
    
    return p.is_on
def translateBool(inputB):
    
    if(inputB):
        return " On"
    else: 
        return " Off"
script = "The Switch is"
status1 = translateBool(asyncio.run(status()))

async def on():
    await p.update()
    
    await p.turn_on()
async def off():
    await p.update()
    await p.turn_off()


def startGui():
    
    layout = [[sg.Text(), sg.Text(size=(15,1), key = '-OUTPUT-')] , 
    [sg.Button("ON"), sg.Button("OFF")]]
    

    window = sg.Window("Light Switch", layout)
    event, values = window.read()
    while True:
        status1 = translateBool(asyncio.run(status()))
        window['-OUTPUT-'].update(script + status1)
        event, values = window.read()
        # End program if user closes window or
        # presses the OK buttons
        if event == "ON":
            asyncio.run(on())
        if event == "OFF":
            asyncio.run(off())
        if event == sg.WIN_CLOSED:
            break
        status1 = translateBool(asyncio.run(status()))
        window['-OUTPUT-'].update(script + status1)
    window.close()

if __name__ == "__main__":
    startGui()
   

