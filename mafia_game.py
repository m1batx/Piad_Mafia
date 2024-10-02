import tkinter
from tkinter import messagebox
import random

# Function to register a new user
def register():
    # Read existing usernames and login attempts from the file
    with open("filelist.txt", "r") as file:
        user_data = [line.strip() for line in file.readlines()]
    
    new_username = username_register_entry.get()
    
    # Check if the username already exists
    if any(new_username == user.split()[0] for user in user_data):
        messagebox.showerror(title="Error", message="Username already exists. Choose a different username.")
    else:
        # Append the new username with login attempts count to the file
        with open("filelist.txt", "a") as file:
            file.write(f"{new_username} 0\n")  # Initialize login attempts count to 0
        messagebox.showinfo(title="Registration", message="Registration Successful! You can now login.")

# Function to login with an existing user
def login():
    username = username_login_entry.get()
    
    # Read existing usernames and login attempts from the file
    with open("filelist.txt", "r") as file:
        user_data = [line.strip() for line in file.readlines()]
    
    # Find the user in the list
    for i, user in enumerate(user_data):
        if username == user.split()[0]:
            login_attempts = int(user.split()[1])
            
            # Check login attempts limit
            if login_attempts < 2:
                # Increment login attempts count
                user_data[i] = f"{username} {login_attempts + 1}\n"
                with open("filelist.txt", "w") as file:
                    file.writelines(user_data)
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                open_game_window()
            else:
                messagebox.showerror(title="Error", message="Login attempts limit reached. Contact support.")
                return
    
    # If the user is not found
    messagebox.showerror(title="Error", message="Invalid login.")

# Function to open the game window
def open_game_window():
    game_window = tkinter.Toplevel(window)
    game_window.title("Mafia Game")
    game_window.geometry('300x200')
    game_window.configure(bg='#333333')
    
    # Display a simple pop-up message as a substitute for notifications
    messagebox.showinfo(title='Game Notification', message='You have a limited log; you just have 3 logs after this you have to pay.')
    
    target_number = random.randint(1, 5)

    def check_guess():
        user_guess = int(guess_entry.get())
        if user_guess == target_number:
            messagebox.showinfo(title="Congratulations", message="You are the Mafia!")
            game_window.destroy()
        else:
            messagebox.showerror(title="Wrong Guess", message="Take care, you citizen!")

    game_label = tkinter.Label(game_window, text="Guess the number (1-5)", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    guess_entry = tkinter.Entry(game_window, font=("Arial", 16))
    guess_button = tkinter.Button(game_window, text="Check Guess", bg="#FF3399", fg="#FFFFFF", font=("Arial", 12), command=check_guess)

    game_label.pack(pady=20)
    guess_entry.pack(pady=10)
    guess_button.pack(pady=20)

# GUI setup
window = tkinter.Tk()
window.title("Login Form")
window.geometry('600x600')
window.configure(bg='#333333')

# Registration Frame
registration_frame = tkinter.Frame(window, bg='#333333')
registration_label = tkinter.Label(registration_frame, text="Registration", bg='#333333', fg="#FF3399", font=("Arial", 20))
username_register_label = tkinter.Label(registration_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_register_entry = tkinter.Entry(registration_frame, font=("Arial", 16))
register_button = tkinter.Button(registration_frame, text="Register", bg="#009900", fg="#FFFFFF", font=("Arial", 16), command=register)

registration_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_register_label.grid(row=1, column=0)
username_register_entry.grid(row=1, column=1, pady=20)
register_button.grid(row=2, column=0, columnspan=2, pady=10)

# Login Frame
login_frame = tkinter.Frame(window, bg='#333333')
login_label = tkinter.Label(login_frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 20))
username_login_label = tkinter.Label(login_frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_login_entry = tkinter.Entry(login_frame, font=("Arial", 16))
login_button = tkinter.Button(login_frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_login_label.grid(row=1, column=0)
username_login_entry.grid(row=1, column=1, pady=20)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

registration_frame.pack(pady=20)
login_frame.pack()

window.mainloop()