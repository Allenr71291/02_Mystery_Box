from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self, parent):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        self.temp_Converter_label = Label(self.start_frame,
                                          text="Mystery Box Game",
                                          font=("Arial", "19", "bold"),
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="please enter a dollar amount "
                                          "(Between $5 and $50). in the box "
                                          "below. Then choose the stakes."
                                          "The higher the stakes the more "
                                          "you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame, width=10)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0, column=0)

        self.add_funds_button = Button(self.entry_error_frame,
                                       font="Arial 19 bold",
                                       text="Add Funds",
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # button frame (row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons here:
        button_font = "Arial 12 bold"

        # Orange low stakes button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Yellow Medium stakes button
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#FFFF33")
        self.medium_stakes_button.grid(row=0, column=1, pady=10)

        # Green High Stakes button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="#99FF33")
        self.high_stakes_button.grid(row=0, column=2, pady=10)

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        # help button
        self.help_button = Button(self.stakes_frame, font="Arial 12 bold",
                                  text="Help/Instructions", command=self.help,
                                  bg="#808080", fg="white")
        self.help_button.grid(row=1, column=1, pady=10)

    # Number checking function
    def check_funds(self):
        starting_balance = self.start_amount_entry.get()
        # Game(self, stakes, starting_balance)

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disabling buttons
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high!  The most you can risk in " \
                                 "This game is $50"

            elif starting_balance >= 15:
                # Enable all buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)

            elif starting_balance >= 10:
                # Enable 2 buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)

            else:
                # Enable low stakes button
                self.low_stakes_button.config(state=NORMAL)

        except ValueError:
            has_errors= "yes"
            error_feedback = "Please enter a dollar amount(no text / decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        # hide start up menu disabled for testing purposes
        root.withdraw()

    def help(self):
        get_help = Help(self)

        help_text="Choose an amount to play with and then choose the stakes. "\
        "Higher stakes cost more per round but you can win more as well. \n\n"\
        "When you enter the play area, you will see three mystery boxes.\n"\
        "To Reveal the contents of the boxes, click the 'Open Boxes' button.\n\n"\
        "If you don't have enough money to play, the button will turn red and "\
        "You will need to quit the game.\n\n"\
        "The Contents of the boxes will be added to your balance. The boxes could contain....\n"\
        "Low:Lead($0) | Copper($1) | Silver($2) | Gold($10)\n"\
        "Medium:Lead($0) | Copper($2) | Silver($4) | Gold($25)\n"\
        "High:Lead($0) | Copper($5) | Silver($10) | Gold($50)\n"\
        "\n\n"\
        "If each box contains gold, you earn $30(low stakes). If they contained " \
        "copper, silver and gold, you will receive $13 (1 + 2 + 10) and so on."
        get_help.help_text.configure(text=help_text)


class Help:
    def __init__(self, partner):
        background = "white"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (Help Box)
        self.help_box = Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Sets up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, bg=background, wrap=350)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", bg=background,
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Game:
    def __init__(self, partner, stakes, starting_balance):

        self.balance = IntVar()

        self.balance.set(starting_balance)

        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        self.game_stats_list = [starting_balance, starting_balance]
        self.round_stats_list = []

        # List for holding stats
        self.round_stats_list = []

        # GUI Setup
        self.game_box = Toplevel()

        # If user cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="question.gif")

        self.prize1_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFF333", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance Label (row 4)

        start_text = "Game Cost: ${} \n "" \nHow Much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                   text=start_text, wrap=300,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  command=self.help,
                                  bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats....",
                                   font="Arial 15 bold",
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list),
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):

        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []

        copper = ["copper_low.gif", "copper_med.gif", "copper_high.gif"]
        silver = ["silver_low.gif", "silver_med.gif", "silver_high.gif"]
        gold = ["gold_low.gif", "gold_med.gif", "gold_high.gif"]

        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file=gold[stakes_multiplier - 1])
                prize_list = "gold (${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 1 < prize_num <= 25:
                prize = PhotoImage(file=silver[stakes_multiplier - 1])
                prize_list = "silver (${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 3 < prize_num <= 65:
                prize = PhotoImage(file=copper[stakes_multiplier - 1])
                prize_list = "copper (${})".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "lead ($0)"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes and edit background...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1

        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2

        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add Winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)
        # update game_stats_list with current balance (replace item in
        # position 1 with current balance)
        self.game_stats_list[1] = current_balance

        balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Add round results to stats list
        round_summary = "{} | {} | {} - Cost: ${} |" \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(stats_prizes[0], stats_prizes[1],
                                     stats_prizes[2],
                                     5 * stakes_multiplier, round_winnings,
                                     current_balance)
        self.round_stats_list.append(round_summary)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()

    def help(self):

        get_help = Help(self)

        help_text="Choose an amount to play with and then choose the stakes. Higher stakes cost more per " \
                  "round but you can win more as well. \n\n When you enter the play area, you will see three " \
                  "mystery boxes.\n To Reveal the contents of the boxes, click the 'Open Boxes' button.\n\n" \
                  "If you don't have enough money to play, the button will turn red and "" \
                  ""You will need to quit the game.\n\n"" \
                  ""The Contents of the boxes will be added to your balance. The boxes could contain....\n"\
                  "Low:Lead($0) | Copper($1) | Silver($2) | Gold($10)\n"" \
                  ""Medium:Lead($0) | Copper($2) | Silver($4) | Gold($25)\n"" \
                  ""High:Lead($0) | Copper($5) | Silver($10) | Gold($50)\n"" \
                  ""\n\n"" \
                  ""If each box contains gold, you earn $30(low stakes). If they contained "" \
                  ""copper, silver and gold, you will recieve $13 (1 + 2 + 10) and so on."
        get_help.help_text.configure(text=help_text)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)


class GameStats:
    def __init__(self, partner, game_history, game_stats):

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = " Arial 12 bold"
        content = "Arial 12"

        # Sets up child window(ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up help heading (row 0)
        self.stats_heading = Label(self.stats_frame, text="Game Statistics",
                                   font="arial 19 bold")
        self.stats_heading.grid(row=0)

        self.export_instructions = Label(self.stats_frame,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "round that you played", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (Row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance (row 0)
        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value = Label(self.details_frame, font=content,
                                         text="${}".format(game_stats[0]), anchor="w")
        self.start_balance_value.grid(row=0, column=1, padx=0)

        # Current Balance (row 1.0)
        self.current_balance_label = Label(self.details_frame, font=heading,
                                           text="Current Balance:",
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_label = Label(self.details_frame, font=content,
                                           text="${}".format(game_stats[1]), anchor="e")
        self.current_balance_label.grid(row=1, column=1, padx=1)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=heading,
                                              text="Games Played:",
                                              anchor="e")
        self.games_played_value_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history),
                                              anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)


        # Dismiss Button (Row 3)
        self.dismiss_export = Frame(self.stats_frame)
        self.dismiss_export.grid(row=3)

        self.dismiss_btn = Button(self.dismiss_export, text="Dismiss", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=7,
                                  command=partial(self.close_stats, partner))
        self.dismiss_btn.grid(row=6, column=0, pady=10, padx=5)

        self.export_btn = Button(self.dismiss_export, text="Export", fg="white",
                                  bg="#003366", font="Arial 15 bold", width=7,
                                  command=lambda: self.to_export(game_history, game_stats))
        self.export_btn.grid(row=6, column=1, pady=10, padx=5)

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def to_export(self, game_history, game_stats):
        Export(self, game_history, game_stats)


class Export:
    def __init__(self, partner, game_history, all_game_stats):

        # disable export button
        partner.export_btn.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, )
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / "
                                                         "Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box below and press the "
                                                         "Save button to save your "
                                                         "calculation history to a "
                                                         "text file. ",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning Text Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your calculation history ",
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        self.save_error_label = Label(self.export_frame, text="")
        self.save_error_label.grid(row=5, pady=10)

        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=4)

        # Save and Canel Buttons (row 0 of save_cancel_frame
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(lambda: self.close_export(partner)))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"
        problem = ""

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
                has_error = "yes"

            elif letter == ".":
                problem = "(no .'s allowed)"
                has_error = "yes"

            else:
                problem = "(the filename you chose is not valid)"
                has_error = "yes"

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.filename_entry.config(bg="#ffafaf")
            self.save_error_label.config(text=problem)

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt
            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Game Statistics\n\n")

            # Game stats
            f.write("Starting Balance : ${:.2f}\n".format(game_stats[0]))
            f.write("Current Balance : ${:.2f}\n".format(game_stats[1]))
            f.write("Amount Won / Lost : ${:.2f}\n".format(game_stats[1] - game_stats[0]))

            # heading for rounds
            f.write("\n\nRound Details\n\n")

            for item in game_history:
                f.write(item + "\n")

            f.close()

        self.close_export(partner)

    def close_export(self, partner):
        partner.export_btn.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
