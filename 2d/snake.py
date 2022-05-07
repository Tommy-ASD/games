from pickle import FALSE
import random
import time
import os
import keyboard


class snake:
    def __init__(self):
        pass


class template:
    def __init__(self):
        self.length = 10
        self.height = 10
        self.spaces = self.height * self.length
        self.movement = 0
        self.alive = True
        self.field = []
        self.snakePartData = {"position": 0}
        self.snake = [self.snakePartData.copy()]
        self.fieldData = {"state": ".", "neighbors": 0}

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def generateObject(self):
        index = random.randrange(0, self.spaces)
        # if object position is a part of the snake, choose new position
        if self.field[index]["state"] == "▮":
            return self.generateObject()
        self.field[index]["state"] = "b"
        self.objectPosition = index

    def viewField(self):
        os.system("cls")
        currentX = 0
        msg = ""
        for i in range(self.spaces):
            currentX += 1
            msg += self.field[i]["state"]
            msg += " "
            # if current x is length, jump to next y
            if currentX % self.length == 0:
                msg += "\n"
                currentX = 0
        print(msg)

    def convertToIndex(self, x, y):
        # input y: 10
        # output y: 9 * length
        adjustedY = (y - 1) * self.length
        adjustedX = x - 1
        index = adjustedX + adjustedY
        return index

    def move(self):
        selfPos = self.snake[0]["position"]
        match self.movement:
            # Case 0: down
            case 0:
                move = self.length
                nextPosition = selfPos + move
                # same as previous, except index + length is exactly the one below
                if not nextPosition < self.spaces:
                    self.alive = False
            # Case 1: right
            case 1:
                move = 1
                nextPosition = selfPos + move
                if selfPos % self.length == self.length - 1:
                    self.alive = False
            # Case 2: left
            case 2:
                move = -1
                nextPosition = selfPos + move
                if selfPos % self.length == 0:
                    self.alive = False
            # Case 3: up
            case 3:
                move = -self.length
                nextPosition = selfPos + move
                # index - (-length) is the one exactly below
                if not nextPosition >= 0:
                    self.alive = False
        if self.alive:
            self.field[selfPos]["state"] = "."
            self.moveChildren(1)
            self.snake[0]["position"] += move
            selfPos = self.snake[0]["position"]
            if self.field[selfPos]["state"] == "▮":
                self.alive = False
            self.field[selfPos]["state"] = "▮"
            if selfPos == self.objectPosition:
                self.snake.append(self.snakePartData.copy())
                self.snake[-1]["position"] = self.snake[-2]["position"] - 1
                self.generateObject()

            time.sleep(0.1)

    def moveChildren(self, index):
        if index < len(self.snake):
            self.field[self.snake[index]["position"]]["state"] = "."
            self.moveChildren(index + 1)
            self.snake[index]["position"] = self.snake[index - 1]["position"]
            self.field[self.snake[index]["position"]]["state"] = "▮"


def index_in_list(a_list, index):
    return index < len(a_list)


while True:
    input()
    temp = template()
    temp.createField()
    temp.generateObject()
    temp.viewField()
    while temp.alive:
        temp.move()
        temp.viewField()
        if keyboard.is_pressed("s"):
            temp.movement = 0
        if keyboard.is_pressed("d"):
            temp.movement = 1
        if keyboard.is_pressed("a"):
            temp.movement = 2
        if keyboard.is_pressed("w"):
            temp.movement = 3
        if keyboard.is_pressed("q"):
            temp.snake.append(temp.snakePartData.copy())

    print("died")
