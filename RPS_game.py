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
    
