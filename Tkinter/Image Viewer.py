#this viewer works for many pic just open the pic and add it in the list below

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('this is the image shit')
root.iconbitmap('Image/Icon.png')

#defining the images and opening it(place gareko chiana ajjai)
img = ImageTk.PhotoImage(Image.open("Image/1st.jpg").resize((500,500), Image.ANTIALIAS)) # you can leave it as default size by removing the resize.
img1 = ImageTk.PhotoImage(Image.open("Image/Flower.jpeg").resize((500,500), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("Image/Second Flower.jpg").resize((500,500), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("Image/Third Flower.jpg").resize((500,500), Image.ANTIALIAS))


#keeping them in list so that it is useful in future
img_list = [img ,img1,img2,img3]

#making a status bar to display image number

status = Label(root, text="Image 1 of" + str(len(img_list)),bd = 1, relief = SUNKEN,anchor = E)

#keeping image in a label (image needs any weidget to stay in and i used label here)
label = Label(root,image = img)
label.grid(row= 0,column = 0,columnspan = 3)

#defining the funtions for the forward and backward movement of the viewer
def back(n):
    global label
    global button_front
    global button_back

    label.grid_forget()
    label = Label(image = img_list[n-1])
    button_front = Button(root, text=">>", command=lambda: forward(n + 1))
    button_back = Button(root,text ="<<", command =lambda : back(n-1))


    if n == 1:
        button_back = Button(root,text="<<",state = DISABLED)

    status = Label(root, text="Image" + str(n) + "of" + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    label.grid(row=0, column=0, columnspan=3)
    button_front.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def forward(n):
    global label
    global button_front
    global button_back

    label.grid_forget()
    label = Label(image = img_list[n-1])
    button_front = Button(root, text=">>", command=lambda: forward(n + 1))#this recursive method helps to run it each time the buttons is clicked
    button_back = Button(root,text ="<<", command =lambda : back(n-1))

    if n == len(img_list):#this is the condition to disable the button when the limit is reached
        button_front=Button(root,text =">>", state = DISABLED)

    status = Label(root, text="Image"+ str(n)+"of" + str(len(img_list)), bd=2, relief=SUNKEN, anchor=E)

    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    label.grid(row=0, column=0, columnspan=3)
    button_front.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


#defining the buttons and placing it
button_back = Button(root, text="<<",state = DISABLED)
button = Button(root,text= "exit", command = root.quit)
button_front = Button(root, text=">>",command = lambda:forward(2)) #sending one value first to work on it ...next recursion method is used for multiple input

button_back.grid(row = 1, column = 0)
button.grid(row=1,column=1,pady=10)
button_front.grid(row=1,column=2)
status.grid(row=2, column= 0, columnspan = 3, sticky = W+E)

root.mainloop()