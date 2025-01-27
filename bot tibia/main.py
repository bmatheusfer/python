import pyautogui as pg
import pyscreeze
import json

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
         
REGION_BATTLE = 1565, 171, 175, 70 
REGION_LOOT = 752, 366, 236, 245
REGION_MAP = 1574, 27, 338, 146   
FOLDER_NAME = 'troll_thais'
BOX_LOOT = 1743, 505, 174, 61

def check_battle():
    return pg.locateOnScreen('imgs/region_battle.png', region=REGION_BATTLE)

def ava_loot():
    return pg.locateOnScreen('imgs/ava_loot.png', region=BOX_LOOT)

def dead_body():
    return pg.locateCenterOnScreen('imgs/dead_body.png', confidence=0.7, region=REGION_LOOT)

def kill_monster():
    while check_battle() == None:
        print('entrei aqui')     
        pg.press('space')
        while pg.pixelMatchesColor(1585, 221, (255, 0, 0), tolerance=10):
            print('esperando o monstro morrer')
        print('procurando outro monstro')

def get_loot():
    dead_body = pg.locateCenterOnScreen('imgs/dead_rat.png', confidence=0.7, region=REGION_LOOT)
    pg.moveTo(dead_body)
    pg.keyDown('ctrl')
    pg.click(button="left")
    pg.keyUp('ctrl')
    if ava_loot() == None:
        pg.keyDown('ctrl')
        pg.moveTo(1769, 543)
        pg.click(button='left')
        pg.keyUp('ctrl')

def soltar_magia():
    pg.press('F1')

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, confidence=0.8, region=REGION_MAP)
    if flag:
        x, y = pg.center(flag)
        pg.moveTo(x, y)         
        pg.click()
        pg.sleep(wait)
       
def run(): 
    with open(f'{FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
    for item in data:       
        kill_monster()
        pg.sleep(0.2)
        get_loot()
        soltar_magia()
        pg.sleep(0.2)            
        go_to_flag(item['path'], item['wait'])

while True:
    run()