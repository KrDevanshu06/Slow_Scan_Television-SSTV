# src/gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import threading

def select_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        image_path.set(filepath)

def select_audio():
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if filepath:
        audio_path.set(filepath)

def encode_image():
    image_file = image_path.get()
    mode = mode_var.get()
    if not image_file:
        messagebox.showerror("Error", "Please select an image to encode.")
        return
    output_audio = "encoded_sstv.wav"
    command = ["python", "src/main.py", "encode", "--image", image_file, "--mode", mode, "--output", output_audio]
    progress.start()
    def run():
        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", f"Image encoded to SSTV audio: {output_audio}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Encoding failed. Check console for details.")
        progress.stop()
    threading.Thread(target=run, daemon=True).start()

def decode_audio():
    audio_file = audio_path.get()
    if not audio_file:
        messagebox.showerror("Error", "Please select an audio file to decode.")
        return
    output_image = "decoded_image.png"
    command = ["python", "src/main.py", "decode", "--audio", audio_file, "--output", output_image]
    progress.start()
    def run():
        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", f"SSTV audio decoded to image: {output_image}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Decoding failed. Check console for details.")
        progress.stop()
    threading.Thread(target=run, daemon=True).start()

def play_audio():
    audio_file = "encoded_sstv.wav"
    if not os.path.exists(audio_file):
        messagebox.showerror("Error", "No encoded audio file found. Please encode an image first.")
        return
    # Windows example; for macOS or Linux, adjust the command accordingly
    subprocess.run(["start", audio_file], shell=True)

def create_gui():
    root = tk.Tk()
    root.title("SSTV Encoder/Decoder")
    root.geometry("450x350")

    global image_path, audio_path, mode_var, progress
    image_path = tk.StringVar()
    audio_path = tk.StringVar()
    mode_var = tk.StringVar(value="martin_m1")

    ttk.Label(root, text="Image to SSTV Audio").pack(pady=5)
    ttk.Button(root, text="Select Image", command=select_image).pack()
    ttk.Entry(root, textvariable=image_path, state='readonly', width=50).pack()
    ttk.Label(root, text="SSTV Mode").pack()
    ttk.Combobox(root, textvariable=mode_var, values=["martin_m1", "scottie_s1"]).pack()
    ttk.Button(root, text="Encode Image", command=encode_image).pack()

    ttk.Label(root, text="SSTV Audio to Image").pack(pady=5)
    ttk.Button(root, text="Select Audio", command=select_audio).pack()
    ttk.Entry(root, textvariable=audio_path, state='readonly', width=50).pack()
    ttk.Button(root, text="Decode Audio", command=decode_audio).pack()

    ttk.Button(root, text="Play SSTV Audio", command=play_audio).pack(pady=5)

    progress = ttk.Progressbar(root, mode='indeterminate')
    progress.pack(fill=tk.X, padx=10, pady=5)

    ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    create_gui()
