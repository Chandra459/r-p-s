'''import wx
import random

class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(400, 300))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Choose Rock, Paper, or Scissors")
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        rock_btn = wx.Button(panel, label="Rock")
        paper_btn = wx.Button(panel, label="Paper")
        scissors_btn = wx.Button(panel, label="Scissors")

        hbox.Add(rock_btn, flag=wx.ALL, border=10)
        hbox.Add(paper_btn, flag=wx.ALL, border=10)
        hbox.Add(scissors_btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)

        # Result labels
        self.comp_choice = wx.StaticText(panel, label="Computer chose: ")
        self.result = wx.StaticText(panel, label="Result: ")

        vbox.Add(self.comp_choice, flag=wx.ALIGN_CENTER|wx.TOP, border=20)
        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        panel.SetSizer(vbox)

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.comp_choice.SetLabel(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            result = "It's a Draw!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
        else:
            result = "You Lose!"

        self.result.SetLabel(f"Result: {result}")

if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()

import wx
import random
import winsound
class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(400, 350))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Choose Rock, Paper, or Scissors")
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        rock_btn = wx.Button(panel, label="Rock")
        paper_btn = wx.Button(panel, label="Paper")
        scissors_btn = wx.Button(panel, label="Scissors")

        hbox.Add(rock_btn, flag=wx.ALL, border=10)
        hbox.Add(paper_btn, flag=wx.ALL, border=10)
        hbox.Add(scissors_btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)

        # Result labels
        self.comp_choice = wx.StaticText(panel, label="Computer chose: ")
        self.result = wx.StaticText(panel, label="Result: ")

        vbox.Add(self.comp_choice, flag=wx.ALIGN_CENTER|wx.TOP, border=20)
        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        # Score labels
        self.player_score = 0
        self.computer_score = 0
        self.score_label = wx.StaticText(panel, label="Score - You: 0 | Computer: 0")
        vbox.Add(self.score_label, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        panel.SetSizer(vbox)

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.comp_choice.SetLabel(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            result = "It's a Draw!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.player_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        self.result.SetLabel(f"Result: {result}")
        self.score_label.SetLabel(f"Score - You: {self.player_score} | Computer: {self.computer_score}")

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                wx.MessageBox("🎉 You won the best of 3!", "Game Over")
            else:
                wx.MessageBox("😢 Computer won the best of 3!", "Game Over")
        if result == "You Win!":
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
        elif result == "You Lose!":
            winsound.PlaySound("lose.wav", winsound.SND_FILENAME)
        else:
            winsound.PlaySound("draw.wav", winsound.SND_FILENAME)
    
            # Reset scores for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("Score - You: 0 | Computer: 0")
            self.result.SetLabel("Result: ")
            self.comp_choice.SetLabel("Computer chose: ")

if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()

import wx
import random
import winsound

class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(500, 500))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Choose Rock, Paper, or Scissors")
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        rock_btn = wx.Button(panel, label="Rock")
        paper_btn = wx.Button(panel, label="Paper")
        scissors_btn = wx.Button(panel, label="Scissors")

        hbox.Add(rock_btn, flag=wx.ALL, border=10)
        hbox.Add(paper_btn, flag=wx.ALL, border=10)
        hbox.Add(scissors_btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)

        # Result labels
        self.comp_choice = wx.StaticText(panel, label="Computer chose: ")
        self.result = wx.StaticText(panel, label="Result: ")

        vbox.Add(self.comp_choice, flag=wx.ALIGN_CENTER|wx.TOP, border=20)
        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        # Score labels
        self.player_score = 0
        self.computer_score = 0
        self.score_label = wx.StaticText(panel, label="Score - You: 0 | Computer: 0")
        vbox.Add(self.score_label, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Images for player and computer
        img_box = wx.BoxSizer(wx.HORIZONTAL)

        # Player image + label
        player_vbox = wx.BoxSizer(wx.VERTICAL)
        self.player_image = wx.StaticBitmap(panel, bitmap=wx.Bitmap("rock.jpeg"))
        self.player_label = wx.StaticText(panel, label="You: Rock")
        player_vbox.Add(self.player_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        player_vbox.Add(self.player_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        # Computer image + label
        comp_vbox = wx.BoxSizer(wx.VERTICAL)
        self.computer_image = wx.StaticBitmap(panel, bitmap=wx.Bitmap("rock.jpeg"))
        self.computer_label = wx.StaticText(panel, label="Computer: Rock")
        comp_vbox.Add(self.computer_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        comp_vbox.Add(self.computer_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        img_box.Add(player_vbox, flag=wx.ALL, border=20)
        img_box.Add(comp_vbox, flag=wx.ALL, border=20)

        vbox.Add(img_box, flag=wx.ALIGN_CENTER)

        panel.SetSizer(vbox)

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.comp_choice.SetLabel(f"Computer chose: {computer_choice}")

        # Update images
        self.player_image.SetBitmap(wx.Bitmap(f"{player_choice.lower()}.jpeg"))
        self.player_label.SetLabel(f"You: {player_choice}")
        self.computer_image.SetBitmap(wx.Bitmap(f"{computer_choice.lower()}.jpeg"))
        self.computer_label.SetLabel(f"Computer: {computer_choice}")

        # Game logic
        if player_choice == computer_choice:
            result = "It's a Draw!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.player_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        self.result.SetLabel(f"Result: {result}")
        self.score_label.SetLabel(f"Score - You: {self.player_score} | Computer: {self.computer_score}")

        # Play sound
        if result == "You Win!":
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
        elif result == "You Lose!":
            winsound.PlaySound("lose.wav", winsound.SND_FILENAME)
        else:
            winsound.PlaySound("draw.wav", winsound.SND_FILENAME)

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                wx.MessageBox("🎉 You won the best of 3!", "Game Over")
            else:
                wx.MessageBox("😢 Computer won the best of 3!", "Game Over")

            # Reset scores for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("Score - You: 0 | Computer: 0")
            self.result.SetLabel("Result: ")
            self.comp_choice.SetLabel("Computer chose: ")
            self.player_label.SetLabel("You: ")
            self.computer_label.SetLabel("Computer: ")

if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()'''
'''
import wx
import random
import winsound

class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(500, 500))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title = wx.StaticText(panel, label="Choose Rock, Paper, or Scissors")
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        rock_btn = wx.Button(panel, label="Rock")
        paper_btn = wx.Button(panel, label="Paper")
        scissors_btn = wx.Button(panel, label="Scissors")

        hbox.Add(rock_btn, flag=wx.ALL, border=10)
        hbox.Add(paper_btn, flag=wx.ALL, border=10)
        hbox.Add(scissors_btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)

        # Result labels
        self.comp_choice = wx.StaticText(panel, label="Computer chose: ")
        self.result = wx.StaticText(panel, label="Result: ")

        vbox.Add(self.comp_choice, flag=wx.ALIGN_CENTER|wx.TOP, border=20)
        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        # Score labels
        self.player_score = 0
        self.computer_score = 0
        self.score_label = wx.StaticText(panel, label="Score - You: 0 | Computer: 0")
        vbox.Add(self.score_label, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Images for player and computer
        img_box = wx.BoxSizer(wx.HORIZONTAL)

        # Player image + label
        player_vbox = wx.BoxSizer(wx.VERTICAL)
        self.player_image = wx.StaticBitmap(panel, bitmap=self.load_image("rock.jpeg"))
        self.player_label = wx.StaticText(panel, label="You: Rock")
        player_vbox.Add(self.player_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        player_vbox.Add(self.player_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        # Computer image + label
        comp_vbox = wx.BoxSizer(wx.VERTICAL)
        self.computer_image = wx.StaticBitmap(panel, bitmap=self.load_image("rock.jpeg"))
        self.computer_label = wx.StaticText(panel, label="Computer: Rock")
        comp_vbox.Add(self.computer_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        comp_vbox.Add(self.computer_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        img_box.Add(player_vbox, flag=wx.ALL, border=20)
        img_box.Add(comp_vbox, flag=wx.ALL, border=20)

        vbox.Add(img_box, flag=wx.ALIGN_CENTER)

        panel.SetSizer(vbox)

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

    def load_image(self, filename, size=(100, 100)):
        """Helper to load and scale JPEG images safely"""
        img = wx.Image(filename, wx.BITMAP_TYPE_JPEG).Scale(size[0], size[1])
        return wx.Bitmap(img)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.comp_choice.SetLabel(f"Computer chose: {computer_choice}")

        # Update images with JPEGs
        self.player_image.SetBitmap(self.load_image(f"{player_choice.lower()}.jpeg"))
        self.player_label.SetLabel(f"You: {player_choice}")
        self.computer_image.SetBitmap(self.load_image(f"{computer_choice.lower()}.jpeg"))
        self.computer_label.SetLabel(f"Computer: {computer_choice}")

        # Game logic
        if player_choice == computer_choice:
            result = "It's a Draw!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.player_score += 1
        else:
            result = "You Lose!"
            self.computer_score += 1

        self.result.SetLabel(f"Result: {result}")
        self.score_label.SetLabel(f"Score - You: {self.player_score} | Computer: {self.computer_score}")

        # Play sound
        if result == "You Win!":
            winsound.PlaySound("win.wav", winsound.SND_FILENAME)
        elif result == "You Lose!":
            winsound.PlaySound("lose.wav", winsound.SND_FILENAME)
        else:
            winsound.PlaySound("draw.wav", winsound.SND_FILENAME)

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                wx.MessageBox("🎉 You won the best of 3!", "Game Over")
            else:
                wx.MessageBox("😢 Computer won the best of 3!", "Game Over")

            # Reset scores for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("Score - You: 0 | Computer: 0")
            self.result.SetLabel("Result: ")
            self.comp_choice.SetLabel("Computer chose: ")
            self.player_label.SetLabel("You: ")
            self.computer_label.SetLabel("Computer: ")
            self.player_image.SetBitmap(self.load_image("rock.jpeg"))
            self.computer_image.SetBitmap(self.load_image("rock.jpeg"))

if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()'''

'''

import wx
import random
import sys # Import sys for platform check

# --- Helper for Cross-Platform Sound ---
# winsound is Windows-only. Define a dummy function for other OS or remove it
def play_sound(filename):
    """Placeholder for sound playing for cross-platform compatibility."""
    # If running on Windows, we can use winsound, otherwise, do nothing.
    if sys.platform == 'win32':
        import winsound
        try:
            # SND_ASYNC is safer than SND_FILENAME for short sounds
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC) 
        except:
            # Fails silently if sound file is missing
            pass
    else:
        # Placeholder for other OS, or just pass
        pass

# Replace all calls to winsound.PlaySound in play() with play_sound()

class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(600, 650))
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(240, 248, 255)) # Light blue background
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 1. Title (Enhanced Font)
        title_font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title = wx.StaticText(panel, label="⚔️ Rock, Paper, Scissors! ✂️")
        title.SetFont(title_font)
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=25)

        # 2. Buttons (Styled)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # Define a consistent button style
        button_size = (150, 40)
        button_font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        rock_btn = wx.Button(panel, label="👊 ROCK", size=button_size)
        paper_btn = wx.Button(panel, label="✋ PAPER", size=button_size)
        scissors_btn = wx.Button(panel, label="✌️ SCISSORS", size=button_size)
        
        for btn in [rock_btn, paper_btn, scissors_btn]:
            btn.SetFont(button_font)
            hbox.Add(btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)
        
        # 3. Game Status (Using GridSizer for better alignment)
        # Score and result information will be placed here
        status_sizer = wx.GridSizer(rows=3, cols=2, vgap=10, hgap=10)
        
        # Labels setup
        status_font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        
        wx.StaticText(panel, label="Last Move:").SetFont(status_font)
        self.comp_choice = wx.StaticText(panel, label="Computer chose: ?")
        self.comp_choice.SetFont(status_font)
        
        wx.StaticText(panel, label="Outcome:").SetFont(status_font)
        self.result = wx.StaticText(panel, label="Result: Choose an option!")
        self.result.SetFont(status_font)
        self.result.SetForegroundColour(wx.RED) # Initial color

        wx.StaticText(panel, label="Current Score:").SetFont(status_font)
        self.score_label = wx.StaticText(panel, label="You: 0 | Computer: 0")
        self.score_label.SetFont(status_font)
        
        # Add labels to the GridSizer
        status_sizer.AddMany([
            (wx.StaticText(panel, label="Computer's Choice:"), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL),
            (self.comp_choice, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL),
            
            (wx.StaticText(panel, label="Result:"), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL),
            (self.result, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL),
            
            (wx.StaticText(panel, label="Score:"), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL),
            (self.score_label, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        ])

        vbox.Add(status_sizer, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=20)

        # 4. Images for player and computer
        img_box = wx.BoxSizer(wx.HORIZONTAL)
        image_label_font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Player image + label
        player_vbox = wx.BoxSizer(wx.VERTICAL)
        # Placeholder image load, assuming a 'default.jpeg' exists for robustness
        self.player_image = wx.StaticBitmap(panel, bitmap=self.load_image("rock.jpeg")) 
        self.player_label = wx.StaticText(panel, label="You: N/A")
        self.player_label.SetFont(image_label_font)
        player_vbox.Add(self.player_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        player_vbox.Add(self.player_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        # Separator for visual distinction
        separator = wx.StaticText(panel, label="VS")
        separator_font = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        separator.SetFont(separator_font)
        separator.SetForegroundColour(wx.Colour(0, 102, 204)) # Blue color

        # Computer image + label
        comp_vbox = wx.BoxSizer(wx.VERTICAL)
        self.computer_image = wx.StaticBitmap(panel, bitmap=self.load_image("rock.jpeg"))
        self.computer_label = wx.StaticText(panel, label="Computer: N/A")
        self.computer_label.SetFont(image_label_font)
        comp_vbox.Add(self.computer_image, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        comp_vbox.Add(self.computer_label, flag=wx.ALIGN_CENTER|wx.TOP, border=5)

        img_box.Add(player_vbox, flag=wx.ALL, border=20)
        img_box.Add(separator, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL, border=20)
        img_box.Add(comp_vbox, flag=wx.ALL, border=20)

        vbox.Add(img_box, flag=wx.ALIGN_CENTER)

        panel.SetSizer(vbox)
        vbox.Layout() # Ensure the new layout is applied

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

        # Score initialization
        self.player_score = 0
        self.computer_score = 0


    def load_image(self, filename, size=(150, 150)):
        """Helper to load and scale images safely. Use a default image if file not found."""
        try:
            # Use BITMAP_TYPE_ANY for better compatibility with different file types
            img = wx.Image(filename, wx.BITMAP_TYPE_ANY).Scale(size[0], size[1], wx.IMAGE_QUALITY_HIGH)
            return wx.Bitmap(img)
        except:
            # Create a simple colored placeholder if the file is missing
            print(f"Warning: Image file '{filename}' not found. Using placeholder.")
            img = wx.Image(size[0], size[1])
            img.SetRGB(wx.Rect(0, 0, size[0], size[1]), 128, 128, 128) # Grey rectangle
            return wx.Bitmap(img)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.comp_choice.SetLabel(f"Computer chose: {computer_choice}")

        # Update images and labels
        # Note: I've changed the expectation from ".jpeg" to a simple lowercase name,
        # but the actual file type should match what you provide.
        player_img_file = f"{player_choice.lower()}.jpeg"
        comp_img_file = f"{computer_choice.lower()}.jpeg"
        
        self.player_image.SetBitmap(self.load_image(player_img_file))
        self.player_label.SetLabel(f"You: {player_choice}")
        self.computer_image.SetBitmap(self.load_image(comp_img_file))
        self.computer_label.SetLabel(f"Computer: {computer_choice}")

        # Game logic
        if player_choice == computer_choice:
            result = "It's a DRAW!"
            color = wx.BLUE
            sound_file = "draw.wav"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "YOU WIN!"
            self.player_score += 1
            color = wx.Colour(34, 139, 34) # Forest Green
            sound_file = "win.wav"
        else:
            result = "YOU LOSE!"
            self.computer_score += 1
            color = wx.RED
            sound_file = "lose.wav"

        self.result.SetLabel(f"Result: {result}")
        self.result.SetForegroundColour(color) # Change color based on outcome
        self.score_label.SetLabel(f"You: {self.player_score} | Computer: {self.computer_score}")

        # Play sound using the cross-platform helper
        play_sound(sound_file)

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                final_msg = "🎉 You won the best of 3! Congratulations!"
            else:
                final_msg = "😢 Computer won the best of 3! Better luck next time."

            wx.MessageBox(final_msg, "Game Over")

            # Reset scores for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("You: 0 | Computer: 0")
            self.result.SetLabel("Result: Choose an option!")
            self.result.SetForegroundColour(wx.RED)
            self.comp_choice.SetLabel("Computer chose: ?")
            self.player_label.SetLabel("You: N/A")
            self.computer_label.SetLabel("Computer: N/A")
            # Reset images to a neutral state (e.g., rock)
            self.player_image.SetBitmap(self.load_image("rock.jpeg"))
            self.computer_image.SetBitmap(self.load_image("rock.jpeg"))


if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()'''
'''
import wx
import random
import winsound
import sys

# --- Helper for Cross-Platform Sound ---
def play_sound(filename):
    """Placeholder for sound playing for cross-platform compatibility."""
    if sys.platform == 'win32':
        try:
            # Use SND_ASYNC for safer, non-blocking playback
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC) 
        except:
            pass
    # For other OS, or if sound file is missing, we silently pass


class RPSFrame(wx.Frame):
    def __init__(self):
        # Increased size slightly for better spacing without images
        super().__init__(None, title="Rock Paper Scissors", size=(550, 450))
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(240, 248, 255)) # Light blue background
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Define common fonts for better appearance
        title_font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        status_font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        score_font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # 1. Title
        title = wx.StaticText(panel, label="⚔️ Rock, Paper, Scissors! ✂️")
        title.SetFont(title_font)
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=25)

        # 2. Buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        button_size = (150, 40)
        rock_btn = wx.Button(panel, label="👊 ROCK", size=button_size)
        paper_btn = wx.Button(panel, label="✋ PAPER", size=button_size)
        scissors_btn = wx.Button(panel, label="✌️ SCISSORS", size=button_size)

        for btn in [rock_btn, paper_btn, scissors_btn]:
            btn.SetFont(status_font)
            hbox.Add(btn, flag=wx.ALL, border=10)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)
        
        # 3. Game Choices (Replaces Images)
        # Use a GridSizer for neat alignment of player's and computer's choices
        choices_grid = wx.GridSizer(rows=2, cols=2, vgap=10, hgap=20)
        
        # Player Choice Label
        player_choice_label = wx.StaticText(panel, label="Your Move:")
        player_choice_label.SetFont(status_font)
        self.player_choice_text = wx.StaticText(panel, label="?")
        self.player_choice_text.SetFont(score_font)
        self.player_choice_text.SetForegroundColour(wx.Colour(0, 102, 204)) # Blue

        # Computer Choice Label
        comp_choice_label = wx.StaticText(panel, label="Computer's Move:")
        comp_choice_label.SetFont(status_font)
        self.comp_choice_text = wx.StaticText(panel, label="?")
        self.comp_choice_text.SetFont(score_font)
        self.comp_choice_text.SetForegroundColour(wx.Colour(204, 102, 0)) # Orange
        
        choices_grid.Add(player_choice_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(self.player_choice_text, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(comp_choice_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(self.comp_choice_text, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        
        vbox.Add(choices_grid, flag=wx.ALIGN_CENTER | wx.TOP, border=20)


        # 4. Result and Score
        self.result = wx.StaticText(panel, label="Result: Choose an option!")
        self.result.SetFont(score_font)
        self.result.SetForegroundColour(wx.RED)

        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        # Score labels
        self.player_score = 0
        self.computer_score = 0
        self.score_label = wx.StaticText(panel, label="Score - You: 0 | Computer: 0")
        self.score_label.SetFont(score_font)
        vbox.Add(self.score_label, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        
        panel.SetSizer(vbox)
        vbox.Layout()

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock"))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper"))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors"))

    # Removed load_image method entirely

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        # Update choice text labels (replaces image update)
        self.player_choice_text.SetLabel(player_choice)
        self.comp_choice_text.SetLabel(computer_choice)

        # Game logic
        if player_choice == computer_choice:
            result = "It's a DRAW!"
            color = wx.BLUE
            sound_file = "draw.wav"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "YOU WIN!"
            self.player_score += 1
            color = wx.Colour(34, 139, 34) # Forest Green
            sound_file = "win.wav"
        else:
            result = "YOU LOSE!"
            self.computer_score += 1
            color = wx.RED
            sound_file = "lose.wav"

        self.result.SetLabel(f"Result: {result}")
        self.result.SetForegroundColour(color) # Change color based on outcome
        self.score_label.SetLabel(f"Score - You: {self.player_score} | Computer: {self.computer_score}")

        # Play sound
        play_sound(sound_file)

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                final_msg = "🎉 You won the best of 3! Congratulations!"
            else:
                final_msg = "😢 Computer won the best of 3! Better luck next time."

            wx.MessageBox(final_msg, "Game Over")

            # Reset scores and labels for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("Score - You: 0 | Computer: 0")
            self.result.SetLabel("Result: Choose an option!")
            self.result.SetForegroundColour(wx.RED)
            self.player_choice_text.SetLabel("?")
            self.comp_choice_text.SetLabel("?")


if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()
    '''

import wx
import random
import winsound
import sys

# --- Helper for Cross-Platform Sound ---
def play_sound(filename):
    """Placeholder for sound playing for cross-platform compatibility."""
    if sys.platform == 'win32':
        try:
            # Use SND_ASYNC for safer, non-blocking playback
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC) 
        except:
            pass

class RPSFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Rock Paper Scissors", size=(550, 450))
        
        # --- Interactive Panel Setup ---
        panel = wx.Panel(self)
        # New: Set a slightly darker/more interactive background color
        self.default_panel_color = wx.Colour(220, 230, 240) # Light Slate Blue
        panel.SetBackgroundColour(self.default_panel_color) 
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Define common fonts and colors
        title_font = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        status_font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        score_font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        
        # Button Colors
        self.default_btn_color = wx.Colour(255, 255, 255) # White
        self.hover_btn_color = wx.Colour(173, 216, 230)   # Light Blue for hover
        self.click_btn_color = wx.Colour(144, 238, 144)   # Light Green for click

        # 1. Title
        title = wx.StaticText(panel, label="⚔️ Rock, Paper, Scissors! ✂️")
        title.SetFont(title_font)
        vbox.Add(title, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=25)

        # 2. Buttons (with Interactivity)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        button_size = (150, 40)
        rock_btn = wx.Button(panel, label="👊 ROCK", size=button_size)
        paper_btn = wx.Button(panel, label="✋ PAPER", size=button_size)
        scissors_btn = wx.Button(panel, label="✌️ SCISSORS", size=button_size)

        for btn in [rock_btn, paper_btn, scissors_btn]:
            btn.SetFont(status_font)
            btn.SetBackgroundColour(self.default_btn_color)
            hbox.Add(btn, flag=wx.ALL, border=10)
            
            # --- Bind Hover Events ---
            btn.Bind(wx.EVT_ENTER_WINDOW, self.on_button_hover)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_button_leave)

        vbox.Add(hbox, flag=wx.ALIGN_CENTER)
        
        # 3. Game Choices 
        choices_grid = wx.GridSizer(rows=2, cols=2, vgap=10, hgap=20)
        
        player_choice_label = wx.StaticText(panel, label="Your Move:")
        player_choice_label.SetFont(status_font)
        self.player_choice_text = wx.StaticText(panel, label="?")
        self.player_choice_text.SetFont(score_font)
        self.player_choice_text.SetForegroundColour(wx.Colour(0, 102, 204)) # Blue

        comp_choice_label = wx.StaticText(panel, label="Computer's Move:")
        comp_choice_label.SetFont(status_font)
        self.comp_choice_text = wx.StaticText(panel, label="?")
        self.comp_choice_text.SetFont(score_font)
        self.comp_choice_text.SetForegroundColour(wx.Colour(204, 102, 0)) # Orange
        
        choices_grid.Add(player_choice_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(self.player_choice_text, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(comp_choice_label, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        choices_grid.Add(self.comp_choice_text, 0, wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        
        vbox.Add(choices_grid, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        # 4. Result and Score
        self.result = wx.StaticText(panel, label="Result: Choose an option!")
        self.result.SetFont(score_font)
        self.result.SetForegroundColour(wx.RED)

        vbox.Add(self.result, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        self.player_score = 0
        self.computer_score = 0
        self.score_label = wx.StaticText(panel, label="Score - You: 0 | Computer: 0")
        self.score_label.SetFont(score_font)
        vbox.Add(self.score_label, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        
        panel.SetSizer(vbox)
        vbox.Layout()

        # Bind events
        rock_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Rock", evt.GetEventObject()))
        paper_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Paper", evt.GetEventObject()))
        scissors_btn.Bind(wx.EVT_BUTTON, lambda evt: self.play("Scissors", evt.GetEventObject()))

    # --- Button Interactivity Methods ---
    def on_button_hover(self, event):
        """Changes button color when mouse enters."""
        button = event.GetEventObject()
        button.SetBackgroundColour(self.hover_btn_color)
        button.Refresh()

    def on_button_leave(self, event):
        """Reverts button color when mouse leaves."""
        button = event.GetEventObject()
        button.SetBackgroundColour(self.default_btn_color)
        button.Refresh()

    def on_button_click_feedback(self, button):
        """Temporarily changes button color after click for feedback."""
        original_color = self.default_btn_color
        
        # Change to click color
        button.SetBackgroundColour(self.click_btn_color)
        button.Refresh()
        
        # Use wx.CallLater to revert the color after 100 milliseconds
        wx.CallLater(100, button.SetBackgroundColour, original_color)
        wx.CallLater(100, button.Refresh)
    # ------------------------------------

    def play(self, player_choice, clicked_button):
        # Trigger the visual click feedback
        self.on_button_click_feedback(clicked_button)
        
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        self.player_choice_text.SetLabel(player_choice)
        self.comp_choice_text.SetLabel(computer_choice)

        # Game logic
        if player_choice == computer_choice:
            result = "It's a DRAW!"
            color = wx.BLUE
            sound_file = "draw.wav"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "YOU WIN!"
            self.player_score += 1
            color = wx.Colour(34, 139, 34) # Forest Green
            sound_file = "win.wav"
        else:
            result = "YOU LOSE!"
            self.computer_score += 1
            color = wx.RED
            sound_file = "lose.wav"

        self.result.SetLabel(f"Result: {result}")
        self.result.SetForegroundColour(color)
        self.score_label.SetLabel(f"Score - You: {self.player_score} | Computer: {self.computer_score}")

        play_sound(sound_file)

        # Check best of 3
        if self.player_score == 2 or self.computer_score == 2:
            if self.player_score > self.computer_score:
                final_msg = "🎉 You won the best of 3! Congratulations!"
            else:
                final_msg = "😢 Computer won the best of 3! Better luck next time."

            wx.MessageBox(final_msg, "Game Over")

            # Reset scores and labels for new round
            self.player_score = 0
            self.computer_score = 0
            self.score_label.SetLabel("Score - You: 0 | Computer: 0")
            self.result.SetLabel("Result: Choose an option!")
            self.result.SetForegroundColour(wx.RED)
            self.player_choice_text.SetLabel("?")
            self.comp_choice_text.SetLabel("?")


if __name__ == "__main__":
    app = wx.App(False)
    frame = RPSFrame()
    frame.Show()
    app.MainLoop()     
    
