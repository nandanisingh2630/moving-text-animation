# 🖥️ Python Tkinter Moving Text Animation

A simple **GUI animation project built with Python Tkinter** that displays moving text across a fullscreen window. The text continuously moves from left to right and automatically reappears from the left when it reaches the edge of the screen.

## ✨ Features

* 🖥️ Fullscreen GUI window
* 🎨 Navy background with white text
* ➡️ Smooth left-to-right text animation
* 🔄 Automatically repeats the animation
* ⚡ Uses Tkinter's built-in `after()` method
* 🐍 Beginner-friendly Python project
* 📦 No external libraries required

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter**
* Canvas Widget
* `after()` method

## 📂 Project Structure

```text
python-tkinter-moving-text/
│
├── moving_text.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-tkinter-moving-text.git
```

### 2. Navigate to the project folder

```bash
cd python-tkinter-moving-text
```

### 3. Run the program

```bash
python moving_text.py
```

A fullscreen window will open with the animated text:

```text
Welcome to Animation!
```

## 🎬 How It Works

The project uses the **Tkinter Canvas** to create and animate the text.

### 1. Create the GUI

A Tkinter window is created and configured to run in fullscreen mode.

### 2. Create a Canvas

A Canvas widget is used as the drawing area:

```python
self.canvas = tk.Canvas(root, bg="navy", highlightthickness=0)
```

### 3. Add Text

The text is placed on the Canvas using `create_text()`:

```python
self.text = self.canvas.create_text(
    0, 100,
    text="Welcome to Animation!",
    fill="white",
    font=("Arial", 48, "bold")
)
```

### 4. Move the Text

The `canvas.move()` method changes the text's position:

```python
self.canvas.move(self.text, 5, 0)
```

This moves the text **5 pixels to the right** each time the animation runs.

### 5. Repeat the Animation

Tkinter's `after()` method calls the animation function every 30 milliseconds:

```python
self.root.after(30, self.animate)
```

When the text moves beyond the right edge of the window, its position is reset so the animation starts again.

## 🧠 Concepts Practiced

This project demonstrates:

* Python classes and objects
* Object-oriented programming
* Tkinter GUI development
* Canvas widgets
* Event scheduling
* Animation using `after()`
* Coordinate positioning
* Conditional statements
* Functions and methods
* Fullscreen window configuration

## 🎯 Learning Objective

The main goal of this project is to understand how **GUI elements can be animated using Python and Tkinter**.

It is a beginner-friendly project for learning the basics of graphical user interfaces, object-oriented programming, and timed animations.

## 🔮 Future Improvements

Possible improvements include:

* Add multiple animated texts
* Add different fonts and text sizes
* Add colorful text
* Add text bouncing from screen edges
* Add speed controls
* Add Start/Pause buttons
* Allow users to enter custom text
* Add different animation effects
* Add background animations

## 👩‍💻 Author

**Nandani Singh**

BCA – Artificial Intelligence

Interested in **Python, Data Analytics, AI/ML, and Software Development**.

⭐ If you like this project, consider giving the repository a star!
