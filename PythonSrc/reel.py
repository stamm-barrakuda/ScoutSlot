import pygame


class Reel:
    def __init__(self, screen, card_size, x):
        self.card_size = card_size
        self.reel_position = 0
        self.screen = screen
        reel = []
        for i in range(0, 3):
            curr = pygame.image.load("../cards200x300/pic" + str(i) + ".png")
            curr_rect = curr.get_rect()
            if curr_rect.size != card_size:
                raise Exception("wrong image format", "../cards200x300/pic" + str(i) + ".png has the wrong format")
            curr_rect = curr_rect.move((x, -curr_rect.height * i))
            card_id = str(i+1)
            reel.append([curr, curr_rect, card_id])
        self.reel = reel
        self.move(card_size[1] * 5)
        print(self.reel[self.reel_position][2])

    def get_current_id(self):
        return self.reel[self.reel_position][2]

    def get_current_rect(self):
        return self.reel[self.reel_position][1]

    def draw(self):
        for curr in self.reel:
            self.screen.blit(curr[0], curr[1])

    def move(self, y):
        if y > self.reel[0][1].height:  # if a move is longer than 1 card_size split it up to several moves
            for _ in range(1, y // self.card_size[1]):
                self.move(self.card_size[1])
            self.move(y % self.card_size[1])
            return
        for curr in self.reel:
            curr[1].move_ip((0, y))
        reel_position_rect = (self.reel[self.reel_position])[1]
        if reel_position_rect.bottomleft[1] > self.card_size[1] * 2:  # if self.reel_position leaves screen

            self.reel_position = (self.reel_position + 1) % len(self.reel)  # update reel Position
            reel_position_rect = (self.reel[self.reel_position])[1]
            new_position = reel_position_rect.topleft[1] - self.card_size[1]  # determine where the 2nd reel
            # after the current reel position at the beginning has to be placed to make the reel goes round and round
            move_position_rect = (self.reel[(self.reel_position + 1) % len(self.reel)])[1]
            move_position_rect.y = new_position  # place the 2nd reel
