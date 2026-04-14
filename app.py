import customtkinter as ctk
from tkinter import messagebox
from data import QUESTIONS
from logic import calculate_results

class PersonalityApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Personality Predictor")
        self.geometry("600x700")
        
        self.questions = QUESTIONS
        self.answers = []
        self.current_idx = 0

        # UI Elements
        self.label_title = ctk.CTkLabel(self, text="Personality Prediction System", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)

        self.question_label = ctk.CTkLabel(self, text=self.questions[0], font=("Arial", 18), wraplength=500)
        self.question_label.pack(pady=30)

        # Rating Buttons (1 to 5)
        self.radio_var = ctk.IntVar(value=3)
        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.pack(pady=20)

        for i in range(1, 6):
            rb = ctk.CTkRadioButton(self.radio_frame, text=str(i), variable=self.radio_var, value=i)
            rb.pack(side="left", padx=10)

        self.next_btn = ctk.CTkButton(self, text="Next Question", command=self.next_question)
        self.next_btn.pack(pady=40)

    def next_question(self):
        self.answers.append(self.radio_var.get())
        self.current_idx += 1
        
        if self.current_idx < len(self.questions):
            self.question_label.configure(text=self.questions[self.current_idx])
            self.progress.set(self.current_idx / len(self.questions))
            self.radio_var.set(3) # Reset to middle
        else:
            self.show_result()

    def show_result(self):
        result_text = calculate_results(self.answers)
        messagebox.showinfo("Result", result_text)
        self.destroy()
