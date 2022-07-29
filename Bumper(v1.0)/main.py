#version 1.0

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle as pk
from tkinter import *
from tkinter.messagebox import showinfo
import tkinter as tk



def main(email_entry, pass_entry):
    load_site = pk.load(open("website", "rb"))


    print("Processing")
    browser = webdriver.Chrome("chromedriver.exe")

    browser.get("https://rocket-league.com/trades/TJ_Frags")

    accept = browser.find_element(By.ID, "acceptPrivacyPolicy")
    accept.click()
    # Login
    lgn = browser.find_element(By.XPATH, "/html/body/header/section[1]/div/div[2]/div/a[1]")
    lgn.click()
    status = True
    while status:
        email = browser.find_element(By.NAME, "email")
        password = browser.find_element(By.NAME, "password")
        login = browser.find_element(By.NAME, "submit")
        email.send_keys(email_entry)
        password.send_keys(pass_entry)
        login.click()

        bump = browser.find_element(By.CSS_SELECTOR,
                                     'body > main:nth-child(5) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1) > span:nth-child(2)')
        browser.execute_script("arguments[0].click();", bump)
        accept = browser.find_element(By.CSS_SELECTOR, ".fa.fa-times")
        browser.execute_script("arguments[0].click();", accept)
        print("Trade Bumped")




        if browser.find_element(By.XPATH, "/html/body/div[1]/div").is_displayed():
            showinfo("Incorrect credentials", "Please close chrome and re-enter your login information")
            wrong = browser.find_element(By.XPATH, "/html/body/div[1]/div/span/i")
            wrong.click()
            time.sleep(2)
        else:
            break

        if browser.find_element(By.XPATH, "/html/body/main/div/section[1]/h1").is_displayed():
            browser.get(load_site)
        else:
            break
    # Trade
    print("starting")
    trades = browser.find_elements(By.CLASS_NAME, "rlg-trade")

    # https://rocket-league.com/trades/TJ_Frags
    # https://rocket-league.com/trades/TJRyz3

    trading = True

    while trading:
        for trade in trades:


            bumptp = 0
            while bumptp < 960:
                bumptp = bumptp + 1
                print(bumptp, "/960 sec")
                time.sleep(1)

                if bumptp == 960:
                    time.sleep(2)

                    bump = browser.find_element(By.CSS_SELECTOR,
                                                'body > main:nth-child(5) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1) > span:nth-child(2)')
                    browser.execute_script("arguments[0].click();", bump)

                    time.sleep(2)
                    accept = browser.find_element(By.CSS_SELECTOR, ".fa.fa-times")
                    browser.execute_script("arguments[0].click();", accept)
                    print("Trade Bumped")
                    bumptp = 0

                if bumptp in [180, 360, 540, 720, 900]:
                    browser.refresh()
                    print("Updated")


    print("Done")


def webload():
    top_win = tk.Toplevel()
    top_win.geometry("500x500")

    web_entry = tk.Label(top_win, font=1, text="Please paste the URL of the websites with your trades here:")
    web_entry.place(anchor=CENTER, relx=0.5, rely=0.45)

    web_entry = tk.Entry(top_win, font=2)
    web_entry.place(relx=0.5, rely=0.5, relwidth=0.6, anchor=CENTER)

    load_web_button = tk.Button(top_win, text="Load website", command =lambda: save_web(web_entry.get(), top_win))
    load_web_button.place(relx=0.5, rely=0.8,  anchor=CENTER)
    top_win.iconbitmap('icon.ico')


def guid():
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://tjfrags.000webhostapp.com/2022/01/guid")
    time.sleep(960)



root = tk.Tk()

root.geometry("500x500")
root.title("RL-Trading Bot")




# load website
web_load_button = tk.Button(root, text="Load website", command=lambda: webload())
web_load_button.place(relx=0.8, rely=0.8)

Guid_button = tk.Button(root, text="Guid", command=lambda: guid() )
Guid_button.place(relx=0.2, rely=0.8, anchor=CENTER)




start_button = tk.Button(root, text="start", command=lambda: main(email_entry.get(), pass_entry.get()))
start_button.place(relx=0.45, rely=0.8, relheight=0.1, relwidth=0.2, anchor=CENTER)


email_entry = tk.Entry()
email_entry.place(relx=0.45, rely=0.3, relheight=0.05, relwidth=0.4, anchor=CENTER)


pass_entry = tk.Entry()
pass_entry.place(relx=0.45, rely=0.55, relheight=0.05, relwidth=0.4, anchor=CENTER)


def save_web(web_entry, top_win):
    pk.dump(web_entry, open("website", "wb"))
    time.sleep(1)
    top_win.destroy()


root.mainloop()
