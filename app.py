import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, font, colorchooser, filedialog
import os

# title and size
root=tk.Tk()
root.geometry('1200x900')
root.title('App')

# icon
root.wm_iconbitmap('icon.ico')

# **************************** menu*****************************
main_menu=tk.Menu(root)
file_menu=tk.Menu(main_menu,tearoff=0)
edit_menu=tk.Menu(main_menu,tearoff=0)
view_menu=tk.Menu(main_menu,tearoff=0)
color_menu=tk.Menu(main_menu,tearoff=0)


# add item in a drop down
# file icon
new_file_icon=tk.PhotoImage(file='icons2/new.png')
open_file_icon=tk.PhotoImage(file='icons2/open.png')
save_file_icon=tk.PhotoImage(file='icons2/save.png')
saveas_file_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_file_icon=tk.PhotoImage(file='icons2/exit.png')

# edit icon
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

# view icon
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

# color icon
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

# add radio because at the time only one color is used 
# color menu instead mainly we used loop 
# color_menu.add_radiobutton(label='Light Default',compound=tk.LEFT,image=light_default_icon,command=func)
# color_menu.add_radiobutton(label='Dark',compound=tk.LEFT,image=dark_icon,command=func)
# color_menu.add_radiobutton(label='Blue',compound=tk.LEFT,image=night_blue_icon,command=func)
# color_menu.add_radiobutton(label='Red',compound=tk.LEFT,image=red_icon,command=func)

# add dropdown in a menu cascade
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Color Theme',menu=color_menu)

# *******************end menu*************************

# ********************tool menu**************************
# label frame widget
tool_bar=ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font family
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0)

# font size
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81,2))
font_size.current(3)
font_size.grid(row=0,column=1)

# bold 
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

# italic 
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

# underline
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# font color
font_icon=tk.PhotoImage(file='icons2/font_color.png')
font_clr_btn=ttk.Button(tool_bar,image=font_icon)
font_clr_btn.grid(row=0,column=5,padx=5)

# align left
align_lt_icon=tk.PhotoImage(file='icons2/align_left.png')
align_lt_btn=ttk.Button(tool_bar,image=align_lt_icon)
align_lt_btn.grid(row=0,column=6,padx=5)

# align center
align_ct_icon=tk.PhotoImage(file='icons2/align_center.png')
align_ct_btn=ttk.Button(tool_bar,image=align_ct_icon)
align_ct_btn.grid(row=0,column=7,padx=5)

# align right
align_rt_icon=tk.PhotoImage(file='icons2/align_right.png')
align_rt_btn=ttk.Button(tool_bar,image=align_rt_icon)
align_rt_btn.grid(row=0,column=8,padx=5)

# ***************end tool menu******************


# ***************text editor******************
text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)

#   scroll bar 
scroll_bar=tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family='Arial'
current_font_size=14

# default setting
text_editor.configure(font=('Arial',14))

# function for change font family
def change_font(event=None):
   global current_font_family
   current_font_family=font_family.get()
   # without using font-size in a font show unexpected error
   text_editor.configure(font=(current_font_family,current_font_size))
font_box.bind('<<ComboboxSelected>>',change_font)

# function for change font size
def change_size(root):
   global current_font_size
   current_font_size=size_var.get()
   text_editor.configure(font=(current_font_family,current_font_size))
font_size.bind('<<ComboboxSelected>>',change_size)
  
# bold functionality
# print(tk.font.Font(font=text_editor['font']).actual())--gives output-->{'family': 'Arial', 'size': 14, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
def bold_action():
   text_property=tk.font.Font(font=text_editor['font']).actual()
   if text_property['weight']=='normal':
      text_editor.configure(font=(current_font_family,current_font_size,'bold'))
   if text_property['weight']=='bold':
      text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=bold_action)

# italic functionality
def italic_action():
   text_property=tk.font.Font(font=text_editor['font']).actual()
   if text_property['slant']=='roman':
      text_editor.configure(font=(current_font_family,current_font_size,'italic'))
   if text_property['slant']=='italic':
      text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=italic_action)

# underline action functionality
def underline_action():
   text_property=tk.font.Font(font=text_editor['font']).actual()
   if text_property['underline']==0:
      text_editor.configure(font=(current_font_family,current_font_size,'underline'))
   if text_property['underline']==1:
      text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=underline_action)

# font color functionality
def font_color_action():
   color_var=tk.colorchooser.askcolor()
   # print(color_var)--> output-->((128.5, 0.0, 128.5), '#800080')
   # fg means foreground and action in text
   text_editor.configure(fg=color_var[1])
font_clr_btn.configure(command=font_color_action)

# align left functionality--> in this we store all text in any variable after that dlt all content and add according to align function.
def align_left_action():
   # 1.0,'end'--> it means we want to all content start with 1 and end with end
   text_content=text_editor.get(1.0,'end')
   text_editor.tag_config('left',justify=tk.LEFT)
   text_editor.delete(1.0,tk.END)
   text_editor.insert(tk.INSERT,text_content,'left')
align_lt_btn.configure(command=align_left_action)

# align center functionality
def align_center_action():
   # 1.0,'end'--> it means we want to all content start with 1 and end with end
   text_content=text_editor.get(1.0,'end')
   text_editor.tag_config('center',justify=tk.CENTER)
   text_editor.delete(1.0,tk.END)
   text_editor.insert(tk.INSERT,text_content,'center')
align_ct_btn.configure(command=align_center_action)

# align right functionality
def align_right_action():
   # 1.0,'end'--> it means we want to all content start with 1 and end with end
   text_content=text_editor.get(1.0,'end')
   text_editor.tag_config('right',justify=tk.RIGHT)
   text_editor.delete(1.0,tk.END)
   text_editor.insert(tk.INSERT,text_content,'right')
align_rt_btn.configure(command=align_right_action)

# ***************end text editor******************


# ***************main status bar******************
status_bar=ttk.Label(root,text='Status bar')
status_bar.pack(side=tk.BOTTOM)

# functionality
text_change=False
def status_show(event=None):
   global text_change
   # edit_modified is a function to check any update or not
   if text_editor.edit_modified():
      # it also add new line so we use this end-1c
      text_change=True
      words_count=len(text_editor.get(1.0,'end-1c').split())
      # if we want to space not count in a character we use (1.0,'end-1c').replace(' ','')
      character_count=len(text_editor.get(1.0,'end-1c'))
      status_bar.config(text=f"Words: {words_count} and characters: {character_count}")
   text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',status_show)

# ***************end main status bar*******************


# **************main menu functionallity******************

# variablee
# file exist checking by url if url exist so file exist otherwise not
url=''

# new file functionality
def new_file_action(event=None):
   global url
   url=''
   text_editor.delete(1.0,tk.END)

# open functionality
def open_file_action(event=None):
   global url
   # dont change *.* file icon otherwise is not properly work
   url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File' , '*.txt'),('All Files' , '*.*')))
   try:
      with open(url,'r') as fp:
         text_editor.delete(1.0,tk.END)
         text_editor.insert(1.0,fp.read())
   except FileNotFoundError:
      return
   except:
      return
   root.title(os.path.basename(url))

# save file functionality
def save_file_action(event=None):
   global url
   try:
      if url:
         content=str(text_editor.get(1.0,tk.END))
         with open(url,'w',encoding='utf-8') as fp:
            fp.write(content)
      else:
         url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File' , '*.txt'),('All Files' , '*.*')))
         content2=text_editor.get(1.0,tk.END)
         url.write(content2)
         url.close()
   except:
      return

# save as functionality
def save_as_file_action(event=None):
   global url
   try:
      content=text_editor.get(1.0,tk.END)
      url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File' , '*.txt'),('All Files' , '*.*')))
      url.write(content)
      url.close()
   except:
      return

# exit functionality
def exit_file_action(event=None):
   global url,text_change
   try:
      if text_change:
         msgbox=messagebox.askyesnocancel('Warning','Do you want to save the file? ')
         if msgbox is True:
            if url:
               content=text_editor.get(1.0,tk.END)
               with open(url,'w',encoding='utf-8') as fp:
                  fp.write(content)
            else:
               content2=str(text_editor.get(1.0,tk.END))
               url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
               url.write(content2)
               url.close()
            root.destroy()
         elif msgbox is False:
            root.destroy()
      else:
         root.destroy()
   except:
      return


# compound=tk.left it icon move left and label in a right
file_menu.add_command(label='New',compound=tk.LEFT,image=new_file_icon,accelerator='Ctrl+N', command=new_file_action)
file_menu.add_command(label='Open',compound=tk.LEFT,image=open_file_icon,accelerator='Ctrl+O',command=open_file_action)
file_menu.add_command(label='Save',compound=tk.LEFT,image=save_file_icon,accelerator='Ctrl+S',command=save_file_action)
file_menu.add_command(label='Save As',compound=tk.LEFT,image= saveas_file_icon,accelerator='Ctrl+Alt+S',command= save_as_file_action)
file_menu.add_command(label='Exit',compound=tk.LEFT,image=exit_file_icon,accelerator='Ctrl+Q',command=exit_file_action)

# find functionality --> also use find and save in a list
def find_text_action(event=None):

   def find_action():
      word=find_input.get()
      text_editor.tag_remove('match','1.0',tk.END)
      matches=0
      if word:
         start_pos='1.0'
         while True:
            start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
            if not start_pos:
               break;
            end_pos=f'{start_pos} + {len(word)}c'
            text_editor.tag_add('match',start_pos,end_pos)
            matches+=1
            start_pos=end_pos
            text_editor.tag_config('match',foreground='red',background='yellow')


   def replace_action():
      word=find_input.get()
      replace_word=replace_input.get()
      content=text_editor.get(1.0,tk.END)
      new_content=content.replace(word,replace_word)
      text_editor.delete(1.0,tk.END)
      text_editor.insert(1.0,new_content)

   # toplevel is a window
   find_dialogue=tk.Toplevel()
   # 450x250+500+200 size wdth*height and top left
   find_dialogue.geometry=('450x250+500+200')
   find_dialogue.title('Find')
   # further not resize a find frame
   find_dialogue.resizable(0,0)

   # frame
   find_frame=ttk.LabelFrame(find_dialogue ,text='Find/ Replace')
   find_frame.pack(pady=20,padx=20)

   # label
   find_text_label=ttk.Label(find_frame,text='Find : ')
   replace_text_label=ttk.Label(find_frame,text='Replace : ')

   # entry
   find_input=ttk.Entry(find_frame,width=20)
   replace_input=ttk.Entry(find_frame,width=20)

   # button
   find_btn=ttk.Button(find_frame,text='Find',command=find_action)
   replace_btn=ttk.Button(find_frame,text='Replace',command=replace_action)

   # label grid
   find_text_label.grid(row=0,column=0,padx=4,pady=4)
   replace_text_label.grid(row=1,column=0,padx=4,pady=4)

   # entry grid
   find_input.grid(row=0,column=1,padx=4,pady=4)
   replace_input.grid(row=1,column=1,padx=4,pady=4)

   # button grid
   find_btn.grid(row=2,column=0,padx=4,pady=4)
   replace_btn.grid(row=2,column=1,padx=4,pady=4)

   find_dialogue.mainloop()



# edit menu
edit_menu.add_command(label='Copy',compound=tk.LEFT,image=copy_icon,accelerator="Ctrl+C",command=lambda :text_editor.event_generate("<Control c>") )
edit_menu.add_command(label='Cut',compound=tk.LEFT,image=cut_icon,accelerator="Ctrl+X",command=lambda : text_editor.event_generate("<Control x>"))
edit_menu.add_command(label='Paste',compound=tk.LEFT,image=paste_icon,accelerator="Ctrl+V",command=lambda : text_editor.event_generate("<Control v>"))
edit_menu.add_command(label='Clear',compound=tk.LEFT,image=clear_all_icon,accelerator="Ctrl+Alt+X",command=lambda : text_editor.delete(1.0,tk.END))
edit_menu.add_command(label='Find',compound=tk.LEFT,image=find_icon,accelerator="Ctrl+F",command=find_text_action)

# view checkbar variable
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

# view functionality
# toolbar
def hide_tool_bar():
   global show_toolbar
   if show_toolbar:
      # it used for hide
      tool_bar.pack_forget()
      show_toolbar=False
   else:
      text_editor.pack_forget()
      status_bar.pack_forget()
      tool_bar.pack(side=tk.TOP,fill=tk.X)
      text_editor.pack(expand=True,fill=tk.BOTH)
      status_bar.pack(side=tk.BOTTOM)
      show_toolbar=True

# statusbar
def hide_status_bar():
   global show_statusbar
   if show_statusbar:
      status_bar.pack_forget()
      show_statusbar=False
   else:
      status_bar.pack(side=tk.BOTTOM)
      show_statusbar=True

# view menu
view_menu.add_checkbutton(label='Tool bar',compound=tk.LEFT,variable= show_toolbar, onvalue=True,offvalue=False, image=tool_bar_icon,command=hide_tool_bar)
view_menu.add_checkbutton(label='Side bar',compound=tk.LEFT,variable= show_statusbar, onvalue=True,offvalue=False ,image=status_bar_icon,command=hide_status_bar)

# color functionality
def change_theme_action():
   color_theme=theme_color_choice.get()
   color_tuple=color_dict.get(color_theme)
   fg_color,bg_color=color_tuple[0],color_tuple[1]
   text_editor.config(background=bg_color,fg=fg_color)

# color effect
theme_color_choice=tk.StringVar()
color_icons = (light_default_icon, dark_icon, red_icon, night_blue_icon)

color_dict = {
   # first is text color and second is background color
    'Light Default ' : ('#000000', '#ffffff'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Night Blue' :('#ededed', '#6b9dc2')
}
count=0
# loop
for i in color_dict:
   color_menu.add_radiobutton(label=i,image=color_icons[count],variable=theme_color_choice,compound=tk.LEFT,command= change_theme_action)
   count+=1

root.config(menu=main_menu)

# ***************end main menu functionallity******************

# *************************bind shortcut key******************

root.bind("<Control-n>",new_file_action)
root.bind("<Control-o>",open_file_action)
root.bind("<Control-s>",save_file_action)
root.bind("<Control-Alt-s>",save_as_file_action)
root.bind("<Control-q>",exit_file_action)
root.bind("<Control-f>",find_text_action)
root.bind("<Control-h>",find_text_action)

# *************************end bind shortcut key******************

root.mainloop()