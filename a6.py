
import customtkinter as ctk
import google.generativeai as genai

# Configure the API key for the Gemini API
genai.configure(api_key="AIzaSyDjshNndspp2phvzQf2fCN494R1tqUlsFU")

# Function to get response from the Gemini API
def query_gemini_api(user_input):
    model = genai.GenerativeModel('gemini-pro')  # Create a generative model instance
    chat = model.start_chat(history=[])  # Start a chat session with no prior history
    response = chat.send_message(user_input)  # Send user input and get the response
    return response.text  # Return the bot's response

# Function to handle user input
def send_message(event=None):  # Allow event to handle Enter key press
    user_input = user_input_field.get()  # Get the user's input from the entry field
    if user_input:  # Proceed only if the input is not empty
        chat_display.configure(state="normal")  # Enable the chat display for editing
        chat_display.insert(ctk.END, f"You: {user_input}\n\n", "user")  # Insert user message with user tag
        response_text = query_gemini_api(user_input)  # Get response from the bot
        chat_display.insert(ctk.END, f"Bot: {response_text}\n\n", "bot")  # Insert bot response with bot tag
        chat_display.configure(state="disabled")  # Disable editing the chat display
        user_input_field.delete(0, ctk.END)  # Clear the input field

# Function to start the chat
def start_chat():
    chat_display.configure(state="normal")  # Enable the chat display
    chat_display.delete(1.0, ctk.END)  # Clear previous chat history
    chat_display.insert(ctk.END, "Chat started. Ask me anything!\n\n", "bot")  # Initial message from bot
    chat_display.configure(state="disabled")  # Disable editing

# Function to exit the application
def exit_app():
    root.quit()  # Close the application

# Setting up the main CustomTkinter window
ctk.set_appearance_mode("light")  # Set appearance mode to light
ctk.set_default_color_theme("blue")  # Set default color theme

root = ctk.CTk()  # Create the main application window
root.title("Simple Chatbot")  # Set the window title
root.geometry("400x400")  # Set the window size

# Frame for buttons at the top
button_frame = ctk.CTkFrame(root)  # Create a frame for the buttons
button_frame.pack(fill="x")  # Pack the frame to fill the x-axis

# Exit button on the left
exit_button = ctk.CTkButton(button_frame, text="Exit", command=exit_app, width=80)  # Create an exit button
exit_button.pack(side="left", padx=(10, 5), pady=10)  # Pack it to the left side of the frame

# Start button on the right
start_button = ctk.CTkButton(button_frame, text="Start", command=start_chat, width=80)  # Create a start button
start_button.pack(side="right", padx=(5, 10), pady=10)  # Pack it to the right side of the frame

# Chat display area
chat_display = ctk.CTkTextbox(root, wrap="word", state="disabled", border_width=0)  # No border for a cleaner look
chat_display.pack(padx=10, pady=(0, 10), fill="both", expand=True)  # Pack the chat display

# User input field
user_input_field = ctk.CTkEntry(root)  # Create an entry field for user input
user_input_field.pack(padx=10, pady=(0, 3), fill="x", side="left", expand=True)  # Pack the input field

# Send button positioned closer to the input field
send_button = ctk.CTkButton(root, text="Send", command=send_message)  # Create a send button
send_button.pack(pady=(3, 10), side="left")  # Pack the send button

# Bind the Enter key to send the message
user_input_field.bind('<Return>', send_message)  # Call send_message when Enter is pressed

# Define tag configurations for user and bot messages
chat_display.tag_config("user", background="#e0f7fa", foreground="black")  # Light cyan for user messages
chat_display.tag_config("bot", background="#ffe0b2", foreground="black")    # Light orange for bot messages

# Start the main loop to run the application
root.mainloop()