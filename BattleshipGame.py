import tkinter as tk
from tkinter import messagebox
import random

# Global variables
# Գլոբալ փոփոխականներ
root = None
buttons = []
board_size = 6            # 6x6/Դաշտի չափ
destroyed_ships = 0       # Count of destoryed ships/Ոչնչացված նավերի քանակը
max_steps = 20            # Count of max steps/Առավելագույն քայլերի քանակը
current_steps = 0         # Count of current steps/Ընթացիկ քայլերի քանակը
ship_positions = set()    # Positions of ships/Նավերի տեղորոշումը

def create_board():
    global buttons
    buttons = [[tk.Button(root, width=4, height=2, bg='blue', command=lambda x=i, y=j: button_click(x, y))
                for j in range(board_size)] for i in range(board_size)]
    
    for i in range(board_size):
        for j in range(board_size):
            buttons[i][j].grid(row=i, column=j)

def button_click(x, y):
    global destroyed_ships, current_steps

    # Increment the step counter
    # Ցույց է տալիս քայլերի քանակը
    current_steps += 1

    # Check if max steps have been reached
    # Ստուգում ենք արդյոք առավելագույն քայլերի քանակին է հասել
    if current_steps > max_steps:
        messagebox.showinfo("Unique Battleship", "You've reached the 20-step limit! Game over.")
        root.destroy()
        return
    
    if (x, y) in ship_positions:
        current_steps -= 1 
        buttons[x][y].config(bg='red', state=tk.DISABLED)
        destroyed_ships += 1
        if destroyed_ships == 1:
            messagebox.showinfo("Unique Battleship", f"You kicked the first ship.\nSteps left: {max_steps - current_steps}")
        elif destroyed_ships == 2:
            messagebox.showinfo("Unique Battleship", f"You kicked the second ship.\nSteps left: {max_steps - current_steps}")
        elif destroyed_ships == 3:
            messagebox.showinfo("Unique Battleship", "Congratulations! You kicked all ships.")
            root.destroy()
    else:
        buttons[x][y].config(bg='white', state=tk.DISABLED)
        messagebox.showinfo("Unique Battleship", f"Oops! Try again.\nSteps left: {max_steps - current_steps}")

    # End game if no more steps left
    # Խաղն ավարտվում է, երբ քայլեր չեն մնացել
    if current_steps == max_steps and destroyed_ships < 3:
        messagebox.showinfo("Unique Battleship", "Game over! You've used all 20 steps.")
        root.destroy()

def main():
    global root, ship_positions, current_steps, destroyed_ships

    # Initialize the main window
    # Ստեղծում ենք դաշտը
    root = tk.Tk()
    root.title("Unique Battleship Game")

    # Reset steps and destroyed ships
    # Քայլերի և խոցված նավերի սկզբնարժեքավորում 
    current_steps = 0
    destroyed_ships = 0

    # Create 3 unique random ship positions
    # Տարբեր տեղորոշմամբ 3 նավերի ստեղծում
    while len(ship_positions) < 3:
        ship_positions.add((random.randint(0, board_size - 1), random.randint(0, board_size - 1)))

    # Create the board of buttons
    # Վանդակներով դաշտի ստեղծում
    create_board()

    # Start the main event loop
    # Սկսում ենք ծրագրի ցիկլը
    root.mainloop()

if __name__ == "__main__":
    main()
