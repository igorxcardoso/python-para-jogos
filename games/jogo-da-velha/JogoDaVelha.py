import pygame

class JogoDaVelha:

  def tabuleiro(self, window):
    pygame.draw.line(window, self.color['black'], (self.offset + 200, self.offset), (self.offset + 200, self.offset + 600), 9)
    pygame.draw.line(window, self.color['black'], (self.offset + 400, self.offset), (self.offset + 400, self.offset + 600), 9)
    pygame.draw.line(window, self.color['black'], (self.offset, self.offset + 200), (self.offset + 600, self.offset + 200), 9)
    pygame.draw.line(window, self.color['black'], (self.offset, self.offset + 400), (self.offset + 600, self.offset + 400), 9)
