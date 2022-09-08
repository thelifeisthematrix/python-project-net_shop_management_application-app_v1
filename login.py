from tkinter import *
from tkinter.ttk import Separator
from PIL import Image, ImageTk

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
LOGIN_FRAME_WIDTH = 1000
LOGIN_FRAME_HEIGHT = 600


class Login:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+0+0")
        self.window.resizable(width=False,
                              height=False)
        self.window.title('Login')

        # BACKGROUND
        self.background = Label(master=self.window)
        self.background.image = ImageTk.PhotoImage(
            Image.open(fp="images/login/background.jpg").resize((SCREEN_WIDTH, SCREEN_HEIGHT)))
        self.background.configure(image=self.background.image)
        self.background.pack()

        # LOGIN FRAME
        self.login_frame = Frame(self.window,
                                 background="#C6C5FF",
                                 width=LOGIN_FRAME_WIDTH,
                                 height=LOGIN_FRAME_HEIGHT, )
        self.login_frame.place(x=SCREEN_WIDTH / 2 - LOGIN_FRAME_WIDTH / 2,
                               y=SCREEN_HEIGHT / 2 - LOGIN_FRAME_HEIGHT / 2)

        # LOGIN FRAME - HEADING
        self.heading = Label(self.login_frame,
                             text="WELCOME",
                             font=('System', 25, "bold"),
                             foreground="white",
                             background="#C6C5FF")
        self.heading.place(x=LOGIN_FRAME_WIDTH / 2 - self.heading.winfo_reqwidth() / 2,
                           y=10)

        # LOGIN FRAME - LEFT SIDE IMAGE
        self.left_side_image = Label(self.login_frame,
                                     border=0)
        self.left_side_image.image = ImageTk.PhotoImage(
            Image.open('images/login/left_side_image.jpg').resize((500, 500)))
        self.left_side_image.configure(image=self.left_side_image.image)
        self.left_side_image.place(x=5,
                                   y=100)

        # LOGIN FRAME - ANCHOR CONTENT
        anchor_x = 700

        # LOGIN FRAME - PADDING CONTENT
        padding_y = 10

        # LOGIN FRAME - LOGIN ICON
        self.login_icon = Label(self.login_frame,
                                background="#C6C5FF")
        self.login_icon.image = ImageTk.PhotoImage(Image.open('images/login/login_icon.png'))
        self.login_icon.configure(image=self.login_icon.image)
        self.login_icon.place(x=anchor_x - self.login_icon.winfo_reqwidth() / 2,
                              y=100)
        self.window.update()

        # LOGIN FRAME - LOGIN TITLE
        self.login_title = Label(self.login_frame,
                                 text="SIGN IN",
                                 foreground="white",
                                 font=("System", 20, "bold"),
                                 background="#C6C5FF")
        self.login_title.place(x=anchor_x - self.login_title.winfo_reqwidth() / 2,
                               y=self.login_icon.winfo_y() + self.login_icon.winfo_reqheight() + padding_y)
        self.window.update()

        # LOGIN FRAME - USERNAME LABEL
        self.username_label = LabelFrame(self.login_frame,
                                         text="USERNAME",
                                         font=("System", 15, "bold"),
                                         background="#C6C5FF")
        self.username_label.place(x=anchor_x - 170,
                                  y=self.login_title.winfo_y() + self.login_title.winfo_reqheight() + padding_y)
        self.username_icon = Label(self.username_label,
                                   background='#C6C5FF')
        self.username_icon.image = ImageTk.PhotoImage(Image.open('images/login/username_icon.png'))
        self.username_icon.configure(image=self.username_icon.image)
        self.username_icon.pack(side="left")
        self.username_entry = Entry(self.username_label,
                                    width=37,
                                    font=("System", 17, "bold"),
                                    background="#C6C5FF",
                                    border=0)
        self.username_entry.pack(side="left")
        self.window.update()

        # LOGIN FRAME - PASSWORD LABEL
        self.password_label = LabelFrame(self.login_frame,
                                         text="USERNAME",
                                         font=("System", 15, "bold"),
                                         background="#C6C5FF")
        self.password_label.place(x=anchor_x - 170,
                                  y=self.username_label.winfo_y() + self.username_label.winfo_reqheight() + padding_y)
        self.password_icon = Label(self.password_label,
                                   background='#C6C5FF')
        self.password_icon.image = ImageTk.PhotoImage(Image.open('images/login/password_icon.png'))
        self.password_icon.configure(image=self.password_icon.image)
        self.password_icon.pack(side="left")
        self.password_entry = Entry(self.password_label,
                                    width=35,
                                    font=("System", 17, "bold"),
                                    background="#C6C5FF",
                                    border=0,
                                    show="*")
        self.password_entry.pack(side="left")
        self.show_hide_button = Button(self.password_label,
                                       command=self.show,
                                       border=0,
                                       background="#C6C5FF",
                                       activebackground="#C6C5FF",
                                       cursor="hand2")
        self.show_hide_button.show_image = ImageTk.PhotoImage(Image.open(fp='images/login/show.png').resize((16, 16)))
        self.show_hide_button.hide_image = ImageTk.PhotoImage(Image.open(fp='images/login/hide.png').resize((16, 16)))
        self.show_hide_button.configure(image=self.show_hide_button.show_image)
        self.show_hide_button.pack(expand=True)
        self.window.update()

        # LOGIN FRAME - LOGIN BUTTON
        self.login_button = Button(self.login_frame,
                                   text='LOGIN',
                                   font=("System", 15, "bold"),
                                   foreground='white',
                                   background="#C6C5FF",
                                   activebackground='#C6C5FF',
                                   border=0,
                                   cursor='hand2',
                                   compound="center")
        self.login_button.image = ImageTk.PhotoImage(Image.open('images/login/login_button.png'))
        self.login_button.configure(image=self.login_button.image)
        self.login_button.place(x=anchor_x - self.login_button.winfo_reqwidth() / 2,
                                y=self.password_label.winfo_y() + self.password_label.winfo_reqheight() + padding_y)
        self.window.update()

        # LOGIN FRAME - FORGOT BUTTON (PASSWORD)
        self.forgot_button = Button(self.login_frame,
                                    text="Forgot Password?",
                                    font=("System", 15, "bold underline"),
                                    foreground="black",
                                    activebackground="#C6C5FF",
                                    background="#C6C5FF",
                                    border=0,
                                    cursor="hand2")
        self.forgot_button.place(x=anchor_x - self.forgot_button.winfo_reqwidth() / 2,
                                 y=self.login_button.winfo_y() + self.login_button.winfo_reqheight() + padding_y)
        self.window.update()

        # LOGIN FRAME - SEPARATOR
        self.separator = Separator(master=self.login_frame,
                                   orient="horizontal")
        self.separator.place(relx=0.6,
                             rely=0.9,
                             relwidth=0.2,
                             relheight=0.005)
        self.window.update()

        # LOGIN FRAME - SIGN UP BUTTON
        self.signup_img = ImageTk.PhotoImage(file='images/login/register.png')
        self.sign_up_button = Button(self.login_frame,
                                     image=self.signup_img,
                                     bg='#98a65d',
                                     cursor="hand2",
                                     border=0,
                                     background="#C6C5FF",
                                     activebackground="#C6C5FF")
        self.sign_up_button.place(x=anchor_x - self.sign_up_button.winfo_reqwidth() / 2,
                                  y=self.separator.winfo_y() + self.separator.winfo_reqheight() + padding_y)

        self.window.mainloop()

    def show(self):
        self.show_hide_button.configure(image=self.show_hide_button.hide_image,
                                        command=self.hide,
                                        background="#C6C5FF")
        self.password_entry.config(show='')

    def hide(self):
        self.show_hide_button.configure(image=self.show_hide_button.show_image,
                                        command=self.show,
                                        background="#C6C5FF")
        self.password_entry.config(show='*')

    def destroy(self):
        self.window.destroy()
