import turtle as t
import pandas as pd
from random import choice

class State_turtle(t.Turtle):
    
    def __init__ (self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_data = pd.read_csv('day25/50_states.csv')
        self.state_list = self.state_data['state'].to_list()
        self.create_screen()

        self.state_remaining = len(self.state_list)
        self.state_counter = t.Turtle()
        self.state_counter.hideturtle()
        self.state_counter.penup()
        self.state_counter.goto(x=0, y=280)

        self.help = t.Turtle()
        self.help.hideturtle()
        self.help.penup()
        self.help.goto(x=250, y=280)
        self.help.write('P for escape\nSPACE for random state')
        
    def create_screen(self):
        self.screen = t.Screen()
        self.screen.screensize(canvwidth=725, canvheight=491)
        self.screen.bgpic('day25/blank_states_img.gif')
        self.screen.listen()
        self.screen.tracer(0)

    def get_screen_events(self):
        self.screen.onkeypress(fun=self.place_state, key='space')
        self.screen.onkeypress(fun=self.screen.bye, key='p')

    def place_state(self):
        if self.state_remaining != 0:
            state = self.state_data[self.state_data.state == choice(self.state_list)].squeeze()
            self.state_list.remove(state.state)
            placed_state = t.Turtle()
            placed_state.hideturtle()
            placed_state.penup()
            placed_state.goto(x=state.x, y=state.y)
            placed_state.write(state.state)
            self.state_remaining = len(self.state_list)
            self.update_counter(message=self.state_remaining)
        else:
            self.update_counter(message='Finish !')
        self.screen.update()
    
    def update_counter(self, message):
        self.state_counter.clear()
        self.state_counter.write(message, align='center', font=('Arial', 15))

def main():
    writer = State_turtle()
    writer.get_screen_events()
    writer.screen.exitonclick()

if __name__ == '__main__':
    main()