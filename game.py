from turtle import Screen
import pgzrun
import random
import pygame
FONT_COLOR = (255, 255, 255)
WIDTH = 1000
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED = 5
COLORS = ["orange", "blue"]
current_level = 1
final_level = 5
game_over = False
game_complete = False
imposters = []
animation = []
red_image = {}

#in ra luc game hoan thien
def draw(): 
    global game_over, game_complete, imposters,current_level
    screen.clear()
    screen.blit('dark', (0, 0))
    if game_over:
        display_message("Game Over","Press space to play again")
    elif game_complete:
        display_message("Win game","Press space to play again")
    else:
        for im in imposters:
            im.draw()

def update():
    global game_over, game_complete, imposters, current_level
    if len(imposters) == 0:
        imposters = make_imposters(current_level) # them impostor dung voi level hien tai
    if (game_over or game_complete) and (keyboard.space):
        imposters = []
        current_level = 1
        game_over = False
        game_complete = False

#thiet ke cac imposters
def make_imposters(number_of_imposters):
    color_to_create = gets_color_to_create(number_of_imposters)#thiet ke mau cho imposters
    new_imposters = creat_imposters(color_to_create)#tao cac imposters
    layout_imposters(new_imposters)#tinh toan vi tri cac imposters
    animate_imposters(new_imposters)#hien thi qua trinh rot cac imposters
    return new_imposters

def gets_color_to_create(number_of_imposters):
    colors_to_create = ["red"]
    for i in range(0, number_of_imposters):
        ramdom_color = random.choice(COLORS)
        colors_to_create.append(ramdom_color)
    return colors_to_create

def creat_imposters(color_to_create):
    new_imposters = []
    for color in color_to_create:
        impostor = Actor(color + "-im")
        new_imposters.append(impostor)
    return new_imposters

def layout_imposters(imposters_to_layout):
    number_of_gap = len(imposters_to_layout) + 1
    gap_size = WIDTH / number_of_gap
    random.shuffle(imposters_to_layout)
    for indx, impostor in enumerate(imposters_to_layout):
        new_x_pos = (indx + 1) * gap_size
        impostor.x = new_x_pos

def animate_imposters(imposters_to_animate):
    for impostor in imposters_to_animate:
        duration = (START_SPEED - current_level)  + 2
        impostor.anchor = ("center", "bottom")
        animaton = animate(impostor, duration=duration, on_finished=handle_game_over, y = HEIGHT)
        animation.append(animaton)

def handle_game_over():
    global game_over, game_complete
    game_over = True
    game_complete = False

# def get_imposter_color(imposter):
#     color = imposter.image.split("-")[0] if "-" in imposter.image else imposter.image.split(".")[0]
#     return color
def on_mouse_down(pos):
    global imposters, current_level
    for im in imposters:
        if im.collidepoint(pos):
            if "red" in im.image:
                red_imposter_click()
            else:
                handle_game_over()

def red_imposter_click():
    global game_complete, current_level, imposters, animation
    stop_animation(animation)
    if current_level == final_level:
        game_complete = True
    else:
        current_level = current_level + 1
        imposters = []  
        animation = []

def stop_animation(animation_to_stop):
    for animation in animation_to_stop:
        if animation.running:
            animation.stop()

def display_message(title, message):
    screen.draw.text(title, center=CENTER, fontsize=70, color = FONT_COLOR)
    screen.draw.text(message, center=(CENTER_X, CENTER_Y + 100), fontsize=40, color = FONT_COLOR)
pgzrun.go()
