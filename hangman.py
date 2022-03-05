import pygame
import random

#setup display
pygame.init() # intilialize all imported pygame modules.
WIDTH,HEIGHT = 1000, 600
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Project")

#fonts
LETTER_FONT = pygame.font.SysFont('comicsansms', 40)
WORD_FONT = pygame.font.SysFont('comicsansms',50)
TITLE_FONT = pygame.font.SysFont('verdana',60)

#load images
images = []
for i in range(0,7):
    image = pygame.image.load("hangman"+ str(i) + ".png")
    images.append(image)

#button variables
BOX_WIDTH = 50
BOX_HEIGHT = 60
GAP = 15
letters = []
startx = round((WIDTH - (BOX_WIDTH + GAP) * 13)/2)
starty = 400
A = 65 #ASCII CODE
for i in range (0,26):
    x = startx + ((BOX_WIDTH + GAP) * (i % 13))
    y = starty + ((i //13) * (GAP + BOX_HEIGHT))
    letters.append([x, y, chr(A + i), True])

#game variables
hangman_status = 0
words = ["PYTHON", "HANGMAN", "VIDYALANKAR", "CODE" , "LAPTOP"]
word = random.choice(words)
guessed = []
bg=pygame.image.load("bgg.png")
hint = {'PYTHON':"Hint : A programming language", 'HANGMAN':"Hint : The game you are playing",
'VIDYALANKAR':"Hint : Your College", 'CODE':"Hint : What do you write in a programming language?" ,
'LAPTOP': "Hint : What do you use for practicals?"} #dictionary , key aur ek value 
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)



#setup game loop
FPS = 60 #Frames Per Second

clock = pygame.time.Clock()
run = True # boolean value T or F
def draw():
    win.fill(WHITE)
    win.blit(bg,(0,0))
    #draw title
    text = TITLE_FONT.render("Hangman Project", 1, '#DFFF00')
    win.blit(text, (WIDTH/2 - text.get_width()/2, 0))

    #draw word
    display_word = "" #local variable
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word , 1, BLACK)
    win.blit(text, (400, 200))
    h = hint[word]
    hints = LETTER_FONT.render(h , 1, '#DFFF00')
    win.blit(hints, (WIDTH/2 - hints.get_width()/2, HEIGHT - 70))


    #draw buttons
    for letter in letters:
        x,y,ltr, visible = letter #unpacking of variable 
        if visible:
            pygame.draw.rect(win, BLACK, (x , y , BOX_WIDTH, BOX_HEIGHT), 3)
            text = LETTER_FONT.render(ltr, 1, BLACK) #anti aliasing
            win.blit(text,(x + (BOX_WIDTH/2 - text.get_width()/2), y + (BOX_HEIGHT/2 - text.get_height()/2)))
    win.blit(images[hangman_status],(150,100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1500)
    win.blit(bg,(0,0))
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_width()/2))
    pygame.display.update()
    pygame.time.delay(3000)

while run:
    clock.tick(FPS)
    
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            for i,letter in enumerate(letters): 
                x, y, ltr, visible = letter
                if visible:
                    pos = pygame.mouse.get_pos()
                    box = pygame.Rect(x , y , BOX_WIDTH, BOX_HEIGHT)
                    if box.collidepoint(pos):
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status +=1
    draw()
    
    won = True
    for letter in word: #code
        if letter not in guessed:
            won = False 
            break
    if won:
        display_message("You Won")
        break

    if hangman_status == 6:
        display_message("You Lost")
        break
pygame.quit()