## ==========================================================
##  Student Progression Outcome Predictor (Enhanced UI)
##  ----------------------------------------------------------
##  Student ID: 20230351
##  Date: 29/11/2023
##  ----------------------------------------------------------
##  I declare that my work contains no examples of misconduct,
##  such as plagiarism or collusion.
##  Any code taken from other sources is referenced.
## ==========================================================

from graphics import *

# ---------------------- GLOBALS ----------------------
progress_count = 0
trailing_count = 0
retriever_count = 0
excluded_count = 0
credits_data = []

# ---------------------- FILE HANDLING ----------------------
open('progression_data.txt', 'w').close()

def save_to_file(data):
    """Save progression data to file."""
    with open('progression_data.txt', 'a') as f:
        f.write(data + '\n')

# ---------------------- LOGIC ----------------------
def calculate_outcome(passed, defer, fail):
    """Determine progression outcome and update counts."""
    global progress_count, trailing_count, retriever_count, excluded_count
    if passed == 120:
        progress_count += 1
        return "Progress"
    elif passed == 100:
        trailing_count += 1
        return "Progress (module trailer)"
    elif fail >= 80:
        excluded_count += 1
        return "Exclude"
    else:
        retriever_count += 1
        return "Module retriever"

def get_valid_credits():
    """Collect and validate credit inputs."""
    while True:
        try:
            passed = int(input("Enter your total PASS credits: "))
            if passed not in range(0, 121, 20):
                print("Out of range"); continue
            defer = int(input("Enter your total DEFER credits: "))
            if defer not in range(0, 121, 20):
                print("Out of range"); continue
            fail = int(input("Enter your total FAIL credits: "))
            if fail not in range(0, 121, 20):
                print("Out of range"); continue
            if passed + defer + fail != 120:
                print("Total incorrect"); continue
            return passed, defer, fail
        except ValueError:
            print("Integer required.")
        except (KeyboardInterrupt, EOFError):
            print("Error: Invalid interruption.")

# ---------------------- START SCREEN ----------------------
def start_screen():
    """Show a stylish welcome window with gradient and buttons."""
    win = GraphWin("Welcome", 600, 400)
    win.setBackground(color_rgb(230, 240, 255))

    # Gradient background (light blue to white)
    for i in range(400):
        shade = color_rgb(230 - int(i * 0.1), 240 - int(i * 0.05), 255)
        rect = Rectangle(Point(0, i), Point(600, i + 1))
        rect.setFill(shade)
        rect.setOutline(shade)
        rect.draw(win)

    # Title
    title = Text(Point(300, 90), "🎓 Student Progression Predictor 🎓")
    title.setSize(20)
    title.setStyle("bold")
    title.setFill(color_rgb(40, 60, 100))
    title.draw(win)

    subtitle = Text(Point(300, 130), "Select your mode to continue")
    subtitle.setSize(12)
    subtitle.setFill(color_rgb(80, 80, 80))
    subtitle.draw(win)

    # Buttons
    student_btn = Rectangle(Point(150, 200), Point(260, 270))
    student_btn.setFill(color_rgb(100, 200, 150))
    student_btn.setOutline(color_rgb(50, 150, 100))
    student_btn.draw(win)

    student_label = Text(Point(205, 235), "Student (S)")
    student_label.setSize(12)
    student_label.draw(win)

    staff_btn = Rectangle(Point(340, 200), Point(450, 270))
    staff_btn.setFill(color_rgb(90, 160, 255))
    staff_btn.setOutline(color_rgb(60, 110, 200))
    staff_btn.draw(win)

    staff_label = Text(Point(395, 235), "Staff (T)")
    staff_label.setSize(12)
    staff_label.draw(win)

    footer = Text(Point(300, 340), "Click a button to start")
    footer.setFill("gray")
    footer.draw(win)

    # Wait for click
    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()
        if 150 <= x <= 260 and 200 <= y <= 270:
            win.close()
            return 's'
        elif 340 <= x <= 450 and 200 <= y <= 270:
            win.close()
            return 't'
