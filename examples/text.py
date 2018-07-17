from guizero import App, Text, Box

app = App()
box = Box(app)
box.width = 300
box2 = Box(box)

text = Text(box2)
#text.width = 10
text.value = "hello\ngoodbye\nno way\nthis is a very long stream of text, very long indeed, the best long line of text, its super bigly and very long, I dont think it could possibly be any better particularly as it was created by someone who is super good at creating long lines of text."
#text.wrap = True
#text.justify = "left"
print(app.tk.winfo_reqwidth()) 
#print(text._get_master_width(text.master))
# print(text.width)
# print(text.master.width)
# text._set_tk_config("wraplength", text.master.width)
# print(text.tk.keys())
# print(text.tk["wraplength"])
# print(text._has_tk_config("wraplength"))

app.display()