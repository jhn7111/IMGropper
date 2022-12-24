import os
import sys
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.messagebox

from PIL import ImageTk, Image

#Set var
start_flag = 0
out_count = 0
f_stk = 0
img = Image.new("RGB", (0, 0), color="#fff")
res_x = 0
res_y = 0
file = []

#Start app
window = tkinter.Tk()
window.title("IMGropper")
window.geometry("0x0+480+480")
#Set env
res_main = tkinter.simpledialog.askstring("Discription", "Resolution you want to work (Width x Length)", parent=window)
if(res_main == None):
    sys.exit()
res_output = tkinter.simpledialog.askstring("Discription","Output resolution (Width x Length", parent=window)
if(res_output == None):
    sys.exit()
dir_work = tkinter.filedialog.askdirectory(title="Select work folder", parent=window)
if(dir_work == ""):
    sys.exit()
elif "worked" not in os.listdir(dir_work):
    os.mkdir(dir_work + "/worked")
dir_out = dir_work + "/worked"

#Decipher inputed env
if(res_main == ''):
    main_rx = 1920
    main_ry = 1080
else:
    res_main = res_main.replace("x", " ")
    main_rx = int(res_main.split(' ')[0])
    main_ry = int(res_main.split(' ')[-1])
if(res_output == ''):
    out_rx = 480
    out_ry = 480
else:
    res_output = res_output.replace("x", " ")
    out_rx = int(res_output.split(' ')[0])
    out_ry = int(res_output.split(' ')[-1])

#Set init box
res_x = out_rx
res_y = out_ry
#Load photo
fi = os.listdir(dir_work)
for i in fi:
    if '.jpg' in i:
        file.append(i)
if(len(file) == 0):
    tkinter.messagebox.showinfo("Error", "The document is empty. Please check them or choose other document.")
    sys.exit()
#Set window size
window.geometry(str(main_rx) + 'x' + str(main_ry))
window.resizable(True, True)
#Set initial bg
timg = ImageTk.PhotoImage(img)
#Start Canvas
can = tkinter.Canvas(window,width= main_rx, height=main_ry)
can.pack()

#Canvas
def motion(event):
    x, y = event.x, event.y
    #print(x, y)
    can.delete('all')
    can.create_image(main_rx/2, main_ry/2, image=timg)
    can.create_rectangle(x - res_x/2, y - res_y/2, x + res_x/2, y + res_y/2)

def btn1(event):
    global out_count
    global res_x
    global res_y
    x, y = event.x, event.y
    imgToSave = img.crop((x - (main_rx-img.size[0])/2 - res_x/2, y - res_y/2, x - (main_rx-img.size[0])/2 + res_x/2, y + res_y/2))
    imgToSave.save(dir_out + '/' + str(out_count) +'.jpg')
    out_count += 1
    print(str(out_count))

def btn3(event):
    global f_stk
    global timg
    global img
    if f_stk < len(file) - 1:
        f_stk += 1
    else:
        tkinter.messagebox.showinfo("Discription", "You have ended. Saved in './worked'.", parent=window)
        window.quit()
    print(f_stk)
    img = Image.open(dir_work + '/' + file[f_stk])
    img = img.resize((int(img.size[0] * main_ry / img.size[1]), main_ry))
    timg = ImageTk.PhotoImage(img)

def btn4(event):
    global res_x
    global res_y
    if event.delta == 120:
        res_x += 0.03 * out_rx
        res_y += 0.03 * out_ry
    elif event.delta == -120:
        res_x -= 0.03 * out_rx
        res_y -= 0.03 * out_ry
    motion(event)

#Bind funtion
window.bind('<Motion>', motion)#mouse cordinate
window.bind('<Button-1>', btn1)#mouse left btn
window.bind('<Button-3>', btn3)#mouse right btn
window.bind("<MouseWheel>", btn4)#mouse wheel

#Do loop
window.mainloop()