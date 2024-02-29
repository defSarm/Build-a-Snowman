from gamelib import *
from time import sleep 

game = Game(1000,600,"   Build a Snowman")

# start menu images
bg = Image('./startMenu/startBG.png',game)
game.setBackground(bg)

play = Image("./startMenu/playButton.png", game)
play.moveTo(680,260)

quit = Image("./startMenu/quit_button.png", game)
quit.moveTo(680,410)

# mouse cursor
mousec = Image('./startMenu/cursor.png', game)
mousec.resizeBy(-70)
cursor = Image('./startMenu/cursor.png',game)
cursor.resizeBy(-70)
pointer = Image('./startMenu/pointer.png',game)
pointer.resizeBy(-60)

mouse.visible=False

'''
game.setMusic('./startMenu/audio/bgMusic.mp3')
game.setVolume(15)
game.playMusic()


buttonClick = Sound("./startMenu/audio/buttonClick.wav",0)
'''

OVER = False

def cursorPhys():
    mousec.moveTo(mouse.x,mouse.y)
    mousec.draw()

# Start menu loop
while not(game.over) and not(OVER):
    game.processInput()

    #background
    bg.draw()

    # buttons
    play.draw()
    quit.draw()

    # cursor
    cursorPhys()


    # button clicking/hovering
    mousec.setImage(cursor.image)
    if mousec.collidedWith(play,'rectangle'):
        mousec.setImage(pointer.image)

    if mousec.collidedWith(quit,'rectangle'):
        mousec.setImage(pointer.image)


    if mousec.collidedWith(play,'rectangle') and mouse.LeftClick:
        #buttonClick.play()
        game.over=True

    if mousec.collidedWith(quit,'rectangle') and mouse.LeftClick:
        #buttonClick.play()
        game.over = True
        OVER = True

    game.update(30)


# THE CHARACTER ****

# idle movement (right)
stickmanRidle = Image("./stage1/CRidle.png",game)
stickmanRidle.resizeBy(-65)
stickmanRidle.moveTo(200,450)

# right movement
stickmanRight = Animation("./stage1/rightwalk1.png",10,game,2048/5,1310/2,3)
stickmanRight.resizeBy(-65)
stickmanRight.moveTo(200,450)

# idle movement (left)
stickmanLidle = Image("./stage1/CLidle.png",game)
stickmanLidle.resizeBy(-65)
stickmanLidle.moveTo(200,450)

# left movement
stickmanLeft = Animation("./stage1/leftwalk.png",10,game,2048/5,1310/2,3)
stickmanLeft.resizeBy(-65)
stickmanLeft.moveTo(200,450)

# character control function (IMPORTANT) ****
def characterControl():
    # right movement
    if keys.Pressed[K_d]:
        stickmanRight.visible=True
        stickmanRight.x+=7

        stickmanLeft.visible=False
        stickmanLidle.visible=False

        stickmanRidle.visible=False

        stickmanRidle.moveTo(stickmanRight.x,stickmanRight.y)
        stickmanLeft.moveTo(stickmanRight.x,stickmanRight.y)
        stickmanLidle.moveTo(stickmanRight.x,stickmanRight.y)
    if not(keys.Pressed[K_d]) and not(stickmanLidle.visible or stickmanLeft.visible) :
        stickmanRight.visible=False
        stickmanRidle.visible=True

        stickmanLeft.visible=False
        stickmanLidle.visible=False

    # left movement
    if keys.Pressed[K_a]:
        stickmanLeft.visible=True
        stickmanLeft.x-=7

        stickmanRight.visible=False
        stickmanRidle.visible=False

        stickmanLidle.visible=False

        stickmanLidle.moveTo(stickmanLeft.x,stickmanLeft.y)
        stickmanRight.moveTo(stickmanLeft.x,stickmanLeft.y)
        stickmanRidle.moveTo(stickmanLeft.x, stickmanLeft.y)
    if not(keys.Pressed[K_a]) and not(stickmanRidle.visible or stickmanRight.visible) :
        stickmanLeft.visible=False
        stickmanLidle.visible=True

        stickmanRight.visible=False
        stickmanRidle.visible=False

    if keys.Pressed[K_a] and keys.Pressed[K_d]:
        stickmanRidle.visible=True

        stickmanLeft.visible=False
        stickmanLidle.visible=False
        stickmanRight.visible=False

# PICK UP CONTROL (IMPORTANT) *************

pickUp=False
def itemGrab(object,character,charIdle):
    global pickUp
    if character.collidedWith(object,"rectangle") or charIdle.collidedWith(object,"rectangle"):
        if keys.Pressed[K_e]:
            pickUp=True
        if keys.Pressed[K_q]:
            pickUp=False

    if pickUp:
        object.y = character.y+20
        object.x=character.x
    else:
        if object.y < 540:
            object.y+=5

# WALL BORDER (IMPORTANT) *************
def border(characterR,characterL, left=False, right=False):
    if not(right):
        if characterR.x+32 > 1000:
            characterR.x=970
    if not(left):
        if characterL.x-32 < 0:
            characterL.x=30

# Stage switch
def stageSwitch(show,items):
    for item in range(len(items)):
        items[item].visible=show

# Starting Scene >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# scene images
sc1 = Image("./opening/s1.png",game)
sc2 = Image("./opening/s2.png",game)
sc3 = Image("./opening/s3.png",game)
sc4 = Image("./opening/s4.png",game)
sc5 = Image("./opening/s5.png",game)
sc6 = Image("./opening/s6.png",game)
sc7 = Image("./opening/s7.png",game)
sc8 = Image("./opening/s8.png",game)
sc9 = Image("./opening/s9.png",game)
sc10 = Image("./opening/s10.png",game)

scenes = [sc1,sc2,sc3,sc4,sc5,sc6,sc7,sc8,sc9,sc10]

for i in range(len(scenes)):
    scenes[i].visible=False
    scenes[i].resizeTo(1000,600)

sceneTime = 0
def scene(image,time):
    global sceneTime
    image.visible = True
    sceneTime += 1

    if sceneTime == time:
        image.visible=False
        sceneTime = 0

# stage 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# stage bg's
stage1BG = Image('./stage1/stage1BG.jpg',game)
game.setBackground(stage1BG)

# general settings
mousec.setImage(cursor.image)
#game.stopMusic()

# shovel
shovel = Image("./stage1/objects/shovel.png",game)
shovel.resizeBy(-90)
shovel.moveTo(760,520)

# snowman
snowman = Image('./stage1/snowman/snowman.png',game)
snowman.resizeBy(-60)
snowman.moveTo(650,410)

# snowman body parts
snowman3 = Image("./stage1/snowman/snow1.png",game)
snowman3.moveTo(650,403)
snowman3.resizeBy(-55)
snowman3.visible=False
digging3=False

snowman2 = Image("./stage1/snowman/snow2.png",game)
snowman2.moveTo(650,406)
snowman2.resizeBy(-55)
snowman2.visible=False
digging2=False

snowman1 = Image("./stage1/snowman/snow3.png",game)
snowman1.moveTo(650,417)
snowman1.resizeBy(-55)
snowman1.visible=False
digging1=False

# snowman buttons/step2
face = Image("./stage1/snowman/step2.png",game)
face.visible=False
face.resizeBy(-60)
face.moveTo(655,410)

# dig animation
digAnimation = Animation("./stage1/snowman/digSprite.png",55,game,3000/5,3960/11,1)
digAnimation.visible=False
digAnimation.resizeTo(1000,600)

digTimer=0

# scarf / cabinet 
closed = Image("./stage1/objects/closedCabinet.png",game)
closed.visible=False
closed.moveTo(350,450)
closed.resizeBy(-70)

openEmpty = Image("./stage1/objects/openEmpty.png",game)
openEmpty.visible=False
openEmpty.moveTo(350,450)
openEmpty.resizeBy(-70)

openScarf = Image("./stage1/objects/openScarf.png",game)
openScarf.visible=False
openScarf.moveTo(350,450)
openScarf.resizeBy(-70)

scarf = Image("./stage1/objects/scarf.png",game)
scarf.visible=False
scarf.moveTo(600,50)
scarf.resizeBy(-80)

snowmanScarf = Image("./stage1/snowman/scarf.png",game)
snowmanScarf.moveTo(650,410)
snowmanScarf.visible=False
snowmanScarf.resizeBy(-60)

carrotNose = Image("./stage1/snowman/carrotNose.png",game)
carrotNose.visible=False
carrotNose.moveTo(650,410)
carrotNose.resizeBy(-60)

instructions = Image("./stage1/Instructions.png",game)
instructions.resizeBy(-55)
instructions.moveTo(500,400)
instructions.visible=False

instruction = True

# stage 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# stage 2 bg
stage2BG = Image("./stage2/stage2BG.png",game)
stage2BG.visible=False

# rocks
r1 = Image('./stage2/r1.png',game)
r1.resizeBy(-92)
r1.moveTo(300,500)
r1.visible=False
rock1=False

r2 = Image('./stage2/r2.png',game)
r2.resizeBy(-92)
r2.moveTo(200,550)
r2.visible=False
rock2=False

r3 = Image('./stage2/r3.png',game)
r3.resizeBy(-92)
r3.visible=False
r3.moveTo(700,460)
rock3=False

r4 = Image('./stage2/r4.png',game)
r4.resizeBy(-92)
r4.moveTo(100,500)
r4.visible=False
rock4=False

r5 = Image('./stage2/r5.png',game)
r5.resizeBy(-92)
r5.moveTo(600,480)
r5.visible=False
rock5=False

r6 = Image('./stage2/r3.png',game)
r6.resizeBy(-92)
r6.visible=False
r6.moveTo(700,460)
rock6=False

r7 = Image('./stage2/r4.png',game)
r7.resizeBy(-92)
r7.moveTo(240,490)
r7.visible=False
rock7=False

r8 = Image('./stage2/r1.png',game)
r8.resizeBy(-92)
r8.moveTo(900,490)
r8.visible=False
rock8=False

r9 = Image('./stage2/r4.png',game)
r9.resizeBy(-92)
r9.moveTo(300,510)
r9.visible=False
rock9=False

r10 = Image('./stage2/r2.png',game)
r10.resizeBy(-92)
r10.moveTo(600,550)
r10.visible=False
rock10=False

rockCounter = 0
rockLabel = Image('./stage2/r5.png',game)
rockLabel.moveTo(50,50)
rockLabel.resizeBy(-70)

rx, ry = 105, 35

rc = Font("black",50)

rockLabel.visible=False

rockStatement = [rock1,rock2,rock3,rock4,rock5,rock6,rock7,rock8,rock9,rock10]
rocks = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]

# Car
carHat = Image("./stage2/carHat.png",game)
carHat.visible=False
carHat.resizeBy(-50)
carHat.moveTo(620,410)

carEmpty = Image("./stage2/carEmpty.png",game)
carEmpty.visible=False
carEmpty.resizeBy(-50)
carEmpty.moveTo(620,410)

carA = False

# car keys
carKeys = Image("./stage1/carKey.png",game)
carKeys.moveTo(190,435)
carKeys.resizeBy(-90)
carKeys.rotateBy(90)

key = False

# glue
glue = Image("./stage1/glue.png",game)
glue.resizeBy(-90)
glue.moveTo(430,500)
glue.rotateBy(90)
glue.visible=False

oglue = False

# hat
hat = Image("./stage2/topHat.png",game)
hat.resizeBy(-80)
hat.moveTo(225,50)
hat.visible=False
hatOn = False

# stage 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stage3BG = Image("./stage3/stage3BG.png",game)
stage3BG.visible=False

# stage 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stage4BG = Image("./stage4/stage4BG.png",game)
stage4BG.visible=False

brokenStool = Image("./stage4/brokenStool.png",game)
brokenStool.resizeBy(-80)
brokenStool.visible=False
brokenStool.moveTo(205,470)
brokenStool.rotateBy(20)

brokenPiece = Image("./stage4/brokenPiece.png",game)
brokenPiece.resizeBy(-80)
brokenPiece.visible=False
brokenPiece.moveTo(210,540)
brokenPiece.rotateBy(-80)


stool = Image("./stage4/fixedStool.png",game)
stool.resizeBy(-80)
stool.visible=False
stool.moveTo(205,470)
fixed = False
step = False

carrot = Image("./stage4/carrot.png",game)
carrot.moveTo(790,195)
carrot.resizeBy(-76)
carrot.visible=False

nose = False


# neighbor
insideHouse = Image("./stage4/insideHouse.png",game)
insideHouse.resizeTo(1000,600)
insideHouse.visible=False

house = False


neighbor = Image("./stage4/neighbor.png",game)
neighbor.resizeBy(-72)
neighbor.visible=False
neighbor.moveTo(400,440)

text = False

speak = False
count=0
def timer(text,time):
    global count
    text.visible=True
    count +=1

    if count == time:
        text.visible=False
        count=0
    


# dialogue ----------------------------------------------------------------------
d1 = Image("./stage4/dialogue/d1.png",game)
d1.resizeBy(-55)
d1.moveTo(500,400)
d1.visible=False

d2 = Image("./stage4/dialogue/d2.png",game)
d2.resizeBy(-55)
d2.moveTo(500,400)
d2.visible=False

d3 = Image("./stage4/dialogue/d3.png",game)
d3.resizeBy(-55)
d3.moveTo(500,400)
d3.visible=False

d4 = Image("./stage4/dialogue/d4.png",game)
d4.resizeBy(-55)
d4.moveTo(500,400)
d4.visible=False

d5 = Image("./stage4/dialogue/d5.png",game)
d5.resizeBy(-55)
d5.moveTo(500,400)
d5.visible=False

d6 = Image("./stage4/dialogue/d6.png",game)
d6.resizeBy(-55)
d6.moveTo(500,400)
d6.visible=False

d7 = Image("./stage4/dialogue/d7.png",game)
d7.resizeBy(-55)
d7.moveTo(500,400)
d7.visible=False

talking = False
 

# stage 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stage5BG = Image("./stage5/stage5BG.png",game)
stage5BG.visible=False

# stage 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stage6BG = Image("./stage6/stage6BG.png",game)
stage6BG.visible=False

# sticks
st1 = Image("./stage6/st1.png",game)
st1.moveTo(340,290)
st1.rotateBy(-160)

st2 = Image("./stage6/st2.png",game)
st2.moveTo(600,330)
st2.rotateBy(60)

st3 = Image("./stage6/st3.png",game)
st3.moveTo(700,100)
st3.rotateBy(40)

st4 = Image("./stage6/st4.png",game)
st4.moveTo(330,50)
st4.rotateBy(90)

st5 = Image("./stage6/st5.png",game)
st5.moveTo(760,280)
st5.rotateBy(70)

stLabel = Image("./stage6/st5.png",game)
stLabel.moveTo(400,70)
stLabel.resizeBy(-70)
stLabel.rotateBy(50)
stLabel.visible=False

sx, sy = 510, 35

arms = Image("./stage1/snowman/arms.png",game)
arms.visible=False
arms.moveTo(647,410)
arms.resizeBy(-50)

stC = 0

sticks = [st1,st2,st3,st4,st5]

for i in range(len(sticks)):
    sticks[i].visible=False
    sticks[i].resizeBy(-70)

stickD = Image("./stage6/stickD.png",game)
stickD.resizeBy(-55)
stickD.moveTo(500,400)
stickD.visible=False
s = False

# final stage ------------------------------------------------------------------------------------------
lastStage = Image("./stage1/end.png",game)
lastStage.visible=False

end = False


# THE GAME LOOP ********************************************************************************************************************

# stage activation
startingScene = True
s1 = False
s2 = False
s3 = False
s4 = False
s5 = False
s6 = False
s7 = False

# special altercations
switch = False
complete = False
start=False
go = False
openTimer = 0


stickmanLeft.visible = False
stickmanLidle.visible = False
game.over=False

while not(game.over) and not(OVER):
    game.processInput()

    #bgs

    # opening scene
    for i in range(len(scenes)):
        scenes[i].draw()

    stage1BG.draw()
    stage2BG.draw()
    stage3BG.draw()
    stage4BG.draw()
    stage5BG.draw()
    stage6BG.draw()
    lastStage.draw()

    insideHouse.draw()

    # snowman drawing
    snowman.draw()

    snowman1.draw()
    snowman2.draw()
    snowman3.draw()

    face.draw()

    snowmanScarf.draw()

    carrotNose.draw()

    # object drawing STAGE 1
    shovel.draw()
    glue.draw()

    closed.draw()
    openEmpty.draw()
    openScarf.draw()
    scarf.draw()


    # ROCKS ***
    rockLabel.draw()
    if rockCounter>0:
        rockLabel.visible=True
        # 105 35
        game.drawText(rockCounter,rx,ry,rc)

    for i in range(len(rocks)):
        rocks[i].draw() 

    # sticks ***
    for i in range(len(sticks)):
        sticks[i].draw()

    arms.draw()
    
    stLabel.draw()
    if stC > 0:
        stLabel.visible=True
        # 510, 35
        game.drawText(stC,sx,sy,rc)

    # stage 4 --------------------------------------------------------
    neighbor.draw()
    stool.draw()
    brokenPiece.draw()
    brokenStool.draw()
    carrot.draw()

    # car
    carHat.draw()
    carEmpty.draw()
    carKeys.draw()

    hat.draw()

    if mousec.collidedWith(carKeys,"rectangle") and mouse.LeftClick:
        carKeys.moveTo(250,50)
        carKeys.resizeTo(300,200)
        key=True

    if key and mousec.collidedWith(carHat,"rectangle") and mouse.LeftClick:
        carA = True
        hat.visible=True

    # stickman drawings
    stickmanRidle.draw()
    stickmanRight.draw()

    stickmanLeft.draw()
    stickmanLidle.draw()

    # digging
    digAnimation.draw()

    # dialogue ---------------------------------------------------------------
    d1.draw()
    d2.draw()
    d3.draw()
    d4.draw()
    d5.draw()
    d6.draw()
    d7.draw()

    instructions.draw()

    stickD.draw()

    #mouse 
    cursorPhys()

    #character
    characterControl()
    itemGrab(shovel,stickmanLeft,stickmanLidle)
    itemGrab(shovel,stickmanRight,stickmanRidle)

    border(stickmanRight,stickmanLeft)

    # snowman body
    if snowman1.visible and snowman2.visible and snowman3.visible:
        switch=True
        complete=True

    if digging3:
        snowman3.visible=True
    if digging2:
        snowman2.visible=True
    if digging1:
        snowman1.visible=True

    # digging to make ^^^
    if mousec.collidedWith(snowman,"rectangle") and mouse.LeftClick and pickUp and not(complete):
        digAnimation.visible=True

    if digAnimation.visible:
        digTimer+=1
        if digTimer == 19:
            digTimer=0
            #snowbody
            if not(digging3):
                digging3=True
            elif digging3 and not(digging2):
                digging2=True
            elif digging2 and not(digging1):
                digging1=True

            digAnimation.visible=False

    # border for changing stages --------------------------------------------------------------------------------------------------------------------------

    # stage 1 >> stage 2
    if startingScene:
        stageSwitch(False,[stage1BG, shovel,carKeys, snowman,stickmanLeft,stickmanRight,stickmanLidle,stickmanRidle,closed])
        if sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc1,70)
        if sc1.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc2,80)
        if sc1.visible==False and sc2.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc3,80)
        if sc1.visible==False and sc2.visible==False and sc3.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc4,100)
        if sc1.visible==False and sc2.visible==False and sc3.visible==False and sc4.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc5,120)
        if sc1.visible==False and sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc6,160)
        if sc1.visible==False and sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc7,160)
        if sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc1.visible==False and sc9.visible==False and sc10.visible==False:
            scene(sc8,160)
        if sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc1.visible==False and sc10.visible==False:
            scene(sc9,80)
        if sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc1.visible==False:
            scene(sc10, 100)
        if sc1.visible==False and sc2.visible==False and sc3.visible==False and sc4.visible==False and sc5.visible==False and sc6.visible==False and sc7.visible==False and sc8.visible==False and sc9.visible==False and sc10.visible==False:
            startingScene = False
            s1=True

    if s1:
        border(stickmanRight,stickmanLeft,False,True)
        stageSwitch(True,[stage1BG, shovel, carKeys, snowman,closed])

        if instruction:
            timer(instructions,180)
            if instructions.visible==False:
                instruction=False

        if rockCounter == 10 and mousec.collidedWith(snowman,"rectangle") and mouse.LeftClick:
            face.visible=True
            rockLabel.visible=False
            rx, ry = -100, -100
        
        if hat.visible or hatOn:
            carKeys.visible=False
        
        if mousec.collidedWith(snowman,"rectangle") and mouse.LeftClick and hat.visible and not(hatOn):
            hatOn = True
            hat.resizeBy(15)
            hat.moveTo(653,270)
        
        if mousec.collidedWith(snowman,"rectangle") and snowman1.visible and snowman2.visible and snowman3.visible and mouse.LeftClick:
            scarf.visible=False
            snowmanScarf.visible=True
        
        if mousec.collidedWith(snowman,"rectangle") and mouse.LeftClick and carrot.visible:
            nose=True
            carrotNose.visible=True
            carrot.visible=False
        
        if nose:
            carrotNose.visible=True
        
        # end stage
        if hatOn and arms.visible and face.visible and carrotNose.visible and snowmanScarf.visible:
            end = True
        if end:
            stageSwitch(False,[stickmanLeft,stickmanLidle,stickmanRight,stickmanRidle, stage1BG, snowman,snowman1,snowman2,snowman3,rockLabel,stLabel,arms,face,hat,shovel,snowmanScarf,closed,openEmpty,carKeys,carrotNose])
            lastStage.visible=True
            game.setBackground(lastStage)
        
        if stC == 2 and mousec.collidedWith(snowman,"rectangle") and mouse.LeftClick:
            arms.visible=True
            stLabel.visible=False
            sx, sy = -100, -100

        # scarf
        if mousec.collidedWith(closed,"rectangle") and mouse.LeftClick and scarf.visible==False:
            closed.visible=False
            openScarf.visible=True
        if mousec.collidedWith(openScarf,"rectangle") and mouse.LeftClick:
            openScarf.visible=False
            openEmpty.visible=True
            scarf.visible=True

        # stage1 >>> stage 2
        if stickmanRight.x + 32 > 1000 and switch and not(pickUp):
            # object visibility
            stageSwitch(False,[shovel,snowman,snowman1,snowman2,snowman3,face,closed,openEmpty,snowmanScarf])
            stageSwitch(True, [r1,stage2BG,carHat])

            if key:
                carKeys.visible=True
            if not(key):
                carKeys.visible=False
            if carA:
                carHat.visible=False
                carEmpty.visible=True
                key=False
            if hatOn:
                hat.visible=False

            game.setBackground(stage2BG)
            stickmanRight.x = 50

            # stage switch
            s2=True
            s1=False


    # stage 2 
    if s2:
        border(stickmanRight,stickmanLeft,True,True)

        # visibility for this stage
        stageSwitch(False,[snowman1,snowman2,snowman3,face,closed,openEmpty,snowmanScarf,carrotNose,arms])
        stageSwitch(True, [r1,stage2BG,carHat]) 

        if openEmpty.visible and scarf.visible==False:
            snowmanScarf.visible=False

        if key:
            carKeys.visible=True
        if not(key):
            carKeys.visible=False

        if carA:
            carHat.visible=False
            carEmpty.visible=True
            key=False
        if hatOn:
            hat.visible=False

        # pick up rock
        if mousec.collidedWith(r1) and mouse.LeftClick:
            r1.visible=False
            rock1 = True
            rockCounter+=1
            r1.moveTo(-100,-100)
        if rock1:
            r1.visible=False


        # stage 2 >> stage 1
        if stickmanLeft.x - 32 < 0:
            # object visibility
            stageSwitch(True,[shovel,snowman,snowman1,snowman2,snowman3,carKeys,closed,openEmpty])
            stageSwitch(False,[r1,stage2BG,carHat,carEmpty])

            if openEmpty.visible and scarf.visible==False:
                snowmanScarf.visible=True
            
            if nose:
                carrotNose.visible=True                

            if hat.visible:
                carKeys.visible=False

            game.setBackground(stage1BG)
            stickmanLeft.x = 950

            if hatOn:
                hat.visible=True

            # stage switch
            s1=True
            s2=False

        # stage 2 >> stage 3
        if stickmanRight.x+32 > 1000:
            # object visibility
            stageSwitch(True,[stage3BG,r2,r3])
            stageSwitch(False,[stage2BG,snowman1,snowman2,snowman3,carHat,carEmpty])


            stickmanRight.x = 50

            game.setBackground(stage3BG)
            # stage switch
            s2=False
            s3=True

    #stage3
    if s3:
        border(stickmanRight,stickmanLeft,True,True)
        #visibility for this stage
        stageSwitch(True,[stage3BG,r2,r3])
        stageSwitch(False,[stage2BG,snowman1,snowman2,snowman3,r1])
        game.setBackground(stage3BG)

        # pick up rock2
        if mousec.collidedWith(r2) and mouse.LeftClick:
            r2.visible=False
            rock2 = True
            rockCounter+=1
            r2.moveTo(-100,-100)
        if rock2:
            r2.visible=False

        # pick up rock3
        if mousec.collidedWith(r3) and mouse.LeftClick:
            r3.visible=False
            rock3 = True
            rockCounter+=1
            r3.moveTo(-100,-100)
        if rock3:
            r3.visible=False

        # stage3 >> stage2
        if stickmanLeft.x - 32 < 0:
            # object visibility
            stageSwitch(True,[r1,stage2BG])
            stageSwitch(False,[r2,r3,stage3BG,neighbor])

            game.setBackground(stage2BG)
            stickmanLeft.x = 950

            # stage switch
            s3=False
            s2=True

        # stage3 >> stage4
        if stickmanRight.x+32 > 1000:
            # object visibility
            stageSwitch(True,[stage4BG,r4,neighbor])
            stageSwitch(False,[stage3BG,r2,r3])

            stickmanRight.x = 50

            game.setBackground(stage4BG)
            # stage switch
            s3=False
            s4=True

    # stage 4
    if s4:
        border(stickmanRight,stickmanLeft,True,True)
        # object visibility
        stageSwitch(True,[stage4BG,r4,r8,neighbor])
        stageSwitch(False,[stage3BG,r2,r3,snowman1,snowman2,snowman3])
        game.setBackground(stage4BG)

        # pick up rock4
        if mousec.collidedWith(r4) and mouse.LeftClick:
            r4.visible=False
            rock4 = True
            rockCounter+=1
            r4.moveTo(-100,-100)
        if rock4:
            r4.visible=False

        # pick up rock8
        if mousec.collidedWith(r8) and mouse.LeftClick:
            r8.visible=False
            rock8 = True
            rockCounter+=1
            r8.moveTo(-100,-100)
        if rock8:
            r8.visible=False
        
        # dialogue
        if mousec.collidedWith(neighbor,"rectangle") and mouse.LeftClick and not(text):
            speak = True
            talking = True
        if speak:
            if d2.visible == False and d3.visible == False and d4.visible == False and d5.visible == False and d6.visible == False:
                timer(d1,80)
            if d1.visible == False and d3.visible == False and d4.visible == False and d5.visible == False and d6.visible == False:
                timer(d2,100)
            if d1.visible == False and d2.visible == False and d4.visible == False and d5.visible == False and d6.visible == False:
                timer(d3,120)
            if d1.visible == False and d2.visible == False and d3.visible == False and d5.visible == False and d6.visible == False:
                timer(d4,250)
            if d1.visible == False and d2.visible == False and d3.visible == False and d4.visible == False and d6.visible == False:
                timer(d5,80)
            if d1.visible == False and d2.visible == False and d3.visible == False and d4.visible == False and d5.visible == False:
                timer(d6,80)
            
            if d1.visible==False and d2.visible == False and d3.visible == False and d4.visible == False and d5.visible==False and d6.visible == False:
                speak=False
                text=True
                house = True
                talking = False
        
        # stage4 >> house
        if house:
            stageSwitch(True, [insideHouse,glue])
            stageSwitch(False,[stage4BG,r4,r8,neighbor,snowman1,snowman2,snowman3])

            if nose == False:
                carrot.visible=True
            else:
                carrot.visible=False

            if not(fixed):
                brokenStool.visible = True
                brokenPiece.visible=True

                stool.visible=False
            else:
                stool.visible=True
            
            if nose == False:
                carrot.visible=True
            else:
                carrot.visible=False

            stickmanLeft.x = 950
            stickmanRight.x = 950
            stickmanRidle.x = 950
            stickmanLidle.x = 950

            s4 = False
            house = True
        
        if mousec.collidedWith(neighbor,"rectangle") and text and mouse.LeftClick:
            start = True
            talking = True
        if start:
            timer(d7,80)
            if d7.visible==False:
                house=True
                start=False
                talking = False


        # stage4 >> stage3
        if stickmanLeft.x - 32 < 0 and not(talking):
            # object visibility
            stageSwitch(True,[r2,r3,stage3BG])
            stageSwitch(False,[r4,r8,stage4BG,neighbor])

            game.setBackground(stage3BG)
            stickmanLeft.x = 950

            # stage switch
            s4=False
            s3=True

        # stage4 >> stage5
        if stickmanRight.x+32 > 1000 and not(talking):
            # object visibility
            stageSwitch(True,[stage5BG,r5,r6,r7])
            stageSwitch(False,[stage4BG,r4,r8,neighbor])

            stickmanRight.x = 50

            game.setBackground(stage5BG)
            # stage switch
            s4=False
            s5=True

    # house
    if house:
        border(stickmanRight,stickmanLeft,True,False)
        stageSwitch(True, [insideHouse,glue])
        stageSwitch(False,[stage4BG,r4,r8,neighbor,snowman1,snowman2,snowman3])

        if mousec.collidedWith(glue,"rectangle") and mouse.LeftClick and not(oglue):
            oglue=True
            glue.resizeTo(250,150)
            glue.moveTo(400,50)
        
        if nose == False:
            carrot.visible=True
        else:
            carrot.visible=False

        if mousec.collidedWith(carrot,"rectangle") and mouse.LeftClick:
            carrot.moveTo(750,50)

        if not(fixed) and not(step):
            brokenStool.visible = True
            brokenPiece.visible=True
            stool.visible=False

            if oglue and mousec.collidedWith(brokenStool) and mouse.LeftClick:
                brokenStool.visible=False
                brokenPiece.visible=False
                stool.visible=True
                fixed=True
                glue.visible=False
                oglue=False
        else:
            stool.visible=True
        
        if step:
            stool.visible=False
        
        if fixed and mouse.LeftClick and mousec.collidedWith(stool):
            stool.moveTo(400,50)
            glue.visible=False
            glue.moveTo(-100,-100)
            oglue=False

        game.setBackground(insideHouse)

        # house >> stage 4
        if stickmanRight.x+32 > 1000:
            stageSwitch(False, [insideHouse,glue,brokenPiece,brokenStool])
            stageSwitch(True,[stage4BG,r4,r8,neighbor])

            if nose == False:
                carrot.visible=True
            else:
                carrot.visible=False

            if oglue:
                glue.visible=True
            
            if fixed and stool.y != 50:
                stool.visible=False
            else:
                stool.visible=True

            stickmanRight.x = 600

            s4=True
            house=False
            start=False

    if s5:
        border(stickmanRight,stickmanLeft,True,True)
        # object visibility
        stageSwitch(True,[stage5BG,r5,r6,r7])
        stageSwitch(False,[stage4BG,r4,r8,snowman1,snowman2,snowman3,neighbor])
        game.setBackground(stage5BG)

        # pick up rock5
        if mousec.collidedWith(r5) and mouse.LeftClick:
            r5.visible=False
            rock5 = True
            rockCounter+=1
            r5.moveTo(-100,-100)
        if rock5:
            r5.visible=False

        # pick up rock6
        if mousec.collidedWith(r6) and mouse.LeftClick:
            r6.visible=False
            rock6 = True
            rockCounter+=1
            r6.moveTo(-100,-100)
        if rock6:
            r6.visible=False

        # pick up rock7
        if mousec.collidedWith(r7) and mouse.LeftClick:
            r7.visible=False
            rock7 = True
            rockCounter+=1
            r7.moveTo(-100,-100)
        if rock7:
            r7.visible=False

        # stage 5 >> stage 4
        if stickmanLeft.x - 32 < 0:
            # object visibility
            stageSwitch(True,[r4,r8,stage4BG])
            stageSwitch(False,[r5,r6,r7,stage5BG])

            game.setBackground(stage4BG)
            stickmanLeft.x = 950

            # stage switch
            s5=False
            s4=True

        # stage 5 >> stage 6
        if stickmanRight.x+32 > 1000:
            # object visibility
            stageSwitch(True,[stage6BG,r9,r10,st1,st2,st3,st4,st5])
            stageSwitch(False,[stage5BG,r5,r6,r7])
            stickmanRight.x = 50

            if step:
                stool.visible=True

            game.setBackground(stage6BG)
            # stage switch
            s5=False
            s6=True

    if s6:
        border(stickmanRight,stickmanLeft,True,False)
        # object visibility
        stageSwitch(True,[stage6BG,r9,r10,st1,st2,st3,st4,st5])
        stageSwitch(False,[stage5BG,r5,r6,r7,snowman1,snowman2,snowman3])
        game.setBackground(stage6BG)

        if step:
            stool.visible=True

        # pick up rock9
        if mousec.collidedWith(r9) and mouse.LeftClick:
            r9.visible=False
            rock9 = True

            rockCounter+=1
            r9.moveTo(-100,-100)
        if rock9:
            r9.visible=False

        # pick up rock10
        if mousec.collidedWith(r10) and mouse.LeftClick:
            r10.visible=False
            rock10 = True
            rockCounter+=1
            r10.moveTo(-100,-100)
        if rock10:
            r10.visible=False

        # pickup sticks
        if (mousec.collidedWith(st1,"rectangle") or mousec.collidedWith(st2,"rectangle")) and mouse.LeftClick and not(fixed):
            s = True
        
        if s:
            timer(stickD,80)
            if stickD.visible==False:
                s = False
        
        if (mousec.collidedWith(st1) or mousec.collidedWith(st2)) and mouse.LeftClick and fixed and not(step):
            stool.moveTo(500,520)
            step=True
        
        if mousec.collidedWith(stool) and mouse.LeftClick and step:
            if stickmanLeft.collidedWith(stool) or stickmanRight.collidedWith(stool) or stickmanRidle.collidedWith(stool) or stickmanLidle.collidedWith(stool):
                stickmanLeft.moveTo(500,400)
                stickmanRight.moveTo(500,400)
                stickmanLidle.moveTo(500,400)
                stickmanRidle.moveTo(500,400)
                go = True
        
        if go:
            if stickmanRight.x > 520 or stickmanLeft.x < 480:
                stickmanLeft.y = 450
                stickmanRight.y = 450
                stickmanLidle.y = 450
                stickmanRidle.y = 450
                go = False

            if mousec.collidedWith(st1) and mouse.LeftClick:
                st1.visible=False
                st1.moveTo(-100,-100)
                
                stC+=1
            if mousec.collidedWith(st2) and mouse.LeftClick:
                st2.visible=False
                st2.moveTo(-100,-100)
                
                stC +=1


        #stage6 >> stage5
        if stickmanLeft.x - 32 < 0:
            # object visibility
            stageSwitch(True,[r5,stage5BG,r6,r7])
            stageSwitch(False,[stage6BG,r9,r10,st1,st2,st3,st4,st5])

            if step:
                stool.visible=False
            

            game.setBackground(stage5BG)
            stickmanLeft.x = 950

            # stage switch
            s6=False
            s5=True




    game.update(30)

game.quit()