#Code by GPT-5 and Noanb for correction of our version without graphic interface !
import random
import tkinter as tk
from tkinter import messagebox

def creerEnchevetrements_acycliques(bag, i, pos, max_edges):
    """Create acyclic entanglements for the Mikado game."""
    candidats = [x for x in bag if x != i and pos[x] < pos[i]]
    nb = random.randint(0, min(len(candidats), max_edges))
    random.shuffle(candidats)
    return [(i, x) for x in candidats[:nb]]

def creerMikado_acyclique(bag):
    """Create an acyclic Mikado game setup."""
    ordre_retrait = bag.copy()
    random.shuffle(ordre_retrait)
    pos = {v: idx for idx, v in enumerate(ordre_retrait)}
    jeu = []
    for i in bag:
        jeu += creerEnchevetrements_acycliques(bag, i, pos, max(0, len(bag)-1))
    return jeu, ordre_retrait

def peutRetirer(i, bag, jeu):
    """Check if a stick can be removed from the game."""
    for (a, b) in jeu:
        if a == i and b in bag:
            return False
    return True

def quelOrdre(bag, jeu):
    """Determine the order of stick removal."""
    if not bag:
        return []
    for i in bag:
        if peutRetirer(i, bag, jeu):
            suite = quelOrdre([x for x in bag if x != i], jeu)
            if suite is not None:
                return [i] + suite
    return None

#Interface graphqiue avec tkinter
class MikadoGUI:
    def __init__(self, root):
        """Initialize the Mikado game GUI."""
        self.root = root
        self.root.title("🎋 Jeu du Mikado - BAB1 Sc. Info.")
        self.root.geometry("960x700")
        self.root.configure(bg="#1E1E2E")  # fond sombre moderne

        # Canvas (zone de dessin)
        self.canvas = tk.Canvas(self.root, width=880, height=500, bg="#2E2E3E", highlightthickness=0)
        self.canvas.pack(pady=30)

        # Zone des boutons
        btn_frame = tk.Frame(self.root, bg="#1E1E2E")
        btn_frame.pack(pady=10)

        style = {"bg": "#3A3A4A", "fg": "#304652", "activebackground": "#5A5AFF", "font": ("Segoe UI", 11, "bold"), "bd": 0, "relief": "flat", "width": 30, "height": 2}

        self.btn_gen = tk.Button(btn_frame, text="🎲 Créer un Mikado jouable (aléatoire)", command=self.generer_mikado, **style)
        self.btn_gen.grid(row=0, column=0, padx=10, pady=5)

        self.btn_gen_static = tk.Button(btn_frame, text="📘 Charger exemple statique (test)", command=self.charger_exemple_stat, **style)
        self.btn_gen_static.grid(row=1, column=0, padx=10, pady=5)

        self.btn_ordre = tk.Button(btn_frame, text="🧩 Afficher l'ordre de retrait (solution)", command=self.afficher_ordre, **style)
        self.btn_ordre.grid(row=2, column=0, padx=10, pady=5)

        self.btn_ordre = tk.Button(btn_frame, text="Matis est trop beau il a pas besion de GPT-5 pour le faire ", command=messagebox.showwarning("Attention", "oui matis est plus chaud que moi en code ! "), **style)
        self.btn_ordre.grid(row=3, column=0, padx=10, pady=5)

        self.info_label = tk.Label(self.root, text="", bg="#1E1E2E", fg="#D0D0FF", font=("Consolas", 12, "bold"))
        self.info_label.pack(pady=10)

        self.bag, self.jeu, self.lines, self.y_positions = [], [], {}, {}
        self.animation_token = 0

    def _clear_canvas_state(self):
        """Clear the canvas and reset state."""
        self.canvas.delete("all")
        self.lines.clear()
        self.y_positions.clear()

    def generer_mikado(self):
        """Generate a playable random Mikado game."""
        self.animation_token += 1
        self._clear_canvas_state()

        n = random.randint(4, 8)
        self.bag = list(range(n))
        self.jeu, ordre_retrait = creerMikado_acyclique(self.bag)

        spacing = 400 // max(1, n - 1)
        base_y = 80
        margin_left, margin_right = 100, 780
        colors = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#C06C84", "#A29BFE", "#81ECEC", "#55E6C1", "#F5A623"]

        for idx, b in enumerate(self.bag):
            x1 = margin_left + (idx % 3) * 15
            y = base_y + idx * spacing
            x2 = margin_right - (idx % 4) * 10
            line_color = colors[idx % len(colors)]
            line = self.canvas.create_line(x1, y, x2, y, width=10, fill=line_color, capstyle=tk.ROUND)
            self.canvas.create_text(x2 + 40, y, text=f"B{b}", fill="#FFFFFF", font=("Segoe UI", 12, "bold"))
            self.lines[b] = line
            self.y_positions[b] = ((x1 + x2) / 2, y)

        # flèches visibles et stylées
        for (a, b) in self.jeu:
            if a in self.y_positions and b in self.y_positions:
                x_a, y_a = self.y_positions[a]
                x_b, y_b = self.y_positions[b]
                self.canvas.create_line(
                    x_b, y_b - 10, (x_a + x_b) / 2, (y_b + y_a) / 2, x_a, y_a + 10,
                    arrow=tk.LAST, fill="#FFDD55", width=3, dash=(5, 2), smooth=True
                )

        self.info_label.config(text=f"{n} baguettes générées ✨  ({len(self.jeu)} enchevêtrements)")

    def charger_exemple_stat(self):
        """Load a static example of the Mikado game."""
        self.animation_token += 1
        self._clear_canvas_state()

        self.bag = [0, 1, 2, 3]
        self.jeu = [(0, 1), (0, 2), (3, 2)]
        margin_left, margin_right = 100, 780
        spacing, base_y = 90, 100
        colors = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#C06C84"]

        for idx, b in enumerate(self.bag):
            x1 = margin_left + idx * 10
            y = base_y + idx * spacing
            x2 = margin_right - idx * 10
            line = self.canvas.create_line(x1, y, x2, y, width=10, fill=colors[idx % len(colors)], capstyle=tk.ROUND)
            self.canvas.create_text(x2 + 40, y, text=f"B{b}", fill="#FFFFFF", font=("Segoe UI", 12, "bold"))
            self.lines[b] = line
            self.y_positions[b] = ((x1 + x2) / 2, y)

        for (a, b) in self.jeu:
            if a in self.y_positions and b in self.y_positions:
                x_a, y_a = self.y_positions[a]
                x_b, y_b = self.y_positions[b]
                self.canvas.create_line(
                    x_b, y_b - 10, (x_a + x_b) / 2, (y_b + y_a) / 2, x_a, y_a + 10,
                    arrow=tk.LAST, fill="#FFDD55", width=3, dash=(5, 2), smooth=True
                )

        self.info_label.config(text="Exemple statique chargé ✅ (4 baguettes, 3 enchevêtrements)")

    def afficher_ordre(self):
        """Display the order of stick removal."""
        if not self.bag:
            messagebox.showwarning("Attention", "Veuillez d'abord générer ou charger un Mikado.")
            return

        ordre = quelOrdre(self.bag, self.jeu)
        if ordre is None:
            messagebox.showerror("Aucun ordre possible", "Impossible de retirer toutes les baguettes sans bouger les autres.")
        else:
            self.info_label.config(text=f"Ordre de retrait : {' → '.join(map(str, ordre))}")
            token = self.animation_token
            self.root.after(400, lambda: self.animer_retrait(ordre, 0, token))

    def animer_retrait(self, ordre, index, token):
        """Animate the removal of sticks in the specified order."""
        if token != self.animation_token or index >= len(ordre):
            return
        i = ordre[index]
        if i in self.lines:
            self.canvas.itemconfig(self.lines[i], fill="#666666")
        self.root.after(800, lambda: self.animer_retrait(ordre, index + 1, token))


if __name__ == "__main__":
    root = tk.Tk()
    app = MikadoGUI(root)
    root.mainloop()