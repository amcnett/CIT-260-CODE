# simple ball catching game
# can you fix the errors?

import tkinter as tk
import random

class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        
        self.paddle = self.canvas.create_rectangle(170, 380, 230, 390, fill="blue")
        self.ball = self.canvas.create_oval(190, 10, 210, 30, fill="red")
        
        self.dx = 0  # Paddle movement
        self.dy = 0  # Ball speed
        
        score = 0
        
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        self.update_ball()

    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
    
    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
    
    def update_ball(self):
        self.canvas.move(self.ball, 0, 0)
        ball_coords = self.canvas.coords(self.ball)

        
        if ball_coords[3] >= 400:
            self.check_collision(ball_coords)
        
        self.root.after(50, self.update_ball)

    def check_collision(self, ball_coords):
        paddle_coords = self.canvas.coords(self.paddle)
        
        if paddle_coords[0] <= ball_coords[0] <= paddle_coords[2] or paddle_coords[0] <= ball_coords[2] <= paddle_coords[2]:
            self.score += 1
            print(f"Score: {self.score}")
            # would be nice if this printed to the GUI instead... label maybe!
        else:
            print("Game Over!")
            self.root.quit()
        
        self.canvas.coords(self.ball, random.randint(10, 390), 10, random.randint(30, 390), 30)

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheBallGame(root)
    root.mainloop()
