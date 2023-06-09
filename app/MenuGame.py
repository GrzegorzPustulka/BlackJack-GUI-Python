import customtkinter
from PIL import Image
import tkinter
from app.MainWindowGame import WindowGame
import pygame.mixer
from app.Settings import Settings
from app.Info import Info


class Menu(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        pygame.mixer.init()
        pygame.mixer.music.load('music/casino.mp3')
        pygame.mixer.music.play(-1)
        self.title("Black Jack")
        self.set_window_size('612x612')
        self.resizable(False, False)
        self.background_image = self.create_background_image()
        self.background = self.set_background()
        self.background.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.start_button = self.create_start_button()
        self.start_button.place(relx=0.20, rely=0.9, anchor=tkinter.CENTER)
        self.settings_button = self.create_settings_button()
        self.settings_button.place(relx=0.80, rely=0.9, anchor=tkinter.CENTER)
        self.info_button = self.create_info_button()
        self.info_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.settings = None
        self.menu_window_game = None
        self.info = None

    def set_window_size(self, size):
        self.geometry(size)

    def start_button_callback(self):
        # self.destroy()
        # app = WindowGame()
        # app.mainloop()
        if self.menu_window_game is None or not self.menu_window_game.winfo_exists():
            self.menu_window_game = WindowGame(self)  # create window if its None or destroyed
        else:
            self.menu_window_game.focus()  # if window exists focus it

    def settings_button_callback(self):
        if self.settings is None or not self.settings.winfo_exists():
            self.settings = Settings(self)  # create window if its None or destroyed
        else:
            self.settings.focus()  # if window exists focus it

    def info_button_callback(self):
        if self.info is None or not self.info.winfo_exists():
            self.info = Info(self)  # create window if its None or destroyed
        else:
            self.info.focus()  # if window exists focus it

    def create_background_image(self):
        return customtkinter.CTkImage(light_image=Image.open("images/menu.jpg"),
                                      dark_image=Image.open("images/menu.jpg"),
                                      size=(612, 612))

    def set_background(self):
        return customtkinter.CTkLabel(master=self,
                                      width=612,
                                      height=612,
                                      text='',
                                      image=self.background_image)

    def create_start_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Start",
                                       font=('arial', 38),
                                       width=150,
                                       height=32,
                                       command=self.start_button_callback)

    def create_settings_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Settings",
                                       font=('arial', 38),
                                       width=150,
                                       height=32,
                                       command=self.settings_button_callback)

    def create_info_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Info",
                                       font=('arial', 38),
                                       width=150,
                                       height=32,
                                       command=self.info_button_callback)

