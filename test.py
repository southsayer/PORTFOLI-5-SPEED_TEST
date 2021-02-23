from tkinter import *
TEXT="Text items can display a block of text. Positioning the text works the same as with image items. Specify the text to display using the text attribute. All of the text in the item will have the same color (specified by the fill attribute) and the same font (specified by a font attribute).The text item can display multiple lines of text if you embed \n in the text. Alternatively, you can have the item automatically wrapped into multiple lines by providing a width attribute to represent the maximum width of a line. The alignment of multiple lines of text can be set using the justify attribute, which can be one of left (the default), right, or center."

def entry_disable():
    user_input.config(state="disabled")
    user_typed_data = user_input.get()
    word_list = user_typed_data.split()
    actual_word_list=TEXT.split()
    i=0
    count=0
    for word in word_list:
        if word==actual_word_list[i]:
            count+=1
        i+=1
    output_label.config(text= f"Your WPM speed is={count}")
    output_label.place(x=150, y=370, width=250, height=20)

def word_counter():
    user_input.place(x=20, y=260, width=500, height=100)
    window.after(60000,entry_disable)

window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)
window.minsize(width=600, height=450)

canvas=Canvas(width=560,height=200,bg="grey75")
canvas.grid(row=0,column=0)
canvas.create_text(280,100,text=TEXT, fill="black", width=500)

start_button=Button(text="Start",command=word_counter)
start_button.grid(row=1,column=0, padx=20, pady=20)

user_input=Entry(width=80)
user_input.place_forget()

output_label=Label(text="Your WPM speed is=")
output_label.place_forget()

window.mainloop()