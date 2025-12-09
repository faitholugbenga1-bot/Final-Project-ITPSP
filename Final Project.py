import turtle
import random
import time

class VirtualPet:
    def __init__(self, shape, name):
        self.shape = shape
        self.name = name
        self.hunger = 50
        self.cleanliness = 50
        self.happiness = 50
        self.age = 0
        self.friendship = 0
        self.favorite_activity = random.choice(["feeding", "cleaning", "playing"])
        
        # Setup turtle screen
        self.screen = turtle.Screen()
        self.screen.title(f"🌟 {self.name} the {self.shape.title()} 🌟")
        self.screen.bgcolor("lightblue")
        self.screen.setup(width=800, height=700)
        
        # Pet turtle
        self.pet = turtle.Turtle()
        self.pet.speed(0)
        self.pet.penup()
        
        # Text turtle for stats
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.speed(0)
        
        # Mood turtle
        self.mood = turtle.Turtle()
        self.mood.hideturtle()
        self.mood.penup()
        self.mood.speed(0)
        
    def get_color(self):
        """Get color based on stats"""
        avg = (self.hunger + self.cleanliness + self.happiness) / 3
        if avg >= 80:
            return ["pink", "magenta", "hot pink", "deep pink", "violet"]  # Rainbow effect
        elif avg >= 70:
            return ["hot pink"]
        elif avg >= 50:
            return ["pink"]
        elif avg >= 30:
            return ["light pink"]
        else:
            return ["gray"]
    
    def draw_cat(self, colors):
        """Draw a cute cat"""
        color = random.choice(colors)
        
        # Body (oval)
        self.pet.goto(0, -50)
        self.pet.color(color)
        self.pet.setheading(0)
        self.pet.begin_fill()
        self.pet.circle(45)
        self.pet.end_fill()
        
        # Head (round)
        self.pet.goto(0, 10)
        self.pet.begin_fill()
        self.pet.circle(35)
        self.pet.end_fill()
        
        # Pointy ears (triangles)
        self.pet.goto(-20, 40)
        self.pet.setheading(60)
        self.pet.begin_fill()
        self.pet.forward(75)
        self.pet.right(120)
        self.pet.forward(37)
        self.pet.end_fill()
        
        self.pet.goto(20, 40)
        self.pet.setheading(120)
        self.pet.begin_fill()
        self.pet.forward(75)
        self.pet.left(120)
        self.pet.forward(37)
        self.pet.end_fill()
        
        # Tail (curved)
        self.pet.goto(-30, -40)
        self.pet.setheading(180)
        self.pet.pensize(8)
        self.pet.pendown()
        self.pet.circle(30, 90)
        self.pet.penup()
        self.pet.pensize(1)
        
        # Eyes
        self.pet.color("black")
        self.pet.goto(-12, 55)
        self.pet.dot(8)
        self.pet.goto(12, 55)
        self.pet.dot(8)

        
        # Whiskers
        self.pet.color("black")
        self.pet.pensize(1)
        # Left whiskers
        self.pet.goto(-25, 40)
        self.pet.setheading(170)
        self.pet.pendown()
        self.pet.forward(15)
        self.pet.penup()
        self.pet.goto(-25, 40)
        self.pet.setheading(185)
        self.pet.pendown()
        self.pet.forward(15)
        self.pet.penup()
        # Right whiskers
        self.pet.goto(25, 40)
        self.pet.setheading(10)
        self.pet.pendown()
        self.pet.forward(15)
        self.pet.penup()
        self.pet.goto(25, 40)
        self.pet.setheading(25)
        self.pet.pendown()
        self.pet.forward(15)
        self.pet.penup()
        
    def draw_dog(self, colors):
        """Draw a cute dog"""
        color = random.choice(colors)
        
        # Body
        self.pet.goto(0, -50)
        self.pet.color(color)
        self.pet.begin_fill()
        self.pet.circle(50)
        self.pet.end_fill()
        
        # Head
        self.pet.goto(0, 10)
        self.pet.begin_fill()
        self.pet.circle(40)
        self.pet.end_fill()
        
        # Floppy ears
        self.pet.goto(-40, 35)
        self.pet.begin_fill()
        self.pet.circle(18)
        self.pet.end_fill()
        
        self.pet.goto(40, 35)
        self.pet.begin_fill()
        self.pet.circle(18)
        self.pet.end_fill()
        
        # Snout
        self.pet.goto(0, 0)
        self.pet.color("tan")
        self.pet.begin_fill()
        self.pet.circle(18)
        self.pet.end_fill()
        
        # Eyes
        self.pet.color("black")
        self.pet.goto(-15, 28)
        self.pet.dot(10)
        self.pet.goto(15, 28)
        self.pet.dot(10)
        
        # Nose
        self.pet.goto(0, 8)
        self.pet.dot(8)
        
        # Tongue
        self.pet.goto(0, -5)
        self.pet.color("red")
        self.pet.begin_fill()
        self.pet.circle(6)
        self.pet.end_fill()
        
        # Tail
        self.pet.goto(-35, -35)
        self.pet.color(color)
        self.pet.setheading(200)
        self.pet.pensize(8)
        self.pet.pendown()
        self.pet.circle(-25, 80)
        self.pet.penup()
        self.pet.pensize(1)
        
    def draw_bunny(self, colors):
        """Draw a cute bunny"""
        color = random.choice(colors)
        
        # Body
        self.pet.goto(0, -50)
        self.pet.color(color)
        self.pet.begin_fill()
        self.pet.circle(50)
        self.pet.end_fill()
        
        # Head
        self.pet.goto(0, 15)
        self.pet.begin_fill()
        self.pet.circle(38)
        self.pet.end_fill()
        
        # Long ears
        self.pet.goto(-12, 50)
        self.pet.setheading(80)
        self.pet.begin_fill()
        for _ in range(2):
            self.pet.circle(12, 90)
            self.pet.circle(40, 90)
        self.pet.end_fill()
        
        self.pet.goto(12, 50)
        self.pet.setheading(100)
        self.pet.begin_fill()
        for _ in range(2):
            self.pet.circle(12, 90)
            self.pet.circle(40, 90)
        self.pet.end_fill()
        
        # Fluffy tail
        self.pet.goto(-35, -45)
        self.pet.begin_fill()
        self.pet.circle(15)
        self.pet.end_fill()
        
        # Eyes
        self.pet.color("black")
        self.pet.goto(-12, 35)
        self.pet.dot(10)
        self.pet.goto(12, 35)
        self.pet.dot(10)
        
        # Nose
        self.pet.goto(0, 25)
        self.pet.color("pink")
        self.pet.dot(6)
        
        # Bunny teeth
        self.pet.color("white")
        self.pet.goto(-4, 18)
        self.pet.begin_fill()
        self.pet.setheading(270)
        self.pet.forward(8)
        self.pet.right(90)
        self.pet.forward(6)
        self.pet.right(90)
        self.pet.forward(8)
        self.pet.end_fill()
        
        self.pet.goto(4, 18)
        self.pet.begin_fill()
        self.pet.setheading(270)
        self.pet.forward(8)
        self.pet.left(90)
        self.pet.forward(6)
        self.pet.left(90)
        self.pet.forward(8)
        self.pet.end_fill()
        
    def draw_bear(self, colors):
        """Draw a cute bear"""
        color = random.choice(colors)
        
        # Body
        self.pet.goto(0, -55)
        self.pet.color(color)
        self.pet.begin_fill()
        self.pet.circle(55)
        self.pet.end_fill()
        
        # Head
        self.pet.goto(0, 15)
        self.pet.begin_fill()
        self.pet.circle(40)
        self.pet.end_fill()
        
        # Round ears
        self.pet.goto(-28, 50)
        self.pet.begin_fill()
        self.pet.circle(15)
        self.pet.end_fill()
        
        self.pet.goto(28, 50)
        self.pet.begin_fill()
        self.pet.circle(15)
        self.pet.end_fill()
        
        # Snout
        self.pet.goto(0, 5)
        self.pet.color("tan")
        self.pet.begin_fill()
        self.pet.circle(18)
        self.pet.end_fill()
        
        # Eyes
        self.pet.color("black")
        self.pet.goto(-12, 32)
        self.pet.dot(8)
        self.pet.goto(12, 32)
        self.pet.dot(8)
        
        # Nose
        self.pet.goto(0, 14)
        self.pet.dot(10)
        
        # Belly
        self.pet.goto(0, -30)
        self.pet.color("tan")
        self.pet.begin_fill()
        self.pet.circle(28)
        self.pet.end_fill()
        
    def draw_bird(self, colors):
        """Draw a cute bird"""
        color = random.choice(colors)
        
        # Body
        self.pet.goto(0, -30)
        self.pet.color(color)
        self.pet.begin_fill()
        self.pet.circle(45)
        self.pet.end_fill()
        
        # Head
        self.pet.goto(0, 20)
        self.pet.begin_fill()
        self.pet.circle(30)
        self.pet.end_fill()
        
        # Wings
        self.pet.goto(-45, -5)
        self.pet.setheading(200)
        self.pet.begin_fill()
        self.pet.circle(30, 100)
        self.pet.goto(-45, -5)
        self.pet.end_fill()
        
        self.pet.goto(45, -5)
        self.pet.setheading(-20)
        self.pet.begin_fill()
        self.pet.circle(30, 100)
        self.pet.goto(45, -5)
        self.pet.end_fill()
        
        # Eyes
        self.pet.color("black")
        self.pet.goto(-10, 35)
        self.pet.dot(8)
        self.pet.goto(10, 35)
        self.pet.dot(8)
        
        # Beak
        self.pet.goto(0, 30)
        self.pet.color("orange")
        self.pet.setheading(-60)
        self.pet.begin_fill()
        for _ in range(3):
            self.pet.forward(12)
            self.pet.left(120)
        self.pet.end_fill()
        
        # Feet
        self.pet.goto(-10, -70)
        self.pet.pensize(3)
        self.pet.setheading(-90)
        self.pet.pendown()
        self.pet.forward(10)
        self.pet.penup()
        
        self.pet.goto(10, -70)
        self.pet.pendown()
        self.pet.forward(10)
        self.pet.penup()
        self.pet.pensize(1)
        
    def draw_pet(self):
        """Draw the pet based on shape"""
        self.pet.clear()
        self.pet.penup()
        colors = self.get_color()
        
        if self.shape == "cat":
            self.draw_cat(colors)
        elif self.shape == "dog":
            self.draw_dog(colors)
        elif self.shape == "bunny":
            self.draw_bunny(colors)
        elif self.shape == "bear":
            self.draw_bear(colors)
        elif self.shape == "bird":
            self.draw_bird(colors)
    
    def draw_emoji(self, emoji, x, y):
        """Draw emoji next to pet"""
        self.mood.goto(x, y)
        self.mood.write(emoji, align="center", font=("Arial", 40, "normal"))
    
    def display_status(self):
        """Display stats and pet"""
        self.pet.clear()
        self.text.clear()
        self.mood.clear()
        
        # Draw pet
        self.draw_pet()
        
        # Draw mood emoji
        if self.happiness >= 80:
            emoji = random.choice(["😊", "🥰", "😄", "✨"])
        elif self.happiness >= 60:
            emoji = "🙂"
        elif self.happiness >= 40:
            emoji = "😐"
        elif self.happiness >= 20:
            emoji = "😟"
        else:
            emoji = "😢"
        self.draw_emoji(emoji, 100, 50)
        
        # Draw stats
        self.text.goto(0, -200)
        self.text.color("black")
        stats_text = f"{self.name} the {self.shape.title()}\n\n"
        stats_text += f"💚 Hunger: {self.hunger}%\n"
        stats_text += f"✨ Cleanliness: {self.cleanliness}%\n"
        stats_text += f"😊 Happiness: {self.happiness}%\n"
        stats_text += f"💝 Friendship: {self.friendship}\n"
        stats_text += f"🎂 Age: {self.age} turns\n\n"
        
        hunger = self.hunger / 1
        if hunger >= 80:
            stats_text += "HUNGER:✨ RAINBOW MODE! ✨"
        elif hunger >= 70:
            stats_text += "HUNGER:✅ Thriving!"
        elif hunger >= 50:
            stats_text += "HUNGER:Lunch time?"
        elif hunger >= 30:
            stats_text += "HUNGER:⚠️ Needs attention"
        else:
            stats_text += "HUNGER:🚨 URGENT CARE NEEDED!"
        dirt  = self.cleanliness / 1
        if dirt >= 80:
            stats_text += "CLEANLINESS:✨ RAINBOW MODE! ✨"
        elif dirt >= 70:
            stats_text += "CLEANLINESS:✅ Squeaky Clean!"
        elif dirt >= 50:
            stats_text += "CLEANLINESS:bath time?"
        elif dirt >= 30:
            stats_text += "CLEANLINESS:⚠ Needs attention"
        else:
            stats_text += "CLEANLINESS:🚨 URGENT CARE NEEDED!"
            
        sad  = self.happiness / 1
        if dirt >= 80:
            stats_text += "HAPPINESS:✨ RAINBOW MODE! ✨"
        elif dirt >= 70:
            stats_text += "HAPPINESS:✅ Doing Great!"
        elif dirt >= 50:
            stats_text += "HAPPINESS:play time?"
        elif dirt >= 30:
            stats_text += "HAPPINESS:⚠️ Needs attention"
        else:
            stats_text += "HAPPINESS:🚨 URGENT CARE NEEDED!"

        
        self.text.write(stats_text, align="center", font=("Arial", 12, "normal"))
        
        # Instructions
        self.text.goto(0, 280)
        self.text.write("Press: [F]eed  [C]lean  [P]lay  [W]ait  [R]estart  [Q]uit", 
                       align="center", font=("Arial", 10, "bold"))
    
    def show_message(self, message):
        """Show temporary message"""
        msg_turtle = turtle.Turtle()
        msg_turtle.hideturtle()
        msg_turtle.penup()
        msg_turtle.goto(0, 150)
        msg_turtle.color("blue")
        msg_turtle.write(message, align="center", font=("Arial", 14, "bold"))
        self.screen.update()
        time.sleep(1.5)
        msg_turtle.clear()
    
    def feed(self):
        bonus = 10 if self.favorite_activity == "feeding" else 0
        self.hunger = min(100, self.hunger + 30 + bonus)
        self.happiness = min(100, self.happiness + 10 + bonus)
        self.friendship += 2
        messages = ["*munch munch* 😋", "*nom nom* Yum!", "Delicious! 🍖"]
        self.show_message(random.choice(messages))
        
    def clean(self):
        bonus = 10 if self.favorite_activity == "cleaning" else 0
        self.cleanliness = min(100, self.cleanliness + 40 + bonus)
        self.happiness = min(100, self.happiness + 5 + bonus)
        self.friendship += 2
        messages = ["*splash* So fresh! 🛁", "Sparkling clean! ✨", "That tickles! 😊"]
        self.show_message(random.choice(messages))
        
    def play(self):
        bonus = 10 if self.favorite_activity == "playing" else 0
        self.happiness = min(100, self.happiness + 35 + bonus)
        self.hunger = max(0, self.hunger - 10)
        self.friendship += 3
        messages = ["Wheee! 🎾", "Best day ever! 🎉", "Let's go! 🌟"]
        self.show_message(random.choice(messages))
        
    def pass_time(self):
        self.hunger = max(0, self.hunger - 15)
        self.cleanliness = max(0, self.cleanliness - 10)
        self.happiness = max(0, self.happiness - 12)
        self.age += 1
        
        if self.hunger < 30 or self.cleanliness < 30 or self.happiness < 30:
            messages = ["*stomach growls* 🥺", "*looks sad*", "*whimpers*"]
            self.show_message(random.choice(messages))

def main():
    print("🌟 WELCOME TO VIRTUAL PET! 🌟")
    print("\nChoose your pet:")
    print("1. Cat 🐱")
    print("2. Dog 🐶")
    print("3. Bunny 🐰")
    print("4. Bear 🐻")
    print("5. Bird 🐦")
    
    shapes = {"1": "cat", "2": "dog", "3": "bunny", "4": "bear", "5": "bird"}
    choice = input("\nEnter number (1-5): ")
    shape = shapes.get(choice, "cat")
    
    name = input(f"Name your {shape}: ").strip()
    if not name:
        name = f"Pinky"
    
    pet = VirtualPet(shape, name)
    print(f"\n✨ {name} loves {pet.favorite_activity}!")
    print("\nControls:")
    print("F = Feed | C = Clean | P = Play | W = Wait | R = Restart | Q = Quit")
    
    game_over = False
    
    def feed_action():
        pet.feed()
        pet.pass_time()
        pet.display_status()
    
    def clean_action():
        pet.clean()
        pet.pass_time()
        pet.display_status()
    
    def play_action():
        pet.play()
        pet.pass_time()
        pet.display_status()
    
    def wait_action():
        pet.show_message("⏰ Time passes...")
        pet.pass_time()
        pet.display_status()
    
    def restart_action():
        pet.screen.bye()
        turtle.TurtleScreen._RUNNING = True
        main()
    
    def quit_action():
        pet.screen.bye()
    
    pet.screen.onkey(feed_action, "f")
    pet.screen.onkey(clean_action, "c")
    pet.screen.onkey(play_action, "p")
    pet.screen.onkey(wait_action, "w")
    pet.screen.onkey(restart_action, "r")
    pet.screen.onkey(quit_action, "q")
    pet.screen.listen()
    
    pet.display_status()
    
    pet.screen.mainloop()

if __name__ == "__main__":
    main()
