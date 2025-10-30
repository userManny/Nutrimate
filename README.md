# 🥗 NutriMate v2 - Smart Nutrition Tracker with Motivation

**Author:** Maneesh  
**Tech Stack:** Python, Tkinter, Spoonacular API  

---

## 📘 Overview

**NutriMate v2** is a **smart nutrition and fitness tracker** built with Python’s Tkinter GUI.  
It helps users **calculate daily calorie needs**, **track meals**, and get **motivational feedback** based on their daily intake.

The app combines **offline food data** for quick lookups and **real-time online data** (via the Spoonacular API) for any custom foods entered by the user.

---

## 🌟 Key Features

✅ **Daily Calorie Target Calculation**  
Automatically calculates your recommended calorie intake based on:
- Age  
- Gender  
- Height & Weight  
- Activity level (Low / Medium / High)  
- Fitness Goal (Gain / Maintain / Lose)

✅ **Food Entry & Tracking**  
Add any food item and quantity (in grams).  
If not found in local data, it fetches nutrition details from the Spoonacular API.

✅ **Smart Motivation System**  
After tracking meals, get friendly and motivational feedback:
- 🔥 “Excellent! You’re right on track!”  
- 💪 “Try adding a small snack!”  
- ⚠ “You’ve gone a bit over your target!”

✅ **Offline + Online Hybrid System**  
- Built-in local dataset for common Indian foods like *roti, rice, milk, egg, apple*  
- API fallback for any custom item

✅ **Beautiful Tkinter GUI**  
A simple, clean, and interactive interface for everyday use.

---

## 🧠 Tech Details

**Language:** Python  
**GUI Library:** Tkinter  
**API Used:** [Spoonacular Nutrition API](https://spoonacular.com/food-api)  
**HTTP Requests:** `requests` library

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/userManny/Nutrimate.git
cd Nutrimate
### 2️⃣ Install Dependencies

Make sure you have **Python (3.8 or higher)** installed.  
Then install the required library:

```bash
pip install requests

