from tkinter import *
from tkinter import ttk, messagebox, font, filedialog, colorchooser
from PIL import Image, ImageTk
import time, win32api, pyttsx3, threading, webbrowser, PyPDF2, datetime
from fpdf import FPDF
class TextPad:
    def __init__(self, root):
        self.window = root
        self.window.title(f"TextPad")

        # This frame make to give right position
        mainframe = Frame(self.window, bg="white")
        mainframe.pack(pady=56)

        # Voice Control
        self.engine_control = pyttsx3.init('sapi5')
        self.engine_control.setProperty('rate', 130)


        # Varibales Initialization for particular account
        self.record_no = -1
        self.record_status = "Yes"
        self.saved_file_name = "New Document"
        self.searching_things_in_google = "Nothing To Show"
        self.send_msg_to_wp = "Nothing To Show"
        self.pdf_saved_file_name = "Nothing To Show"
        self.saved_file_name_in_google_drive = "Nothing To Show"


        # Font Family Variable Initialization
        self.font_family = StringVar()

        # Some Important variable initialization
        self.current_font_size = 20
        self.current_font = "Arial"
        self.get_time = -1

        # Instructional button Store for future use
        self.header_1_components = []
        self.header_2_components = []
        self.acc_components = []
        self.status_components = []

        # Some basic function call
        self.__writing_area()
        self.__header()
        self.__menu_decor()

    def __menu_decor(self):  # Menu decorating function
        global file_new_img, file_open_img, file_save_img, file_pdf_img, file_print_img, file_exit_img, edit_undo_img, edit_redo_img, edit_cut_img, edit_copy_img, edit_paste_img, edit_clear_img, view_find_img, view_replace_img, view_dark_img, view_light_img, customization_bold_img, customization_italic_img, customization_underline_img, customization_foreground_color_img, customization_background_color_img
        menu_control = Menu(self.window)
        self.window.config(menu=menu_control)

        # Image bringing for menu

        file_new_img = ImageTk.PhotoImage(Image.open("new_img.jpg").resize((30, 30), Image.LANCZOS))
        file_open_img = ImageTk.PhotoImage(Image.open("open_img.jpg").resize((30, 30), Image.LANCZOS))
        file_save_img = ImageTk.PhotoImage(Image.open("save_img.png").resize((30, 30), Image.LANCZOS))
        file_pdf_img = ImageTk.PhotoImage(Image.open("pdf_text.jpg").resize((30, 30), Image.LANCZOS))
        file_print_img = ImageTk.PhotoImage(Image.open("print_img.png").resize((30, 30), Image.LANCZOS))
        file_exit_img = ImageTk.PhotoImage(Image.open("exit_img.png").resize((30, 30), Image.LANCZOS))

        edit_undo_img = ImageTk.PhotoImage(Image.open("undo_img.jpg").resize((30, 30), Image.LANCZOS))
        edit_redo_img = ImageTk.PhotoImage(Image.open("redo_icon.png").resize((30, 30), Image.LANCZOS))
        edit_cut_img = ImageTk.PhotoImage(Image.open("cut_img.png").resize((30, 30), Image.LANCZOS))
        edit_copy_img = ImageTk.PhotoImage(Image.open("copy_img.jpg").resize((30, 30), Image.LANCZOS))
        edit_paste_img = ImageTk.PhotoImage(Image.open("paste_img.jpg").resize((30, 30), Image.LANCZOS))
        edit_clear_img = ImageTk.PhotoImage(Image.open("clear_img.png").resize((30, 30), Image.LANCZOS))

        view_find_img = ImageTk.PhotoImage(Image.open("magnifier.jpg").resize((30, 30), Image.LANCZOS))
        view_replace_img = ImageTk.PhotoImage(Image.open("replace_icon.png").resize((30, 30), Image.LANCZOS))
        view_dark_img = ImageTk.PhotoImage(Image.open("dark_mode_img.png").resize((30, 30), Image.LANCZOS))
        view_light_img = ImageTk.PhotoImage(Image.open("bulb_img.jpg").resize((30, 30), Image.LANCZOS))

        customization_bold_img = ImageTk.PhotoImage(Image.open("bold_img.jpg").resize((30, 30), Image.LANCZOS))
        customization_italic_img = ImageTk.PhotoImage(Image.open("italic_img.png").resize((30, 30), Image.LANCZOS))
        customization_underline_img = ImageTk.PhotoImage(
            Image.open("underline_img.png").resize((30, 30), Image.LANCZOS))
        customization_foreground_color_img = ImageTk.PhotoImage(
            Image.open("font_color.png").resize((30, 30), Image.LANCZOS))
        customization_background_color_img = ImageTk.PhotoImage(
            Image.open("background_color.png").resize((30, 30), Image.LANCZOS))

        # Menu Make
        self.file_menu = Menu(menu_control, tearoff=False)
        menu_control.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+N)", compound=LEFT,
                                   image=file_new_img, command=self.new_window)
        self.file_menu.add_command(label="Open", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+O)", compound=LEFT,
                                   image=file_open_img, command=self.open_another_file)
        self.file_menu.add_separator(background="paleturquoise")
        self.file_menu.add_command(label="Save", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), compound=LEFT, image=file_save_img,
                                   command=self.save)
        self.file_menu.add_command(label="Save As", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+S)", compound=LEFT,
                                   image=file_save_img, command=self.save_as)
        self.file_menu.add_command(label="Save File as PDF", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Alt+P)", compound=LEFT,
                                   image=file_pdf_img, command=self.save_file_as_pdf)
        self.file_menu.add_separator(background="paleturquoise")
        self.file_menu.add_command(label="Print", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+P)", compound=LEFT,
                                   image=file_print_img, command=self.print_a_file)
        self.file_menu.add_command(label="Exit", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="ESC", compound=LEFT,
                                   image=file_exit_img, command=self.take_exit)
        self.window.bind('<Control-Key-n>', self.new_window)
        self.window.bind('<Control-Key-o>', self.open_another_file)
        self.window.bind('<Control-Key-s>', self.save_as)
        self.window.bind('<Alt-p>', self.save_file_as_pdf)
        self.window.bind('<Control-Key-p>', self.print_a_file)
        self.window.bind('<Escape>', self.take_exit)

        self.edit_menu = Menu(menu_control, tearoff=False)
        menu_control.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+Z)", compound=LEFT,
                                   image=edit_undo_img, command=self.undo)
        self.edit_menu.add_command(label="Redo", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+Y)", compound=LEFT,
                                   image=edit_redo_img, command=self.redo)
        self.edit_menu.add_separator(background="paleturquoise")
        self.edit_menu.add_command(label="Cut", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+X)", compound=LEFT,
                                   image=edit_cut_img, command=self.cut)
        self.edit_menu.add_command(label="Copy", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+C)", compound=LEFT,
                                   image=edit_copy_img)
        self.edit_menu.add_command(label="Paste", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+V)", compound=LEFT,
                                   image=edit_paste_img, command=self.paste)
        self.edit_menu.add_separator(background="paleturquoise")
        self.edit_menu.add_command(label="Clear", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), compound=LEFT, image=edit_clear_img,
                                   command=self.clear)
        self.window.bind('<Control-Key-z>', self.undo)
        self.window.bind('<Control-Key-y>', self.undo)
        self.window.bind('<Control-Key-x>', self.cut)
        self.window.bind('<Control-Key-c>', self.copy)
        self.window.bind('<Control-Key-v>', self.paste)

        self.view_menu = Menu(menu_control, tearoff=False)
        menu_control.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Find", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+F)", compound=LEFT,
                                   image=view_find_img, command=self.find_UI)
        self.view_menu.add_command(label="Replace", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+R)", compound=LEFT,
                                   image=view_replace_img, command=self.replace_UI)
        self.view_menu.add_separator(background="paleturquoise")
        self.view_menu.add_command(label="Dark Mode", background="paleturquoise", foreground="black",
                                   activebackground="darkcyan", activeforeground="darkcyan",
                                   font=("Arial", 10, "bold", "italic"), compound=LEFT, image=view_dark_img,
                                   command=self.dark_mode)
        self.view_menu.add_command(label="Light Mode", background="paleturquoise", foreground="black",
                                   activebackground="black", activeforeground="paleturquoise",
                                   font=("Arial", 10, "bold", "italic"), compound=LEFT, image=view_light_img,
                                   command=self.light_mode)
        self.window.bind('<Control-Key-f>', self.find_UI)
        self.window.bind('<Control-Key-r>', self.replace_UI)

        self.customization_menu = Menu(menu_control, tearoff=False)
        menu_control.add_cascade(label="Customization", menu=self.customization_menu)
        self.customization_menu.add_command(label="Bold", background="paleturquoise", foreground="black",
                                            activebackground="black", activeforeground="paleturquoise",
                                            font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+B)", compound=LEFT,
                                            image=customization_bold_img, command=self.change_bold)
        self.customization_menu.add_command(label="Italics", background="paleturquoise", foreground="black",
                                            activebackground="black", activeforeground="paleturquoise",
                                            font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+I)", compound=LEFT,
                                            image=customization_italic_img, command=self.change_italic)
        self.customization_menu.add_command(label="Underline", background="paleturquoise", foreground="black",
                                            activebackground="black", activeforeground="paleturquoise",
                                            font=("Arial", 10, "bold", "italic"), accelerator="(Ctrl+U)", compound=LEFT,
                                            image=customization_underline_img, command=self.change_underline)
        self.customization_menu.add_separator(background="paleturquoise")
        self.customization_menu.add_command(label="Foreground-Color", background="paleturquoise", foreground="black",
                                            activebackground="black", activeforeground="paleturquoise",
                                            font=("Arial", 10, "bold", "italic"), accelerator="(Alt+F)", compound=LEFT,
                                            image=customization_foreground_color_img, command=self.change_fg_color)
        self.customization_menu.add_command(label="Background-Color", background="paleturquoise", foreground="black",
                                            activebackground="black", activeforeground="paleturquoise",
                                            font=("Arial", 10, "bold", "italic"), accelerator="(Alt+F)", compound=LEFT,
                                            image=customization_foreground_color_img, command=self.change_fg_color)
        self.window.bind('<Control-Key-b>', self.change_bold)
        self.window.bind('<Control-Key-r>', self.change_italic)
        self.window.bind('<Control-Key-u>', self.change_underline)
        self.window.bind('<Alt-f>', self.change_fg_color)
        self.window.bind('<Alt-b>', self.change_bg_color)

    def __header(self):
        self.header_1 = Frame(self.window, bg="darkcyan", relief=RAISED, bd=3, width=325, height=90)
        self.header_1.place(x=0, y=0)

        self.header_2 = Frame(self.window, bg="darkcyan", relief=RAISED, bd=3, width=260, height=90)
        self.header_2.place(x=325, y=0)

        self.header_3 = Frame(self.window, bg="darkcyan", relief=RAISED, bd=3, width=325, height=90)
        self.header_3.place(x=325 * 2 - 65, y=0)

        self.header_4 = Frame(self.window, bg="darkcyan", relief=RAISED, bd=3, width=305, height=90)
        self.header_4.place(x=325 * 3 - 65, y=0)

        self.acc = Frame(self.window, bg="darkcyan", relief=RAISED, bd=3, width=50 + 85, height=90)
        self.acc.place(x=325 * 4 - 85, y=0)

        # Every Header Portion call
        self.__header_1_decoration()
        self.__header_2_decoration()
        self.__header_3_decoration()
        self.__header_4_decoration()


    def __status(self):  # Status Section Make
        pass

    def __writing_area(self):  # Main Writing Space
        make_scroll_vertical = Scrollbar(self.window)
        make_scroll_vertical.pack(side=RIGHT, fill=Y)

        self.main_writing_space = Text(self.window, font=(self.current_font, self.current_font_size), relief=RAISED,
                                       bd=10, yscrollcommand=make_scroll_vertical.set, undo=True)
        self.main_writing_space.pack(fill=BOTH, expand=1, anchor=W)
        self.main_writing_space.focus()

        make_scroll_vertical.config(command=self.main_writing_space.yview)

    def __header_1_decoration(self):
        global l_img, m_img, r_img

        # Image bringing
        l_img = ImageTk.PhotoImage(Image.open("align.png").resize((50, 50), Image.LANCZOS))
        m_img = ImageTk.PhotoImage(Image.open("m_align.png").resize((50, 50), Image.LANCZOS))
        r_img = ImageTk.PhotoImage(Image.open("r_align.png").resize((50, 50), Image.LANCZOS))

        # Font Size Controller Scale
        font_size_controller = Scale(self.header_1, font=("Arial", 10, "bold"), width=15, orient=HORIZONTAL,
                                     background="green", from_=1, to=100,
                                     relief=RAISED, bd=2, command=self.change_font_size)
        font_size_controller.place(x=0, y=0)
        font_size_controller.set(self.current_font_size)

        # Make buttons
        l_align = Button(self.header_1, width=30, height=30, image=l_img, bg="black", relief=RAISED, bd=3,
                         command=self.make_align_left)
        l_align.place(x=110 + 20, y=2)

        m_align = Button(self.header_1, width=30, height=30, image=m_img, bg="black", relief=RAISED, bd=3,
                         command=self.make_align_center)
        m_align.place(x=110 + 90, y=2)

        r_align = Button(self.header_1, width=30, height=30, image=r_img, bg="black", relief=RAISED, bd=3,
                         command=self.make_align_right)
        r_align.place(x=280 - 10, y=2)

        # Instructional Label
        self.font_size_label = Label(self.header_1, text="Font Size", font=("Arial", 15, "bold"),bg="darkcyan",
                                     fg="black")
        self.font_size_label.place(x=5, y=50)
        self.alignment_label = Label(self.header_1, text="Alignment", font=("Arial", 15, "bold"), bg="darkcyan",
                                     fg="black")
        self.alignment_label.place(x=150 + 20, y=50)

        # Store instructional buttons
        self.header_1_components.append(font_size_controller)
        self.header_1_components.append(l_align)
        self.header_1_components.append(m_align)
        self.header_1_components.append(r_align)

    def __header_2_decoration(self):
        # Font Collection
        font_combobox = ttk.Combobox(self.header_2, width=30, values=font.families(), foreground="black",
                                     font=("Arial", 10, "bold"), state="readonly", textvariable=self.font_family)
        font_combobox.place(x=5 + 5, y=0)
        font_combobox.set("Arial")
        print(font_combobox.get())

        # Combobox Binding
        font_combobox.bind("<<ComboboxSelected>>", self.change_font_manually)

        # Background Color list
        select_bg_color = [1, 2, 3, 4, 5, 6]
        bg_color_combobox = ttk.Combobox(self.header_2, width=30, values=select_bg_color, foreground="black",
                                         font=("Arial", 10, "bold"), state="readonly")
        bg_color_combobox.place(x=5 + 5, y=30)
        bg_color_combobox.current(0)

        # Combobox Binding
        bg_color_combobox.bind("<<ComboboxSelected>>",
                               lambda e: self.change_line_space_to_selected_text(int(bg_color_combobox.get())))

        # Bullets list
        total_bullets = ["1   2   3", "#   #   #", "!   !   !", ">    >    >", "o   o   o"]
        bullet_collection = ttk.Combobox(self.header_2, width=30, values=total_bullets, foreground="darkcyan",
                                         font=("Arial", 10, "bold"), state="readonly", background="black")
        bullet_collection.place(x=5 + 5, y=60)
        bullet_collection.current(0)

        # Combobox Binding
        bullet_collection.bind("<<ComboboxSelected>>",
                               lambda e: self.add_bullet_in_selected_text(bullet_collection.get()))

        # Store instructional buttons
        self.header_2_components.append(font_combobox)
        self.header_2_components.append(bg_color_combobox)
        self.header_2_components.append(bullet_collection)

    def __header_3_decoration(self):
        global ts_img, u_img, lc_img, g_search_image, find_image_take, replace_image_take

        # Image bringing
        u_img = ImageTk.PhotoImage(Image.open("U.png").resize((50, 50), Image.LANCZOS))
        lc_img = ImageTk.PhotoImage(Image.open("L.png").resize((50, 50), Image.LANCZOS))
        g_search_image = ImageTk.PhotoImage(Image.open("g_search.png").resize((50, 50), Image.LANCZOS))
        find_image_take = ImageTk.PhotoImage(Image.open("magnifier.jpg").resize((50, 30), Image.LANCZOS))
        replace_image_take = ImageTk.PhotoImage(Image.open("replace_icon.png").resize((50, 30), Image.LANCZOS))

        # Instructional Buttons
        u_case = Button(self.header_3, width=35, height=30, image=u_img, bg="#00FF00", relief=RAISED, bd=3,
                        command=lambda: self.case_change('u'))
        u_case.place(x=25, y=0)

        l_case = Button(self.header_3, width=35, height=30, image=lc_img, bg="#00FF00", relief=RAISED, bd=3,
                        command=lambda: self.case_change('l'))
        l_case.place(x=140, y=0)


        w_mark = Button(self.header_3, width=35, height=30, image=g_search_image, bg="#00FF00", relief=RAISED, bd=3,
                        command=self.ui_for_searching)
        w_mark.place(x=250, y=0)

        g_search = Button(self.header_3, width=35, height=30, image=find_image_take, bg="#00FF00", relief=RAISED, bd=3,
                          command=self.find_UI)
        g_search.place(x=25, y=45)

        w_meaning = Button(self.header_3, width=35, height=30, image=replace_image_take, bg="#00FF00", relief=RAISED,
                           bd=3, command=self.replace_UI)
        w_meaning.place(x=145, y=45)

    def __header_4_decoration(self):
        global pdf_txt_img, dark_mode_img_take, wp_logo_img, wiki_img, light_mode_image, paint_image

        # Image Bringing
        pdf_txt_img = ImageTk.PhotoImage(Image.open("pdf_text_btn.jpg").resize((50, 50), Image.LANCZOS))
        dark_mode_img_take = ImageTk.PhotoImage(Image.open("dark_mode_img.png").resize((50, 50), Image.LANCZOS))
        wp_logo_img = ImageTk.PhotoImage(Image.open("wp_logo.jpg").resize((50, 50), Image.LANCZOS))
        wiki_img = ImageTk.PhotoImage(Image.open("wiki.png").resize((50, 50), Image.LANCZOS))
        light_mode_image = ImageTk.PhotoImage(Image.open("bulb_img.jpg").resize((40, 40), Image.LANCZOS))

        # Instructional buttons
        pdf_txt = Button(self.header_4, width=35, height=30, image=pdf_txt_img, font=("Arial", 11, "bold"),
                         bg="#00FF00", relief=RAISED, bd=3, command=self.pdf_to_text)
        pdf_txt.place(x=25, y=0)

        sg = Button(self.header_4, width=35, height=30, image=dark_mode_img_take, font=("Arial", 2, "bold"), bg="darkcyan",
                    relief=RAISED, bd=3, command=self.dark_mode)
        sg.place(x=125, y=0)

        g = Button(self.header_4, width=35, height=30, image=wp_logo_img, bg="green", relief=RAISED, bd=3,
                   command=self.send_msg_to_whatsapp)
        g.place(x=230, y=0)

        w = Button(self.header_4, width=35, height=30, image=wiki_img, font=("Arial", 11, "bold"), bg="#00FF00",
                   relief=RAISED, bd=3, command=self.open_wikipedia)
        w.place(x=25, y=45)

        ts = Button(self.header_4, width=35, height=30, image=light_mode_image, bg="white", relief=RAISED, bd=3,
               command=self.light_mode)
        ts.place(x=125, y=45)

    def __table_checking(self, all_result, acc_name):  # Checking Account name present or not in database
        take = []
        for x in all_result:
            take.append(x[0])
        take.sort()

        # Checking account named table present or not
        def binary_search_table_check(take_it, start, end, find_it):
            while start <= end:
                mid = int((start + end) / 2)
                if take_it[mid] == find_it:
                    return True
                elif find_it > take[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        return binary_search_table_check(take, 0, len(take) - 1, acc_name)


    def previous_tag_remove(self):
        for every in self.font_tag_name_store:
            self.main_writing_space.tag_remove(every[0], every[1], every[2])
        self.font_tag_name_store.clear()
        self.font_tag_counter = 0

        for every in self.fg_tag_name_store:
            self.main_writing_space.tag_remove(every[0], every[1], every[2])
        self.fg_tag_name_store.clear()
        self.fg_tag_counter = 0

        for every in self.bg_tag_name_store:
            self.main_writing_space.tag_remove(every[0], every[1], every[2])
        self.bg_tag_name_store.clear()
        self.bg_tag_counter = 0

    # New_Menu Configuration
    def new_window(self, e=None):
        take_response = messagebox.askyesno("New Window Conformation", "Do you want to open new Window?")
        if take_response:
            self.main_writing_space.delete(1.0, END)
            self.previous_tag_remove()
            self.window.title(f"TextPad          {self.saved_file_name}")
            if self.permission_to_update == 1:
                self.total_word_and_line_counter(None)

    def open_another_file(self, e=None):
        file_name = filedialog.askopenfilename(initialdir="\\Desktop", title="Select a file", filetypes=(
        ("Text Files", "*.txt"), ("C Files", "*.c"), ("CPP Files", "*.cpp"), ("Python Files", "*.py"),
        ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("JavaScript Files", "*.js")))
        if file_name:
            self.main_writing_space.delete(1.0, END)
            self.saved_file_name = file_name
            self.window.title(f"TextPad         {self.saved_file_name}")
            get_file = open(file_name, "r")
            get_text = get_file.read()
            self.main_writing_space.insert(END, get_text)
            get_file.close()
            if self.permission_to_update == 1:
                self.total_word_and_line_counter(None)

    def save(self, e=None):
        if self.saved_file_name == "New Document":
            self.save_as()
        else:
            take_file = open(self.saved_file_name, "w")
            take_text = self.main_writing_space.get(1.0, END)
            take_file.write(take_text)
            take_file.close()
            messagebox.showinfo("Saved", "Your file saved securely")

    def save_as(self, e=None):
        take_file_name = filedialog.asksaveasfilename(initialdir="\\Desktop", title="Save As", defaultextension=".txt",
                                                      filetypes=(("Text Files", "*.txt"), ("C Files", "*.c"),
                                                                 ("CPP Files", "*.cpp"), ("Python Files", "*.py"),
                                                                 ("HTML Files", "*.html"), ("CSS Files", "*.css"),
                                                                 ("JavaScript Files", "*.js")))
        if take_file_name:
            self.saved_file_name = take_file_name
            self.window.title(f"TextPad         {self.saved_file_name}")
            take_file = open(take_file_name, "w")
            take_text = self.main_writing_space.get(1.0, END)
            take_file.write(take_text)
            take_file.close()
            messagebox.showinfo("Successfully Saved", "Your file saved successfully")

    def save_file_as_pdf(self, e=None):
        self.main_writing_space.clipboard_clear()
        take_file_name = filedialog.asksaveasfilename(initialdir="\\Desktop",
                                                      title="Select location and name to save that file as PDF",
                                                      defaultextension=".pdf")
        if take_file_name:
            file_name_extract = take_file_name.split("/")

            if self.pdf_saved_file_name == "Nothing To Show":
                self.pdf_saved_file_name = file_name_extract[len(file_name_extract) - 1]
            else:
                self.pdf_saved_file_name += file_name_extract[len(file_name_extract) - 1]

            self.window.title(f"TextPad         {take_file_name}")
            pdf_control = FPDF()
            pdf_control.add_page()
            pdf_control.set_font(family="Arial", size=10)
            take_input = self.main_writing_space.get(1.0, END).split("\n")
            print(take_input)
            for i in take_input:
                pdf_control.cell(1000, 5, txt=i, ln=1, align="L")
            pdf_control.output(take_file_name)

            messagebox.showinfo("Saved as PDF", "The Current File Saved as PDF")

    def print_a_file(self, e=None):
        self.save()
        ask_pls = messagebox.askyesno("Conformation of printing", "Are you ready to print the file?")
        if ask_pls:
            win32api.ShellExecute(0, "print", self.saved_file_name, None, ".", 0)

    def take_exit(self, e=None):
        conform = messagebox.askyesno("Exit Conformation", "Are you sure to exit?")
        if conform:
            self.window.destroy()

    # Edit_menu Configuration
    def undo(self, e=None):
        try:
            self.edit_menu.entryconfigure(0, command=self.main_writing_space.edit_undo)
        except:
            messagebox.showinfo("Container Empty", "No action to perform")

    def redo(self, e=None):
        try:
            self.edit_menu.entryconfigure(1, command=self.main_writing_space.edit_redo)
        except:
            messagebox.showinfo("Container Empty", "No action to perform")

    def cut(self, e=None):
        try:
            get_text = self.main_writing_space.get("sel.first", "sel.last")
            self.main_writing_space.delete("sel.first", "sel.last")
            print(get_text)
            self.main_writing_space.clipboard_clear()
            self.main_writing_space.clipboard_append(get_text)
        except:
            print("Cut selection error")

    def copy(self, e=None):
        try:
            get_text = self.main_writing_space.get("sel.first", "sel.last")
            print(get_text)
            self.main_writing_space.clipboard_clear()
            self.main_writing_space.clipboard_append(get_text)
        except:
            print("Copy selection error")

    def paste(self, e=None):
        try:
            self.main_writing_space.insert(INSERT, self.main_writing_space.clipboard_get())
        except:
            print("Paste Selection Error")

    def clear(self):
        conform = messagebox.askyesno("Conformation to clean", "Do you want to clean the writing space?")
        if conform:
            self.main_writing_space.delete(1.0, END)
            self.previous_tag_remove()

    # View_menu Configuration
    def find_UI(self, e=None):
        top = Toplevel()
        top.title("Finding")
        top.geometry("600x300")
        top.maxsize(600, 300)
        top.minsize(600, 300)
        top.config(bg="#141414")

        Label(top, text="Enter a text to search", font=("Arial", 25, "bold", "italic"), bg="#141414", fg="gold").place(
            x=135, y=50)

        take_entry = Entry(top, font=("Arial", 20, "bold", "italic"), bg="#141400", fg="#d6b575",
                           insertbackground="#d6b575", relief=SUNKEN, bd=5)
        take_entry.place(x=150, y=120)
        take_entry.focus()

        def find_pattern(search_it):
            if self.main_writing_space.get(1.0, END):
                if search_it:
                    remove_highlight()
                    start_index = "1.0"
                    self.main_writing_space.tag_configure("highlight", background="black")
                    match_pattern = 0
                    while True:
                        start_index = self.main_writing_space.search(search_it, start_index, stopindex=END)
                        if not start_index:
                            break
                        end_pos = f"{start_index}+{len(search_it)}c"
                        match_pattern += 1
                        self.main_writing_space.tag_add("highlight", start_index, end_pos)
                        start_index = end_pos
                    messagebox.showinfo("Finding result", f"Total finding result: {match_pattern}")
                else:
                    messagebox.showinfo("Input Error", "Nothing to find")
            else:
                messagebox.showinfo("Text absent", "No text present")

        def remove_highlight():
            try:
                self.main_writing_space.tag_remove("highlight", 1.0, END)
            except:
                print("Tag not found error")

        ok_btn = Button(top, text="Ok", width=5, font=("Arial", 18, "bold", "italic"), bg="#262626", fg="#FF0000",
                        activebackground="#262626", activeforeground="#FF0000",
                        command=lambda: find_pattern(take_entry.get()))
        ok_btn.place(x=100, y=200)

        remove_tag = Button(top, text="Remove Highlight", font=("Arial", 18, "bold", "italic"), bg="#262626",
                            fg="#FF0000", activebackground="#262626", activeforeground="#FF0000",
                            command=remove_highlight)
        remove_tag.place(x=300, y=200)

        top.mainloop()

    def replace_UI(self, e=None):
        top = Toplevel()
        top.title("Replacing")
        top.geometry("600x400")
        top.maxsize(600, 400)
        top.minsize(600, 400)
        top.config(bg="#141414")

        Label(top, text="Enter a text to search", font=("Arial", 25, "bold", "italic"), bg="#141414", fg="gold").place(
            x=135, y=50)
        Label(top, text="Find", font=("Arial", 17, "bold", "italic"), bg="#141414", fg="#00FF00").place(x=50, y=125)
        Label(top, text="Replace", font=("Arial", 17, "bold", "italic"), bg="#141414", fg="#00FF00").place(x=50, y=205)

        take_entry = Entry(top, font=("Arial", 20, "bold", "italic"), bg="#141400", fg="#d6b575",
                           insertbackground="#d6b575", relief=SUNKEN, bd=5)
        take_entry.place(x=150, y=120)

        replacing_word = Entry(top, font=("Arial", 20, "bold", "italic"), bg="#141400", fg="#d6b575",
                               insertbackground="#d6b575", relief=SUNKEN, bd=5)
        replacing_word.place(x=150, y=200)

        take_entry.focus()

        def replace_pattern(search_it, replaced_by):
            if self.main_writing_space.get(1.0, END):
                if search_it and replaced_by:
                    start_index = "1.0"
                    match_pattern = 0
                    while True:
                        start_index = self.main_writing_space.search(search_it, start_index, stopindex=END)
                        if not start_index:
                            break
                        end_pos = f"{start_index}+{len(search_it)}c"
                        match_pattern += 1
                        self.main_writing_space.replace(start_index, end_pos, replaced_by)
                        start_index = end_pos
                    messagebox.showinfo("Replacing result", f"Total replacing result: {match_pattern}")
                else:
                    messagebox.showinfo("Input Error", "Nothing to replace")
            else:
                messagebox.showinfo("Text absent", "No text present")

        ok_btn = Button(top, text="Ok", width=5, font=("Arial", 18, "bold", "italic"), bg="#262626", fg="#FF0000",
                        activebackground="#262626", activeforeground="#FF0000",
                        command=lambda: replace_pattern(take_entry.get(), replacing_word.get()))
        ok_btn.place(x=270, y=280)

        top.mainloop()

    def dark_mode(self):
        self.main_writing_space.config(bg="#0d0d0d", fg="#00FF00", insertbackground="green", selectbackground="#8989ff")

        self.header_1.config(bg="#474747")
        self.font_size_label.config(bg="#474747", fg="gold")
        self.alignment_label.config(bg="#474747", fg="gold")
        self.header_1_components[0].config(bg="#6c6c93")

        self.header_2.config(bg="#474747")
        self.header_3.config(bg="#474747")
        self.header_4.config(bg="#474747")
        self.acc.config(bg="#474747")

        for every in self.status_components:
            every.config(bg="#474747", fg="#00e600")

        self.file_menu.entryconfig("New", background="#474747")
        self.file_menu.entryconfig("Open", background="#474747")
        self.file_menu.entryconfig("Save", background="#474747")
        self.file_menu.entryconfig("Save As", background="#474747")
        self.file_menu.entryconfig("Save File as PDF", background="#474747")
        self.file_menu.entryconfig("Print", background="#474747")
        self.file_menu.entryconfig("Exit", background="#474747")
        self.file_menu.delete(2)
        self.file_menu.delete(5)
        self.file_menu.insert_separator(2, background="#474747")
        self.file_menu.insert_separator(6, background="#474747")

        self.edit_menu.entryconfig("Undo", background="#474747")
        self.edit_menu.entryconfig("blacko", background="#474747")
        self.edit_menu.entryconfig("Cut", background="#474747")
        self.edit_menu.entryconfig("Copy", background="#474747")
        self.edit_menu.entryconfig("Paste", background="#474747")
        self.edit_menu.entryconfig("Clear", background="#474747")
        self.edit_menu.delete(2)
        self.edit_menu.delete(5)
        self.edit_menu.insert_separator(2, background="#474747")
        self.edit_menu.insert_separator(6, background="#474747")

        self.view_menu.entryconfig("Find", background="#474747")
        self.view_menu.entryconfig("Replace", background="#474747")
        self.view_menu.entryconfig("Dark Mode", background="#474747")
        self.view_menu.entryconfig("Light Mode", background="#474747")
        self.view_menu.delete(2)
        self.view_menu.insert_separator(2, background="#474747")

        self.customization_menu.entryconfig("Bold", background="#474747")
        self.customization_menu.entryconfig("Italics", background="#474747")
        self.customization_menu.entryconfig("Underline", background="#474747")
        self.customization_menu.entryconfig("Foreground-Color", background="#474747")
        self.customization_menu.entryconfig("Background-Color", background="#474747")
        self.customization_menu.delete(3)
        self.customization_menu.insert_separator(3, background="#474747")

    def light_mode(self):
        self.main_writing_space.config(bg="white", fg="black", insertbackground="black", selectbackground="black")

        self.header_1.config(bg="darkcyan")
        self.font_size_label.config(bg="darkcyan", fg="black")
        self.alignment_label.config(bg="darkcyan", fg="black")
        self.header_1_components[0].config(bg="green")

        self.header_2.config(bg="darkcyan")
        self.header_3.config(bg="darkcyan")
        self.header_4.config(bg="darkcyan")
        self.acc.config(bg="darkcyan")

        for every in self.status_components:
            every.config(bg="darkyan", fg="black")

        self.file_menu.entryconfig("New", background="green", foreground="black")
        self.file_menu.entryconfig("Open", background="green", foreground="black")
        self.file_menu.entryconfig("Save", background="green", foreground="black")
        self.file_menu.entryconfig("Save As", background="green", foreground="black")
        self.file_menu.entryconfig("Save File as PDF", background="green", foreground="black")
        self.file_menu.entryconfig("Print", background="green", foreground="black")
        self.file_menu.entryconfig("Exit", background="green", foreground="black")
        self.file_menu.delete(2)
        self.file_menu.delete(5)
        self.file_menu.insert_separator(2, background="green")
        self.file_menu.insert_separator(6, background="green")

        self.edit_menu.entryconfig("Undo", background="green", foreground="black")
        self.edit_menu.entryconfig("o", background="green", foreground="black")
        self.edit_menu.entryconfig("Cut", background="green", foreground="black")
        self.edit_menu.entryconfig("Copy", background="green", foreground="black")
        self.edit_menu.entryconfig("Paste", background="green", foreground="black")
        self.edit_menu.entryconfig("Clear", background="green", foreground="black")
        self.edit_menu.delete(2)
        self.edit_menu.delete(5)
        self.edit_menu.insert_separator(2, background="green")
        self.edit_menu.insert_separator(6, background="green")

        self.view_menu.entryconfig("Find", background="green", foreground="black")
        self.view_menu.entryconfig("Replace", background="green", foreground="black")
        self.view_menu.entryconfig("Dark Mode", background="green", foreground="black")
        self.view_menu.entryconfig("Light Mode", background="green", foreground="black")
        self.view_menu.delete(2)
        self.view_menu.insert_separator(2, background="green")

        self.customization_menu.entryconfig("Bold", background="green", foreground="black")
        self.customization_menu.entryconfig("Italics", background="green", foreground="black")
        self.customization_menu.entryconfig("Underline", background="green", foreground="black")
        self.customization_menu.entryconfig("Foreground-Color", background="green", foreground="black")
        self.customization_menu.entryconfig("Background-Color", background="green", foreground="black")
        self.customization_menu.delete(3)
        self.customization_menu.insert_separator(3, background="green")

    # customization_menu configuration
    def change_bold(self, e=None):
        try:
            get_font = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))
            get_font.configure(weight="bold")

            self.main_writing_space.tag_configure("make_bold", font=get_font)

            current_tags = self.main_writing_space.tag_names("sel.first")

            if "make_bold" in current_tags:
                self.main_writing_space.tag_remove("make_bold", "sel.first", "sel.last")
            else:
                self.main_writing_space.tag_add("make_bold", "sel.first", "sel.last")
        except:
            print("\nSelection Error")

    def change_italic(self, e=None):
        try:
            get_font = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))
            get_font.configure(slant="italic")

            self.main_writing_space.tag_configure("make_italic", font=get_font)

            current_tags = self.main_writing_space.tag_names("sel.first")

            if "make_italic" in current_tags:
                self.main_writing_space.tag_remove("make_italic", "sel.first", "sel.last")
            else:
                self.main_writing_space.tag_add("make_italic", "sel.first", "sel.last")
        except:
            print("\nSelection Error")

    def change_underline(self, e=None):
        try:
            get_font = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))
            get_font.configure(underline=True)

            self.main_writing_space.tag_configure("make_underline", font=get_font)

            current_tags = self.main_writing_space.tag_names("sel.first")

            if "make_underline" in current_tags:
                self.main_writing_space.tag_remove("make_underline", "sel.first", "sel.last")
            else:
                self.main_writing_space.tag_add("make_underline", "sel.first", "sel.last")
        except:
            print("\nSelection Error")

    def change_fg_color(self, e=None):
        try:
            take_color = colorchooser.askcolor()[1]
            font_change = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))

            if len(self.fg_tag_name_store) == 0:
                temp_store = [self.fg_tag_counter, self.main_writing_space.index("sel.first"),
                              self.main_writing_space.index("sel.last")]
                self.fg_tag_name_store.append(temp_store)
                temp = self.fg_tag_name_store[0][0]
                self.fg_tag_counter += 1
            else:
                def search_it():
                    start = self.main_writing_space.index("sel.first")
                    end = self.main_writing_space.index("sel.last")
                    for take in self.fg_tag_name_store:
                        if take[1] == start and take[2] == end:
                            temp = take[0]
                            return temp
                    return -1

                temp = search_it()

                if temp == -1:
                    temp_store = [self.fg_tag_counter, self.main_writing_space.index("sel.first"),
                                  self.main_writing_space.index("sel.last")]
                    self.fg_tag_name_store.append(temp_store)
                    temp = self.fg_tag_name_store[self.fg_tag_counter][0]
                    self.fg_tag_counter += 1

            self.main_writing_space.tag_configure(temp, font=font_change, foreground=take_color)
            self.main_writing_space.tag_add(temp, "sel.first", "sel.last")
        except:
            messagebox.showerror("Selection Error", "Select select a text to change font")

    def change_bg_color(self, e=None):
        try:
            take_color = colorchooser.askcolor()[1]
            font_change = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))

            if len(self.bg_tag_name_store) == 0:
                temp_store = [self.fg_tag_counter, self.main_writing_space.index("sel.first"),
                              self.main_writing_space.index("sel.last")]
                self.bg_tag_name_store.append(temp_store)
                temp = self.bg_tag_name_store[0][0]
                self.bg_tag_counter += 1
            else:
                def search_it():
                    start = self.main_writing_space.index("sel.first")
                    end = self.main_writing_space.index("sel.last")
                    for take in self.bg_tag_name_store:
                        if take[1] == start and take[2] == end:
                            temp = take[0]
                            return temp
                    return -1

                temp = search_it()

                if temp == -1:
                    temp_store = [self.bg_tag_counter, self.main_writing_space.index("sel.first"),
                                  self.main_writing_space.index("sel.last")]
                    self.bg_tag_name_store.append(temp_store)
                    temp = self.bg_tag_name_store[self.bg_tag_counter][0]
                    self.bg_tag_counter += 1

            self.main_writing_space.tag_configure(temp, font=font_change, background=take_color)
            self.main_writing_space.tag_add(temp, "sel.first", "sel.last")
        except:
            messagebox.showerror("Selection Error", "Select select a text to change font")

    # Header 1 Configuration
    def change_font_size(self, e):
        self.current_font_size = int(e)
        self.main_writing_space['font'] = (self.font_family.get(), self.current_font_size)

    def make_align_left(self):
        try:
            store_selection_start_position = list(self.main_writing_space.index(INSERT))
            checking_if_empty_space_present = list(
                self.main_writing_space.get(int(store_selection_start_position[0]) * 1.0, "sel.first"))

            if len(checking_if_empty_space_present) == 0 or checking_if_empty_space_present[0] == '\t' or \
                    checking_if_empty_space_present[0] == ' ':
                get_all_text = self.main_writing_space.get("sel.first", "sel.last")
                self.main_writing_space.tag_configure("left", justify=LEFT)
                self.main_writing_space.delete("sel.first", "sel.last")
                self.main_writing_space.insert(int(store_selection_start_position[0]) * 1.0, get_all_text, "left")
            else:
                messagebox.showerror("Not allowed",
                                     "Not allowed to make selected text left aligned!! text present in left side")
        except:
            messagebox.showerror("Selection Error", "Please select a text to make left aligned")

    def make_align_center(self):
        try:
            store = list(self.main_writing_space.index("sel.first"))
            store = int(store[0]) * 1.0
            checking_if_empty_space_present = list(self.main_writing_space.get("sel.last", "current lineend"))

            if len(checking_if_empty_space_present) == 0 or checking_if_empty_space_present[
                len(checking_if_empty_space_present) - 1] == '\t' or checking_if_empty_space_present[
                len(checking_if_empty_space_present) - 1] == ' ':
                get_all_text = self.main_writing_space.get(store, "sel.last")
                self.main_writing_space.tag_configure("middle", justify=CENTER)
                self.main_writing_space.delete(store, "sel.last")
                self.main_writing_space.insert(INSERT, get_all_text, "middle")
            else:
                messagebox.showerror("Not empty", "Right side not empty")
        except:
            messagebox.showerror("Selection Error", "Nothing selected here")

    def make_align_right(self):
        try:
            store = list(self.main_writing_space.index("sel.first"))
            store = int(store[0]) * 1.0
            checking_if_empty_space_present = list(self.main_writing_space.get("sel.last", "current lineend"))

            if len(checking_if_empty_space_present) == 0 or checking_if_empty_space_present[
                len(checking_if_empty_space_present) - 1] == '\t' or checking_if_empty_space_present[
                len(checking_if_empty_space_present) - 1] == ' ':
                get_all_text = self.main_writing_space.get(store, "sel.last")
                self.main_writing_space.tag_configure("right", justify=RIGHT)
                self.main_writing_space.delete(store, "sel.last")
                self.main_writing_space.insert(INSERT, get_all_text, "right")
            else:
                messagebox.showerror("Not empty", "Right side not empty")
        except:
            messagebox.showerror("Selection Error", "Nothing selected here")

    # Header 2 configuration
    def change_font_manually(self, e):
        try:
            font_change = font.Font(self.main_writing_space, self.main_writing_space.cget("font"))
            font_change.configure(family=self.font_family.get())

            if len(self.font_tag_name_store) == 0:
                temp_store = [self.font_tag_counter, self.main_writing_space.index("sel.first"),
                              self.main_writing_space.index("sel.last")]
                self.font_tag_name_store.append(temp_store)
                temp = self.font_tag_name_store[0][0]
                self.font_tag_counter += 1
            else:
                def search_it():
                    start = self.main_writing_space.index("sel.first")
                    end = self.main_writing_space.index("sel.last")
                    for take in self.font_tag_name_store:
                        if take[1] == start and take[2] == end:
                            temp = take[0]
                            return temp
                    return -1

                temp = search_it()

                if temp == -1:
                    temp_store = [self.font_tag_counter, self.main_writing_space.index("sel.first"),
                                  self.main_writing_space.index("sel.last")]
                    self.font_tag_name_store.append(temp_store)
                    temp = self.font_tag_name_store[self.font_tag_counter][0]
                    self.font_tag_counter += 1

            self.main_writing_space.tag_configure(temp, font=font_change)
            self.main_writing_space.tag_add(temp, "sel.first", "sel.last")
        except:
            messagebox.showerror("Selection Error", "Select select a text to change font")

    def change_line_space_to_selected_text(self, take):
        try:
            starting_index = int(list(self.main_writing_space.index("sel.first").split("."))[0])

            get_text = self.main_writing_space.get(starting_index * 1.0, "sel.last").split("\n")
            self.main_writing_space.delete(starting_index * 1.0, "sel.last")
            print("Before: ", get_text)

            for modified_element in get_text:
                if modified_element == '':
                    pass
                else:
                    self.main_writing_space.insert(starting_index * 1.0, modified_element)
                    for _ in range(take):
                        self.main_writing_space.insert((starting_index + 1) * 1.0, '\n')
                        starting_index += 1

            print("After: ", get_text)
        except:
            messagebox.showerror("Selection Error", "Nothing Selected to change line space")

        if self.permission_to_update == 1:
            self.total_word_and_line_counter(None)

    def add_bullet_in_selected_text(self, bullet_is):
        try:
            if int(self.header_2_components[1].get()) > 1:
                messagebox.showwarning("Restriction", "Bullet add can happen only for line spacing: 1")
                return

            bullet_is = list(bullet_is)[0]
            if bullet_is == '1':
                bullet_is = 1

            starting_index = int(list(self.main_writing_space.index("sel.first").split("."))[0])

            get_text = self.main_writing_space.get(starting_index * 1.0, "sel.last").split("\n")
            self.main_writing_space.delete(starting_index * 1.0, "sel.last")

            print("Before get_text: ", get_text)

            for element in get_text:
                element_index_finder = get_text.index(element)
                element = list(element)
                print("Element is: ", element)

                while True:
                    print("Element is in loop: ", element)

                    if element:
                        if element[0] == '' or element[0] == ' ' or element[0] == '\t' or element[0] == '\n' or element[
                            0] == '#' or element[0] == '!' or element[0] == '>' or element[0] == 'o' or element[
                            0] == '.':
                            element.remove(element[0])

                        elif len(element) >= 5 and (element[3] == '.' and element[4] == ' '):
                            count_delete = 5
                            while count_delete:
                                element.remove(element[0])
                                count_delete -= 1

                        elif len(element) >= 4 and (element[2] == '.' and element[3] == ' '):
                            count_delete = 4
                            while count_delete:
                                element.remove(element[0])
                                count_delete -= 1

                        elif len(element) >= 3 and (element[1] == '.' and element[2] == ' '):
                            count_delete = 3
                            while count_delete:
                                element.remove(element[0])
                                count_delete -= 1
                        else:
                            break
                    else:
                        break

                element = "".join(element)

                if type(bullet_is) == int:
                    element = f"{bullet_is}. {element}"
                else:
                    element = f"{bullet_is} {element}"
                if element_index_finder < len(get_text) - 1:
                    element += '\n'

                get_text[element_index_finder] = element

                if type(bullet_is) == int:
                    bullet_is += 1
            print(get_text)

            for modified_element in get_text:
                self.main_writing_space.insert(starting_index * 1.0, modified_element)
                starting_index += 1

            print(get_text)
        except:
            messagebox.showerror("Selection Error", "Nothing Selected to make bullet before it")

        if self.permission_to_update == 1:
            self.total_word_and_line_counter(None)

    # header 3 configuration
    def case_change(self, indexing):
        try:
            get_text = self.main_writing_space.get("sel.first", "sel.last")
            get_index = self.main_writing_space.index("sel.first")
            self.main_writing_space.delete("sel.first", "sel.last")
            if indexing == 'u':
                get_text = get_text.upper()
            else:
                get_text = get_text.lower()
            self.main_writing_space.insert(get_index, get_text)
        except:
            print("Here's the selection error in case change")

    def text_to_speech_convert_with_threading(self):
        def text_to_speech_convert():
            try:
                get_text = self.main_writing_space.get("sel.first", "sel.last")
                self.engine_control.say(get_text)
                self.engine_control.runAndWait()
            except:
                messagebox.showerror("Selection Problem", "Nothing selected here")

        threading.Thread(target=text_to_speech_convert).start()

    def ui_for_searching(self):
        top = Toplevel(relief=RAISED, bd=10)
        top.title("Searching Option")
        top.geometry("600x600")
        top.maxsize(600, 600)
        top.minsize(600, 600)
        top.config(bg="#141414")

        def speak(main_searching_text, medium):
            self.engine_control.say(f"Searching a topic {main_searching_text} in {medium}")
            self.engine_control.runAndWait()

        def searching_option(index, searching_text):
            text_to_search = searching_text.split(" ")
            if index == "Google":
                if self.searching_things_in_google == "Nothing To Show":
                    self.searching_things_in_google = searching_text
                else:
                    self.searching_things_in_google += searching_text

                text_to_search = '+'.join(text_to_search)
                webbrowser.open(f'https://www.google.com/search?q={text_to_search}')
                threading.Thread(target=lambda: speak(searching_text, index)).start()

            elif index == "Youtube":
                text_to_search = '+'.join(text_to_search)
                webbrowser.open(f'https://www.youtube.com/search?q={text_to_search}')
                threading.Thread(target=lambda: speak(searching_text, index)).start()

            elif index == "Facebook":
                text_to_search = '-'.join(text_to_search)
                webbrowser.open(f'https://www.facebook.com/public/{text_to_search}')
                threading.Thread(target=lambda: speak(searching_text, index)).start()

            elif index == "Linkedin":
                text_to_search = '/'.join(text_to_search)
                webbrowser.open(f'https://www.linkedin.com/pub/dir/{text_to_search}')
                threading.Thread(target=lambda: speak(searching_text, index)).start()

            else:
                text_to_search = '_'.join(text_to_search)
                webbrowser.open(f'https://www.instagram.com/{text_to_search}/?hl=en')
                threading.Thread(target=lambda: speak(searching_text, index)).start()

            top.destroy()

        try:
            get_text = self.main_writing_space.get("sel.first", "sel.last")

            google_search = Button(top, text="Search in Google", font=("Arial", 25, "bold", "italic"), bg="#262626",
                                   fg="#FF0000", relief=RAISED, bd=5, activebackground="green", activeforeground="gold",
                                   command=lambda: searching_option("Google", get_text))
            google_search.pack(pady=20)

            youtube_search = Button(top, text="Search in Youtube", font=("Arial", 25, "bold", "italic"), bg="#262626",
                                    fg="black", relief=RAISED, bd=5, activebackground="green", activeforeground="gold",
                                    command=lambda: searching_option("Youtube", get_text))
            youtube_search.pack(pady=20)

            facebook_search = Button(top, text="Search in Facebook", font=("Arial", 25, "bold", "italic"), bg="#262626",
                                     fg="#00FF00", relief=RAISED, bd=5, activebackground="green",
                                     activeforeground="gold", command=lambda: searching_option("Facebook", get_text))
            facebook_search.pack(pady=20)

            linkedin_search = Button(top, text="Search in LinkedIn", font=("Arial", 25, "bold", "italic"), bg="#262626",
                                     fg="magenta", relief=RAISED, bd=5, activebackground="green",
                                     activeforeground="gold", command=lambda: searching_option("Linkedin", get_text))
            linkedin_search.pack(pady=20)

            instagram_search = Button(top, text="Search in Instagram", font=("Arial", 25, "bold", "italic"),
                                      bg="#262626", fg="chocolate", relief=RAISED, bd=5, activebackground="green",
                                      activeforeground="gold", command=lambda: searching_option("Instagram", get_text))
            instagram_search.pack(pady=20)

            top.mainloop()
        except:
            top.destroy()
            messagebox.showerror("Selection Error", "Nothing Selected Here to Search")

    # Header 4 Configuration
    def pdf_to_text(self):
        take_pdf = filedialog.askopenfilename(initialdir="\\Desktop", defaultextension="*.pdf",
                                              title="Select a pdf file")
        if take_pdf:
            take_control = open(take_pdf, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(take_control)
            for i in range(pdf_reader.numPages):
                pageobject = pdf_reader.getPage(i)
                self.main_writing_space.insert(INSERT, pageobject.extractText())
            take_control.close()

    def send_msg_to_whatsapp(self):
        try:
            import pywhatkit
            top = Toplevel()
            top.title("Replacing")
            top.geometry("800x400")
            top.maxsize(800, 400)
            top.minsize(800, 400)
            top.config(bg="#141414")

            messagebox.showwarning("Browser Open Alert",
                                   "Please open your browser and connect your whatsapp with whatsapp web by scanning the barcode and don't minimised the browser to send message properly")

            Label(top, text="Enter some details to send message", font=("Arial", 25, "bold", "italic"), bg="#141414",
                  fg="gold").place(x=120, y=50)
            Label(top, text="Receiver Number", font=("Arial", 17, "bold", "italic"), bg="#141414", fg="#00FF00").place(
                x=20, y=125)
            Label(top, text="Text To Send", font=("Arial", 17, "bold", "italic"), bg="#141414", fg="#00FF00").place(
                x=20, y=205)

            num_entry = Entry(top, font=("Arial", 20, "bold", "italic"), bg="#141400", fg="#d6b575",
                              insertbackground="#d6b575", relief=SUNKEN, bd=5, show="*")
            num_entry.place(x=230, y=120)

            text_body = Entry(top, font=("Arial", 20, "bold", "italic"), bg="#141400", fg="#d6b575",
                              insertbackground="#d6b575", relief=SUNKEN, bd=5)
            text_body.place(x=230, y=200)

            num_entry.focus()

            def msg_send_with_verification(sending_no, text_to_send):
                try:
                    get_no = list(sending_no)
                    get_no.remove('+')
                    remake_no = "".join(get_no)
                    if len(get_no) == 12 and int(remake_no) and text_to_send:
                        def send_msg_finally_to_wp():
                            top.destroy()
                            self.engine_control.say('Please Wait.. This will take time to send message......')
                            self.engine_control.runAndWait()
                            self.send_msg_to_wp = text_to_send
                            current_time = datetime.datetime.now()
                            pywhatkit.sendwhatmsg(sending_no, text_to_send, time_hour=current_time.hour,
                                                  time_min=(current_time.minute + 1),
                                                  wait_time=(60 - current_time.second) // 2 + 2)

                        threading.Thread(target=send_msg_finally_to_wp).start()
                    else:
                        messagebox.showerror('Number Input Error',
                                             'Number should start with countrycode and without consider countrycode, it should be 10 digit number')
                except:
                    messagebox.showerror('Number Input Error',
                                         'Number should start with countrycode and without consider countrycode, it should be 10 digit number')

            def change_visibility_ph_num():
                if num_entry['show'] == '*':
                    num_entry['show'] = ''
                    visibility_other['text'] = "Hide"
                else:
                    num_entry['show'] = '*'
                    visibility_other['text'] = "Show"

            visibility_other = Button(top, text="Show", font=("Arial", 18, "bold", "italic"), bg="#141414",
                                      fg="#00FF00", relief=RAISED, bd=2, command=change_visibility_ph_num)
            visibility_other.place(x=600, y=120)

            ok_btn = Button(top, text="Ok", width=5, font=("Arial", 18, "bold", "italic"), bg="#262626", fg="#FF0000",
                            activebackground="#262626", activeforeground="#FF0000",
                            command=lambda: msg_send_with_verification(num_entry.get(), text_body.get()))
            ok_btn.place(x=360, y=280)

            top.mainloop()
        except:
            messagebox.showerror("Error", "Make Sure that your internet is connected and your browser is not minimised")

    def open_wikipedia(self):
        try:
            get_text = self.main_writing_space.get("sel.first", "sel.last")

            def speak(text_to_speak):
                self.engine_control.say(f"Searching {text_to_speak} in Wikipedia")
                self.engine_control.runAndWait()

            threading.Thread(target=lambda: speak(get_text)).start()
            get_text = "_".join(get_text.split(" "))
            webbrowser.open(f'https://en.wikipedia.org/wiki/{get_text}')
        except:
            messagebox.showerror("Error",
                                 "Please check your internet connection and select a text to search in wikipedia")


    # Status Functionality Controller
    def total_word_and_line_counter(self, e=None):
        total_take = list(self.main_writing_space.get(1.0, END).split("\n"))

        self.total_line = len(total_take) - 1
        self.status_components[1]['text'] = "Total Line: " + str(len(total_take) - 1)

        count = 0
        for element in total_take:
            temp = list(element)
            if temp and (temp[0] == "#" or temp[0] == ">" or temp[0] == "o" or temp[0] == "" or temp[0] == "!"):
                temp.remove(temp[0])

            if temp.count('\t') > 0:
                temp[temp.index('\t')] = " "
                while temp.count('\t') > 0:
                    temp.remove('\t')

            while temp.count('.') > 0:
                index = temp.index('.')
                if (index + 1 < len(temp) and temp[index + 1] == ' ') and (index - 1 >= 0):
                    temp.remove(temp[index])
                else:
                    break

            element = "".join(temp)
            store = list(element.split(" "))

            while store.count('') > 0:
                store.remove('')

            count += len(store)

        self.total_word = count
        self.status_components[0]['text'] = "Total Word: " + str(count)

    def __time_counter(self):
        pass

if __name__ == '__main__':
    window = Tk()
    window.geometry("1350x715")
    window.maxsize(1350, 715)
    window.minsize(500, 500)
    window.config(bg="black")
    TextPad(window)
    window.mainloop()
