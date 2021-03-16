# Import QRCode from pyqrcode 
from tkinter import *
import pyqrcode 
import png 
from pyqrcode import QRCode 
def qR():
   
        # String which represents the QR code 
    s = "https://github.com/aniket941"
    
    # Generate QR code 
    url = pyqrcode.create(s) 
    
    # Create and save the svg file naming "myqr.svg" 
    url.svg("myqr.svg", scale = 8) 
    
    # Create and save the png file naming "myqr.png" 
    url.png('myqr.png', scale = 6) 
        
    

w=Tk()
w.geometry('600x700')



qr=Button(w,text="QRgeerator",command=qR)
qr.place(x=20,y=40)
w.mainloop()