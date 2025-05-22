import tkinter as tk
from tkinter import messagebox

# Function to calculate total pixels
def calculate_total_pixels():
    try:
        width_ft = float(width_entry.get())
        height_ft = float(height_entry.get())
        pixel_pitch_mm = float(pixel_pitch_entry.get())
        
        # Convert pixel pitch from mm to feet
        pixel_pitch_ft = pixel_pitch_mm / 304.8
        
        # Calculate pixels per foot
        pixels_per_foot = 1 / pixel_pitch_ft
        
        # Calculate width and height in pixels
        width_px = int(width_ft * pixels_per_foot)
        height_px = int(height_ft * pixels_per_foot)
        
        # Calculate total pixels
        total_pixels = width_px * height_px
        
        result_label.config(text=f"Screen Resolution: {width_px} x {height_px} pixels\nTotal Pixels: {total_pixels}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("LED Pixel Calculator")
root.geometry("350x250")

# Input Fields
tk.Label(root, text="Screen Width (ft):").pack()
width_entry = tk.Entry(root)
width_entry.pack()

tk.Label(root, text="Screen Height (ft):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Pixel Pitch (mm):").pack()
pixel_pitch_entry = tk.Entry(root)
pixel_pitch_entry.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_total_pixels)
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Run Application
root.mainloop()
