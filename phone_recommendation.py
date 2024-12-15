import tkinter as tk
from tkinter import Tk, Label, ttk
from tkinter import Entry
from tkinter import messagebox
from PIL import Image, ImageTk
from experta import Fact, KnowledgeEngine, Rule, MATCH

class Preference(Fact):
    """User preferences for phone recommendation."""
    pass
    
class PhoneRecommendation(KnowledgeEngine):
        
# Rules for Apple
    
    @Rule(Preference(brand='apple', storage = '64', ram = "3", camera = "budget"))
    def recommend_apple_64_3_b(self):
        print("Recommendation: Apple iPhone SE (2nd Gen)")
        self.result = "Recommendation: Apple iPhone SE (2nd Gen)"
    
    @Rule(Preference(brand='apple', storage = '64', ram = "3", camera = "premium"))
    def recommend_apple_64_3_p(self):
        print("Recommendation: Apple iPhone 8 Plus")
        self.result = "Recommendation: Apple iPhone 8 Plus"
    
    @Rule(Preference(brand='apple', storage = '64', ram = "4", camera = "budget"))
    def recommend_apple_64_4_b(self):
        print("Recommendation: Apple iPhone 11")
        self.result = "Recommendation: Apple iPhone 11"
            
    @Rule(Preference(brand='apple', storage = '64', ram = "4", camera = "premium"))
    def recommend_apple_64_4_p(self):
        print("Recommendation: Apple iPhone 12 Mini")
        self.result = "Recommendation: Apple iPhone 12 Mini"
    
    @Rule(Preference(brand='apple', storage = '128', ram = "3", camera = "budget"))
    def recommend_apple_128_3_b(self):
        print("Recommendation: Apple iPhone SE (2020)")
        self.result = "Recommendation: Apple iPhone SE (2020)"
        
    @Rule(Preference(brand='apple', storage = '128', ram = "3", camera = "premium"))
    def recommend_apple_128_3_p(self):
        print("Recommendation: Apple iPhone XR")
        self.result = "Recommendation: Apple iPhone XR"
    
    @Rule(Preference(brand='apple', storage = '128', ram = "4", camera = "budget"))
    def recommend_apple_128_4_b(self):
        print("Recommendation: Apple iPhone 11")
        self.result = "Recommendation: Apple iPhone 11"
        
    @Rule(Preference(brand='apple', storage = '128', ram = "4", camera = "premium"))
    def recommend_apple_128_4_p(self):
        print("Recommendation: Apple iPhone 12")
        self.result = "Recommendation: Apple iPhone 12"
        
    @Rule(Preference(brand='apple', storage = '128', ram = "6", camera = "budget"))
    def recommend_apple_128_6_b(self):
        print("Recommendation: Apple iPhone 13")
        self.result = "Recommendation: Apple iPhone 13"
        
    @Rule(Preference(brand='apple', storage = '128', ram = "6", camera = "premium"))
    def recommend_apple_128_6_p(self):
        print("Recommendation: Apple iPhone 12 Pro")
        self.result = "Recommendation: Apple iPhone 12 Pro"
    
    @Rule(Preference(brand='apple', storage = '256', ram = "4", camera = "budget"))
    def recommend_apple_256_4_b(self):
        print("Recommendation: Apple iPhone XS Max")
        self.result = "Recommendation: Apple iPhone XS Max"
    
    @Rule(Preference(brand='apple', storage = '256', ram = "4", camera = "premium"))
    def recommend_apple_256_4_p(self):
        print("Recommendation: Apple iPhone 11 Pro Max")
        self.result = "Recommendation: Apple iPhone 11 Pro Max"
    
    @Rule(Preference(brand='apple', storage = '256', ram = "6", camera = "budget"))
    def recommend_apple_256_6_b(self):
        print("Recommendation: Apple iPhone 13 Pro Max")
        self.result = "Recommendation: Apple iPhone 13 Pro Max"
    
    @Rule(Preference(brand='apple', storage = '256', ram = "6", camera = "premium"))
    def recommend_apple_256_6_p(self):
        print("Recommendation: Apple iPhone 13 Pro Max")
        self.result = "Recommendation: Apple iPhone 13 Pro Max"
        
# Rules for Google
        
    @Rule(Preference(brand='google', storage='128', ram = "6", camera = "budget"))
    def recommend_google_128_6_b(self):
        print("Recommendation: Google Pixel 4")
        self.result = "Recommendation: Google Pixel 4"

    @Rule(Preference(brand='google', storage='128', ram = "6", camera = "premium"))
    def recommend_google_128_6_p(self):
        print("Recommendation: Google Pixel 4a 5G")
        self.result = "Recommendation: Google Pixel 4a 5G"

    @Rule(Preference(brand='google', storage='128', ram = "8", camera = "budget"))
    def recommend_google_128_8_b(self):
        print("Recommendation: Google Pixel 5")
        self.result = "Recommendation: Google Pixel 5"

    @Rule(Preference(brand='google', storage='128', ram = "8", camera = "premium"))
    def recommend_google_128_8_p(self):
        print("Recommendation: Google Pixel 6")
        self.result = "Recommendation: Google Pixel 6"

# Rules for Samsung    
    
    @Rule(Preference(brand='samsung'))
    def recommend_samsung(self):
        print("Recommendation: Samsung phone")
        self.result = "Recommendation: Samsung phone"
        
# Rules for other recommendations
    
    @Rule(Preference(storage='yes', ram = "yes", camera = "yes", battery = "yes", budget="yes"))
    def recommend_google_128_6_b(self):
        print("Recommendation: Samsung Galaxy S20 Ultra 5G")
        self.result = "Recommendation: Samsung Galaxy S20 Ultra 5G"
        
class PhoneRecommendationApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Phone Recommendation System")
        
        self.brand_var = tk.StringVar(value="")
        self.storage_var = tk.StringVar()
        self.ram_var = tk.StringVar()
        self.camera_var = tk.StringVar()
        self.battery_var = tk.StringVar()
        self.budget_var = tk.StringVar()
        
        self.create_welcome_page()
        
    def create_welcome_page(self):
        """Creates the initial welcome page."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        ttk.Label(self.root, text="Do you have any knowledge about phone characteristics?",
                font=("Helvetica", 14)).pack(pady=20)
            
        yes_button = ttk.Button(self.root, text="Yes", command=self.select_brand_gui)
        yes_button.pack(side="left", padx=20, pady=20)

        no_button = ttk.Button(self.root, text="No", command=lambda: self.open_recommendation_gui("camera"))
        no_button.pack(side="right", padx=20, pady=20)

    def no_knowledge(self):
        """Handles the case when user clicks 'No'."""
        messagebox.showinfo("Info", "Please research more about phone characteristics before proceeding.")

    def open_recommendation_gui(self, field):
        """Opens the phone recommendation GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        print("Field is ",field)
                
        if field == "camera":
            qst = "Do you use your phone to take photos and videos a lot?"
            image = Image.open("camera.jfif")
        elif field == "storage":
            qst = "Do you download a lot of apps and games?"
            image = Image.open("storage.jfif")
        elif field == "ram":
            qst = "Do you need to handle heavy apps and/or multitask apps?"
            image = Image.open("ram.jfif")
        elif field == "battery":
            qst = "Do you use your phone for a long periods of time?"
            image = Image.open("battery.jfif")
        elif field == "budget":
            qst = "Are you willing to spend a lot of money on your new phone?"
            image = Image.open("money.jfif")
                        
        ttk.Label(self.root, text=qst, font=("Helvetica", 14)).pack(pady=20)
            
        # image = Image.open("storage.jfif")
        image = image.resize((200,150))
        photo = ImageTk.PhotoImage(image)
        image_label = Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
            
        yes_button = ttk.Button(self.root, text="Yes", command=lambda: self.handle_response(field, "yes"))
        yes_button.pack(side="left", padx=20, pady=20)

        no_button = ttk.Button(self.root, text="No", command=lambda: self.handle_response(field, "no"))
        no_button.pack(side="right", padx=20, pady=20)
        if field == "budget":
            self.result_screen_pack()
        
    def handle_response(self, field, response):
        """Handles button clicks and saves the response."""
        if field == "camera":
            self.camera_var = response
            self.open_recommendation_gui("storage")
        elif field == "storage":
            self.storage_var = response
            self.open_recommendation_gui("ram")           
        elif field == "ram":
            self.ram_var = response
            self.open_recommendation_gui("battery")
        elif field == "battery":
            self.battery_var = response
            self.open_recommendation_gui("budget")
        elif field == "budget":
            self.budget_var = response
            self.get_recommendation_alt()
        print(f"{field} Response saved: {response}")  # Debugging to confirm the value
        
    def select_brand_gui(self):
        """Opens the brand selection GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        ttk.Label(root, text="Select a brand").grid(row=0, column=0,columnspan=3,padx=10,pady=20)
        ttk.Label(root, text="Apple").grid(row=2, column=0,padx=20,pady=10)
        ttk.Label(root, text="Google").grid(row=2, column=1,padx=20,pady=10)
        ttk.Label(root, text="Samsung").grid(row=2, column=2,padx=20,pady=10)
        self.brand_buttons = {
            "apple": self.create_logo_button("apple_logo.png", "Apple", 1, 0),
            "google": self.create_logo_button("google_logo.png", "Google", 1, 1),
            "samsung": self.create_logo_button("samsung_logo.png", "Samsung", 1, 2)
            
        }
        
    def create_logo_button(self, logo_path, brand_name, row, col):
        image = Image.open(logo_path)
        image = image.resize((80,80))
        logo = ImageTk.PhotoImage(image)
    
        button = ttk.Button(self.root, image=logo, command=lambda: self.select_brand(brand_name))
        button.image = logo
        button.grid(row = row, column = col, padx=5, pady=5)
        
        return button
        
    def select_brand(self, brand_name):
        self.brand_var.set(brand_name)
        print(self.brand_var.get())
        self.select_storage_gui()
        # messagebox.showinfo("Brand selected", f"You selected: {brand_name}")
    
    def select_storage_gui(self):
        """Opens the brand selection GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        ttk.Label(self.root, text="Select a storage").grid(row=0, column=0,columnspan=2,padx=5,pady=5)
        image = Image.open("storage.jfif")
        image = image.resize((80,80))
        logo = ImageTk.PhotoImage(image)
        panel = Label(self.root, image=logo)
        panel.image = logo
        panel.grid(row=1,column=0,columnspan=2, pady = 10)
        
        # Textbox for User Input
        ttk.Label(self.root, text="Enter Your Storage Preference (e.g., 64GB):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.storage_input = ttk.Entry(self.root, textvariable=self.storage_var, width=20)
        self.storage_input.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Submit Button
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_storage)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def submit_storage(self):
        """Handles the submission of the storage preference."""
        storage_var = self.storage_input.get().strip()
        print(f"User entered storage: {storage_var}")
        self.select_ram_gui()
        
    def select_ram_gui(self):
        """Opens the brand selection GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        ttk.Label(self.root, text="Select a ram").grid(row=0, column=0,columnspan=2,padx=5,pady=5)
        image = Image.open("ram.jfif")
        image = image.resize((80,80))
        logo = ImageTk.PhotoImage(image)
        panel = Label(self.root, image=logo)
        panel.image = logo
        panel.grid(row=1,column=0,columnspan=2, pady = 10)
        
        # Textbox for User Input
        ttk.Label(self.root, text="Enter Your Ram Preference (e.g., 4GB):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.ram_input = ttk.Entry(self.root, textvariable=self.ram_var, width=20)
        self.ram_input.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Submit Button
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_ram)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def submit_ram(self):
        """Handles the submission of the ram preference."""
        ram_var = self.ram_input.get().strip()
        print(f"User entered ram: {ram_var}")
        self.select_camera_gui()
        
    def select_camera_gui(self):
        """Opens the camera selection GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        ttk.Label(self.root, text="Select a camera").grid(row=0, column=0,columnspan=2,padx=5,pady=5)
        image = Image.open("camera.jfif")
        image = image.resize((80,80))
        logo = ImageTk.PhotoImage(image)
        panel = Label(self.root, image=logo)
        panel.image = logo
        panel.grid(row=1,column=0,columnspan=2, pady = 10)
        
        # Textbox for User Input
        ttk.Label(self.root, text="Enter Your camera Preference (Budget or premium):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.camera_input = ttk.Entry(self.root, textvariable=self.camera_var, width=20)
        self.camera_input.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Submit Button
        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_camera)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)
        
    def submit_camera(self):
        """Handles the submission of the camera preference."""
        camera_var = self.camera_input.get().strip()
        print(f"User entered camera: {camera_var}")
        self.result_screen()
        self.get_recommendation()
        
    def result_screen(self):
        # Display area for recommendation
        self.result_label = ttk.Label(root, text="", foreground="blue", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)
    
    def result_screen_pack(self):
        # Display area for recommendation
        self.result_label = ttk.Label(root, text="", foreground="blue", font=("Helvetica", 12))
        self.result_label.pack(side="left",padx=10, pady=10)
        
    def create_recommendation_gui(self):
        """Creates the recommendation GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Create input widgets
        ttk.Label(self.root, text="Brand:").grid(row=0, column=0, padx=5, pady=5)
        self.brand_entry = ttk.Entry(self.root, textvariable=self.brand_var)
        self.brand_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Storage (64Gb/128Gb/256Gb):").grid(row=1, column=0, padx=5, pady=5)
        self.storage_entry = ttk.Entry(self.root, textvariable=self.storage_var)
        self.storage_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="RAM (3Gb/4Gb/6Gb):").grid(row=2, column=0, padx=5, pady=5)
        self.ram_entry = ttk.Entry(self.root, textvariable=self.ram_var)
        self.ram_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Camera (budget/premium):").grid(row=3, column=0, padx=5, pady=5)
        self.camera_entry = ttk.Entry(self.root, textvariable=self.camera_var)
        self.camera_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Create submit button
        self.submit_button = ttk.Button(root, text="Get Recommendation", command=self.get_recommendation)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Display area for recommendation
        self.result_label = ttk.Label(root, text="", foreground="blue", font=("Helvetica", 12))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def get_recommendation(self):
    
        brand = self.brand_var.get().strip().lower()
        storage = self.storage_var.get().strip().lower().removesuffix("gb")
        ram = self.ram_var.get().strip().lower().removesuffix("gb")
        camera = self.camera_var.get().strip().lower()    
        
        print("recommendation system data:", brand, storage, ram, camera)
        # Run the recommendation engine
        engine = PhoneRecommendation()
        engine.reset()
        engine.declare(Preference(brand=brand, storage=storage, ram=ram, camera=camera))
        engine.run()

        # Display the result
        if engine.result:
            self.result_label.config(text=engine.result)
        else:
            self.result_label.config(text="No recommendations found.")
    
    def get_recommendation_alt(self):
        
        print("recommendation system data:", self.storage_var, self.ram_var, self.camera_var, self.battery_var, self.budget_var)
        # Run the recommendation engine
        engine = PhoneRecommendation()
        engine.reset()
        engine.declare(Preference(storage=self.storage_var, ram=self.ram_var, camera=self.camera_var, battery = self.battery_var,budget=self.budget_var ))
        engine.run()

        # Display the result
        if engine.result:
            self.result_label.config(text=engine.result)
        else:
            self.result_label.config(text="No recommendations found.")
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneRecommendationApp(root)
    root.mainloop()    