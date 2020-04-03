import pygame
import keyboard, mouse

# defining colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controller Status")


done = False


clock = pygame.time.Clock()


pygame.joystick.init()
    

textPrint = TextPrint()

joystick = pygame.joystick.Joystick(1)
joystick.init()
# -------- Main Program Loop -----------
while done==False:

    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(0):
            	keyboard.press_and_release("f")
            if joystick.get_button(1):
            	keyboard.press_and_release("r")
            if joystick.get_button(2):
            	keyboard.press_and_release("q")
            if joystick.get_button(3):
            	keyboard.press_and_release("e")
            if joystick.get_button(4):
                mouse.right_click()
            if joystick.get_button(5):
                keyboard.press_and_release('enter')
            if joystick.get_button(6):
                keyboard.press_and_release('ctrl')
            if joystick.get_button(7):
                keyboard.press_and_release('space')
            if joystick.get_button(8):
                keyboard.press_and_release('f6')
            if joystick.get_button(9):
                keyboard.press_and_release('o')
            if joystick.get_button(10):
                keyboard.press_and_release('shift')



        if event.type == pygame.JOYBUTTONUP:
            pass

        if event.type == pygame.JOYHATMOTION:
            hat_pos = joystick.get_hat(0)
            if hat_pos == (1,0):
                keyboard.press_and_release('+')
            elif hat_pos == (-1, 0):
                keyboard.press_and_release('-')
            else:
                pass

        if event.type == pygame.JOYAXISMOTION:
            lsAxis = [joystick.get_axis(0), joystick.get_axis(1)]
            rsAxis = [joystick.get_axis(3), joystick.get_axis(2)]

            if lsAxis[0] > 0:
                keyboard.press('d')
            elif lsAxis[0] < 0:
                keyboard.press('a')
            elif lsAxis[0] == 0:
                keyboard.release('a')
                keyboard.release('d')

            if lsAxis[1] > 0:
                keyboard.press('s')
            elif lsAxis[1] < 0:
                keyboard.press('w')
            elif lsAxis[1] == 0:
                keyboard.release('s')
                keyboard.release('w')


            if rsAxis[0] > 0:
                keyboard.press('right')
            elif rsAxis[0] < 0:
                keyboard.press('left')

            elif rsAxis[0] == 0:
                keyboard.release('right')
                keyboard.release('left')

            if rsAxis[1] > 0:
                keyboard.press('down')
            elif rsAxis[1] < 0:
                keyboard.press('up')
            elif rsAxis[1] == 0:
                keyboard.release('up')
                keyboard.release('down')
                

    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()

    # For 1 joystick (set range to joystick_count if all controllers are wanted):
    for i in range(1):
        
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        textPrint.unindent()
.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats) )
        textPrint.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        textPrint.unindent()
        
        textPrint.unindent()

    
    pygame.display.flip()

    clock.tick(30)

pygame.quit ()
