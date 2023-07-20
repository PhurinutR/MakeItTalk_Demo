import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import os
import argparse
import threading

# Create the main window
root = tk.Tk()
root.title('Make It Talk Palette')

# Create a frame to hold the image buttons on the left
image_button_frame = tk.Frame(root, highlightbackground="magenta", highlightthickness=2)
image_button_frame.grid(row=1, column=0, padx=10, pady=10)

# Create a list to hold references to the PhotoImage objects for the image buttons
image_button_photo_list = []

# Create a global variable to store the index of the last clicked image button
last_clicked_image_index = None

# Loop through the image paths and create an image button for each image
image_button_list = []
num_image_buttons_per_row = 4  # Number of image buttons to display in each row
image_paths = ['examples/asian_face.png',
               'examples/example_00012.png',
               'examples/example_00039.png',
               'examples/example_00048.png',
               'examples/example_00051.png',
               'examples/example_00064.png',
               'examples/example_00083.png',
               'examples/example_00116.png',
               'examples/example_00128.png',
               'examples/example_00154.png',
               'examples/example_00328.png',
               'examples/example_00357.png',
               'examples/example_00402.png',
               'examples/example_00432.png',
               'examples/example_00482.png',
               'examples/example_00507.png',
               'examples/example_01639.png',
               'examples/Taylor.png']

audio_paths = ['examples/sample_audios/action_1.wav',
               'examples/sample_audios/action_2.wav',
               'examples/sample_audios/attack_1.wav',
               'examples/sample_audios/attack_2.wav',
               'examples/sample_audios/cantonese.wav',
               'examples/sample_audios/male.wav',
               'examples/sample_audios/obama.wav']

for index, image_path in enumerate(image_paths):
    # Load the image using PIL
    image = Image.open(image_path)
    # Resize the image to fit the button
    image = image.resize((70, 70))
    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(image)
    # Add the PhotoImage object to the list
    image_button_photo_list.append(photo)

    # Create an image button with the image
    button = tk.Button(image_button_frame, image=photo, command=lambda index=index: image_button_click(index))

    # Set the button size and add it to the frame
    button.config(width=70, height=70, highlightbackground="white", highlightthickness=1)
    button.grid(row=index // num_image_buttons_per_row, column=index % num_image_buttons_per_row, padx=10, pady=10)
    image_button_list.append(button)
    # Store a reference to the PhotoImage object on the button widget
    button.image_without_rectangle = photo

# Create the frame for the image label
image_label_frame = tk.Frame(root, highlightbackground="magenta", highlightthickness=2)
image_label_frame.grid(row=0, column=0, pady=10)

choose_face_label = tk.Label(image_label_frame, text="Choose A Face")
choose_face_label.pack()

# Create a function to handle image button clicks
def image_button_click(index):
    global last_clicked_image_index
    if last_clicked_image_index is not None and last_clicked_image_index != index:
        # If a previous button has been clicked and it's not the same as the current button, reset its highlight
        image_button_list[last_clicked_image_index].config(highlightbackground="white", highlightthickness=1)
    # Set the highlight of the clicked button to indicate that it's selected
    image_button_list[index].config(highlightbackground="blue", highlightthickness=1)
    last_clicked_image_index = index

# Create the frame for the image label
audio_label_frame = tk.Frame(root, highlightbackground="lightblue", highlightthickness=2)
audio_label_frame.grid(row=0, column=1, pady=10)

choose_audio_label = tk.Label(audio_label_frame, text="Choose An Audio")
choose_audio_label.pack()

# Create a frame to wrap the text buttons
text_button_wrapper = tk.Frame(root, highlightbackground="lightblue", highlightthickness=2)
text_button_wrapper.grid(row=1, column=1, padx=10, pady=10)

# Create a frame to hold the text buttons on the right
text_button_frame = tk.Frame(text_button_wrapper)
text_button_frame.pack(side=tk.RIGHT)

# Create a list to hold the text buttons
text_button_list = []

# Create the text buttons
last_clicked_text_index = None
# Create a function to handle text button clicks
def text_button_click(index):
    global last_clicked_text_index
    if last_clicked_text_index is not None:
        # Deselect the previously selected text button
        text_button_list[last_clicked_text_index].config(relief=tk.RAISED, fg='black')
    # Select the clicked text button
    text_button_list[index].config(relief=tk.SUNKEN, fg='red')
    last_clicked_text_index = index


# Loop through the text labels and create a text button for each label
text_labels = ['Speech 1', 'Speech 2', 'Speech 3', 'Speech 4', 'Speech 5', 'Male', 'Obama']
for index, text_label in enumerate(text_labels):
    # Create a text button with the label
    button = tk.Button(text_button_frame, text=text_label, command=lambda index=index: text_button_click(index))
    button.config(fg='black')
    # Set the button size and add it to the frame
    button.config(width=10, height=3)
    button.grid(row=index, column=0, pady=5)
    text_button_list.append(button)


# Create a frame to hold the check buttons
check_button_frame = tk.Frame(root, highlightbackground="lightgreen", highlightthickness=2)
check_button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="n")

# Create the BooleanVar() objects for the checkbuttons
No_Content_Animate = tk.BooleanVar()
No_Speaker_Aware_Animate = tk.BooleanVar()

# Create the checkbuttons using the BooleanVar() objects
check_button_1 = tk.Checkbutton(check_button_frame, text="No Content Animate", variable=No_Content_Animate)
check_button_2 = tk.Checkbutton(check_button_frame, text="No Speaker Aware Animate", variable=No_Speaker_Aware_Animate)

# Add the check buttons to the frame
check_button_1.pack(side="left", padx=5)
check_button_2.pack(side="left", padx=5)


def go_button_click(last_clicked_image_index):
    if last_clicked_image_index is not None:
        # Get the status of the check buttons
        No_Content_Animate_status = No_Content_Animate.get()
        No_Speaker_Aware_Animate_status = No_Speaker_Aware_Animate.get()
        parser = argparse.ArgumentParser()
        parser.add_argument('--image', type=str, default=image_paths[last_clicked_image_index])
        parser.add_argument('--audio', type=str, default=audio_paths[last_clicked_text_index])
        parser.add_argument('--No_Content_Animate', default=No_Content_Animate_status, action='store_true')
        parser.add_argument('--No_Speaker_Aware_Animate', default=No_Speaker_Aware_Animate_status, action='store_true')

        # Create a new toplevel window for the progress bar
        progress_window = tk.Toplevel(root)
        progress_window.title("Generating video in progress...")
        progress_window.geometry("300x100")
        progress_window.transient(root)
        progress_window.grab_set()

        # Create a label widget for the text
        label = tk.Label(progress_window, text="Check out intermediate results\nthrough your TERMINAL")
        label.pack(pady=5)

        # Create the progress bar widget and pack it
        progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=250, mode="indeterminate")
        progress_bar.pack(pady=10)

        # Start the progress bar animation
        progress_bar.start()

        # Start a new thread to run the inference function
        def inference_thread():
            import inference as inf
            inf.inference(parser)
            # Stop the progress bar animation
            progress_bar.stop()
            # Destroy the progress bar window
            progress_window.destroy()
            # Show a message box to indicate that the video generation process has finished
            message_finish = "Inferencing Process Finish!!"
            messagebox.showinfo("Notice", message_finish)

        thread = threading.Thread(target=inference_thread)
        thread.start()

# Create a "Go" button
go_button = tk.Button(root, text='Make It Talk!!', command=lambda: go_button_click(last_clicked_image_index))
go_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()