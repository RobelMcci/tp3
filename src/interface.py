# src/interface.py
import tkinter as tk
from tkinter import messagebox
from .DirtyCalc import executer_logique_dirty_calc

class ApplicationSecondDegreDirty:
    
    def __init__(self, master):
        self.master = master
        master.title("Dirty Calc 2nd Degré (Logique exacte du back-end)")

        # --- Variables pour la SÉRIE 1 ---
        self.a1_var = tk.StringVar(value="1")
        self.b1_var = tk.StringVar(value="0")
        self.c1_var = tk.StringVar(value="-4")
        
        # --- Variables pour la SÉRIE 2 (Vérification) ---
        self.a2_var = tk.StringVar(value="1")
        self.b2_var = tk.StringVar(value="0")
        self.c2_var = tk.StringVar(value="-4")
        
        # --- Variable pour la réponse "recommencer" ---
        self.recommencer_var = tk.StringVar(value="n") # 'o' ou 'n'
        
        self.creer_widgets()

    def creer_widgets(self):
        # Frame Principale
        main_frame = tk.Frame(self.master, padx=15, pady=15)
        main_frame.pack()
        
        # --- Section SÉRIE 1 ---
        tk.Label(main_frame, text="1. Coefficients de BASE (a, b, c) :", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=6, sticky='w', pady=(0, 5))
        self.creer_ligne_saisie(main_frame, self.a1_var, self.b1_var, self.c1_var, start_row=1)

        # --- Section SÉRIE 2 (Vérification) ---
        tk.Label(main_frame, text="2. Coefficients de VÉRIFICATION (a2, b2, c2) :", font=('Arial', 10, 'bold')).grid(row=3, column=0, columnspan=6, sticky='w', pady=(10, 5))
        self.creer_ligne_saisie(main_frame, self.a2_var, self.b2_var, self.c2_var, start_row=4)
        
        # --- Section Recommencer ---
        tk.Label(main_frame, text="3. Réponse Recommencer ('o' ou 'n') :", font=('Arial', 10, 'bold')).grid(row=6, column=0, columnspan=2, sticky='w', pady=(10, 5))
        tk.Entry(main_frame, textvariable=self.recommencer_var, width=5).grid(row=6, column=2, padx=10, sticky='w')

        # --- Bouton de calcul ---
        tk.Button(main_frame, text="Exécuter la Logique du Back-end", command=self.calculer, bg='#8A2BE2', fg='white', font=('Arial', 10, 'bold')).grid(row=7, column=0, columnspan=6, pady=20)

        # --- Zone d'affichage des résultats ---
        tk.Label(main_frame, text="Sortie brute de DirtyCalc.py (Logique) :", font=('Arial', 10, 'underline')).grid(row=8, column=0, columnspan=6, sticky='w', pady=(10, 5))
        
        # Le widget Text pour afficher la sortie multi-lignes
        self.resultat_text = tk.Text(main_frame, height=20, width=80, state=tk.DISABLED, wrap=tk.WORD, bg='#f0f0f0')
        self.resultat_text.grid(row=9, column=0, columnspan=6, sticky='nsew')
        
        # Scrollbar pour le widget Text
        scrollbar = tk.Scrollbar(main_frame, command=self.resultat_text.yview)
        self.resultat_text.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=9, column=6, sticky='ns')

    def creer_ligne_saisie(self, parent, a_var, b_var, c_var, start_row):
        # A
        tk.Label(parent, text="a :").grid(row=start_row, column=0, sticky='e')
        tk.Entry(parent, textvariable=a_var, width=10).grid(row=start_row, column=1, padx=5)
        # B
        tk.Label(parent, text="b :").grid(row=start_row, column=2, sticky='e')
        tk.Entry(parent, textvariable=b_var, width=10).grid(row=start_row, column=3, padx=5)
        # C
        tk.Label(parent, text="c :").grid(row=start_row, column=4, sticky='e')
        tk.Entry(parent, textvariable=c_var, width=10).grid(row=start_row, column=5, padx=5)

    def calculer(self):
        """
        Récupère toutes les entrées et appelle la logique back-end complexe.
        """
        try:
            # Récupération des valeurs principales (Série 1)
            a1 = float(self.a1_var.get())
            b1 = float(self.b1_var.get())
            c1 = float(self.c1_var.get())

            # Récupération des valeurs de vérification (Série 2)
            a2 = float(self.a2_var.get())
            b2 = float(self.b2_var.get())
            c2 = float(self.c2_var.get())
            
            # Récupération de la réponse "recommencer"
            recommencer_resp = self.recommencer_var.get()

            # Appel du back-end avec tous les paramètres nécessaires
            resultat_brut_logique = executer_logique_dirty_calc(a1, b1, c1, a2, b2, c2, recommencer_resp)

            # Affichage du résultat dans le widget Text
            self.resultat_text.config(state=tk.NORMAL)
            self.resultat_text.delete(1.0, tk.END)
            self.resultat_text.insert(tk.END, resultat_brut_logique)
            self.resultat_text.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Erreur de Saisie", "Veuillez entrer des nombres valides pour tous les coefficients et 'o' ou 'n' pour la réponse.")
        except Exception as e:
            messagebox.showerror("Erreur Interne", f"Une erreur inattendue est survenue: {e}")


def main_interface():
    """
    Lance l'interface utilisateur.
    """
    root = tk.Tk()
    app = ApplicationSecondDegreDirty(root)
    root.mainloop()

if __name__ == '__main__':
    main_interface()