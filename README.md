# 🎓 Student Progression Outcome Predictor (Enhanced UI)

A visually enhanced Python program that predicts **student progression outcomes** based on their academic credits.  
It features a **graphical user interface (GUI)** using the `graphics.py` library, a **professional bar chart**, and **detailed outcome analysis cards** for better visualization of student performance statistics.

---

## 🧠 Overview

The **Student Progression Outcome Predictor** determines whether a student:
- ✅ Progresses to the next level  
- ⚠️ Progresses (module trailer)  
- 🔁 Is a module retriever  
- ❌ Is excluded from the course  

This decision is based on the number of **credits achieved**, **deferred**, and **failed**, according to the university’s progression rules.

It combines both **student** and **staff** modes:
- **Student Mode (S):** Allows individual prediction for one set of credits.  
- **Staff Mode (T):** Enables multiple entries, stores all outcomes, and generates beautiful visual charts and summaries.

---

## 🚀 Features

### 🧩 Credit Validation
- Accepts user input for **Pass**, **Defer**, and **Fail** credits.
- Ensures total credits = 120.
- Handles invalid entries with clear error messages.

### 🧾 File Storage
- Automatically writes progression results to `progression_data.txt` for record-keeping.
- Displays saved entries in a clean formatted list.

### 🖥️ GUI Start Screen
- Interactive window with animated gradient background.  
- Choose **Student (S)** or **Staff (T)** mode by clicking color-coded buttons.

### 📊 Dynamic Bar Chart Visualization
- Automatically generated **bar chart** showing each progression category.
- Bars are color-coded with a **shadowed 3D effect** and **smooth scaling**.
- Includes:
  - ✅ Total count & average summary box  
  - 📈 Percentage labels for each category  
  - 🪞 Elegant gradient header and shadow effects  
- Fully responsive scaling based on record count.

| Category | Color | Meaning |
|-----------|--------|---------|
| Progress | 🟩 Green | Student advances to next level |
| Trailer | 🟦 Blue | Student progresses with modules to retake |
| Retriever | 🟧 Orange | Student must retake several modules |
| Excluded | 🟥 Red | Student is excluded from the course |

### 📦 Detailed Statistical Dashboard
- Four **modern outcome cards** display:
  - Title (Progress, Trailer, Retriever, Excluded)  
  - Count and Percentage  
  - Descriptive explanation  
- Each card has:
  - Colored header strip  
  - Centered circular badge with animated count  
  - Professional layout and gradient effects  

### 💾 File Output Example
```
Progress - Pass: 120, Defer: 0, Fail: 0
Retriever - Pass: 60, Defer: 40, Fail: 20
Exclude - Pass: 20, Defer: 20, Fail: 80
```

---

## 🧮 Logic Summary

| Condition | Outcome |
|------------|----------|
| Pass = 120 | **Progress** |
| Pass = 100 | **Progress (module trailer)** |
| Fail ≥ 80 | **Exclude** |
| Otherwise | **Module retriever** |

Each outcome updates a respective counter used in the final statistical analysis and visualization.

---

## 📈 Example Visualization

### Bar Chart – Outcome Summary
A clean, gradient-based visualization:

```
📊 Student Progression Outcomes 📊

Progress    ██████████████   5 (41.7%)
Trailer     ██████           2 (16.7%)
Retriever   █████████        3 (25.0%)
Excluded    ██               2 (16.6%)
```

Each bar is scaled proportionally to its count and color-coded.

### Detailed Analysis Dashboard
Each category displayed in a **modern card layout**:
```
+-------------------+       +-------------------+
|   🟩 Progress     |       |   🟦 Trailer      |
|     Count: 5      |       |     Count: 2      |
|   41.7% Students  |       |   16.7% Students  |
+-------------------+       +-------------------+

+-------------------+       +-------------------+
|   🟧 Retriever    |       |   🟥 Excluded     |
|     Count: 3      |       |     Count: 2      |
|   25.0% Students  |       |   16.6% Students  |
+-------------------+       +-------------------+
```

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3 |
| GUI Library | `graphics.py` |
| File Handling | Built-in I/O |
| Visualization | Custom 2D drawing (bars, gradients, labels) |

---

## 📄 File Structure

```
📁 StudentProgressionPredictor/
│
├── progression_data.txt      # Auto-generated record file
├── predictor.py               # Main program file
├── graphics.py                # GUI library dependency
└── README.md                  # Project documentation
```

---

## 🧑‍💻 How to Run

1. Ensure **Python 3** is installed.  
2. Install `graphics.py` if not available:
   ```bash
   pip install graphics.py
   ```
3. Run the script:
   ```bash
   python predictor.py
   ```
4. Choose your mode:
   - **S** for Student Mode (single entry)
   - **T** for Staff Mode (multiple entries with visuals)

---

## 🌈 Highlights for Users

- **Simple yet powerful design** — beginner-friendly, but rich in visuals.  
- **Smooth graphics experience** — color gradients, shadows, rounded bars, and percentages.  
- **Engaging UI** — interactive start screen with emoji-based headers.  
- **Accurate academic logic** — replicates real university progression rules.  

---

## 🏆 Author

**Kavindu Rajapaksha**  
🎓 BSc (Hons) Computer Science  
📍 Informatics Institute of Technology (IIT)  
📧 [kavindurajapaksha848@gmail.com](mailto:kavindurajapaksha848@gmail.com)

---

## 💡 Future Enhancements

- Add **animated bar transitions**.  
- Include **export to CSV** and **PDF summary reports**.  
- Introduce **historical trend tracking** for multi-semester data.  
- Implement **pie chart visualization** for quick ratio comparison.
