import tkinter as tk
from tkinter import messagebox
from random import choice

# Global variables to manage current user and their scores
current_user = 'user1'
user_scores = {'user1': 0, 'user2': 0}

# Function to initialize the user data
def initialize_data():
    global user_scores
    user_scores = {'user1': 0, 'user2': 0}

# Function to get the score for a user
def get_score(user):
    return user_scores.get(user, 0)

# Function to update the score for a user
def update_score(user, score):
    global user_scores
    if user in user_scores:
        user_scores[user] += score
    else:
        user_scores[user] = score

# Function to reset the scores
def reset_scores():
    global user_scores
    user_scores = {'user1': 0, 'user2': 0}
    update_score_label()
    messagebox.showinfo("Reset Scores", "Scores have been reset to zero.")

# Function to get the color for a symbol
def get_color(symbol):
    colors = {
        '🍇': 'purple',
        '🍉': 'green',
        '🍒': 'pink',
        '🍋': 'yellow',
        '🔔': 'gold'
    }
    return colors.get(symbol, 'white')

# Function to handle the spin action
def spin():
    try:
        symbols = ['🍇', '🍉', '🍒', '🍋', '🔔']
        result = [choice(symbols) for _ in range(3)]

        slot1.config(text=result[0], bg=get_color(result[0]))
        slot2.config(text=result[1], bg=get_color(result[1]))
        slot3.config(text=result[2], bg=get_color(result[2]))

        if result[0] == result[1] == result[2]:
            if result[0] == '🍇':
                win_amount = 500
            elif result[0] == '🍉':
                win_amount = 300
            else:
                win_amount = 100
            messagebox.showinfo("Win", f"Congratulations! You won {win_amount} points!")
            update_score(current_user, win_amount)
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            win_amount = 50
            messagebox.showinfo("Win", f"Congratulations! You won {win_amount} points!")
            update_score(current_user, win_amount)
        else:
            lose_amount = -10
            messagebox.showinfo("Loss", f"Sorry, you lost {abs(lose_amount)} points.")
            update_score(current_user, lose_amount)

        update_score_label()
    except Exception as e:
        print(f"An error occurred during spin: {e}")

# Function to handle user switching
def switch_user():
    global current_user
    try:
        current_user = 'user2' if current_user == 'user1' else 'user1'
        messagebox.showinfo("Switch User", f"Switched to {current_user}.")
        update_score_label()
    except Exception as e:
        print(f"An error occurred while switching user: {e}")

# Function to update the score label
def update_score_label():
    try:
        score_label.config(text=f'Score: {get_score(current_user)}')
    except Exception as e:
        print(f"An error occurred while updating score label: {e}")

# Initialize user data on application start
initialize_data()

# Set up the main application window
root = tk.Tk()
root.title("Slot Machine")

# Create and place widgets
label1 = tk.Label(root, text='Slot Machine', font=('Helvetica', 24))
label1.pack()

slot_frame = tk.Frame(root)
slot_frame.pack()

slot1 = tk.Label(slot_frame, text='0', font=('Helvetica', 48), width=3)
slot1.pack(side=tk.LEFT, padx=10)
slot2 = tk.Label(slot_frame, text='0', font=('Helvetica', 48), width=3)
slot2.pack(side=tk.LEFT, padx=10)
slot3 = tk.Label(slot_frame, text='0', font=('Helvetica', 48), width=3)
slot3.pack(side=tk.LEFT, padx=10)

spin_button = tk.Button(root, text='Spin', command=spin)
spin_button.pack(pady=20)

switch_user_button = tk.Button(root, text='Switch User', command=switch_user)
switch_user_button.pack(pady=20)

reset_button = tk.Button(root, text='Reset Scores', command=reset_scores)
reset_button.pack(pady=20)

score_label = tk.Label(root, text=f'Score: {get_score(current_user)}', font=('Helvetica', 14))
score_label.pack(pady=20)

# Start the main event loop
root.mainloop()
