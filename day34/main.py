import tkinter as tk
import html
import requests

class Quizz:

    def __init__(self):
        self.CANVAS_COLOR = '#FAFDD6'
        self.BACKGROUND_COLOR = '#CDB699'
        self.WRONG_COLOR = '#FF0000'
        self.RIGHT_COLOR = '#49FF00'
        self.TEXT_COLOR = '#505050'
        self.QUESTION_FONT = ('Ariel', 20, 'bold')
        self.SCORE_FONT = ('Ariel', 15, 'bold')
        self.question_answer = None
        self.score = 0
        self.trivia_params = {
            'amount': 1,
            'category': 17,
            # 'difficulty': 'easy',
            'type': 'boolean'
        }
        self.trivia_db_url = 'https://opentdb.com/api.php'
        self._window_setup()

    def _window_setup(self):
        self.window = tk.Tk()
        self.window.title('Trivia Quizz')
        self.window.config(bg=self.BACKGROUND_COLOR)
        self._widget_setup()
        self.question_answer = self.get_question()

    def _widget_setup(self):
        self.canvas = tk.Canvas(bg=self.CANVAS_COLOR, width=500, height=300, highlightbackground=self.BACKGROUND_COLOR, highlightthickness=10)
        self.question = self.canvas.create_text(self.canvas.winfo_reqwidth() / 2, self.canvas.winfo_reqheight() / 2,
            text='Question ?', width=self.canvas.winfo_reqwidth() - 30, font=self.QUESTION_FONT, fill=self.TEXT_COLOR,
            justify='center')
        
        self.right_image = tk.PhotoImage(file='day34/images/right.png')
        self.wrong_image = tk.PhotoImage(file='day34/images/wrong.png')
        self.right_button = tk.Button(image=self.right_image, width=70, height=90, relief='flat',
            bg=self.BACKGROUND_COLOR, activebackground=self.BACKGROUND_COLOR, highlightthickness=0, command=self.right_answer)
        self.wrong_button = tk.Button(image=self.wrong_image, width=70, height=90, relief='flat',
            bg=self.BACKGROUND_COLOR, activebackground=self.BACKGROUND_COLOR, highlightthickness=0, command=self.wrong_answer)
        self.score_label = tk.Label(text=f'Score : {self.score}', bg=self.BACKGROUND_COLOR, fg=self.TEXT_COLOR, font=self.SCORE_FONT)
        self._grid_placement()

    def _grid_placement(self):
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.right_button.grid(row=1, column=2)
        self.wrong_button.grid(row=1, column=0)
        self.score_label.grid(row=1, column=1)

    def get_question(self):
        response = requests.get(url=self.trivia_db_url, params=self.trivia_params)
        data = response.json()
        answer = data['results'][0]['correct_answer']
        # question = html.unescape(data['results'][0]['question']) + '\n(Answer : ' + answer + ')'
        question = html.unescape(data['results'][0]['question'])
        self.canvas.itemconfig(self.question, text=question)
        return answer

    def right_answer(self):
        if self.question_answer == 'True':
            self.update_score()
            self.canvas.config(highlightbackground=self.RIGHT_COLOR, highlightthickness=10)
        else:
            self.canvas.config(highlightbackground=self.WRONG_COLOR, highlightthickness=10)

        self.window.after(1000, self.update_canvas)
        self.question_answer = self.get_question()

    def wrong_answer(self):
        if self.question_answer == 'False':
            self.update_score()
            self.canvas.config(highlightbackground=self.RIGHT_COLOR, highlightthickness=10)

        else:
            self.canvas.config(highlightbackground=self.WRONG_COLOR, highlightthickness=10)

        self.window.after(1000, self.update_canvas)
        self.question_answer = self.get_question()

    def update_canvas(self):
        self.canvas.config(highlightbackground=self.BACKGROUND_COLOR, highlightthickness=10)

    def update_score(self):
        self.score += 1
        self.score_label.config(text=f'Score : {self.score}')

    def mainloop(self):
        self.window.mainloop()

def main():
    quizz = Quizz()
    quizz.mainloop()

if __name__ == '__main__':
    main()