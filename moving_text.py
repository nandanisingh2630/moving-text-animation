import tkinter as tk

class MovingText:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(root, bg="navy", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.text = self.canvas.create_text(0, 100, text="Welcome to Animation!", fill="white", font=("Arial", 48, "bold"))
        self.animate()

    def animate(self):
        self.canvas.move(self.text, 5, 0)
        x, y, _, _ = self.canvas.bbox(self.text)
        if x > self.canvas.winfo_width():
            self.canvas.coords(self.text, -300, 100)
        self.root.after(30, self.animate)

root = tk.Tk()
MovingText(root)
root.mainloop()
