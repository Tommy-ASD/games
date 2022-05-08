from pickle import FALSE
import random
import time
import os
import keyboard


class snake:
    def __init__(self):
        self.length = 25
        self.height = 25
        self.spaces = self.height * self.length
        # need a default movement (in this case, down)
        self.movement = 0
        self.alive = True
        self.field = []
        self.snakePartData = {"position": 0}
        self.snake = [self.snakePartData.copy()]

        self.objectDisplay = "a"
        self.snakeDisplay = "▮"
        self.emptySpaceDisplay = "."
        self.fieldData = {"state": self.emptySpaceDisplay, "neighbors": 0}
        self.createField()
        self.generateObject()
        self.viewField()

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def generateObject(self):
        index = random.randrange(0, self.spaces)
        # if object position is a part of the snake, choose new position
        if self.field[index]["state"] == self.snakeDisplay:
            return self.generateObject()
        self.field[index]["state"] = self.objectDisplay
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
        return msg

    def move(self):
        # just to make stuff look better
        selfPos = self.snake[0]["position"]
        match self.movement:
            # Case 0: down
            case 0:
                move = self.length
                nextPosition = selfPos + move
                # if nothing below (if at bottom of screen and going downwards), die
                if not nextPosition < self.spaces:
                    self.alive = False
            # Case 1: right
            case 1:
                move = 1
                nextPosition = selfPos + move
                # if nothing to the right (if at far right side of screen and going right), die
                if selfPos % self.length == self.length - 1:
                    self.alive = False
            # Case 2: left
            case 2:
                move = -1
                # if nothing to the left (if at far left side of screen and going left), die
                nextPosition = selfPos + move
                if selfPos % self.length == 0:
                    self.alive = False
            # Case 3: up
            case 3:
                move = -self.length
                nextPosition = selfPos + move
                # if nothing above (if at top of screen and going upwards), die
                if not nextPosition >= 0:
                    self.alive = False
        # to avoid breaking stuff, add if self.alive
        if self.alive:
            self.field[selfPos]["state"] = self.emptySpaceDisplay
            self.moveChildren(1)
            self.snake[0]["position"] += move
            selfPos = self.snake[0]["position"]
            # need to check if next position is part of snake before making it part of snake
            # if it is, die
            if self.field[selfPos]["state"] == self.snakeDisplay:
                self.alive = False
            # if not, make next position part of snake
            self.field[selfPos]["state"] = self.snakeDisplay
            # if current position is object
            if selfPos == self.objectPosition:
                self.snake.append(self.snakePartData.copy())
                self.generateObject()

            time.sleep(0.1)

    def moveChildren(self, index):
        # if snake is this long
        if index < len(self.snake):
            self.field[self.snake[index]["position"]]["state"] = self.emptySpaceDisplay
            # move children to own position before moving to next position
            self.moveChildren(index + 1)
            # self.snake[1] takes the old position of self.snake[0]
            # all after that take the old position of the one before
            self.snake[index]["position"] = self.snake[index - 1]["position"]
            # move self
            self.field[self.snake[index]["position"]]["state"] = self.snakeDisplay

    def main(self):
        return


def main():
    while True:
        input()
        temp = snake()
        while temp.alive:
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
            temp.move()
            temp.viewField()
        print("died")


main()
