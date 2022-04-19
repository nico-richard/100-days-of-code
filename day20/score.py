import turtle as t

class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color('white')
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f'Score : {self.score}', font=('Arial', 15), align='center')

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(x=00, y=0)
        self.write('GAME OVER !', font=('Arial', 20), align='center')