from random import randint
sprite = Actor('biglesp')
sprite.topright = 10, randint(0,200)

WIDTH = 1096
HEIGHT = 739
music.play('bg_music.ogg')

def draw():
    screen.clear()
    screen.blit('lxf_group.png',(0,0))
    sprite.draw()
    
def update():
    sprite.left += 2
    if keyboard[keys.W]:
        sprite.y -=1
    elif keyboard[keys.S]:
        sprite.y += 1
    elif keyboard[keys.A]:
        sprite.angle += 1
    elif keyboard[keys.D]:
        sprite.angle -= 1
    if sprite.left > WIDTH:
        sprite.right = 0
    if keyboard[keys.ESCAPE]:
        quit()

def on_mouse_down(pos):
    if sprite.collidepoint(pos):
        print("Eek!")
        set_sprite_click()
    else:
        print("You missed me!")
        
def set_sprite_click():
    sprite.image = 'biglesp_inv'
    sounds.cowbell.play()
    clock.schedule_unique(set_sprite_normal, 1.0)
    
def set_sprite_normal():
    sprite.image = 'biglesp'