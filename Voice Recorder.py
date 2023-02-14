from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv


#Window Properties
root=Tk()
root.geometry("600x600+400+80")
root.resizable(False, False)
root.title("e-Nunce8")
root.configure(background='#154c79')

# def RecButton():
#     while Record.temp>0:
#         record(foreground=('red'))
#     else:
#         record(foreground=('white'))

def Record():
    freq=44100
    duration=int(duration.get())
    recording=sound.rec(duration*freq,samplerate=freq,channels=2)

    try:
        temp=int(duration.get())
    except:
        print('Please enter a correct value')
    while temp>0:
        root.update()
        time.sleep(1)
        temp-= 1

        if (temp==0):
            messagebox.showinfo("time Countdown", "Recording Saved")
        Label(text=f"{str(temp)}",font='Calibri 40', width=4,background='#154c79').place(x=240, y=590)

    sound.wait()
    write('enunce8.wav',freq,recording)
#Window Icon
image_icon=PhotoImage(file="mic.png")
root.iconphoto(False,image_icon)

#Logo
photo=PhotoImage(file="record_blue.png")
myimage=Label(image=photo,background='#154c79')
myimage.pack(padx=5, pady=5)

#Name
Label(text="e-Nunce8", font='Candara 30 bold', background='#154c79', foreground='white').pack()
Label(text="by Josh", font='Candara 16', background='#154c79', foreground='white').pack(padx=2, pady=2)

#Entry Box
duration=StringVar()
entry=Entry(root,textvariable=duration,font="Calibri 20", width=15).pack(pady=10)
Label(text='Enter time in seconds', font='Calibri 14', background='#154c79', foreground='white').pack()


#Record Button
record=Button(root, font='Calibri, 20', text='Record', background='#111111', foreground='white', border=0, command=Record).pack(pady=30)







root.mainloop()