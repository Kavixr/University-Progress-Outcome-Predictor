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