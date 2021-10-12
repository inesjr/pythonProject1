import os

from selenium import webdriver
from pages import dragdrop

def before_scenario(context,scenario):
    dir= os.getcwd()
    print(dir+"\configuration\chromedriver.exe")
    context.browser= webdriver.Chrome(executable_path=dir+"\configuration\chromedriver.exe")
    context.browser.maximize_window()
    context.dd = dragdrop.drag_drop(context.browser)


def after_scenario(context,scenario):
    context.browser.close()
