import random
import math


class Ball:
    def __init__(self, canvas, color, paddle, block):
        self.canvas = canvas
        self.paddle = paddle
        self.block = block
        
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5

        self.speed = 0

        self.x = 0
        self.y = 0
         
        
    def start(self, evt):
        if self.speed != 0:
            return
                   
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 5
        
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])
        
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
        self.canvas.delete('text')
    
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)

        if pos[1] <= 0:
            self.fix(0, pos[1])

        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)

        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()

        paddle_pos = self.canvas.coords(self.paddle.id)
        
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])

        block_pos = self.canvas.coords(self.block.id)
            

        if pos[1] <= block_pos[3] and pos[0] <= block_pos[2] \
           and pos[2] >= block_pos[0] and pos[3] >= block_pos[1]:
            self.canvas.delete(self.block.id)
            self.block.revive('red')
            self.out()
            if pos[0] <= block_pos[2] and pos[0] >= block_pos[0]:
                self.x = -self.x
                #self.revive()
                #self.canvas.delete(self.block.id)
                #self.out()
            if pos[1] <= block_pos[3] and pos[1] >= block_pos[1]:
                self.y = -self.y
                #self.revive()
                #self.canvas.delete(self.block.id)
                #self.out()
            if pos[2] >= block_pos[0] and pos[2] <= block_pos[2]:
                self.x = -self.x
                #self.revive()
                #self.canvas.delete(self.block.id)
                #self.out()
            if pos[3] >= block_pos[1] and pos[3] <= block_pos[3]:
                self.y = -self.y
                #self.revive()
                #self.canvas.delete(self.block.id)
                #self.out()
                
                
            
                


                

    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2),  -(diff_y * 2))

        if diff_x != 0:
            self.x = -self.x

        if diff_y != 0:
            self.y = -self.y

    def failed(self):   
        self.x = 0
        self.y = 0
        self.speed = 0
        #self.canvas.delete("all")
        #self.createObjects()
        self.canvas.create_text(250, 200, text = "Game over", font= ("", 40), fill="violet", tag='text')

    
        
    def out(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.canvas.create_text(250, 200, text = "YOU WIN", font= ("", 40), fill="blue", tag='text')
    
        
             
            


        
        
