import customtkinter


class Info(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title("Info")
        self.label = customtkinter.CTkLabel(self, text="Info")
        self.label.pack(padx=20, pady=20)
