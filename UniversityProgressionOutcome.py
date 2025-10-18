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


# ---------------------- PROFESSIONAL HISTOGRAM ----------------------
def display_histogram():
    """Display a professional and beautiful bar chart."""
    
    outcomes = ['Progress', 'Trailer', 'Retriever', 'Excluded']
    counts = [progress_count, trailing_count, retriever_count, excluded_count]
    colors = [color_rgb(16, 185, 129), color_rgb(59, 130, 246), 
              color_rgb(245, 158, 11), color_rgb(239, 68, 68)]
    total = sum(counts)
    max_count = max(counts) if max(counts) > 0 else 1
    
    # Create window
    win = GraphWin("Progression Outcomes", 900, 650)
    win.setBackground(color_rgb(240, 244, 248))
    
    # Gradient header
    for i in range(120):
        shade = color_rgb(230 - i//4, 235 - i//5, 255)
        rect = Rectangle(Point(0, i), Point(900, i + 1))
        rect.setFill(shade)
        rect.setOutline(shade)
        rect.draw(win)
    
    # Title
    title = Text(Point(450, 70), "📊 Student Progression Outcomes 📊")
    title.setSize(24)
    title.setStyle("bold")
    title.setFill(color_rgb(35, 60, 90))
    title.draw(win)
    
    # Bar chart setup
    base_y = 520
    start_x = 80
    bar_width = 110
    gap = 70
    scale = 300 / max_count if max_count > 0 else 1
    
    # Axis
    axis = Line(Point(100, base_y), Point(850, base_y))
    axis.setWidth(2)
    axis.setFill(color_rgb(120, 120, 120))
    axis.draw(win)
    
    # Y-axis labels
    for i in range(0, int(max_count) + 1, max(1, int(max_count) // 5)):
        y_pos = base_y - (i * scale)
        label = Text(Point(80, y_pos), str(i))
        label.setSize(10)
        label.setFill(color_rgb(100, 100, 100))
        label.draw(win)
        
        tick = Line(Point(95, y_pos), Point(100, y_pos))
        tick.setWidth(1)
        tick.draw(win)
    
    # Draw bars
    x = start_x
    for name, count, color in zip(outcomes, counts, colors):
        height = count * scale
        y_top = base_y - height
        
        # Shadow effect
        shadow = Rectangle(Point(x + 4, base_y + 4), Point(x + bar_width + 4, y_top + 4))
        shadow.setFill(color_rgb(200, 200, 200))
        shadow.setOutline(color_rgb(200, 200, 200))
        shadow.draw(win)
        
        # Bar
        bar = Rectangle(Point(x, base_y), Point(x + bar_width, y_top))
        bar.setFill(color)
        bar.setOutline(color_rgb(50, 50, 50))
        bar.setWidth(2)
        bar.draw(win)
        
        # Value label
        label_count = Text(Point(x + bar_width / 2, y_top - 25), str(count))
        label_count.setSize(16)
        label_count.setStyle("bold")
        label_count.setFill(color_rgb(40, 40, 40))
        label_count.draw(win)
        
        # Percentage label
        if total > 0:
            percentage = (count / total) * 100
            label_percent = Text(Point(x + bar_width / 2, y_top - 50), f"{percentage:.1f}%")
            label_percent.setSize(12)
            label_percent.setFill(color_rgb(80, 80, 80))
            label_percent.draw(win)
        
        # Category label
        label = Text(Point(x + bar_width / 2, base_y + 30), name)
        label.setSize(12)
        label.setStyle("bold")
        label.setFill(color_rgb(50, 50, 50))
        label.draw(win)
        
        x += bar_width + gap
    
    # Summary box
    summary_box = Rectangle(Point(50, 560), Point(200, 620))
    summary_box.setFill(color_rgb(224, 231, 255))
    summary_box.setOutline(color_rgb(59, 130, 246))
    summary_box.setWidth(2)
    summary_box.draw(win)
    
    total_text = Text(Point(125, 580), f"Total: {total}")
    total_text.setSize(11)
    total_text.setStyle("bold")
    total_text.setFill(color_rgb(31, 41, 55))
    total_text.draw(win)
    
    avg_text = Text(Point(125, 600), f"Avg: {total/4:.1f}")
    avg_text.setSize(11)
    avg_text.setStyle("bold")
    avg_text.setFill(color_rgb(31, 41, 55))
    avg_text.draw(win)
    
    # Instructions
    instruction = Text(Point(450, 620), "Click anywhere to close")
    instruction.setSize(10)
    instruction.setFill(color_rgb(100, 100, 100))
    instruction.draw(win)
    
    win.getMouse()
    win.close()

# ---------------------- DETAILED STATS DISPLAY ----------------------
def display_detailed_stats():
    """Display detailed statistics with four professional outcome cards."""
    
    outcomes = ['Progress', 'Trailer', 'Retriever', 'Excluded']
    counts = [progress_count, trailing_count, retriever_count, excluded_count]
    colors = [color_rgb(16, 185, 129), color_rgb(59, 130, 246), 
              color_rgb(245, 158, 11), color_rgb(239, 68, 68)]
    descriptions = [
        'Progressing to next level',
        'On module trailer',
        'In module retriever',
        'Excluded from course'
    ]
    total = sum(counts)
    
    win = GraphWin("Detailed Analysis", 1100, 800)
    win.setBackground(color_rgb(245, 247, 250))
    
    # Gradient header
    for i in range(100):
        shade = color_rgb(230 - i//4, 235 - i//5, 255)
        rect = Rectangle(Point(0, i), Point(1100, i + 1))
        rect.setFill(shade)
        rect.setOutline(shade)
        rect.draw(win)
    
    # Title
    title = Text(Point(550, 50), "📈 Detailed Student Progression Analysis 📈")
    title.setSize(24)
    title.setStyle("bold")
    title.setFill(color_rgb(35, 60, 90))
    title.draw(win)
    
    # Card positions and dimensions
    positions = [(220, 250), (820, 250), (220, 620), (820, 620)]
    card_width = 320
    card_height = 260
    
    for idx, (outcome, count, color, desc, (pos_x, pos_y)) in enumerate(
        zip(outcomes, counts, colors, descriptions, positions)):
        
        # Top colored bar
        top_bar = Rectangle(Point(pos_x - card_width//2, pos_y - card_height//2),
                           Point(pos_x + card_width//2, pos_y - card_height//2 + 8))
        top_bar.setFill(color)
        top_bar.setOutline(color)
        top_bar.draw(win)
        
        # Card background
        card = Rectangle(Point(pos_x - card_width//2, pos_y - card_height//2),
                        Point(pos_x + card_width//2, pos_y + card_height//2))
        card.setFill(color_rgb(255, 255, 255))
        card.setOutline(color_rgb(220, 220, 220))
        card.setWidth(1)
        card.draw(win)
        
        # Shadow effect
        shadow = Rectangle(Point(pos_x - card_width//2 + 2, pos_y + card_height//2),
                          Point(pos_x + card_width//2 + 2, pos_y + card_height//2 + 4))
        shadow.setFill(color_rgb(200, 200, 200))
        shadow.setOutline(color_rgb(200, 200, 200))
        shadow.draw(win)
        
        # Outcome name (inside top bar area)
        name_text = Text(Point(pos_x - card_width//2 + 30, pos_y - card_height//2 + 20), outcome)
        name_text.setSize(14)
        name_text.setStyle("bold")
        name_text.setFill(color_rgb(255, 255, 255))
        name_text.draw(win)
        
        # Count circle background
        circle_bg = Circle(Point(pos_x, pos_y - 30), 50)
        circle_bg.setFill(color)
        circle_bg.setOutline(color)
        circle_bg.draw(win)
        
        # Count value
        count_text = Text(Point(pos_x, pos_y - 30), str(count))
        count_text.setSize(36)
        count_text.setStyle("bold")
        count_text.setFill(color_rgb(255, 255, 255))
        count_text.draw(win)
        
        # Percentage
        if total > 0:
            percentage = (count / total) * 100
            percent_text = Text(Point(pos_x, pos_y + 30), f"{percentage:.1f}%")
            percent_text.setSize(16)
            percent_text.setStyle("bold")
            percent_text.setFill(color)
            percent_text.draw(win)
        
        # Description
        desc_text = Text(Point(pos_x, pos_y + 70), desc)
        desc_text.setSize(11)
        desc_text.setFill(color_rgb(100, 100, 100))
        desc_text.draw(win)
    
    # Instructions
    instruction = Text(Point(550, 780), "Click anywhere to close")
    instruction.setSize(10)
    instruction.setFill(color_rgb(120, 120, 120))
    instruction.draw(win)
    
    win.getMouse()
    win.close()

    # ---------------------- MAIN PROGRAM ----------------------
if __name__ == "__main__":
    mode = start_screen()

    while True:
        passed, defer, fail = get_valid_credits()
        outcome = calculate_outcome(passed, defer, fail)
        print(f"\n✓ {outcome}\n")

        if mode == 's':
            break

        data = f"{outcome} - Pass: {passed}, Defer: {defer}, Fail: {fail}"
        credits_data.append(data)
        save_to_file(data)

        cont = input("Enter 'y' to continue or 'q' to quit and view results: ").lower()
        if cont == 'q':
            break

    if mode == 't':
        print("\n" + "="*70)
        print("PROGRESSION STATISTICS".center(70))
        print("="*70 + "\n")
        
        display_histogram()
        display_detailed_stats()

        print("\nPart 2: Progression Data List")
        print("-" * 70)
        for i, record in enumerate(credits_data, 1):
            print(f"{i}. {record}")

        print("\n\nPart 3: File Data")
        print("-" * 70)
        with open('progression_data.txt', 'r') as f:
            content = f.read()
            print(content if content else "No data recorded.")

    print("\n" + "="*70)
    print("Program Ended. Thank you!".center(70))
    print("="*70)

