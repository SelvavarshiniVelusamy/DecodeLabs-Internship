import string
import tkinter as tk
from tkinter import ttk

# Password Strength Checker
# Educational project: checks basic password composition locally.
# Passwords are not saved, transmitted, or logged.

BG = "#081426"
PANEL = "#101f35"
FIELD = "#0b1729"
BLUE = "#2f80ed"
TEXT = "#eef4ff"
MUTED = "#a8bad8"
GREEN = "#35e6a1"
YELLOW = "#ffd166"
RED = "#ff657a"
BORDER = "#233d60"

REQUIREMENTS = [
    ("At least 12 characters", lambda p: len(p) >= 12),
    ("Contains an uppercase letter", lambda p: any(c.isupper() for c in p)),
    ("Contains a lowercase letter", lambda p: any(c.islower() for c in p)),
    ("Contains a number", lambda p: any(c.isdigit() for c in p)),
    ("Contains a symbol", lambda p: any(c in string.punctuation for c in p)),
]


class PasswordCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("900x650")
        self.root.minsize(760, 580)
        self.root.configure(bg=BG)

        self.password_var = tk.StringVar()
        self.show_password = tk.BooleanVar(value=False)
        self.requirement_labels = []
        self.meter_segments = []

        self._build_ui()
        self.password_var.trace_add("write", self._update_strength)
        self._update_strength()

    def _build_ui(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=30, pady=(24, 18))

        tk.Label(
            header, text="🔐  PASSWORD STRENGTH CHECKER",
            bg=BG, fg=TEXT, font=("Segoe UI", 21, "bold")
        ).pack()
        tk.Label(
            header, text="Create stronger passwords. Stay safer online.",
            bg=BG, fg=MUTED, font=("Segoe UI", 10)
        ).pack(pady=(6, 0))

        content = tk.Frame(self.root, bg=BG)
        content.pack(fill="both", expand=True, padx=26, pady=(0, 16))
        content.columnconfigure(0, weight=3)
        content.columnconfigure(1, weight=2)
        content.rowconfigure(0, weight=1)

        left = self._panel(content)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        right = self._panel(content)
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        tk.Label(left, text="Enter your password", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(20, 12))

        entry_row = tk.Frame(left, bg=PANEL)
        entry_row.pack(fill="x", padx=20)
        self.password_entry = tk.Entry(
            entry_row, textvariable=self.password_var, show="•",
            bg=FIELD, fg=TEXT, insertbackground=TEXT,
            relief="flat", font=("Segoe UI", 13),
            highlightthickness=1, highlightbackground=BORDER,
            highlightcolor=BLUE
        )
        self.password_entry.pack(side="left", fill="x", expand=True, ipady=12, padx=(0, 8))
        self.toggle_button = tk.Button(
            entry_row, text="Show", command=self._toggle_password,
            bg=FIELD, fg=MUTED, activebackground=FIELD,
            activeforeground=TEXT, relief="flat", bd=0,
            font=("Segoe UI", 9, "bold"), cursor="hand2"
        )
        self.toggle_button.pack(side="right")

        tk.Button(
            left, text="Check Strength", command=self._update_strength,
            bg=BLUE, fg="white", activebackground="#2368c4",
            activeforeground="white", relief="flat", bd=0,
            font=("Segoe UI", 11, "bold"), cursor="hand2"
        ).pack(fill="x", padx=20, pady=(16, 18), ipady=9)

        tk.Frame(left, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(0, 16))

        self.result_title = tk.Label(left, text="Start typing to check strength",
                                     bg=PANEL, fg=TEXT, font=("Segoe UI", 17, "bold"))
        self.result_title.pack(anchor="w", padx=20)
        self.result_description = tk.Label(
            left, text="Your password is checked only on this device.",
            bg=PANEL, fg=MUTED, font=("Segoe UI", 9), wraplength=400, justify="left"
        )
        self.result_description.pack(anchor="w", padx=20, pady=(5, 15))

        meter = tk.Frame(left, bg=PANEL)
        meter.pack(fill="x", padx=20)
        for _ in range(5):
            segment = tk.Frame(meter, bg="#293b55", height=10)
            segment.pack(side="left", fill="x", expand=True, padx=(0, 5))
            self.meter_segments.append(segment)

        self.score_label = tk.Label(left, text="Strength score: 0/5",
                                    bg=PANEL, fg=MUTED, font=("Segoe UI", 10, "bold"))
        self.score_label.pack(anchor="w", padx=20, pady=(10, 18))

        tk.Label(right, text="Password Requirements", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(20, 14))

        for title, _ in REQUIREMENTS:
            label = tk.Label(right, text="○  " + title, bg=PANEL, fg=MUTED,
                             font=("Segoe UI", 10), anchor="w", wraplength=280, justify="left")
            label.pack(fill="x", padx=20, pady=7)
            self.requirement_labels.append(label)

        tk.Frame(right, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(15, 14))
        tk.Label(right, text="Helpful tips", bg=PANEL, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=20, pady=(0, 8))

        tips = [
            "Use a mix of letters, numbers and symbols.",
            "Avoid names, birthdays and common words.",
            "Longer, unique passwords are generally safer.",
            "Never reuse an important password across sites.",
        ]
        for tip in tips:
            tk.Label(right, text="•  " + tip, bg=PANEL, fg=MUTED,
                     font=("Segoe UI", 9), anchor="w", wraplength=280,
                     justify="left").pack(fill="x", padx=20, pady=4)

        footer = tk.Label(self.root, text="Stronger passwords  •  Safer accounts",
                          bg=BG, fg="#7897c4", font=("Segoe UI", 9))
        footer.pack(pady=(0, 14))

    def _panel(self, parent):
        return tk.Frame(parent, bg=PANEL, highlightthickness=1,
                        highlightbackground=BORDER, bd=0)

    def _toggle_password(self):
        if self.show_password.get():
            self.password_entry.configure(show="•")
            self.toggle_button.configure(text="Show")
            self.show_password.set(False)
        else:
            self.password_entry.configure(show="")
            self.toggle_button.configure(text="Hide")
            self.show_password.set(True)

    def _update_strength(self, *_):
        password = self.password_var.get()
        results = [check(password) for _, check in REQUIREMENTS]
        score = sum(results)

        for index, (title, _) in enumerate(REQUIREMENTS):
            if results[index]:
                self.requirement_labels[index].configure(
                    text="✓  " + title, fg=GREEN
                )
            else:
                self.requirement_labels[index].configure(
                    text="○  " + title, fg=MUTED
                )

        if not password:
            strength, color = "Not checked", MUTED
            description = "Type a password to see your strength assessment."
        elif score <= 2:
            strength, color = "Weak", RED
            description = "This password misses several basic requirements."
        elif score <= 4:
            strength, color = "Medium", YELLOW
            description = "Good start. Meet the remaining requirements to improve it."
        else:
            strength, color = "Strong", GREEN
            description = "All five basic checks passed. Use a unique password."

        self.result_title.configure(text=strength, fg=color)
        self.result_description.configure(text=description)
        self.score_label.configure(text=f"Strength score: {score}/5", fg=color)

        for index, segment in enumerate(self.meter_segments):
            segment.configure(bg=color if index < score and password else "#293b55")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app_root = tk.Tk()
    app = PasswordCheckerApp(app_root)
    app.run()
