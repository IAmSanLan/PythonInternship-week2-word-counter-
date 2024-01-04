import tkinter as tk
import re

#Main class
class WordCounter:
    def __init__(self):
        self.word_count_label = None
        self.char_count_label = None
        self.syllable_count_label = None
        self.sentence_count_label = None
        self.input_text = None
        self.error_label = None  
        self.refresh_button = None
        self.copy_button = None
        self.cut_button = None
        self.paste_button = None

        # Undo/redo History
        self.history = []
        self.current_state = ""
        self.redo_history = []  

        # Welcome window
        self.welcome_window = tk.Tk()
        self.welcome_window.title("Welcome to Word Counter")
        self.welcome_window.geometry("400x300")
        self.welcome_window.configure(bg="peachpuff")

        self.create_welcome_interface()

    def create_welcome_interface(self):
        welcome_label = tk.Label(self.welcome_window, text="Welcome to Word Counter", font=("Verdana", 16, "underline"), bg="peachpuff")
        welcome_label.pack(pady=20)

        note_label = tk.Label(self.welcome_window, text="\n \n (Please enter your text into the textbox placed on the left side.)\n (To start the word counter for the input text, click the Proceed button.)", bg="peachpuff")
        note_label.pack()

        note_label2 = tk.Label(self.welcome_window, text="\n To begin click Continue", bg="peachpuff")
        note_label2.pack()


        #entry button to main window
        continue_button = tk.Button(self.welcome_window, text="Continue", command=self.continue_to_word_counter, bg="darkgray")
        continue_button.pack(pady=40)

    def continue_to_word_counter(self):
        self.welcome_window.destroy()
        self.word_counter_window()

    def count_text(self):
        # Input
        text = self.input_text.get("1.0", "end-1c")

        # Error Handling of No text entered
        if text.strip() == "":
            self.error_label.config(text="Error: No text entered",font=("Comic Sans MS", 12), fg="red")
            return

        # Clear
        self.error_label.config(text="")

        # Append for undo/redo
        self.history.append(self.current_state)
        self.current_state = text

        # Word Counting Logic
        words = text.split()
        word_count = len(words)
        self.word_count_label.config(text=f"Words: \n {word_count} ",font=("Comic Sans MS", 11))

        # Character Counting Logic
        char_count = len(text)
        self.char_count_label.config(text=f"Characters: \n {char_count} ",font=("Comic Sans MS", 11))

        # Syllable Counting Logic
        syllable_count = sum(len(re.findall(r'[aeiouy]+', word)) for word in words)
        self.syllable_count_label.config(text=f"Syllables: \n {syllable_count} ",font=("Comic Sans MS", 11))

        # Sentence Counting Logic
        sentence_count = len(re.findall(r'[.!?]+', text))
        self.sentence_count_label.config(text=f"Sentences: \n {sentence_count} ",font=("Comic Sans MS", 11))

    def undo(self):
        # undoing
        if len(self.history) > 0:
            self.redo_history.append(self.current_state)
            self.current_state = self.history.pop()

            # Update input_text with the current state
            self.input_text.delete("1.0", "end")
            self.input_text.insert("1.0", self.current_state)

    def redo(self):
        #redoing
        if len(self.redo_history) > 0:
            self.history.append(self.current_state)
            self.current_state = self.redo_history.pop()

            # Update input_text 
            self.input_text.delete("1.0", "end")
            self.input_text.insert("1.0", self.current_state)

    def copy_text(self):
        self.input_text.clipboard_clear()
        self.input_text.clipboard_append(self.input_text.selection_get())

    def cut_text(self):
        self.copy_text()
        self.input_text.delete("sel.first", "sel.last")

    def paste_text(self):
        self.input_text.insert("insert", self.input_text.clipboard_get())

    def word_counter_window(self):
        word_counter_window = tk.Tk()
        word_counter_window.title("Word Counter")
        word_counter_window.geometry("700x500")

        #Input Box
        left_panel = tk.Frame(word_counter_window, width=400, bg="white")
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.input_text = tk.Text(left_panel, height=20, width=50)
        self.input_text.pack(pady=10, padx=10)
        

        # Buttons -> copy, cut, and paste
        copy_button = tk.Button(left_panel, text="Copy", command=self.copy_text,bg="coral")
        copy_button.pack(side=tk.RIGHT, padx=10)

        cut_button = tk.Button(left_panel, text="Cut", command=self.cut_text,bg="coral")
        cut_button.pack(side=tk.RIGHT, padx=10)

        paste_button = tk.Button(left_panel, text="Paste", command=self.paste_text,bg="coral")
        paste_button.pack(side=tk.RIGHT, padx=10)

        #Panels
        right_panel = tk.Frame(word_counter_window, width=400, bg="pink")
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        upper_right_panel = tk.Frame(right_panel, bg="pink")
        upper_right_panel.pack(expand=True, pady=10)

        self.word_count_label = tk.Label(upper_right_panel, text="Words: 0", bg="pink")
        self.word_count_label.grid(row=0, column=0, padx=5, pady=5)

        self.char_count_label = tk.Label(upper_right_panel, text="Characters: 0", bg="pink")
        self.char_count_label.grid(row=0, column=1, padx=5, pady=5)

        self.syllable_count_label = tk.Label(upper_right_panel, text="Syllables: 0", bg="pink")
        self.syllable_count_label.grid(row=1, column=0, padx=5, pady=5)

        self.sentence_count_label = tk.Label(upper_right_panel, text="Sentences: 0", bg="pink")
        self.sentence_count_label.grid(row=1, column=1, padx=5, pady=5)

        

        process_button = tk.Button(right_panel, text="Process", command=self.count_text, bg="coral")
        process_button.pack(pady=10)

        lower_right_panel = tk.Frame(right_panel, bg="white")
        lower_right_panel.pack(expand=True, pady=10)

        self.error_label = tk.Label(lower_right_panel, text="", bg="white", fg="red")  # Error msg
        self.error_label.pack(pady=5)

        

        #button details
        undo_button = tk.Button(lower_right_panel, text="Undo", command=self.undo,bg="hotpink")
        undo_button.pack(side=tk.LEFT, padx=10)

        redo_button = tk.Button(lower_right_panel, text="Redo", command=self.redo,bg="hotpink")
        redo_button.pack(side=tk.LEFT, padx=10)

        self.refresh_button = tk.Button(lower_right_panel, text="Refresh", command=self.refresh_counts, bg="hotpink")
        self.refresh_button.pack(side=tk.LEFT, padx=10)


        word_counter_window.mainloop()
        
    def refresh_counts(self):
        # Reset input box
        self.word_count_label.config(text="Words: 0")
        self.char_count_label.config(text="Characters: 0")
        self.syllable_count_label.config(text="Syllables: 0")
        self.sentence_count_label.config(text="Sentences: 0")
        self.input_text.delete(1.0, tk.END)

# instance of WordCounter
word_counter_instance = WordCounter()
