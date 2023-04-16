import customtkinter
from PIL import Image
import tkinter
from Players.Player import Player
from Players.Dealer import Dealer
from Cards.Deck import Deck


class WindowGame(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.dealer_cards_label = []
        self.player_cards_label = []
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        customtkinter.set_appearance_mode("dark")
        self.title("Black Jack")
        self.set_window_size('1300x630')
        self.resizable(False, False)

        self.background_image = self.create_background_image()
        self.background = self.set_background()
        self.background.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.exit_button = self.create_exit_button()
        self.exit_button.place(relx=0.934, rely=0.97, anchor=tkinter.CENTER)

        self.menu_button = self.create_menu_button()
        self.menu_button.place(relx=0.934, rely=0.91, anchor=tkinter.CENTER)

        self.new_game_button = self.create_new_game_button()

        self.player_label = self.create_name_label('Player')
        self.player_label.place(relx=0.26, rely=0.1, anchor=tkinter.CENTER)

        self.dealer_label = self.create_name_label('Dealer')
        self.dealer_label.place(relx=0.74, rely=0.1, anchor=tkinter.CENTER)

        self.chip_10_image = self.create_chip_image('10')
        self.chip_10_button = self.create_chip_button('10')
        self.chip_50_image = self.create_chip_image('50')
        self.chip_50_button = self.create_chip_button('50')
        self.chip_200_image = self.create_chip_image('200')
        self.chip_200_button = self.create_chip_button('200')
        self.chip_500_image = self.create_chip_image('500')
        self.chip_500_button = self.create_chip_button('500')
        self.bet_button = self.create_bet_button()
        self.display_bet_widgets()

        self.hit_button = self.create_hit_button()
        self.stand_button = self.create_stand_button()
        self.double_down_button = self.create_double_down_button()
        self.split_button = self.create_split_button()
        self.surrender_button = self.create_surrender_button()

        self.points_player_label = self.create_statistics_label(f'Points\n{self.player.get_points()}')
        self.points_player_label.place(relx=0.065, rely=0.05, anchor=tkinter.CENTER)

        self.current_money_label = self.create_statistics_label(f'Current Money\n{self.player.get_current_money()}')
        self.current_money_label.place(relx=0.065, rely=0.15, anchor=tkinter.CENTER)

        self.money_in_bet_label = self.create_statistics_label(f'Money in bet\n{self.player.get_money_in_bet()}')
        self.money_in_bet_label.place(relx=0.065, rely=0.25, anchor=tkinter.CENTER)

        self.money_to_win_label = self.create_statistics_label(f'Money to win\n{self.player.get_money_to_win()}')
        self.money_to_win_label.place(relx=0.065, rely=0.35, anchor=tkinter.CENTER)

        self.points_dealer_label = self.create_statistics_label(f'Points\n{self.dealer.get_points()}')
        self.points_dealer_label.place(relx=0.935, rely=0.05, anchor=tkinter.CENTER)

    def create_new_game_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="New Game",
                                       command=self.new_game_button_callback)

    def new_game_button_callback(self):
        self.player.clear_hand()
        self.display_bet_widgets()
        self.player.set_points(0)
        self.points_player_label.configure(text=str(f'Points\n{self.player.get_points()}'))
        for i in range(len(self.player_cards_label)):
            self.player_cards_label[i].destroy()
        self.player_cards_label.clear()

        # self.player.add_card(2, self.deck)
        # self.player.add_points()
        # self.display_player_cards()

    def hit_button_callback(self):
        self.player.add_card(1, self.deck)
        self.player.add_points()
        self.points_player_label.configure(text=f'Points\n{self.player.get_points()}')
        self.display_player_cards()
        if self.player.check_burn():
            self.hide_bet_option_widgets()
            self.new_game_button.place(relx=0.79, rely=0.94, anchor=tkinter.CENTER)

    def surrender_button_callback(self):
        pass

    def split_button_callback(self):
        pass

    def double_down_button_callback(self):
        self.player.set_current_money(self.player.get_current_money() - self.player.get_money_in_bet())
        self.current_money_label.configure(text=f'Current Money\n{self.player.get_current_money()}')
        self.player.set_money_in_bet(self.player.get_money_in_bet()*2)
        self.money_in_bet_label.configure(text=f'Money in bet\n{self.player.get_money_in_bet()}')
        self.player.add_card(1, self.deck)
        self.player.add_points()
        self.points_player_label.configure(text=f'Points\n{self.player.get_points()}')
        self.display_player_cards()
        if self.player.check_burn():
            self.hide_bet_option_widgets()
            self.new_game_button.place(relx=0.79, rely=0.94, anchor=tkinter.CENTER)
        # sprawdzenie remisu
        # sprawdzenie black Jack
        #

    def stand_button_callback(self):
        pass

    def bet_button_callback(self):
        self.player.add_card(2, self.deck)
        self.player.add_points()
        self.dealer.add_card(1, self.deck)
        self.points_player_label.configure(text=f'Points\n{self.player.get_points()}')
        self.points_dealer_label.configure(text=f'Points\n{self.dealer.get_points()}')
        self.display_player_cards()
        self.display_dealer_cards()
        self.hide_bet_widgets()

    def display_bet_option_widgets(self):
        self.hit_button.place(relx=0.18, rely=0.94, anchor=tkinter.CENTER)
        self.stand_button.place(relx=0.265, rely=0.94, anchor=tkinter.CENTER)
        self.double_down_button.place(relx=0.39, rely=0.94, anchor=tkinter.CENTER)
        self.split_button.place(relx=0.515, rely=0.94, anchor=tkinter.CENTER)
        self.surrender_button.place(relx=0.62, rely=0.94, anchor=tkinter.CENTER)

    def display_bet_widgets(self):
        self.chip_10_button.place(relx=0.58, rely=0.92, anchor=tkinter.CENTER)
        self.chip_50_button.place(relx=0.66, rely=0.92, anchor=tkinter.CENTER)
        self.chip_200_button.place(relx=0.74, rely=0.92, anchor=tkinter.CENTER)
        self.chip_500_button.place(relx=0.82, rely=0.92, anchor=tkinter.CENTER)
        self.bet_button.place(relx=0.82, rely=0.82, anchor=tkinter.CENTER)
        self.new_game_button.place_forget()

    def hide_bet_widgets(self):
        self.chip_10_button.place_forget()
        self.chip_50_button.place_forget()
        self.chip_200_button.place_forget()
        self.chip_500_button.place_forget()
        self.bet_button.place_forget()
        self.display_bet_option_widgets()

    def hide_bet_option_widgets(self):
        self.hit_button.place_forget()
        self.stand_button.place_forget()
        self.double_down_button.place_forget()
        self.split_button.place_forget()
        self.surrender_button.place_forget()

    def display_player_cards(self):
        image_cards = self.create_image_player_cards_label()
        relx = 0.17
        for i in range(len(image_cards)):
            self.player_cards_label.append(self.create_card_label(image_cards[i]))
            self.player_cards_label[i].place(relx=relx, rely=0.2, anchor=tkinter.CENTER)
            relx += 0.05

    def create_image_player_cards_label(self):
        image_cards = []
        for i in range(len(self.player.hand_deck)):
            image_cards.append(customtkinter.CTkImage(light_image=Image.open(self.deck.cards_image[self.player.hand_deck[i]]),
                                                      dark_image=Image.open(self.deck.cards_image[self.player.hand_deck[i]]),
                                                      size=(60, 87)))
        return image_cards

    def display_dealer_cards(self):
        image_cards = self.create_image_dealer_cards_label()
        relx = 0.83
        for i in range(len(image_cards)):
            self.dealer_cards_label.append(self.create_card_label(image_cards[i]))
            self.dealer_cards_label[i].place(relx=relx, rely=0.2, anchor=tkinter.CENTER)
            relx -= 0.05

    def create_image_dealer_cards_label(self):
        image_cards = []
        for i in range(len(self.dealer.deck)):
            image_cards.append(customtkinter.CTkImage(light_image=Image.open(self.deck.cards_image[self.dealer.deck[i]]),
                                                      dark_image=Image.open(self.deck.cards_image[self.dealer.deck[i]]),
                                                      size=(60, 87)))
        return image_cards

    def create_card_label(self, image_card):
        return customtkinter.CTkLabel(master=self,
                                      text='',
                                      width=60,
                                      height=87,
                                      image=image_card)

    def create_statistics_label(self, money):
        return customtkinter.CTkLabel(master=self,
                                      text=money,
                                      font=('arial', 18))

    def create_surrender_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="Surrender",
                                       command=self.surrender_button_callback)

    def create_split_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="Split",
                                       command=self.split_button_callback)

    def create_double_down_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="Double Down",
                                       command=self.double_down_button_callback)

    def create_stand_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="Stand",
                                       command=self.stand_button_callback)

    def create_hit_button(self):
        return customtkinter.CTkButton(master=self,
                                       font=('arial', 30),
                                       width=100,
                                       height=32,
                                       text="Hit",
                                       command=self.hit_button_callback)


    def create_chip_button(self, value):
        if value == '10':
            return customtkinter.CTkButton(master=self,
                                           text='',
                                           width=75,
                                           command=self.chip_10_button_callback,
                                           image=self.chip_10_image)
        elif value == '50':
            return customtkinter.CTkButton(master=self,
                                           text='',
                                           width=75,
                                           command=self.chip_50_button_callback,
                                           image=self.chip_50_image)
        elif value == '200':
            return customtkinter.CTkButton(master=self,
                                           text='',
                                           width=75,
                                           command=self.chip_200_button_callback,
                                           image=self.chip_200_image)
        else:
            return customtkinter.CTkButton(master=self,
                                           text='',
                                           width=75,
                                           command=self.chip_500_button_callback,
                                           image=self.chip_500_image)

    def create_chip_image(self, value):
        return customtkinter.CTkImage(light_image=Image.open(f"images/chips/{value}.png"),
                                      dark_image=Image.open(f"images/chips/{value}.png"),
                                      size=(75, 75))

    def chip_10_button_callback(self):
        self.player.set_current_money(self.player.get_current_money() - 10)
        self.current_money_label.configure(text=f'Current Money\n{self.player.get_current_money()}')

        self.player.set_money_in_bet(self.player.get_money_in_bet() + 10)
        self.money_in_bet_label.configure(text=f'Money in bet\n{self.player.get_money_in_bet()}')

    def chip_50_button_callback(self):
        self.player.set_current_money(self.player.get_current_money() - 50)
        self.current_money_label.configure(text=f'Current Money\n{self.player.get_current_money()}')

        self.player.set_money_in_bet(self.player.get_money_in_bet() + 50)
        self.money_in_bet_label.configure(text=f'Money in bet\n{self.player.get_money_in_bet()}')

    def chip_200_button_callback(self):
        self.player.set_current_money(self.player.get_current_money() - 200)
        self.current_money_label.configure(text=f'Current Money\n{self.player.get_current_money()}')

        self.player.set_money_in_bet(self.player.get_money_in_bet() + 200)
        self.money_in_bet_label.configure(text=f'Money in bet\n{self.player.get_money_in_bet()}')

    def chip_500_button_callback(self):
        self.player.set_current_money(self.player.get_current_money() - 500)
        self.current_money_label.configure(text=f'Current Money\n{self.player.get_current_money()}')

        self.player.set_money_in_bet(self.player.get_money_in_bet() + 500)
        self.money_in_bet_label.configure(text=f'Money in bet\n{self.player.get_money_in_bet()}')

    def set_window_size(self, size):
        self.geometry(size)

    def create_background_image(self):
        return customtkinter.CTkImage(light_image=Image.open("images/table.png"),
                                      dark_image=Image.open("images/table.png"),
                                      size=(950, 630))

    def set_background(self):
        return customtkinter.CTkLabel(master=self,
                                      width=950,
                                      height=630,
                                      text='',
                                      image=self.background_image)

    def create_exit_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Exit",
                                       command=self.exit_button_callback)

    def create_menu_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Menu",
                                       command=self.menu_button_callback)

    def create_bet_button(self):
        return customtkinter.CTkButton(master=self,
                                       text="Bet",
                                       width=90,
                                       command=self.bet_button_callback)

    def exit_button_callback(self):
        self.destroy()

    def menu_button_callback(self):
        pass
        # self.destroy()

    def create_name_label(self, name):
        return customtkinter.CTkLabel(master=self,
                                      text=name,
                                      width=120,
                                      height=25,
                                      corner_radius=8)
