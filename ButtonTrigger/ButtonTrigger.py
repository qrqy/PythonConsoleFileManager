# This Python file uses the following encoding: utf-8
import pyperclip
from tkinter import CURRENT
from pynput import keyboard
import os
from click import pause

a = 0


#обработчик нажатия клавиши где 87 это W, 83 это S и 69 это E
def on_press(key):
    try:
        if  key.vk==87:
            press_up()
        elif key.vk==83:
            press_down()
        elif key.vk==69:
            clear();
            print_dir(os.listdir()) 
    except:
        pass

#обработчик отжатия клавиш для специальных клавиш типо стрелки, Esc, Del или Backspace
def on_release(key):
    try:
        if key == keyboard.Key.up:
            press_up()
        elif key == keyboard.Key.down:
            press_down()
        elif key == keyboard.Key.backspace:
            back_dir()
        elif key == keyboard.Key.enter:
            press_enter()
    except :
        pass
#Функция очистки командной строки cmd
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_cur_dir():
    print_dir(os.listdir())
def print_choise_dir(path):
    print_dir(os.listdir(path))
#Вывод дирректории с указателем текущего выбранного элемента
def print_dir(arr):
    global a, current_dir
    print(current_dir)
    for x in arr:
        if arr.index(x)==a:
            print("->"+x)
        else:
            print("  "+x);
#Переход на элемент ниже
def press_down():
    global a, current_dir
    if a<len(os.listdir(current_dir))-1:
        a+=1
        clear();
        print_choise_dir(current_dir);
    
#Переход на элемень выше
def press_up():
    global a, current_dir
    if a>0:
        a-=1
        clear();
        print_choise_dir(current_dir)

def back_dir():
    global a,current_dir
    current_dir = list_to_string(current_dir.split('\\')[:-1], '\\')
    a=0
    clear();
    print_choise_dir(current_dir)

#Обработчик Enterа
def press_enter():
    global a, current_dir
    try:
        filename, file_extension = os.path.splitext(current_dir+'\\'+os.listdir(current_dir)[a])
        print(filename+" - "+file_extension)
        if os.path.isdir(current_dir+'\\'+os.listdir(current_dir)[a]):
            current_dir=current_dir+'\\'+os.listdir(current_dir)[a]
            a=0;
            clear();
            print_choise_dir(current_dir)

        else:
            open_file = open(current_dir+'\\'+os.listdir(current_dir)[a])
            text_file = open_file.read()
            clear()
            #print(text_file)
            pyperclip.copy(text_file);
            print_choise_dir(current_dir)

    except :
        pass


def list_to_string(array, divider):
    try:
        result = ""
        for item in array:
            if item!=array[-1]:
                result+=item+divider
        return result+array[-1]
    except :
        return ""
current_dir = list_to_string(os.path.abspath(__file__).split('\\')[:-1], '\\')
print_dir(os.listdir(current_dir))

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
   listener.join()

  