#color theme maker python tkinter project


#import tkinter gui framework
from cgitb import text
from textwrap import fill
import tkinter
from tkinter.ttk import LabelFrame
from tkinter import *
from turtle import color

#define root window
root = tkinter.Tk()
root.title("Cody's Color Picker")
root.geometry("600x700")
root.resizable(0,0)

#define fonts and colors
#none, we're using system defaults

#define functions

'''red slider function'''
def getred(slidervalue):
    '''turn current slider value for red into a hex value'''
    #the scale value is passed automatically when the scale is moved calling the getred function
    global redvalue

    #turn slider value into an int and then hex value. Stirp leading characters so only two remain
    redvalue = hex(int(slidervalue))
    redvalue = redvalue.lstrip("0x")

    #if hex value is single digit, lead with azero such that d becomes 0d
    while len(redvalue) < 2:
        redvalue = "0" + str(redvalue)

    updatecolor()


'''green slider fiunction'''
def getgreen(slidervalue):
    '''turn current slider value for green into a hex value'''
    #the scale value is passed automatically when the scale is moved calling the getgreen function
    global greenvalue

    #turn slider value into an int and then hex value. Stirp leading characters so only two remain
    greenvalue = hex(int(slidervalue))
    greenvalue = greenvalue.lstrip("0x")

    #if hex value is single digit, lead with azero such that d becomes 0d
    while len(greenvalue) < 2:
        greenvalue = "0" + str(greenvalue)
    updatecolor()

'''blue slider function'''
def getblue(slidervalue):
    '''turn current slider value for blue into a hex value'''
    #the scale value is passed automatically when the scale is moved calling the getblue function
    global bluevalue

    #turn slider value into an int and then hex value. Stirp leading characters so only two remain
    bluevalue = hex(int(slidervalue))
    bluevalue = bluevalue.lstrip("0x")

    #if hex value is single digit, lead with azero such that d becomes 0d
    while len(bluevalue) < 2:
        bluevalue = "0" + str(bluevalue)
    updatecolor()



def updatecolor():
    #update the current color box based on the slider values
    #display tuple and hex values of the current color
    #make the colorbox smaller than the origianl due to ipadx and iapdy on the orignial color box
    colorbox = tkinter. Label(inputframe, bg="#" + redvalue + greenvalue + bluevalue, height=6, width=15)
    colorbox.grid(row=1, column=3, columnspan=2, padx=35, pady=10)

    #display the tuple and hex value for the given color
    colortuple.config(text="(" + str(redslider.get()) + ")" + "(" + str(greenslider.get()) + ")" + "(" + str(blueslider.get()) + ")")
    colorhex.config(text="#" + redvalue + greenvalue + bluevalue)



def setcolor(r, g, b):
    '''set a given color'''
    redslider.set(r)
    greenslider.set(g)
    blueslider.set(b)


def storecolor():
    '''store the current color tuple value and display color'''
    storedred = redslider.get()
    storedgreen = greenslider.get()
    storedblue = blueslider.get()


    #create new widgets for stored color
    recallbutton = tkinter.Button(outputframe, text="Recall Color", command=lambda:setcolor(storedred, storedgreen, storedblue))
    newcolortuple = tkinter.Label(outputframe, text="(" + str(redslider.get()) + ")" + "(" + str(greenslider.get()) + ")" + "(" + str(blueslider.get()) + ")")
    newcolorhex = tkinter.Label(outputframe, text="#" + redvalue + greenvalue + bluevalue)
    newcolorblackbox = tkinter.Label(outputframe, bg="black", width=3, height=1)
    newcolorbox = tkinter.Label(outputframe, bg="#" + redvalue + greenvalue + bluevalue, width=3, height=1)

    #put new widgets on thescreen
    recallbutton.grid(row=storedcolor.get(), column=1, padx=20)
    newcolortuple.grid(row=storedcolor.get(), column=2, padx=20)
    newcolorhex.grid(row=storedcolor.get(), column=3, padx=20)
    newcolorblackbox.grid(row=storedcolor.get(), column=4, ipadx=5, ipady=5)
    newcolorbox.grid(row=storedcolor.get(), column=4)






#define layout
inputframe = tkinter.LabelFrame(root, padx=5, pady=5)
outputframe = tkinter.LabelFrame(root, padx=5, pady=5)
inputframe.pack(fill=BOTH, expand=True, padx=5, pady=5)
outputframe.pack(fill=BOTH, expand=True, padx=5, pady=5)


#setting up the input frame 
#create the labels, sliders, and buttons for each color: R, G, B

'''red'''
redlabel = tkinter.Label(inputframe, text="R")
redslider = tkinter.Scale(inputframe, from_=0, to=255, command=getred)
redbutton = tkinter.Button(inputframe, text="Red", command=lambda:setcolor(255,0,0))
'''green'''
greenlabel = tkinter.Label(inputframe, text="G")
greenslider = tkinter.Scale(inputframe, from_=0, to=255, command=getgreen)
greenbutton = tkinter.Button(inputframe, text="Green", command=lambda:setcolor(0,255,0))
'''blue'''
bluelabel = tkinter.Label(inputframe, text="B")
blueslider = tkinter.Scale(inputframe, from_=0, to=255, command=getblue)
bluebutton = tkinter.Button(inputframe, text="Blue", command=lambda:setcolor(0,0,255))

#create buttons for wach complementary color
yellowbutton = tkinter.Button(inputframe, text="Yellow", command=lambda:setcolor(255,255,0))
cyanbutton = tkinter.Button(inputframe, text="Cyan", command=lambda:setcolor(0,255,255))
magentabutton = tkinter.Button(inputframe, text="Magenta", command=lambda:setcolor(255,0,255))

#create utility buttons
storebutton = tkinter.Button(inputframe, text="Store Color", command=storecolor())
savebutton = tkinter.Button(inputframe, text="Save")
quitbutton = tkinter.Button(inputframe, text="Quit", command=root.destroy)

#put labels sliders and buttons onto the frame (use ipadx with rgb buttons to define column width, then use stick on others to fill out column)
'''red stuff'''
redlabel.grid(row=0, column=0, sticky="W")
redslider.grid(row=1, column=0, sticky="W")
redbutton.grid(row=2, column=0, padx=1, pady=1, ipadx=20)
'''green stuff'''
greenlabel.grid(row=0, column=1, sticky="W")
greenslider.grid(row=1, column=1, sticky="W")
greenbutton.grid(row=2, column=1, padx=1, pady=1, ipadx=15)
'''blue stuff'''
bluelabel.grid(row=0, column=2, sticky="W")
blueslider.grid(row=1, column=2, sticky="W")
bluebutton.grid(row=2, column=2, padx=1, pady=1, ipadx=18)
'''yellow'''
yellowbutton.grid(row=3, column=0, padx=1, pady=1, sticky="WE")
'''cyan'''
cyanbutton.grid(row=3, column=1, padx=1, pady=1, sticky="WE")
'''magenta'''
magentabutton.grid(row=3, column=2, padx=1, pady=1, sticky="WE")
'''store button'''
storebutton.grid(row=4, column=0, columnspan=3, padx=1, pady=1, sticky="WE")
'''save button'''
savebutton.grid(row=4, column=3, padx=1, pady=1, sticky="WE")
'''quit button'''
quitbutton.grid(row=4, column=4, padx=1, pady=1, sticky="WE")


#create the color box and color labels
colorbox = tkinter.Label(inputframe, bg="black", height=6, width=15)
colortuple = tkinter.Label(inputframe, text="(0), (0), (0)")
colorhex = tkinter.Label(inputframe, text="#000000")

#put the colorbox and labels on the frame
colorbox.grid(row=1, column=3, columnspan=2, padx=35, pady=10, ipadx=10, ipady=10)
colortuple.grid(row=2, column=3, columnspan=2)
colorhex.grid(row=3, column=3, columnspan=2)

#setting up the output frame
#initialize the dictionary to hold all storage colors
storedcolors = {}
storedcolor = IntVar()

#create radio buttons to select stored colors and populate each row with placeholder values
for i in range(6):
    radio = tkinter.Radiobutton(outputframe, variable=storedcolor, value=i)
    radio.grid(row=i, column=0, sticky="W")

    recallbutton = tkinter.Button(outputframe, text="Recall Color", state=DISABLED)
    newcolortuple = tkinter.Label(outputframe, text="(255), (255), (255)")
    newcolorhex = tkinter.Label(outputframe, text="#ffffff")
    newcolorblackbox = tkinter.Label(outputframe, bg="black", width=3, height=1)
    newcolorbox = tkinter.Label(outputframe, bg="white", width=3, height=1)
    recallbutton.grid(row=i, column=1, padx=20)
    newcolortuple.grid(row=i, column=2, padx=20)
    newcolorhex.grid(row=i, column=3, padx=20)
    newcolorblackbox.grid(row=i, column=4, pady=2, ipadx=5, ipady=5)
    newcolorbox.grid(row=i, column=4)

    #.cget() returns the value of a specific option. srtore the value of the tuple label and hex label
    storedcolors[storedcolor.get()] = [newcolortuple.cget("text"), newcolorhex.cget("text")]

#initialize the starting values for the colorbox display
redvalue = "00"
greenvalue = "00"
bluevalue = "00"


#run root window's main loop
root.mainloop()