import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
SEG_SIZE = 20
GAME_SPEED = 100  # lower = faster

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game - Tkinter")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.direction = "Right"
        self.running = True

        # Initial snake (3 segments)
        self.snake = [
            [100, 100],
            [80, 100],
            [60, 100]
        ]

        self.food = self.create_food()

        self.root.bind("<KeyPress>", self.change_direction)

        self.score = 0
        self.score_text = self.canvas.create_text(
            60, 10, fill="white", font=("Arial", 14),
            text=f"Score: {self.score}"
        )

        self.update_game()

    def create_food(self):
        x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
        return [x, y]

    def change_direction(self, event):
        key = event.keysym

        if key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Left":
            head_x -= SEG_SIZE
        elif self.direction == "Right":
            head_x += SEG_SIZE
        elif self.direction == "Up":
            head_y -= SEG_SIZE
        elif self.direction == "Down":
            head_y += SEG_SIZE

        new_head = [head_x, head_y]

        # Collision with walls
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT):
            self.game_over()
            return

        # Collision with self
        if new_head in self.snake:
            self.game_over()
            return

        self.snake.insert(0, new_head)

        # Eating food
        if new_head == self.food:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.food = self.create_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("snake")

        # Draw snake
        for i, segment in enumerate(self.snake):
            x, y = segment
            color = "lime" if i == 0 else "green"
            self.canvas.create_rectangle(
                x, y, x + SEG_SIZE, y + SEG_SIZE,
                fill=color, tags="snake"
            )

        # Draw food
        self.canvas.delete("food")
        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy, fx + SEG_SIZE, fy + SEG_SIZE,
            fill="red", tags="food"
        )

    def update_game(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.root.after(GAME_SPEED, self.update_game)

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            fill="white",
            font=("Arial", 24),
            text=f"GAME OVER\nScore: {self.score}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()