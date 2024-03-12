import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resized Image Insertion")

        # Create a canvas
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        # Load the original image
        self.original_image_path = R"C:\Users\anton\Desktop\compooter backups\skola\Programovanie\Python\Tkinter\hgh\bee.png"  # Replace with the actual path to your image file
        self.load_original_image()

        # Button to trigger resized image insertion
        insert_button = tk.Button(self.root, text="Insert Resized Image", command=self.insert_resized_image)
        insert_button.pack()

        move_right_button = tk.Button(self.root, text="Move bee to the right", command=self.move_bee_right)
        move_right_button.pack()

        move_left_button = tk.Button(self.root, text="Move bee to the left", command=self.move_bee_left)
        move_left_button.pack()

        move_up_button = tk.Button(self.root, text="Move bee up", command=self.move_bee_up)
        move_up_button.pack()

        move_down_button = tk.Button(self.root, text="Move bee down", command=self.move_bee_down)
        move_down_button.pack()

        rotate_bee_clockwise_button = tk.Button(self.root, text="Rotate bee clockwise", command=self.rotate_bee_clockwise)
        rotate_bee_clockwise_button.pack()

        # Start the Tkinter event loop
        self.root.mainloop()

    def load_original_image(self):
        self.finalized_image = Image.open(self.original_image_path)

    def insert_resized_image(self):
        # Resize the image to a specific width and height (e.g., 100x100 pixels)
        resized_image = self.finalized_image.resize((100, 100))

        # Convert the resized image to a PhotoImage
        self.resized_img = ImageTk.PhotoImage(resized_image)

        # Insert the resized image into the canvas
        self.finalized_image = self.canvas.create_image(10, 10, anchor=tk.NW, image=self.resized_img)
    
    def move_bee_right(self):
        self.canvas.move(self.finalized_image, 30, 0)
    
    def move_bee_left(self):
        self.canvas.move(self.finalized_image, -30, 0)
    
    def move_bee_up(self):
        self.canvas.move(self.finalized_image, 0, -30)
    
    def move_bee_down(self):
        self.canvas.move(self.finalized_image, 0, 30)
    
    def rotate_bee_clockwise(self):
        # Rotate the original image
        rotated_image = self.finalized_image.rotate(self.angle)

        # Convert the rotated image to a PhotoImage
        rotated_img = ImageTk.PhotoImage(rotated_image)

        # Delete the previous rotated image (if any)
        self.canvas.delete("rotated_image")

        # Insert the rotated image into the canvas
        self.canvas.create_image(200, 150, anchor=tk.CENTER, image=rotated_img, tags="rotated_image")

        # Increment the rotation angle
        self.angle += 1

        # Schedule the next rotation after a delay (in milliseconds)
        self.root.after(10, self.rotate_image)

if __name__ == "__main__":
    app = ImageApp()
