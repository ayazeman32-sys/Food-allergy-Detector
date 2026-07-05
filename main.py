import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox
)

# ----------------------------
# Food Database
# ----------------------------
foods = {
    "Burger": ["Bread", "Cheese", "Chicken", "Mayonnaise"],
    "Pizza": ["Flour", "Cheese", "Tomato"],
    "French Fries": ["Potato", "Salt", "Oil"],
    "Ice Cream": ["Milk", "Sugar"],
    "Peanut Cookies": ["Peanut", "Flour", "Sugar"]
}
allergens = {
    "Cheese": "Milk",
    "Milk": "Milk",
    "Butter": "Milk",
    "Egg": "Egg",
    "Mayonnaise": "Egg",
    "Bread": "Gluten",
    "Flour": "Gluten",
    "Peanut": "Peanut",
    "Shrimp": "Seafood"
}
# ----------------------------
# Function
# ----------------------------
def check_food():

    selected_food = foodBox.currentText()

    selected_allergies = []

    if milk.isChecked():
        selected_allergies.append("Milk")

    if egg.isChecked():
        selected_allergies.append("Egg")

    if peanut.isChecked():
        selected_allergies.append("Peanut")

    if gluten.isChecked():
        selected_allergies.append("Gluten")

    if seafood.isChecked():
        selected_allergies.append("Seafood")

    ingredients = foods[selected_food]

    found = []

    for ingredient in ingredients:
        if ingredient in allergens:
            allergy = allergens[ingredient]

            if allergy in selected_allergies:
                found.append(allergy)

    if found:
        result.setText("❌ NOT SAFE\nContains: " + ", ".join(found))
    else:
        result.setText("✅ SAFE TO EAT")

# ----------------------------
# Application
# ----------------------------
app = QApplication(sys.argv)

# Main Window
window = QWidget()
window.setWindowTitle("Food Allergy Detector")
window.resize(600, 500)

# ----------------------------
# Title
# ----------------------------
title = QLabel("Food Allergy Detector", window)
title.move(200, 20)

# ----------------------------
# Food Selection
# ----------------------------
foodLabel = QLabel("Select Food:", window)
foodLabel.move(50, 80)

foodBox = QComboBox(window)
foodBox.addItems([
    "Burger",
    "Pizza",
    "French Fries",
    "Ice Cream",
    "Peanut Cookies"
])
foodBox.move(150, 80)
foodBox.resize(200, 30)

# ----------------------------
# Allergy Selection
# ----------------------------
allergyLabel = QLabel("Select Your Allergies:", window)
allergyLabel.move(50, 140)

milk = QCheckBox("Milk", window)
milk.move(70, 180)

egg = QCheckBox("Egg", window)
egg.move(70, 210)

peanut = QCheckBox("Peanut", window)
peanut.move(70, 240)

gluten = QCheckBox("Gluten", window)
gluten.move(70, 270)

seafood = QCheckBox("Seafood", window)
seafood.move(70, 300)

# ----------------------------
# Button
# ----------------------------
button = QPushButton("Check Food", window)
button.move(220, 360)
button.resize(150, 40)

# Connect button to function
button.clicked.connect(check_food)

# ----------------------------
# Result
# ----------------------------
result = QLabel("Result will appear here.", window)
result.move(180, 430)

# ----------------------------
# Show Window
# ----------------------------
window.show()

# Run Application
sys.exit(app.exec())