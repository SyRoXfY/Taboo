import random
import time
import tkinter as tk
from tkinter import messagebox
import winsound

# Save scores
def save_score(score):
    with open("scores.txt", "a") as file:
        file.write(f"Score: {score}\n")

# Sound effects
def correct_sound():
    winsound.Beep(1000, 200)

def end_sound():
    winsound.Beep(500, 600)

tabu_words = [
    {"word": "Dog", "forbidden": ["Pet", "Bark", "Tail", "Loyal", "Leash"]},
    {"word": "Cake", "forbidden": ["Sweet", "Birthday", "Cream", "Slice", "Sugar"]},
    {"word": "Sun", "forbidden": ["Star", "Daylight", "Sky", "Heat", "Yellow"]},
    {"word": "Car", "forbidden": ["Vehicle", "Driver", "Road", "Engine", "Wheels"]},
    {"word": "Stool", "forbidden": ["Chair", "Furniture", "Sit", "Legs", "Seat"]},
    {"word": "Book", "forbidden": ["Reading", "Story", "Page", "Author", "Library"]},
    {"word": "Pizza", "forbidden": ["Food", "Cheese", "Slice", "Dough", "Sauce"]},
    {"word": "Tree", "forbidden": ["Plant", "Leaves", "Wood", "Forest", "Roots"]},
    {"word": "Ball", "forbidden": ["Round", "Bounce", "Play", "Sport", "Throw"]},
    {"word": "Phone", "forbidden": ["Call", "Mobile", "Message", "Ring", "Voice"]},
    {"word": "Door", "forbidden": ["Entrance", "Open", "Close", "Lock", "Key"]},
    {"word": "Cat", "forbidden": ["Meow", "Fur", "Purring", "Claws", "Pet"]},
    {"word": "House", "forbidden": ["Home", "Building", "Roof", "Walls", "Window"]},
    {"word": "Pen", "forbidden": ["Write", "Ink", "Paper", "Tip", "Notebook"]},
    {"word": "Key", "forbidden": ["Lock", "Door", "Unlock", "Turn", "Open"]},
    {"word": "Fish", "forbidden": ["Swim", "Water", "Fin", "Aquarium", "Sea"]},
    {"word": "Hat", "forbidden": ["Head", "Cap", "Sun", "Clothing", "Accessory"]},
    {"word": "Table", "forbidden": ["Furniture", "Meal", "Surface", "Work", "Legs"]},
    {"word": "Flower", "forbidden": ["Plant", "Petals", "Garden", "Color", "Smell"]},
    {"word": "Clock", "forbidden": ["Time", "Hands", "Alarm", "Numbers", "Tick"]},
    {"word": "Chair", "forbidden": ["Sit", "Furniture", "Legs", "Cushion", "Seat"]},
    {"word": "Glass", "forbidden": ["Drink", "Cup", "Handle", "Water", "Transparent"]},
    {"word": "Lamp", "forbidden": ["Bulb", "Light", "Shade", "Electric", "Table"]},
    {"word": "Shoes", "forbidden": ["Socks", "Feet", "Laces", "Walk", "Wear"]},
    {"word": "Shirt", "forbidden": ["Clothing", "Wear", "Collar", "Cotton", "Iron"]},
    {"word": "Spoon", "forbidden": ["Food", "Mix", "Metal", "Soup", "Sweet"]},
    {"word": "Apple", "forbidden": ["Fruit", "Red", "Crisp", "Tree", "Green"]},
    {"word": "Window", "forbidden": ["Glass", "View", "Frame", "Open", "Close"]},
    {"word": "Bag", "forbidden": ["Carry", "Shoulder", "School", "Hand", "Back"]},
    {"word": "Orange", "forbidden": ["Fruit", "Citrus", "Peel", "Sweet", "Yellow"]},
    {"word": "Bed", "forbidden": ["Sleep", "Rest", "Blanket", "Pillow", "Cover"]},
    {"word": "Couch", "forbidden": ["Sofa", "Furniture", "Comfort", "Living room", "Sit"]},
    {"word": "Football", "forbidden": ["Sport", "Throw", "Catch", "Round", "Messi"]},
    {"word": "Guitar", "forbidden": ["Instrument", "Strings", "Music", "Chord", "Play"]},
    {"word": "Duck", "forbidden": ["Beak", "Water", "Feathers", "Swim", "Quack"]},
    {"word": "Bread", "forbidden": ["Food", "Slice", "Loaf", "Bake", "Toast"]},
    {"word": "Bird", "forbidden": ["Wing", "Fly", "Feathers", "Nest", "Egg"]},
    {"word": "Chocolate", "forbidden": ["Sweet", "Brown", "Cocoa", "Bar", "Bitter"]},
    {"word": "Sea", "forbidden": ["Salt", "Wave", "Beach", "Water", "Wet"]},
    {"word": "Letter", "forbidden": ["Write", "Post", "Envelope", "Message", "Stamp"]},
    {"word": "Volcano", "forbidden": ["Eruption", "Lava", "Crater", "Magma", "Hot"]},
    {"word": "Renaissance", "forbidden": ["Art", "Rebirth", "Italy", "Middle Ages", "Da Vinci"]},
    {"word": "Dinosaur", "forbidden": ["Extinct", "Fossil", "Jurassic", "Reptile", "Evolution"]},
    {"word": "Solar System", "forbidden": ["Planet", "Moon", "Orbit", "Space", "Galaxy"]},
    {"word": "Revolution", "forbidden": ["Change", "Uprising", "Protest", "Rebellion", "Innovation"]},
    {"word": "Tsunami", "forbidden": ["Wave", "Ocean", "Disaster", "Earthquake", "Hurricane"]},
    {"word": "Picasso", "forbidden": ["Artist", "Cubism", "Painting", "Spain", "Art"]},
    {"word": "Symphony", "forbidden": ["Music", "Orchestra", "Conductor", "Beethoven", "Instrument"]},
    {"word": "Democracy", "forbidden": ["Government", "Voting", "Freedom", "People", "Equality"]},
    {"word": "Statue of Liberty", "forbidden": ["New York", "Torch", "Symbol", "Freedom", "America"]},
    {"word": "Gravity", "forbidden": ["Force", "Apple", "Newton", "Physics", "Mass"]},
    {"word": "Shakespeare", "forbidden": ["Playwright", "Sonnet", "Tragedy", "England", "Theater"]},
    {"word": "Glacier", "forbidden": ["Ice", "Melt", "Pole", "Frozen", "Titanic"]},
    {"word": "Mona Lisa", "forbidden": ["Painting", "Smile", "Da Vinci", "Louvre", "Renaissance"]},
    {"word": "Computer", "forbidden": ["Technology", "Internet", "Device", "Software", "Code"]},
    {"word": "Eiffel Tower", "forbidden": ["Paris", "Olympics", "Steel", "France", "Iron"]},
    {"word": "Desert", "forbidden": ["Sand", "Hot", "Dry", "Arid", "Cactus"]},
    {"word": "Football", "forbidden": ["Sport", "Ball", "Goal", "Field", "Messi"]},
    {"word": "Empire State Building", "forbidden": ["New York", "Skyscraper", "View", "Tall", "America"]},
    {"word": "Bouzouki", "forbidden": ["Instrument", "Strings", "Music", "Play", "Greece"]},
    {"word": "Amazon Rainforest", "forbidden": ["Brazil", "Biodiversity", "Tropical", "Ecosystem", "South America"]},
    {"word": "Mozart", "forbidden": ["Composer", "Classical", "Piano", "Austria", "Beethoven"]},
    {"word": "Internet", "forbidden": ["Network", "Connection", "Information", "Online", "Data"]},
    {"word": "Everest", "forbidden": ["Mountain", "Peak", "Nepal", "Climb", "High"]},
    {"word": "Metro", "forbidden": ["Transport", "Subway", "Train", "Car", "Cabin"]},
    {"word": "Declaration of Independence", "forbidden": ["America", "Freedom", "Document", "1776", "Rights"]},
    {"word": "Starry Night", "forbidden": ["Painting", "Van Gogh", "Sky", "Art Piece", "Brush"]},
    {"word": "Pyramids", "forbidden": ["Egypt", "Pharaoh", "Tomb", "Ancient", "Cleopatra"]},
    {"word": "Agreement", "forbidden": ["Contract", "Deal", "Negotiation", "Sign", "Paper"]},
    {"word": "Journey", "forbidden": ["Trip", "Travel", "Destination", "Adventure", "Path"]},
    {"word": "Library", "forbidden": ["Books", "Read", "Shelf", "Quiet", "Study"]},
    {"word": "Confidence", "forbidden": ["Trust", "Self-esteem", "Believe", "Strong", "Positive"]},
    {"word": "Environment", "forbidden": ["Nature", "Pollution", "Earth", "Climate", "Green"]},
    {"word": "Communication", "forbidden": ["Talk", "Message", "Conversation", "Words", "Understand"]},
    {"word": "Invention", "forbidden": ["Create", "Discovery", "Technology", "New", "Innovation"]},
    {"word": "Friendship", "forbidden": ["Trust", "Companion", "Bond", "Together", "Close"]},
    {"word": "Happiness", "forbidden": ["Joy", "Smile", "Emotion", "Feelings", "Love"]},
    {"word": "Success", "forbidden": ["Achievement", "Win", "Goal", "Hard work", "Result"]},
    {"word": "Education", "forbidden": ["School", "Learning", "Knowledge", "Study", "Teacher"]},
    {"word": "Challenge", "forbidden": ["Difficult", "Test", "Problem", "Overcome", "Task"]},
    {"word": "Opinion", "forbidden": ["Think", "View", "Personal", "Belief", "Expression"]},
    {"word": "Technology", "forbidden": ["Computer", "Internet", "Innovation", "Future", "Machine"]},
    {"word": "Decision", "forbidden": ["Choose", "Think", "Final", "Option", "Plan"]},
    {"word": "Future", "forbidden": ["Tomorrow", "Later", "Time", "Plan", "Destiny"]},
    {"word": "Adventure", "forbidden": ["Exciting", "Experience", "Travel", "Explore", "Danger"]},
    {"word": "Creativity", "forbidden": ["Imagination", "Art", "Ideas", "New", "Innovate"]},
    {"word": "Music", "forbidden": ["Song", "Instrument", "Melody", "Sound", "Listen"]},
    {"word": "Family", "forbidden": ["Parents", "Home", "Children", "Love", "Together"]},
    {"word": "Problem", "forbidden": ["Solve", "Difficult", "Issue", "Fix", "Challenge"]},
    {"word": "Exercise", "forbidden": ["Gym", "Run", "Healthy", "Fit", "Workout"]},
    {"word": "Shopping", "forbidden": ["Buy", "Store", "Money", "Mall", "Groceries"]},
    {"word": "Weather", "forbidden": ["Rain", "Sun", "Cloud", "Forecast", "Temperature"]},
    {"word": "Dream", "forbidden": ["Sleep", "Night", "Imagine", "Fantasy", "Goal"]},
    {"word": "Health", "forbidden": ["Doctor", "Medicine", "Fit", "Well-being", "Sick"]},
    {"word": "Sport", "forbidden": ["Game", "Competition", "Team", "Ball", "Exercise"]},
    {"word": "Language", "forbidden": ["Speak", "Words", "Grammar", "Translate", "Foreign"]},
    {"word": "Internet", "forbidden": ["Website", "Online", "Social media", "Google", "Wi-Fi"]},
    {"word": "Taylor Swift", "forbidden": ["Singer", "Pop", "Music", "Red", "Album"]},
    {"word": "The Office", "forbidden": ["Comedy", "Dunder Mifflin", "Michael Scott", "Employees", "Office"]},
    {"word": "Game of Thrones", "forbidden": ["Dragons", "Winter", "Throne", "Fantasy", "Kings"]},
    {"word": "Leonardo DiCaprio", "forbidden": ["Actor", "Titanic", "Oscar", "Hollywood", "Movie"]},
    {"word": "Breaking Bad", "forbidden": ["Heisenberg", "Walter White", "Drugs", "Chemistry", "Meth"]},
    {"word": "The Beatles", "forbidden": ["Band", "Music", "Lennon", "McCartney", "Rock"]},
    {"word": "Harry Potter", "forbidden": ["Wizard", "Magic", "Hogwarts", "Wand", "Voldemort"]},
    {"word": "Shakespeare", "forbidden": ["Playwright", "Literature", "Hamlet", "Romeo", "Juliet"]},
    {"word": "Star Wars", "forbidden": ["Space", "Jedi", "Luke", "Lightsaber", "Force"]},
    {"word": "Elon Musk", "forbidden": ["Tesla", "SpaceX", "Tech", "Engineer", "Innovation"]},
    {"word": "The Godfather", "forbidden": ["Mafia", "Don", "Crime", "Family", "Corleone"]},
    {"word": "Spider-Man", "forbidden": ["Superhero", "Web", "Peter Parker", "Marvel", "Suit"]},
    {"word": "Iron Man", "forbidden": ["Tony Stark", "Suit", "Superhero", "Avengers", "Metal"]},
    {"word": "Friends", "forbidden": ["Sitcom", "Rachel", "Chandler", "Monica", "Group"]},
    {"word": "The Simpsons", "forbidden": ["Homer", "Cartoon", "Maggie", "Bart", "Family"]},
    {"word": "Matrix", "forbidden": ["Keanu Reeves", "Neo", "Simulation", "Red pill", "Green code"]},
    {"word": "Stranger Things", "forbidden": ["Eleven", "Demogorgon", "Upside down", "Kids", "Horror"]},
    {"word": "Michael Jackson", "forbidden": ["Singer", "Thriller", "Moonwalk", "Pop", "Music"]},
    {"word": "Superman", "forbidden": ["Clark Kent", "Hero", "Kryptonite", "Superpower", "Flying"]},
    {"word": "Spider-Man", "forbidden": ["Web", "Peter Parker", "Marvel", "Hero", "Suit"]},
    {"word": "Avengers", "forbidden": ["Superheroes", "Marvel", "Team", "Iron Man", "Thor"]},
    {"word": "The Lion King", "forbidden": ["Hakuna Matata", "Simba", "Disney", "Africa", "King"]},
    {"word": "The Dark Knight", "forbidden": ["Batman", "Joker", "Gotham", "Hero", "Villain"]},
    {"word": "Avatar", "forbidden": ["James Cameron", "Blue", "Aliens", "Pandora", "Movie"]},
    {"word": "Walt Disney", "forbidden": ["Cartoons", "Movies", "Animation", "Mickey Mouse", "Park"]},
    {"word": "The Hunger Games", "forbidden": ["Katniss", "District", "Arena", "Mockingjay", "Survival"]},
    {"word": "Black Panther", "forbidden": ["Wakanda", "Marvel", "Superhero", "King", "T'Challa"]},
    {"word": "Doctor Strange", "forbidden": ["Sorcerer", "Marvel", "Magic", "Strange", "Multiverse"]},
    {"word": "Brazil", "forbidden": ["Country", "South America", "Rio", "Carnival", "Football"]},
    {"word": "Australia", "forbidden": ["Country", "Sydney", "Opera House", "Great Barrier Reef", "Kangaroo"]},
    {"word": "Game of Thrones", "forbidden": ["Throne", "Winter", "Dragons", "Kings", "Westeros"]},
    {"word": "Paris", "forbidden": ["France", "Eiffel Tower", "City", "Romance", "Fashion"]},
    {"word": "Avengers", "forbidden": ["Iron Man", "Thor", "Captain America", "Superheroes", "Marvel"]},
    {"word": "Narcos", "forbidden": ["Netflix", "Pablo Escobar", "Cartel", "Colombia", "Drugs"]},
    {"word": "Japan", "forbidden": ["Country", "Tokyo", "Sushi", "Technology", "Sumo"]},
    {"word": "Mexico", "forbidden": ["Country", "Tacos", "Cactus", "Chili", "Mariachi"]},
    {"word": "Egypt", "forbidden": ["Pyramids", "Cairo", "Pharaoh", "Mummies", "Sphinx"]},
    {"word": "Al Pacino", "forbidden": ["Actor", "The Godfather", "Scarface", "Legend", "Hollywood"]},
    {"word": "Ariana Grande", "forbidden": ["Singer", "Pop", "Voice", "Dangerous Woman", "Album"]},
    {"word": "Bollywood", "forbidden": ["India", "Films", "Movies", "Dance", "Music"]},
    {"word": "Laptop", "forbidden": ["Computer", "Screen", "Keyboard", "Technology", "Portable"]},
    {"word": "Smartphone", "forbidden": ["Phone", "Touchscreen", "iPhone", "Android", "Mobile"]},
    {"word": "Table", "forbidden": ["Furniture", "Wood", "Flat", "Surface", "Dining"]},
    {"word": "Chair", "forbidden": ["Furniture", "Sit", "Legs", "Seat", "Cushion"]},
    {"word": "TV", "forbidden": ["Screen", "Watch", "Channels", "Remote", "Entertainment"]},
    {"word": "Refrigerator", "forbidden": ["Cold", "Food", "Kitchen", "Fridge", "Freezer"]},
    {"word": "Microwave", "forbidden": ["Oven", "Heat", "Kitchen", "Food", "Cook"]},
    {"word": "Oven", "forbidden": ["Bake", "Heat", "Food", "Cooking", "Kitchen"]},
    {"word": "Washing Machine", "forbidden": ["Clothes", "Laundry", "Wash", "Detergent", "Cycle"]},
    {"word": "Blender", "forbidden": ["Smoothie", "Mix", "Kitchen", "Drink", "Fruit"]},
    {"word": "Toaster", "forbidden": ["Bread", "Heat", "Toast", "Kitchen", "Slices"]},
    {"word": "Headphones", "forbidden": ["Music", "Ear", "Sound", "Listen", "Audio"]},
    {"word": "Shoes", "forbidden": ["Feet", "Footwear", "Socks", "Walk", "Clothes"]},
    {"word": "Glasses", "forbidden": ["Eyes", "Vision", "Lens", "Sight", "Frames"]},
    {"word": "Watch", "forbidden": ["Time", "Wrist", "Clock", "Band", "Hours"]},
    {"word": "Camera", "forbidden": ["Picture", "Photo", "Lens", "Capture", "Photography"]},
    {"word": "Pillow", "forbidden": ["Bed", "Cushion", "Soft", "Sleep", "Head"]},
    {"word": "Blanket", "forbidden": ["Warm", "Cover", "Sleep", "Bed", "Comfort"]},
    {"word": "Suitcase", "forbidden": ["Travel", "Luggage", "Clothes", "Bag", "Packing"]},
]


class TabooGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Taboo Game")
        self.root.geometry("500x600")
        self.score = 0
        self.time_left = 60
        
        self.root.configure(bg="#FFDDC1")
        
        # Create a frame for the word card
        self.card_frame = tk.Frame(root, bg="#FF5733", bd=10, relief="ridge", width=400, height=300)
        self.card_frame.pack(pady=30)
        
        self.word_label = tk.Label(self.card_frame, text="Word: ", font=("Arial", 20, "bold"), fg="white", bg="#FF5733")
        self.word_label.pack(pady=20)
        
        self.forbidden_label = tk.Label(self.card_frame, text="Forbidden Words: ", font=("Arial", 14), fg="white", bg="#FF5733")
        self.forbidden_label.pack(pady=10)
        
        # Removing the input field for guesses
        self.guess_button = tk.Button(root, text="+ (Correct Guess)", command=self.increase_score, bg="#FF5733", fg="white", width=20)
        self.guess_button.pack(pady=10)
        
        self.pass_button = tk.Button(root, text="Pass", command=self.new_word, bg="#33AFFF", fg="white", width=20)
        self.pass_button.pack(pady=10)
        
        self.timer_label = tk.Label(root, text=f"Time: {self.time_left}s", font=("Arial", 14), bg="#FFDDC1")
        self.timer_label.pack(pady=5)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="#FFDDC1")
        self.score_label.pack(pady=5)
        
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", width=20)
        self.start_button.pack(pady=10)
        
        self.game_over_frame = None
    
    def start_game(self):
        if self.game_over_frame:
            self.game_over_frame.destroy()  # Eğer bir oyun bitti ekranı varsa, onu temizle
        self.score = 0
        self.time_left = 60
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time: {self.time_left}s")
        self.root.after(1000, self.timer)
        self.new_word()
    
    def new_word(self):
        if not tabu_words:
            self.end_game()
            return
        
        self.question = random.choice(tabu_words)
        tabu_words.remove(self.question)
        
        self.word_label.config(text=f"Word: {self.question['word']}")
        self.forbidden_label.config(text=f"Forbidden Words: {', '.join(self.question['forbidden'])}")
    
    def increase_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        correct_sound()
        self.new_word()
    
    def timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.root.after(1000, self.timer)
        else:
            self.end_game()
    
    def end_game(self):
        messagebox.showinfo("Game Over", f"Game over! Your score: {self.score}")
        save_score(self.score)
        
        # Create a frame for the game over screen with a 'Start Game' button
        self.game_over_frame = tk.Frame(self.root, bg="#FFDDC1")
        self.game_over_frame.pack(pady=20)
        
        # Only "Start Game" button to restart
        start_game_button = tk.Button(self.game_over_frame, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", width=20)
        start_game_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = TabooGame(root)
    root.mainloop()
