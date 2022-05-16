import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
win = tk.Tk()
win.geometry('1200x800')
win.title(' Starpad ')
win.wm_iconbitmap('pad.ico')
# ----------------------------------------------Main Menu---------------------------------------------------------------

main_menu = tk.Menu(win)
# file icons------------------------------------------
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# edit icons--------------------------------------------
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)

# view icons----------------------------------------------
toolbar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

# color_theme---------------------------------------------------
light_default_color = tk.PhotoImage(file='icons2/light_default.png')
light_plus_color = tk.PhotoImage(file='icons2/light_plus.png')
dark_color = tk.PhotoImage(file='icons2/dark.png')
red_color = tk.PhotoImage(file='icons2/red.png')
monokai_color = tk.PhotoImage(file='icons2/monokai.png')
night_blue_color = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_color, light_plus_color, dark_color,
               red_color, monokai_color, night_blue_color)
color_dict = {  # ('text_color','bg_color')
    'light_default': ('#000000', '#ffffff'),
    'light_plus_default': ('#474747', '#e0e0e0'),
    'dark_default': ('#c4c4c4', '#2d2d2d'),
    'red_default': ('#2d2d2d', '#ffe8e8'),
    'monokai_default': ('#d3b774', '#474747'),
    'night_blue_default': ('#ededed', '#6b9dc2')
}

# cascade-------------------------------------------
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

# **********************************************************************************************************************

# ----------------------------------------------Tool Bar---------------------------------------------------------------
tool_bar = ttk.Label(win)
tool_bar.pack(side=tk.TOP, fill=tk.X)
# font box-----------------------------
font_tuple = font.families()
font_family = tk.StringVar()    # variables
font_box = ttk.Combobox(
    tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)
# size box----------------------------
size_var = tk.IntVar()
font_size = ttk.Combobox(
    tool_bar, width=15, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(4, 81))
font_size.current(8)
font_size.grid(row=0, column=1, padx=2.5)
# bold button------------------------
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=1)
# italic button ----------------------
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=1)
# underline button---------------------
underln_icon = tk.PhotoImage(file='icons2/underline.png')
underln_btn = ttk.Button(tool_bar, image=underln_icon)
underln_btn.grid(row=0, column=4, padx=1)
# font_color button---------------------
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=1)
# align left button
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=1)
# align left button
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=1)
# align left button
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=1)
# **********************************************************************************************************************


# --------------------------------------------Text Editor---------------------------------------------------------------
text_editor = tk.Text(win)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality----------------------------
current_fontfamily = 'Arial'
current_font_size = 12


def change_font(event=None):
    global current_fontfamily
    current_fontfamily = font_family.get()
    text_editor.configure(font=(current_fontfamily, current_font_size))


def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_fontfamily, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

# bold button functionality---------------------------------------


def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)

# italic button functionality---------------------------------------


def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'roman'))


italic_btn.configure(command=change_italic)

# underline button functionality---------------------------------------


def change_underln():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(
            font=(current_fontfamily, current_font_size, 'normal'))


underln_btn.configure(command=change_underln)

# change font_color functionality--------------------------------------


def change_fontcolor():
    color_var = tk.colorchooser.askcolor()
    # print(color_var) #((116.453125, 205.80078125, 203.79296875), '#74cdcb')
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_fontcolor)

# align left functionality----------------------------------------------


def alignleft():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=alignleft)

# align center functionality----------------------------------------------


def aligncenter():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=aligncenter)

# align right functionality----------------------------------------------


def alignright():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=alignright)

text_editor.configure(font=('Arial,12'))  # default font and font size
# **********************************************************************************************************************


# ----------------------------------------------Status Bar---------------------------------------------------------------
status_bar = ttk.Label(win, text='status bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)
# **********************************************************************************************************************


# ----------------------------------------------Main Menu functionality---------------------------------------------------------------
url = ''
# ******** FILE ***************
# New Functionality-------------------------------------------------------


def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


file.add_command(label='New', image=new_icon, compound=tk.LEFT,
                 accelerator='Ctrl+N', command=new_file)

# open Functionality-------------------------------------------------------


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))  #('custom files,*.pdf;*.pdf'),
    try:
        with open(url, 'r') as f:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, f.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))


file.add_command(label='open', image=open_icon, compound=tk.LEFT,
                 accelerator='Ctrl+O', command=open_file)

# save file functionality------------------------------------------------------------------------


def save_file(event=None):
    global url
    try:
        if url:  # if file already exist
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:  # otherwise create it and then save
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                ('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


file.add_command(label='save', image=save_icon, compound=tk.LEFT,
                 accelerator='Ctrl+S', command=save_file)

# save as functionality-------------------------------------------------------------------------


def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
            ('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='save_as', image=save_as_icon,
                 compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

# exit functionality


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                'Warning', 'Do you want to save the file ?')
            if mbox is True:  # if user select yes
                if url:  # if file already exist
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:  # otherwise create it and then save
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                        ('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:  # if user select no
                win.destroy()

        else:
            win.destroy()
    except:
        return


file.add_command(label='exit', image=exit_icon, compound=tk.LEFT,
                 accelerator='Ctrl+Q', command=exit_func)

# *********** EDIT  ******************
edit.add_command(label='copy', image=copy_icon, compound=tk.LEFT,
                 accelerator='Ctrl+C', command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='paste', image=paste_icon, compound=tk.LEFT,
                 accelerator='Ctrl+V', command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+K',
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='clear_all', image=clear_all_icon, compound=tk.LEFT,
                 accelerator='Ctrl+Alt+X', command=lambda: text_editor.delete(1.0, tk.END))


def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    'match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label = ttk.Label(find_frame, text='Replace')
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry
    find_input = ttk.Entry(find_frame, width=30)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input = ttk.Entry(find_frame, width=30)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


edit.add_command(label='find', image=find_icon, compound=tk.LEFT,
                 accelerator='Ctrl+F', command=find_func)

# creating checkbutton

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool_bar', onvalue=True, offvalue=False, variable=show_toolbar, image=toolbar_icon, compound=tk.LEFT,
                     command=hide_toolbar)
view.add_checkbutton(label='Status_bar', onvalue=True, offvalue=False, variable=show_statusbar, image=statusbar_icon, compound=tk.LEFT,
                     command=hide_statusbar)

# Color Theme functionality


def change_theme():
    choose_theme = theme_choice.get()
    color_tuple = color_dict.get(choose_theme)
    (fg_color, bg_color) = (color_tuple[0], color_tuple[1])
    text_editor.config(background=bg_color, fg=fg_color)


# creating radio buttons
count = 0
for i in color_dict:
    color_theme.add_radiobutton(
        label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1

# **********************************************************************************************************************
win.config(menu=main_menu)

# binding short cut keys
win.bind("<Control-n>", new_file)
win.bind("<Control-o>", open_file)
win.bind("<Control-s>", save_file)
win.bind("<Control-Alt-s>", save_as)
win.bind("<Control-q>", exit_func)
win.bind("<Control-f>", find_func)

win.mainloop()
