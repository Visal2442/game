
#============================ IMPORTS ============================
from tkinter import *
from PIL import ImageTk, Image
# import winsound


#============================ CONSTANTS ============================
WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
EMPTY_CELL=0
WALL_CELL=1
PLAYER1_CELL=2
PLAYER2_CELL=12
CARROT_CELL=4
MANGO_CELL=5
WATERMELON_CELL=6
APPLE_CELL=7
VIRUS1_CELL=8
VIRUS2_CELL=9
KEY_CELL=10
DOOR_CELL=11
ALCOHOL_CELL=20


#============================ GLOBAL ============================
isLevel=False
isLose=False
isVirus=True
score=0
countAlcohol=0
countKey=0
player=0
time= 90
countVirus=15


#============================ MAIN WINDOW ============================
root=Tk()
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.title("Forest Home")
frame=Frame()
canvas=Canvas(frame)


#============================ IMAGES ============================
bg=PhotoImage(file="IMAGE/game_bg.png")
bg_winter=PhotoImage(file="IMAGE/bg_winter.png")
bg_halloween=PhotoImage(file="IMAGE/bbh.png")
bg_lose=PhotoImage(file="IMAGE/bg_lose.png")
home_bg=PhotoImage(file="IMAGE/home_bg.png")
player1_img=PhotoImage(file="IMAGE/player1.png")
player1_small_img=PhotoImage(file="IMAGE/player1_copy.png")
player2_img=PhotoImage(file="IMAGE/player2.png")
player2_small_img=PhotoImage(file="IMAGE/player2_copy.png")
virus1_img=PhotoImage(file="IMAGE/virus1.png")
virus2_img=PhotoImage(file="IMAGE/virus1.png")
virus1_big_img=PhotoImage(file="IMAGE/virus1_copy.png")
banana_img=PhotoImage(file="IMAGE/banana.png")
carrot_img=PhotoImage(file="IMAGE/carrot.png")
apple_img=PhotoImage(file="IMAGE/apple.png")
wm_img=PhotoImage(file="IMAGE/wm.png")
mango_img=PhotoImage(file="IMAGE/mango.png")
wall_img=PhotoImage(file="IMAGE/wall.gif")
wall2_img=PhotoImage(file="IMAGE/wall2.gif")
board_img=PhotoImage(file="IMAGE/board.png")
game_win_img=PhotoImage(file="IMAGE/game_win.png")
game_lose_img=PhotoImage(file="IMAGE/game_lose.png")
board_level_img=PhotoImage(file="IMAGE/level.png")
start_img=PhotoImage(file="IMAGE/start.png")
help_img=PhotoImage(file="IMAGE/help.png")
exit_img=PhotoImage(file="IMAGE/exit.png")
key_img=PhotoImage(file="IMAGE/key.png")
door_img=PhotoImage(file="IMAGE/door.gif")
alcohol_img=PhotoImage(file="IMAGE/alcohol.png")
alcohol_small_img=PhotoImage(file="IMAGE/alcohol_copy.png")
introduction_img=PhotoImage(file="IMAGE/introduction.png")
check=PhotoImage(file="IMAGE/accept.png")
back_img=PhotoImage(file="IMAGE/back.png")
next_img=PhotoImage(file="IMAGE/next.png")


#=========================== ALL GRID LEVELS =======================

# DEFAULT VALUE BEFORE START GAME
def default():
    global isLevel, score, countAlcohol, player
    grid[1][1] = player
    isLevel=True
    score=0
    countAlcohol=0

#LEVEL 1
def level1(event):
    global grid, countVirus, img
    grid=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 5, 0, 0, 0, 0, 20, 0, 4, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 5, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 20, 0, 0, 0, 20, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 20, 1, 4, 1, 5, 1, 0, 1, 0, 7, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 0, 0, 0, 1, 20, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 7, 0, 0, 1, 0, 7, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 5, 0, 0, 0, 9, 1],
    [1, 0, 1, 0, 7, 1, 0, 1, 20, 1, 0, 7, 1, 1, 1, 1, 6, 1, 7, 1, 1, 1, 20, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 20, 1, 1, 20, 1, 9, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 20, 1, 0, 1, 0, 1, 4, 0, 7, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 20, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 8, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 9, 1, 20, 0, 0, 1, 0, 1, 6, 0, 0, 0, 9, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 7, 1, 0, 1, 1, 1, 1, 6, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 7, 1, 0, 1],
    [1, 0, 1, 7, 0, 1, 0, 1, 0, 8, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 6, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 4, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 4, 0, 0, 0, 1, 9, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 7, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 4, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 20, 1, 0, 0, 0, 0, 1, 20, 1, 0, 0, 1, 10, 0, 6, 1, 4, 1, 6, 1, 0, 7, 1, 0, 20, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 20, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 20, 1, 0, 0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 11, 0, 8, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 7, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 20, 0, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 6, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    countVirus=10
    img=bg
    default()
    arrayDrawing()
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    
    
#LEVEL 2
def level2(event):
    global grid, countVirus, img
    grid=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 6, 1, 9, 0, 0, 0, 7, 0, 0, 0, 20, 0, 0, 0, 5, 0, 0, 0, 8, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 20, 1, 0, 1, 0, 1, 8, 0, 0, 7, 0, 0, 20, 0, 0, 6, 0, 0, 20, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 20, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 4, 1, 4, 1, 0, 1, 20, 0, 0, 0, 0, 0, 0, 1, 20, 1, 0, 1, 20, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 9, 1, 0, 1, 0, 1, 4, 1],
        [1, 0, 1, 4, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 20, 1, 0, 1, 0, 1, 20, 0, 1, 0, 1, 20, 1, 0, 0, 1, 0, 1, 7, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 7, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 20, 8, 0, 1, 0, 0, 5, 0, 0, 1, 0, 0, 6, 0, 0, 0, 8, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 5, 0, 7, 0, 1],
        [1, 6, 0, 1, 0, 7, 0, 0, 1, 0, 0, 7, 0, 0, 1, 6, 1, 1, 1, 1, 8, 1, 1, 0, 1, 1, 20, 1, 9, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 20, 1, 0, 0, 1, 1, 20, 1, 1, 1, 0, 0, 6, 0, 1, 0, 0, 1],
        [1, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 20, 1, 0, 1, 0, 0, 0, 0, 0, 0, 6, 0, 0, 20, 1, 0, 7, 0, 20, 1],
        [1, 0, 1, 1, 9, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 20, 0, 0, 0, 0, 0, 7, 0, 0, 20, 0, 0, 4, 1, 0, 1, 20, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 1, 0, 1, 0, 1, 6, 0, 0, 20, 0, 0, 5, 0, 0, 0, 20, 1, 6, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 4, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 9, 1, 0, 1, 0, 1, 10, 0, 0, 0, 0, 0, 0, 0, 20, 1, 0, 1],
        [1, 0, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 0, 1],
        [1, 6, 0, 0, 0, 0, 0, 20, 0, 0, 7, 0, 0, 20, 0, 0, 5, 0, 0, 1, 0, 1, 20, 0, 0, 0, 6, 0, 0, 0, 0, 7, 0, 0, 9, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    countVirus=15
    img=bg_halloween
    default()
    arrayDrawing()
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    
#LEVEL 3
def level3(event):
    global grid, countVirus, img
    grid=[
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 6, 0, 0, 7, 0, 0, 0, 6, 0, 0, 0, 9, 1, 20, 1, 5, 20, 1, 20, 0, 0, 6, 0, 0, 8, 1, 20, 1],
        [1, 0, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 20, 1, 0, 1, 8, 1, 9, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 20, 1, 0, 1, 0, 1, 1, 0, 1, 4, 0, 0, 0, 1, 0, 6, 1],
        [1, 0, 7, 1, 0, 1, 0, 5, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 6, 1, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 20, 0, 5, 0, 1, 20, 1, 7, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 20, 1, 4, 0, 8, 20, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 9, 1, 1, 7, 1, 0, 0, 1],
        [1, 0, 6, 1, 0, 0, 0, 0, 7, 1, 7, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 5, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 5, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 20, 0, 1, 1, 1, 6, 0, 0, 8, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 20, 1, 1, 4, 1, 20, 0, 1],
        [1, 20, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 5, 0, 1, 0, 1, 1, 1, 1, 20, 0, 0, 5, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 8, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 0, 0, 20, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 1, 20, 1, 8, 0, 0, 7, 0, 0, 0, 0, 4, 0, 0, 0, 0, 6, 0, 0, 20, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 20, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 20, 5, 0, 1],
        [1, 0, 5, 1, 4, 1, 9, 1, 1, 0, 1, 0, 1, 9, 0, 0, 20, 1, 0, 1, 1, 20, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 7, 1, 0, 1, 0, 1, 1, 1, 1, 5, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 7, 1, 1, 0, 0, 5, 1],
        [1, 0, 0, 1, 20, 0, 0, 0, 1, 1, 1, 5, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 6, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 8, 0, 0, 0, 0, 0, 1, 0, 1],
        [11, 9, 0, 0, 0, 0, 0, 5, 0, 20, 1, 20, 1, 6, 0, 0, 6, 0, 0, 7, 0, 0, 20, 1, 0, 7, 0, 1, 6, 1, 7, 1, 20, 1, 10,1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    countVirus=15
    img=bg_winter
    default()
    arrayDrawing()
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )


#============================ SELECT PLAYER ============================
def selectPlayer():
    canvas.delete("all")
    canvas.create_image(0, 1, image=bg, anchor="nw")
    canvas.create_text(720, 100, text="CHOOSE AVATAR", font=("airal", 70, "bold"))
                            #==== BACK HOME =====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
                            #==== PLAYER 1 =====
    canvas.create_image(370, 200, image=player1_img, anchor="nw", tags="player1")
    canvas.create_image(430, 450, image=board_level_img, anchor="nw", tags="player1")
    canvas.create_text(510, 485, text="NAVY", font=("airal", 30, "bold"), fill="#8D4004",tags="player1")
                            #==== PLAYER 2 =====
    canvas.create_image(700, 200, image=player2_img, anchor="nw", tags="player2")
    canvas.create_image(780, 450, image=board_level_img, anchor="nw", tags="player2")
    canvas.create_text(870, 485, text="VISAL", font=("airal", 30, "bold"), fill="#8D4004",tags="player2")
                            #==== NEXT =====
    canvas.create_image(1260, 610, image=next_img, anchor="nw", tags="next")
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

#PLAYER 1  
def player1(event):
    global player
    canvas.delete("all")
    player=PLAYER1_CELL
    selectPlayer()
    canvas.create_image(480, 530, image=check, anchor="nw")
 
#PLAYER 2  
def player2(event):
    global player
    canvas.delete("all")
    player=PLAYER2_CELL
    selectPlayer()
    canvas.create_image(835, 530, image=check, anchor="nw")


#============================= BACKGROUND =====================
def backGround():
    global img
    canvas.create_image(0, 0, image=img, anchor="nw")

    
#============================= DRAW GRAPHICS =====================
def arrayDrawing():
    global isLevel,isLose, score
    if isLevel:
        canvas.delete("all")
        backGround()
        canvas.create_image(150, 200, image=board_img, anchor="n")
        canvas.create_text(120, 290, text="Score: ", font="arial, 30")
        canvas.create_text(210, 290, text= score, font="arial, 30")
        canvas.create_image(110, 310, image=alcohol_img, anchor="n")
        canvas.create_text(160, 340, text="      :  "+ str(countAlcohol), font="arial, 30")
        canvas.create_image(110, 380, image=virus1_big_img, anchor="n")
        canvas.create_text(170, 390, text="      :  "+ str(countVirus), font="arial, 30")
        y=20
        for row in range(len(grid)):
            x=300
            for col in range(len(grid[row])):
                if grid[row][col] == WALL_CELL:
                    canvas.create_image(x,y, image=wall2_img, anchor="nw")
                elif grid[row][col] == EMPTY_CELL:
                    canvas.create_rectangle(x, y, x+30, y+30,outline="", fill="")
                elif grid[row][col] == KEY_CELL:
                    canvas.create_image(x,y, image=key_img, anchor="nw")
                elif grid[row][col] == DOOR_CELL:
                    canvas.create_image(x,y, image=door_img, anchor="nw")
                elif grid[row][col] == ALCOHOL_CELL:
                    canvas.create_image(x,y, image=alcohol_small_img, anchor="nw")
                elif grid[row][col] == PLAYER1_CELL:
                    canvas.create_image(x,y, image=player1_small_img, anchor="nw")
                elif grid[row][col] == PLAYER2_CELL:
                    canvas.create_image(x,y, image=player2_small_img, anchor="nw")
                elif grid[row][col] == MANGO_CELL:
                    canvas.create_image(x,y, image=mango_img, anchor="nw")
                elif grid[row][col] == APPLE_CELL:
                    canvas.create_image(x,y, image=apple_img, anchor="nw")
                elif grid[row][col] == WATERMELON_CELL:
                    canvas.create_image(x,y, image=wm_img, anchor="nw")
                elif grid[row][col] == CARROT_CELL:
                    canvas.create_image(x,y, image=carrot_img, anchor="nw")
                elif grid[row][col] == VIRUS1_CELL:
                    canvas.create_image(x,y, image=virus1_img, anchor="nw")
                elif grid[row][col] == VIRUS2_CELL:
                    canvas.create_image(x,y, image=virus2_img, anchor="nw")
                x+=30
            y+=30
        canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_level")


#=========================== FUNCTIONS MOVE PLAYER =======================

# GET INDEX OF PLAYER CELL
def getPositionPlayer(index):
    for row in range(len(index)):
        for col in range(len(index[row])):
            if index[row][col] == player:
                return row, col


# MOVE PLAYER
def movePlayer(dx, dy):
    global grid, isLevel, score, isLose, isGood, countKey, player, countAlcohol,countVirus
    playerIndex=getPositionPlayer(grid)
    playerPositionX =  playerIndex[0]
    playerPositionY =  playerIndex[1]
    if isLevel:
        if dx == 1 and dy == 0:
            NewPlayerPositionX= playerPositionX
            NewPlayerPositionY= playerPositionY+1
        elif dx == -1 and dy == 0:
            NewPlayerPositionX= playerPositionX
            NewPlayerPositionY= playerPositionY-1
        elif dx == 0 and dy == 1:
            NewPlayerPositionX= playerPositionX+1
            NewPlayerPositionY= playerPositionY
        elif dx == 0 and dy == -1:
            NewPlayerPositionX= playerPositionX-1
            NewPlayerPositionY= playerPositionY
    if grid[NewPlayerPositionX][NewPlayerPositionY] != WALL_CELL:
        if grid[NewPlayerPositionX][NewPlayerPositionY] == MANGO_CELL or grid[NewPlayerPositionX][NewPlayerPositionY] == CARROT_CELL or grid[NewPlayerPositionX][NewPlayerPositionY] == WATERMELON_CELL or grid[NewPlayerPositionX][NewPlayerPositionY] == APPLE_CELL:            
            grid[NewPlayerPositionX][NewPlayerPositionY] = player
            score+=25
            # winsound.PlaySound("sound/Eat.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
        if grid[NewPlayerPositionX][NewPlayerPositionY] == ALCOHOL_CELL:
            countAlcohol+=1
            # winsound.PlaySound("sound/Eat.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
        if grid[NewPlayerPositionX][NewPlayerPositionY] == KEY_CELL:
             grid[NewPlayerPositionX][NewPlayerPositionY] = player
             countKey+=1
            #  winsound.PlaySound("sound/Eat.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
        if (grid[NewPlayerPositionX][NewPlayerPositionY] == VIRUS1_CELL and countAlcohol >= 2) or (grid[NewPlayerPositionX][NewPlayerPositionY] == VIRUS2_CELL and countAlcohol >= 2):            
            grid[NewPlayerPositionX][NewPlayerPositionY] = player
            countAlcohol-=2
            countVirus-=1
            # winsound.PlaySound("sound/virus.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
        if (grid[NewPlayerPositionX][NewPlayerPositionY] == VIRUS1_CELL) or (grid[NewPlayerPositionX][NewPlayerPositionY] == VIRUS2_CELL) and countAlcohol < 2: 
            lose()           
        if score >= 500 and countKey==1 and grid[NewPlayerPositionX][NewPlayerPositionY]== DOOR_CELL and countVirus == 0:
            win()
        else:
            grid[playerPositionX][playerPositionY] = EMPTY_CELL
            grid[NewPlayerPositionX][NewPlayerPositionY] = player
    if not isLose:
        arrayDrawing()
     
    
# MOVE RIGHT
def moveRight(event):
    movePlayer(1,0)
    
# MOVE LEFT
def moveLeft(event):
    movePlayer(-1,0)
    
# MOVE UP
def moveUp(event):
    movePlayer(0,-1)

# MOVE DOWN
def moveDown(event):
    movePlayer(0,1)    




 # ======================= HOME_PAGE =============================
def home():
    canvas.create_image(1,0, image=home_bg, anchor="nw")
    canvas.create_image(650, 400, image=start_img, anchor="nw", tags="start")
    canvas.create_image(645, 475, image=help_img, anchor="nw", tags="help")
    canvas.create_image(665, 560, image=exit_img, anchor="nw", tags="exit")
    # winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )


# ======================= START =============================
def start(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    selectPlayer()
   

# ======================= BACK TO LEVELS PAGE =============================
def backTolevel(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    allLevels()

    
# ======================= BACK-HOME =============================
def backHome(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    home()

#============================ HELP ============================
def help(event):
    canvas.create_image(0,0 , image=bg, anchor="nw")
    canvas.create_text(720, 100, text="INTRODUCTION", font=("airal", 70, "bold"))
    canvas.create_image(450, 200, image=introduction_img, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

#============================ EXIT ============================
def exit(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    root.destroy()


#============================ ALL LEVELS BUTTON ============================
def allLevels():
    canvas.create_image(0, 0, image=home_bg, anchor="nw")
                            #==== LEVEL 1 =====
    canvas.create_image(650, 400, image=board_level_img, anchor="nw", tags="level1")
    canvas.create_text(735, 435, text="Level 1", font=("airal", 30, "bold"), fill="#8D4004",tags="level1")
                            #==== LEVEL 2 =====
    canvas.create_image(650, 500, image=board_level_img, anchor="nw", tags="level2")
    canvas.create_text(735, 535, text="Level 2", font=("airal", 30, "bold"), fill="#8D4004",tags="level2")
                            #==== LEVEL 3 =====
    canvas.create_image(650, 600, image=board_level_img, anchor="nw", tags="level3")
    canvas.create_text(735, 635, text="Level 3", font=("airal", 30, "bold"), fill="#8D4004",tags="level3")
                            #==== BACK =====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_player")
    
#NEXT
def next(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    allLevels()

#BACK PLAYER
def backPlayer(event):
    # winsound.PlaySound("sound/click.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    selectPlayer()
    

    
#============================ WIN & LOSE ============================
def result(img):
    global isLevel
    canvas.delete("all")
    canvas.create_image(0, 0, image=bg_lose, anchor="nw")
    canvas.create_image(420, 100, image=img, anchor="nw")
    canvas.create_text(700, 408, text=score, font="arial, 35")
    canvas.create_image(490, 450, image=back_img, anchor="nw",tags="back_level")
    isLevel=False

#LOSE
def lose():
    global isLevel
    lose=game_lose_img
    # winsound.PlaySound("sound/lose.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    result(lose)

#WIN
def win():
    global isLevel
    win=game_win_img
    # winsound.PlaySound("sound/win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )
    result(win)
    

#============================ KEY EVENT ============================
canvas.tag_bind("start","<Button-1>",start)
canvas.tag_bind("help","<Button-1>",help)
canvas.tag_bind("exit","<Button-1>",exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
canvas.tag_bind("back_level","<Button-1>",backTolevel)
canvas.tag_bind("back_player","<Button-1>",backPlayer)
canvas.tag_bind("next","<Button-1>",next)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("player1","<Button-1>",player1)
canvas.tag_bind("player2","<Button-1>",player2)

home()

#========================= REMOTES =================
root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()














