import tkinter as tk
from tkinter import messagebox

# Jautājumu un atbilžu dati
questions = [
    {
        "id": "start",
        "question": "Vai vēlies izmantot maģiju vai smagi sist?",
        "options": ["Maģiju", "Smagi sist", "Nevaru izvēlēties..."],
        "next": {
            "Maģiju": "magic",
            "Smagi sist": "melee",
            "Nevaru izvēlēties...": "cannot-choose"
        }
    },
    {
        "id": "magic",
        "question": "Vai vēlies būt reliģiozs?",
        "options": ["Jā, ļoti!", "Varbūt vēlāk..."],
        "next": {
            "Jā, ļoti!": "cleric",
            "Varbūt vēlāk...": "sorcerer"
        }
    },
    {
        "id": "melee",
        "question": "Tuvcīņa vai distancētā cīņa?",
        "options": ["Tuvcīņa", "Distancētā cīņa"],
        "next": {
            "Tuvcīņa": "melee-combat",
            "Distancētā cīņa": "ranged-combat"
        }
    },
    {
        "id": "cannot-choose",
        "question": "Tu esi labs ar cilvēkiem?",
        "options": ["Jā! Cilvēki man patīk!", "Nē, esmu pārāk uz sevi vērsts."],
        "next": {
            "Jā! Cilvēki man patīk!": "good-with-people",
            "Nē, esmu pārāk uz sevi vērsts.": "self-centered"
        }
    },
    {
        "id": "cleric",
        "question": "Vai vēlies dziedināt cīnītājus?",
        "options": ["Jā", "Nē, ne īsti"],
        "next": {
            "Jā": "cleric-result",
            "Nē, ne īsti": "druid-or-bard"
        }
    },
    {
        "id": "sorcerer",
        "question": "Vai tevī ir iedzimta maģija?",
        "options": ["Jā, tā ir manās asinīs!", "Nē, es to apgūstu!"],
        "next": {
            "Jā, tā ir manās asinīs!": "sorcerer-result",
            "Nē, es to apgūstu!": "wizard-or-fighter"
        }
    },
    {
        "id": "melee-combat",
        "question": "Vai cīnies par kādu mērķi?",
        "options": ["Jā. Es cīnos par taisnību!", "Nē. Man patīk lietas dauzīt."],
        "next": {
            "Jā. Es cīnos par taisnību!": "paladin-or-monk",
            "Nē. Man patīk lietas dauzīt.": "barbarian-or-fighter"
        }
    },
    {
        "id": "ranged-combat",
        "question": "Vai tu esi veikls?",
        "options": ["Jā", "Nē"],
        "next": {
            "Jā": "ranger-result",
            "Nē": "fighter-result"
        }
    },
    {
        "id": "druid-or-bard",
        "question": "Vai mīli dzīvniekus?",
        "options": ["Jā, viņi ir tik pūkaini!", "Nē, ne pārāk."],
        "next": {
            "Jā, viņi ir tik pūkaini!": "druid-result",
            "Nē, ne pārāk.": "bard-or-cleric"
        }
    },
    {
        "id": "bard-or-cleric",
        "question": "Vai tu raksti dzeju saviem draugiem?",
        "options": ["Jā! Es rakstu dzeju un dziesmas!", "Nē"],
        "next": {
            "Jā! Es rakstu dzeju un dziesmas!": "bard-result",
            "Nē": "cleric-result"
        }
    },
    {
        "id": "wizard-or-fighter",
        "question": "Vai mācies maģiju?",
        "options": ["Jā", "Nē, maģija ir mana būtība!"],
        "next": {
            "Jā": "wizard-result",
            "Nē, maģija ir mana būtība!": "sorcerer-result"
        }
    },
    {
        "id": "paladin-or-monk",
        "question": "Zini, kā lietot ieročus?",
        "options": ["Jā", "Nē"],
        "next": {
            "Jā": "paladin-result",
            "Nē": "monk-result"
        }
    },
    {
        "id": "barbarian-or-fighter",
        "question": "Vai esi dusmīgs?",
        "options": ["Jā", "Nē, es vienkārši gribu sist"],
        "next": {
            "Jā": "barbarian-result",
            "Nē, es vienkārši gribu sist": "fighter-result"
        }
    },
    {
        "id": "good-with-people",
        "question": "Vai esi viltīgs?",
        "options": ["Jā", "Nē, ne ļoti."],
        "next": {
            "Jā": "rogue-result",
            "Nē, ne ļoti.": "ranger-result"
        }
    },
    {
        "id": "self-centered",
        "question": "Jūsu raksturs ir: Kareivis (Fighter)",
        "options": [],
        "next": {}
    },
    {
        "id": "cleric-result",
        "question": "Jūsu raksturs ir: Priesteris (Cleric)",
        "options": [],
        "next": {}
    },
    {
        "id": "druid-result",
        "question": "Jūsu raksturs ir: Druīds (Druid)",
        "options": [],
        "next": {}
    },
    {
        "id": "bard-result",
        "question": "Jūsu raksturs ir: Bards (Bard)",
        "options": [],
        "next": {}
    },
    {
        "id": "wizard-result",
        "question": "Jūsu raksturs ir: Mags (Wizard)",
        "options": [],
        "next": {}
    },
    {
        "id": "sorcerer-result",
        "question": "Jūsu raksturs ir: Burvis (Sorcerer)",
        "options": [],
        "next": {}
    },
    {
        "id": "paladin-result",
        "question": "Jūsu raksturs ir: Paladins (Paladin)",
        "options": [],
        "next": {}
    },
    {
        "id": "monk-result",
        "question": "Jūsu raksturs ir: Mūks (Monk)",
        "options": [],
        "next": {}
    },
    {
        "id": "barbarian-result",
        "question": "Jūsu raksturs ir: Barbars (Barbarian)",
        "options": [],
        "next": {}
    },
    {
        "id": "rogue-result",
        "question": "Jūsu raksturs ir: Blēdis (Rogue)",
        "options": [],
        "next": {}
    },
    {
        "id": "ranger-result",
        "question": "Jūsu raksturs ir: Mežzinis (Ranger)",
        "options": [],
        "next": {}
    },
    {
        "id": "fighter-result",
        "question": "Jūsu raksturs ir: Kareivis (Fighter)",
        "options": [],
        "next": {}
    }
]

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Viktorīna")
        self.geometry("600x400")
        self.current_question_id = "start"
        self.selected_option_var = tk.StringVar()
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self)
        self.options_frame.pack(pady=10)

        self.next_button = tk.Button(self, text="Nākamais jautājums", command=self.next_question)
        self.next_button.pack(pady=20)

    def load_question(self):
        question_data = next((q for q in questions if q["id"] == self.current_question_id), None)
        if not question_data:
            return

        self.question_label.config(text=question_data["question"])
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.option_vars = []
        for option in question_data["options"]:
            rb = tk.Radiobutton(self.options_frame, text=option, variable=self.selected_option_var, value=option)
            rb.pack(anchor="w")

    def next_question(self):
        selected_option = self.selected_option_var.get()
        if not selected_option:
            messagebox.showerror("Kļūda", "Lūdzu, izvēlieties opciju.")
            return

        question_data = next((q for q in questions if q["id"] == self.current_question_id), None)
        if not question_data:
            return

        next_id = question_data["next"].get(selected_option)
        if next_id:
            self.current_question_id = next_id
            if "result" in next_id:
                self.show_result(next_id)
            else:
                self.load_question()
        else:
            messagebox.showerror("Kļūda", "Nevarēja atrast nākamo jautājumu.")

    def show_result(self, result_id):
        result = next((q for q in questions if q["id"] == result_id), None)
        if result:
            self.question_label.config(text=result["question"])
            self.options_frame.destroy()
            self.next_button.destroy()
        else:
            messagebox.showerror("Kļūda", "Nevarēja atrast rezultātu.")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
 