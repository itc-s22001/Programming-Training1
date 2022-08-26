class Block:
    def __init__(self, canvas, color):
    
        self.canvas = canvas
        #self.id = self.canvas.create_rectangle(420, 7, 40, 25, fill=color)
        self.id = self.canvas.create_rectangle(350, 110, 100, 50, fill=color)

    def delete(self):
        self.canvas.delete(self.block.id)

    def start(self, evt):
        if self.speed != 0:
            return
        self.canvas.create_rectangle(350, 110, 100, 50, fill=color)

    #def blockout(self, canvas):
     #   self.canvas = canvas
     #   self.canvas.dalete(self.block.id)

    def revive(self, color):
        self.id = self.canvas.create_rectangle(1000,3000, 5000, 2000, fill=color)
        


