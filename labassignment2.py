from tkinter import Tk, Label, PhotoImage

root = Tk()

#Load image
photo = PhotoImage(file="C:\\Users\\jayju\\OneDrive\\Pictures\\Shaniyah1.png")

#Reduce image size
small_image = photo.subsample(5, 5)  # Scale down (adjust numbers if needed)

#Create label and display image
label = Label(master=root, image=small_image)
label.pack()
label1 = Label(root, text="Here is my Shaniyah, The one I love the most",font='Helvetica')

root.mainloop()