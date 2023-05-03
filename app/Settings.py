import customtkinter
import tkinter
import pygame.mixer


class Settings(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Settings")
        self.label = customtkinter.CTkLabel(self, text="Music", font=('Arial', 25))
        self.label.pack(padx=20, pady=20)
        self.music_on = customtkinter.CTkCheckBox(self, text="Music on", command=self.music_on_callback)
        self.music_on.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.music_off = customtkinter.CTkCheckBox(self, text="Music off", command=self.music_off_callback)
        self.music_off.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def music_on_callback(self):
        pygame.mixer.music.play(-1)

    def music_off_callback(self):
        pygame.mixer.music.stop()
