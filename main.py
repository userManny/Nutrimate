# NutriMate v2 - Smart Nutrition Tracker with Motivation
# Author: Maneesh 

import tkinter as tk
from tkinter import messagebox
import requests  #  Added for API use

# -----------------------------
# API Configuration
# -----------------------------
API_KEY = "b5497ce09727400c8517360450b5732b"  #  API key 

def fetch_nutrition_online(food_name):
    """
    Fetch nutrition info from Spoonacular API
    """
    try:
        url = "https://api.spoonacular.com/recipes/guessNutrition"
        params = {"title": food_name, "apiKey": API_KEY}
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and "calories" in data:
            return {
                "calories": data["calories"]["value"],
                "protein": data["protein"]["value"],
                "fat": data["fat"]["value"],
                "carbs": data["carbs"]["value"]
            }
        else:
            return None
    except Exception as e:
        print("Error fetching from API:", e)
        return None

# -----------------------------
# Sample Food Data (Offline)
# -----------------------------
food_data = {
    "roti": {"calories": 120, "protein": 3, "fat": 3, "carbs": 20},
    "rice": {"calories": 200, "protein": 4, "fat": 1, "carbs": 44},
    "egg": {"calories": 70, "protein": 6, "fat": 5, "carbs": 1},
    "milk": {"calories": 100, "protein": 3, "fat": 4, "carbs": 12},
    "apple": {"calories": 80, "protein": 0, "fat": 0, "carbs": 22}
}

# -----------------------------
# Global Totals
# -----------------------------
total_calories = 0
total_protein = 0
total_fat = 0
total_carbs = 0
daily_target = 0

# -----------------------------
# Functions
# -----------------------------
def calculate_targets():
    global daily_target
    try:
        age = int(entry_age.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        gender = gender_var.get().lower()
        activity = activity_var.get()
        goal = goal_var.get()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    # Calculate calories (simplified BMR + activity)
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factors = {"Low": 1.2, "Medium": 1.55, "High": 1.9}
    tdee = bmr * activity_factors[activity]

    if goal == "Gain":
        tdee += 300
    elif goal == "Lose":
        tdee -= 300

    daily_target = tdee
    messagebox.showinfo("Daily Target", f"Your daily calorie target: {tdee:.0f} kcal")

def add_food():
    global total_calories, total_protein, total_fat, total_carbs

    food = food_var.get().lower().strip()
    qty = entry_qty.get().strip()

    if not food or not qty:
        messagebox.showerror("Input Error", "Please enter food name and quantity.")
        return

    try:
        qty = float(qty)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")
        return

    # Check in local data first
    if food in food_data:
        data = food_data[food]
    else:
        # Not found locally → fetch from API
        messagebox.showinfo("Online Search", f"'{food}' not in local data, fetching online...")
        data = fetch_nutrition_online(food)

        if not data:
            messagebox.showwarning("Not Found", f"Could not find data for '{food}'.")
            return

        # Optionally, add it to local cache
        food_data[food] = data

    # Update totals
    total_calories += (data["calories"] * qty) / 100
    total_protein += (data["protein"] * qty) / 100
    total_fat += (data["fat"] * qty) / 100
    total_carbs += (data["carbs"] * qty) / 100

    messagebox.showinfo("Food Added", f"Added {qty}g of {food} successfully!")

    # Clear inputs
    food_var.set("")
    entry_qty.delete(0, tk.END)

def show_summary():
    if total_calories == 0:
        messagebox.showinfo("No Data", "Please add some foods first.")
        return

    if daily_target == 0:
        messagebox.showinfo("Missing Target", "Please calculate your daily target first.")
        return

    difference = daily_target - total_calories

    # Motivation logic
    if abs(difference) <= 100:
        message = "🔥 Excellent! You’re right on track. Keep it up!"
    elif difference > 100:
        message = "💪 You’re below your goal. Try adding a small meal or snack!"
    else:
        message = "⚠ You’ve gone a bit over your target. Stay mindful tomorrow!"

    summary = (
        f"🍽 Daily Nutrition Summary:\n\n"
        f"Calories Consumed: {total_calories:.1f} kcal\n"
        f"Target Calories: {daily_target:.1f} kcal\n"
        f"Difference: {difference:.1f} kcal\n\n"
        f"Protein: {total_protein:.1f} g\n"
        f"Fat: {total_fat:.1f} g\n"
        f"Carbs: {total_carbs:.1f} g\n\n"
        f"{message}"
    )

    messagebox.showinfo("Summary", summary)

# -----------------------------
# GUI Layout
# -----------------------------
root = tk.Tk()
root.title("NutriMate - Fitness Tracker")
root.geometry("400x600")

tk.Label(root, text="🥗 NutriMate - Smart Nutrition Tracker", font=("Arial", 16, "bold")).pack(pady=10)

# --- User Info Section ---
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(root, gender_var, "Male", "Female").pack()

tk.Label(root, text="Height (cm):").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Activity Level:").pack()
activity_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, activity_var, "Low", "Medium", "High").pack()

tk.Label(root, text="Goal:").pack()
goal_var = tk.StringVar(value="Maintain")
tk.OptionMenu(root, goal_var, "Gain", "Maintain", "Lose").pack()

tk.Button(root, text="Calculate Daily Target", command=calculate_targets, bg="lightgreen").pack(pady=10)

# --- Food Tracking Section ---
tk.Label(root, text="Enter Food Name:").pack()
food_var = tk.StringVar()
entry_food = tk.Entry(root, textvariable=food_var)
entry_food.pack()

tk.Label(root, text="Quantity (in grams):").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Button(root, text="Add Food", command=add_food, bg="lightblue").pack(pady=10)
tk.Button(root, text="Finish & Show Summary", command=show_summary, bg="orange").pack(pady=10)

root.mainloop()
