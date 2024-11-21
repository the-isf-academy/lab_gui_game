import customtkinter

class GUI:
    def __init__(self, app_title, width, height):

        self.app = customtkinter.CTk()
        self.app.geometry(f"{width}x{height}")
        self.app.title(app_title)
        
    def widget_setup(self):
        '''Sets up all widgets'''
        
        # setup menu  buttons
        self.setup_play_button()

        # setup entry widgets
        self.entry_widgets = {}
        self.setup_entry_widgets()

        # setup entry widget labels
        self.labels = {}
        self.setup_labels()

        # setup submit buttons
        self.setup_button(self.submit_button)
        self.setup_button(self.next_button)

    def setup_play_button(self):
        '''Creates menu buttons'''

        self.play_button.configure(
            font = customtkinter.CTkFont(size=16, family="Georgia"),
            width = 400,
            height= 400,
            text_color="#363e4f",
            fg_color="#10b367",
            hover_color="#c8cedb",
            border_spacing=10)

        self.play_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    def setup_button(self, button):
        '''Create submit buttons for entry widgets'''

        button.configure( 
            font = customtkinter.CTkFont(size=16),
            width = 100,
            height= 50,
            text_color="#ffffff",
            fg_color="#196da6",
            hover_color="#c8cedb",
            border_spacing=10)

    def setup_entry_widgets(self):
        '''Creates entry widgets'''
        
        for label, text in self.entry_dictionary.items():
            self.entry_widgets[label] = customtkinter.CTkEntry(
                self.app,
                placeholder_text = text)

    def setup_labels(self):
        '''Creates labels for entry widgets'''

        for label, text in self.label_dictionary.items():
            self.labels[label] = customtkinter.CTkLabel(
                self.app, 
                text = text, 
                fg_color="transparent")

    
    def display_text_box(self, x, y,height):
        '''Displays text box on the grid'''

        self.text_box.place(relx=x, rely=y, anchor=customtkinter.CENTER)
        self.text_box.configure(height = height) 
        self.text_box.configure(state='disabled') # sets to read-only

    def config_entry_widget(self,widget_list, submit_button):
        '''Sets up entry widgets with appropriate labels 
        and places them on the screen'''

        self.clear()

        # Bind the entry boxes to key entry
        self.setup_entry_bind(widget_list, submit_button)

        # place entry widget and label on window
        for widget in widget_list:
            self.labels[widget].place(relx=0.4, rely=0.4, anchor=customtkinter.CENTER)
            self.entry_widgets[widget].place(relx=0.6, rely=0.4, anchor=customtkinter.CENTER)

        # Place submit button on window
        self.submit_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    def setup_entry_bind(self, widget_list, submit_button):
        '''Binds widgets to typing in the entry box'''

        for widget in widget_list:
            self.entry_widgets[widget].bind(
                '<KeyRelease>', 
                lambda entry: self.enable_submit_guess_button(widget_list, submit_button))

    def enable_submit_guess_button(self, entry_widgets, submit_button):
        '''Only activate submit button if user 
        has entered information into the entry box'''

        num_filled = 0
        
        for widget in entry_widgets:
            if self.entry_widgets[widget].get():
                num_filled += 1
        
        if num_filled == len(entry_widgets):
            submit_button.configure(state="normal")

    def reset_textbox(self):
        '''Remove all text from textbox'''
        
        self.text_box.configure(state='normal') # sets to read
        self.text_box.delete('1.0', 'end')      # deletes all text 
        
    def clear(self):
        '''Clear all widgets that are 
        NOT the menu from the grid'''

        self.reset_textbox()
        self.text_box.place_forget()

        for entry_widget_title, entry_widget in self.entry_widgets.items():
            entry_widget.delete(0,'end')
            entry_widget.place_forget()

        for label_title, label in self.labels.items():
            label.place_forget()
        
        self.submit_button.place_forget()

    def run(self):
        '''Launches the app with the widgets setup'''

        self.widget_setup()
        self.app.mainloop()