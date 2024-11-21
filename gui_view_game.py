from riddle_client import RiddleClient
from gui_template import GUI
import customtkinter
from random import shuffle

class RiddleGameGUI(GUI):
    def __init__(self):
        # inherit all the properties and methods from the parent class
        super().__init__(app_title="Riddler",width=800, height=600)

        self.app.configure(fg_color="#fffbf0")

        # create the riddler client object
        self.riddler_client = RiddleClient()

        # create buttons
        self.play_button = customtkinter.CTkButton(
            self.app,
            text = "Play Game",
            command = lambda: self.play_game_setup()
        )

        self.submit_button = customtkinter.CTkButton(
            self.app,
            text = "Submit",
            command = lambda: self.guess_riddle_submit(),
            state = 'Disabled'
        )

        self.next_button = customtkinter.CTkButton(
            self.app,
            text = "Next",
            command = lambda: self.next_riddle()
        )

        # creates entry widgets
        self.entry_dictionary = {
            'id_widget': "Riddle ID",
            'guess_widget': "Guess",
        }

        # creates labels for the entry widgets
        self.label_dictionary = {
            'id_widget': "Enter Riddle ID",
            'guess_widget': "Enter Riddle Guess",
        }

        # map guess widget with submit button
        self.config_entry_widget(['guess_widget'], self.submit_button)

        # create a text box
        self.text_box = customtkinter.CTkTextbox(
            self.app,
            font=customtkinter.CTkFont(size=16),
            text_color="black",  
            corner_radius=10, 
            border_spacing=20
        )

        # creates properties for game
        self.guess_submitted = False
        self.current_riddle_index = 0
        self.total_guesses = 3

    def play_game_setup(self):
        '''Gets all riddles from client and shuffles them'''

        self.play_button.place_forget()

        self.riddles_list = self.riddler_client.all_riddles()
        shuffle(self.riddles_list)

        self.display_current_riddle()

    def display_current_riddle(self):
        '''Displays the current riddle on the screen 
        and the entry widget'''

        riddle = self.riddles_list[self.current_riddle_index]

        self.reset_textbox()

        self.question_label = customtkinter.CTkLabel(
            self.app,
            text=f"Question: {riddle['question']}",
            fg_color="transparent", 
            font = customtkinter.CTkFont(size=24, family="Georgia"),
        )

        self.question_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.entry_widgets['id_widget'].insert(0, riddle['id'])

    def guess_riddle_submit(self):
        '''Guesses a riddle via the client and decreases a guess'''

        self.total_guesses -= 1
       
        id = self.entry_widgets['id_widget'].get()
        guess =self.entry_widgets['guess_widget'].get()
      
        guess_riddle_json = self.riddler_client.guess_riddle(id,guess)
        message = guess_riddle_json
        self.text_box.insert('end',f"{message}") 
        self.display_text_box(x=.5, y=.7, height=50)

        self.submit_button.grid_forget()

        self.next_button.place(relx=.5, rely=.8, anchor=customtkinter.CENTER)


    def next_riddle(self):
        '''Goes to the next riddle or game over screen'''

        self.next_button.place_forget()
        self.question_label.place_forget()

        self.current_riddle_index += 1

        if self.total_guesses > 0:
            self.display_current_riddle()

        else:
            self.clear()
            self.text_box.insert('end', "Game Over!")
            self.display_text_box(x=.5, y=.5, height=50)

gui = RiddleGameGUI()
gui.run()




