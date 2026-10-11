import string
import secrets
import tkinter as tk


# -------------------- COLORS --------------------

BG = "#0F172A"
PANEL = "#1E293B"
FIELD = "#0B1220"
BLUE = "#3B82F6"
TEXT = "#F8FAFC"
MUTED = "#94A3B8"
GREEN = "#22C55E"
YELLOW = "#FACC15"
RED = "#EF4444"
BORDER = "#334155"


# -------------------- COMMON PASSWORDS --------------------

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123",
    "password1",
    "1234567890",
}


# -------------------- PASSWORD REQUIREMENTS --------------------

REQUIREMENTS = [
    ("At least 12 characters", lambda p: len(p) >= 12),
    ("Contains uppercase letter", lambda p: any(c.isupper() for c in p)),
    ("Contains lowercase letter", lambda p: any(c.islower() for c in p)),
    ("Contains a number", lambda p: any(c.isdigit() for c in p)),
    (
        "Contains a special character",
        lambda p: any(c in string.punctuation for c in p),
    ),
]


class PasswordCheckerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("560x760")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.password_var = tk.StringVar()
        self.show_password = False

        self._build_ui()

        self.password_var.trace_add(
            "write", self._update_strength
        )

    # -------------------- INTERFACE --------------------

    def _build_ui(self):

        tk.Label(
            self.root,
            text="PASSWORD STRENGTH CHECKER",
            font=("Segoe UI", 19, "bold"),
            bg=BG,
            fg=TEXT,
        ).pack(pady=(22, 5))

        tk.Label(
            self.root,
            text="Check your password and improve its security",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED,
        ).pack(pady=(0, 20))

        panel = tk.Frame(
            self.root,
            bg=PANEL,
            padx=22,
            pady=20,
        )
        panel.pack(fill="x", padx=25)

        tk.Label(
            panel,
            text="Enter Password",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL,
            fg=TEXT,
        ).pack(anchor="w")

        password_row = tk.Frame(panel, bg=PANEL)
        password_row.pack(fill="x", pady=(8, 5))

        self.password_entry = tk.Entry(
            password_row,
            textvariable=self.password_var,
            show="*",
            font=("Segoe UI", 12),
            bg=FIELD,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=BLUE,
        )
        self.password_entry.pack(
            side="left", fill="x", expand=True, ipady=10
        )

        self.toggle_button = tk.Button(
            password_row,
            text="Show",
            command=self._toggle_password,
            bg=BLUE,
            fg="white",
            activebackground=BLUE,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=12,
        )
        self.toggle_button.pack(side="left", padx=(8, 0), ipady=7)

        # NEW FEATURE: PASSWORD GENERATOR

        tk.Button(
            panel,
            text="Generate Strong Password",
            command=self._generate_password,
            font=("Segoe UI", 10, "bold"),
            bg=BLUE,
            fg="white",
            activebackground="#2563EB",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=9,
        ).pack(fill="x", pady=(12, 5))

        tk.Button(
            panel,
            text="Copy Password",
            command=self._copy_password,
            font=("Segoe UI", 10),
            bg="#334155",
            fg=TEXT,
            activebackground="#475569",
            activeforeground=TEXT,
            relief="flat",
            cursor="hand2",
            pady=8,
        ).pack(fill="x")

        # STRENGTH DISPLAY

        strength_header = tk.Frame(self.root, bg=BG)
        strength_header.pack(fill="x", padx=28, pady=(20, 8))

        tk.Label(
            strength_header,
            text="Password Strength",
            font=("Segoe UI", 11, "bold"),
            bg=BG,
            fg=TEXT,
        ).pack(side="left")

        self.strength_label = tk.Label(
            strength_header,
            text="Not checked",
            font=("Segoe UI", 10, "bold"),
            bg=BG,
            fg=MUTED,
        )
        self.strength_label.pack(side="right")

        meter_frame = tk.Frame(self.root, bg=BG)
        meter_frame.pack(fill="x", padx=28)

        self.meter_segments = []

        for _ in range(5):
            segment = tk.Frame(
                meter_frame,
                bg=BORDER,
                height=8,
            )
            segment.pack(
                side="left",
                fill="x",
                expand=True,
                padx=2,
            )
            self.meter_segments.append(segment)

        self.score_label = tk.Label(
            self.root,
            text="Score: 0/5",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED,
        )
        self.score_label.pack(anchor="w", padx=30, pady=(8, 12))

        # REQUIREMENTS

        requirements_panel = tk.Frame(
            self.root,
            bg=PANEL,
            padx=20,
            pady=15,
        )
        requirements_panel.pack(fill="x", padx=25, pady=(0, 12))

        tk.Label(
            requirements_panel,
            text="Security Requirements",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL,
            fg=TEXT,
        ).pack(anchor="w", pady=(0, 8))

        self.requirement_labels = []

        for description, _ in REQUIREMENTS:
            label = tk.Label(
                requirements_panel,
                text="○  " + description,
                font=("Segoe UI", 10),
                bg=PANEL,
                fg=MUTED,
                anchor="w",
            )
            label.pack(fill="x", pady=2)
            self.requirement_labels.append(label)

        # NEW FEATURE: COMMON PASSWORD WARNING

        self.warning_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg=BG,
            fg=RED,
            wraplength=490,
            justify="left",
        )
        self.warning_label.pack(
            anchor="w", padx=30, pady=(0, 8)
        )

        # SECURITY TIPS

        tk.Label(
            self.root,
            text="Security Tip: Use a unique password for every account.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED,
            wraplength=500,
        ).pack(pady=(5, 10))

        tk.Label(
            self.root,
            text="Passwords are checked locally and are not saved by this app.",
            font=("Segoe UI", 8),
            bg=BG,
            fg=MUTED,
        ).pack(pady=(0, 12))

    # -------------------- SHOW / HIDE --------------------

    def _toggle_password(self):

        self.show_password = not self.show_password

        if self.show_password:
            self.password_entry.config(show="")
            self.toggle_button.config(text="Hide")
        else:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="Show")

    # -------------------- PASSWORD GENERATOR --------------------

    def _generate_password(self):

        # Ensure at least one character from each required category.
        password_characters = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation),
        ]

        # Fill the remaining length with a mix of character types.
        all_characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password_characters.extend(
            secrets.choice(all_characters)
            for _ in range(12)
        )

        # Securely shuffle the characters.
        secrets.SystemRandom().shuffle(password_characters)

        generated_password = "".join(password_characters)

        self.password_var.set(generated_password)

        # Select the generated password for convenient copying.
        self.password_entry.focus_set()
        self.password_entry.selection_range(0, tk.END)

    # -------------------- COPY PASSWORD --------------------

    def _copy_password(self):

        password = self.password_var.get()

        if not password:
            self.warning_label.config(
                text="Enter or generate a password before copying."
            )
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()

        self.warning_label.config(
            text="Password copied to clipboard.",
            fg=GREEN,
        )

    # -------------------- STRENGTH CHECKER --------------------

    def _update_strength(self, *_):

        password = self.password_var.get()

        if not password:
            self.strength_label.config(
                text="Not checked",
                fg=MUTED,
            )

            self.score_label.config(text="Score: 0/5")

            for segment in self.meter_segments:
                segment.config(bg=BORDER)

            for label, (description, _) in zip(
                self.requirement_labels, REQUIREMENTS
            ):
                label.config(
                    text="○  " + description,
                    fg=MUTED,
                )

            self.warning_label.config(text="")
            return

        score = 0

        for label, (description, check) in zip(
            self.requirement_labels, REQUIREMENTS
        ):

            passed = check(password)

            if passed:
                score += 1
                label.config(
                    text="✓  " + description,
                    fg=GREEN,
                )
            else:
                label.config(
                    text="○  " + description,
                    fg=MUTED,
                )

        # Determine the displayed strength.

        if score <= 2:
            strength = "Weak"
            strength_color = RED
        elif score <= 4:
            strength = "Medium"
            strength_color = YELLOW
        else:
            strength = "Strong"
            strength_color = GREEN

        # Check whether the password is in our common-password list.
        # Case-insensitive comparison is used.

        if password.casefold() in {
            item.casefold() for item in COMMON_PASSWORDS
        }:
            self.warning_label.config(
                text=(
                    "Warning: This is a commonly used password. "
                    "Choose a different password."
                ),
                fg=RED,
            )
        else:
            self.warning_label.config(
                text="",
                fg=RED,
            )

        self.strength_label.config(
            text=strength,
            fg=strength_color,
        )

        self.score_label.config(
            text=f"Score: {score}/5"
        )

        for index, segment in enumerate(self.meter_segments):
            if index < score:
                segment.config(bg=strength_color)
            else:
                segment.config(bg=BORDER)

    # -------------------- RUN APPLICATION --------------------

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":

    app_root = tk.Tk()

    app = PasswordCheckerApp(app_root)

    app.run()

