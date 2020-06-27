# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:15:36 2020

@author: Kailash
"""

# TravelIndia
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import PhotoImage
import random
import tkcalendar
from datetime import date

today = date.today()
L = ["A", "B", "C", "D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
     "15", "16", "17", "18"]
k = str(today)
y = k[0:4]
y1 = int(y)
m = k[6:7]
m1 = int(m)
d = k[8:10]
d1 = int(d)
w = Tk()
w.title("Travel India")
w.geometry('2000x1500')
I = ["C11.png", "C12.png", "C13.png", "C14.png", "C15.png", "C16.png", "C17.png"]
I1 = random.choice(I)
photos = PhotoImage(file=I1, master=w)
Ix = ["obg2.png", "obg3.png", "obg4.png", "obg5.png", "obg6.png"]
Ix1 = random.choice(Ix)
photosobg1 = PhotoImage(file=Ix1, master=w)
obg1 = Label(w, image=photosobg1)
B = Label(w, text='Let Some Memories Be forever', image=photos)
B.pack(side="top", expand="Yes")
photos1 = PhotoImage(file="Back11.png", master=w)
B2 = Label(w, image=photos1)
photos2 = PhotoImage(file="Nat3.png", master=w)
B21 = Label(w, image=photos2)
photos3 = PhotoImage(file="Nat31.png", master=w)
B31 = Label(w, image=photos3)
photos4 = PhotoImage(file="Eva1.png", master=w)
B41 = Label(w, image=photos4)
photos41 = PhotoImage(file="Eva2.png", master=w)
B42 = Label(w, image=photos41)
photos5 = PhotoImage(file="Sha1.png", master=w)
B51 = Label(w, image=photos5)
photos6 = PhotoImage(file="Sha2.png", master=w)
B52 = Label(w, image=photos6)
photos7 = PhotoImage(file="As1.png", master=w)
B61 = Label(w, image=photos7)
photos8 = PhotoImage(file="As2.png", master=w)
B62 = Label(w, image=photos8)
photos9 = PhotoImage(file="Natobk1.png", master=w)
Back1 = Label(w, image=photos9)
Back11 = Label(w, image=photos9)
photos10 = PhotoImage(file="Evobk11.png", master=w)
Back2 = Label(w, image=photos10)
Back21 = Label(w, image=photos10)
photos11 = PhotoImage(file="Shbk1.png", master=w)
Back3 = Label(w, image=photos11)
Back31 = Label(w, image=photos11)
photos12 = PhotoImage(file="Asbk.png", master=w)
Back4 = Label(w, image=photos12)
Back41 = Label(w, image=photos12)
photosbg1 = PhotoImage(file="try.png", master=w)
bg1 = Label(w, image=photosbg1)

photos13 = PhotoImage(file="TI_official.png", master=w)
photo = PhotoImage(file=r"officialTI.png")
x = ""
comboff = Combobox(w, textvariable=x)
TI = Label(w, image=photos13)


def Book():
    B.destroy()
    B1.destroy()
    B2.pack()
    B2.place()
    t1 = Entry(w, width=15, bd=2, font=("Algerian", 22))
    t1.focus()
    t1.config(bg="White")
    t1.place(x=350, y=260, height=53)
    a1 = t1.get()
    L1 = Label(w, text="Source -->", font=("Algerian", 22), bg="#bbf9c6", fg="Dark Blue", bd=10)
    L1.place(x=185, y=260, height=53)
    L2 = Label(w, text="Destination <--->", font=("Algerian", 22), bg="#bbf9c6", fg="Dark Blue", bd=10)
    L2.place(x=600, y=260, height=53)
    t2 = Entry(w, width=15, bd=2, font=("Algerian", 22))

    t2.focus()
    t2.config(bg="White")
    t2.place(x=862, y=260, height=53)

    def proceed():
        L1.destroy()
        L2.destroy()
        P.destroy()
        w.config(bg="White")
        L3 = Label(w, text="Onward Date -->", font=("Algerian", 22), bg="#bbf9c6", fg="Dark Blue", bd=10)
        L3.place(x=70, y=260, height=53)
        cal = tkcalendar.DateEntry(w, width=12, year=y1, month=m1, day=d1,
                                   background='darkblue', font=("Algerian", 15), foreground='white', borderwidth=2)
        cal.place(x=330, y=260, height=53)
        L4 = Label(w, text="Return Date -->", font=("Algerian", 22), bg="#bbf9c6", fg="Dark Blue", bd=10)
        L4.place(x=600, y=260, height=53)
        Opt = Label(w, text="(Optional)", font=("Algerian", 22), bg="#bbf9c6", fg="Dark Blue", bd=10)
        Opt.place(x=600, y=300, height=20)
        t2.place_forget()
        cal1 = tkcalendar.DateEntry(w, width=12, year=y1, month=m1, day=d1,
                                    background='darkblue', font=("Algerian", 15), foreground='white', borderwidth=2)
        cal1.place(x=850, y=260, height=53)

        def Search():
            obg1.place(x=1, y=1)
            nonlocal t1
            nonlocal t2
            nonlocal cal
            nonlocal cal1
            lat = cal.get()
            lat1 = cal1.get()
            tx = t1.get() + " -----> " + t2.get()
            L31 = Label(w, text=tx, font=("Lucida Calligraphy", 20), bg="White", fg="Black")
            L31.place(x=10, y=10)
            ca = cal.get() + " -----> " + cal1.get()
            L31 = Label(w, text=ca, font=("Lucida Calligraphy", 20), bg="White", fg="Black")
            L31.place(x=450, y=10)

            L3.destroy()
            L4.destroy()
            Opt.destroy()
            cal.destroy()
            cal1.destroy()
            t1.destroy()
            t2.destroy()
            Search.destroy()
            B2.destroy()
            Li1 = ["National Travels", "Evacay Travels", "Sharma Travels", "Asian Xpress"]
            r1 = random.choice(Li1)
            Li2 = ["Gujarat Travels", "Seabird Travels", "Kaveri Travels", "Diwakar Travels", "Hebron Travels"]
            r2 = random.choice(Li2)
            Li3 = ["SRS Travels", "Prasanna Travels", "Orange Travels", "Kallada Travels"]
            r3 = random.choice(Li3)
            Li4 = ["Jabbar Travels", "Neeta Travels", "Hans Travels", "SRM Travels", "SVR Travels", "KPN Travels"]
            r4 = random.choice(Li4)
            Li5 = ["Paulo Travels", "Kaleswari Travels", "Shrinath Travels", "Verma Travels"]
            r5 = random.choice(Li5)
            Li6 = ["Anand Tourist", "Supreme Travels", "Neeta Tours and Travels", "JAI DEV YATRA CO."]
            r6 = random.choice(Li6)
            Li7 = ["Raj Ratan Travels", "Orange Tours and Travels", "KGN Travels", "Sheetal Travel",
                   "Sheetal Queen Roadways"]
            r7 = random.choice(Li7)
            Li8 = ["Jambeswar Travels", "Prasanna Purple Travels", "Sahara Travels", "Deep Travels"]
            r8 = random.choice(Li8)
            Li9 = [" Jai Bhawani Travels", "Gulzar Tours and Travels", "Choudhary Travels", "Shri Hari Travels"]
            r9 = random.choice(Li9)
            Li10 = ["Ajay Travels", "Shrinath Nandu Travels", " Dashmesh Travels ", " Dashmesh Travels",
                    "Bhagwati Travel Agency"]
            r10 = random.choice(Li10)
            L5 = Label(w, text="1 Bus found", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L5.place(x=250, y=60)
            L6 = Label(w, text="Info:", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L6.place(x=500, y=60)
            L7 = Label(w, text="Arrival", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L7.place(x=600, y=60)
            L8 = Label(w, text="Departure", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L8.place(x=705, y=60)
            L9 = Label(w, text="Duration", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L9.place(x=830, y=60)
            L10 = Label(w, text="Ratings", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L10.place(x=930, y=60)
            L11 = Label(w, text="Fare", font=("Algerian", 15), bg="#19a0d0", fg="White")
            L11.place(x=1030, y=60)

            def but():

                if r1 == Li1[0]:
                    Back1.place(x=227, y=250)
                    B21.place(x=1225, y=100)
                elif r1 == Li1[1]:
                    Back2.place(x=227, y=250)
                    B41.place(x=1225, y=100)
                elif r1 == Li1[2]:
                    Back3.place(x=227, y=250)
                    B51.place(x=1225, y=100)
                elif r1 == Li1[3]:
                    Back4.place(x=227, y=250)
                    B61.place(x=1225, y=100)

                def back():
                    back.destroy()
                    Back1.place_forget()
                    Back2.place_forget()
                    Back3.place_forget()
                    Back4.place_forget()
                    B21.place_forget()
                    B41.place_forget()
                    B51.place_forget()
                    B61.place_forget()
                    back.destroy()

                back = Button(w, text="Back", font=("Algerian", 17), bg="red", fg="Black", command=back)
                back.place(x=10, y=60)

            B3 = Button(w, bd=2, relief="solid", bg="#d0f9f9", command=but)
            B3.place(x=225, y=100, height=150, width=1000)

            L12 = Label(w, text=r1, font=("Algerian", 22), bg="#d0f9f9", fg="Black")
            L12.place(x=230, y=105)

            L13 = Label(w, text="6:00 PM", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
            L13.place(x=580, y=105)
            L14 = Label(w, text="6:30 PM", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
            L14.place(x=700, y=105)
            L14 = Label(w, text="30 Mins", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
            L14.place(x=830, y=105)
            L15 = Label(w, text="4 Star", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
            L15.place(x=920, y=105)
            L16 = Label(w, text="Rs 650", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
            L16.place(x=1030, y=105)
            L17 = Label(w, text="\nLive \nTracking \nAvailabe", font=("Algerian", 17), bg="#d0f9f9", fg="Black")
            L17.place(x=1100, y=115)
            L18 = Label(w, text="Bharat Benz A/C Seater (2+1)", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black")
            L18.place(x=230, y=150)
            L19 = Label(w, text="Wheels up! It's about the journey.", font=("Lucida Handwriting", 16), bg="#d0f9f9",
                        fg="Black")
            L19.place(x=540, y=150)

            def Amn():
                if r1 == Li1[0]:
                    Back11.place(x=227, y=250)
                    B21.place(x=1225, y=100)
                elif r1 == Li1[1]:
                    Back21.place(x=227, y=250)
                    B41.place(x=1225, y=100)
                elif r1 == Li1[2]:
                    Back31.place(x=227, y=250)
                    B51.place(x=1225, y=100)
                elif r1 == Li1[3]:
                    Back41.place(x=227, y=250)
                    B61.place(x=1225, y=100)

                def back():
                    back.destroy()
                    Back1.place_forget()
                    Back2.place_forget()
                    Back3.place_forget()
                    Back4.place_forget()
                    B21.place_forget()
                    B41.place_forget()
                    B51.place_forget()
                    B61.place_forget()
                    Back11.place_forget()
                    Back21.place_forget()
                    Back31.place_forget()
                    Back41.place_forget()
                    L20.place_forget()
                    back.destroy()

                back = Button(w, text="Back", font=("Algerian", 17), bg="red", fg="Black", command=back)
                back.place(x=10, y=60)
                L20 = Label(w,
                            text=" M-ticket Supported   Charging Point\t Movie\t Emergency Contact Number  Reading Light\t\t    ",
                            font=("Times New Roman", 17), bg="#d0f9f9", fg="Black", borderwidth=2, relief="solid")
                L20.place(x=225, y=250, height=45)

                def ex():
                    L20.destroy()
                    exit.destroy()

                exit = Button(w, text="x", font=("Times New Roman", 12), bg="#d0f9f9", fg="Red", borderwidth=2,
                              relief="solid", command=ex)
                exit.place(x=1200, y=250, width=20, height=20)

            B4 = Button(w, text="Amenities", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black", relief="raised",
                        command=Amn)
            B4.place(x=500, y=215)

            def Img():
                if r1 == Li1[0]:
                    Back1.place(x=227, y=250)
                    B21.place(x=1225, y=100)

                    def N():
                        B31.place(x=1225, y=100)
                        N.destroy()

                    N = Button(w, text=" View More >>>", bg="Yellow", command=N)
                    N.place(x=1420, y=640)

                elif r1 == Li1[1]:
                    Back2.place(x=227, y=250)
                    B41.place(x=1225, y=100)

                    def N():
                        B42.place(x=1225, y=100)
                        N.destroy()

                    N = Button(w, text=" View More >>>", bg="Yellow", command=N)
                    N.place(x=1420, y=640)

                elif r1 == Li1[2]:
                    Back3.place(x=227, y=250)
                    B51.place(x=1225, y=100)

                    def N():
                        B52.place(x=1225, y=100)
                        N.destroy()

                    N = Button(w, text=" View More >>>", bg="Yellow", command=N)
                    N.place(x=1420, y=640)

                elif r1 == Li1[3]:
                    Back4.place(x=227, y=250)
                    B61.place(x=1225, y=100)

                    def N():
                        B62.place(x=1225, y=100)
                        N.destroy()

                    N = Button(w, text=" View More >>>", bg="Yellow", command=N)
                    N.place(x=1420, y=640)

                def back():
                    back.destroy()
                    Back1.place_forget()
                    Back2.place_forget()
                    Back3.place_forget()
                    Back4.place_forget()
                    B21.place_forget()
                    B41.place_forget()
                    B51.place_forget()
                    B61.place_forget()
                    Back11.place_forget()
                    Back21.place_forget()
                    Back31.place_forget()
                    Back41.place_forget()
                    N.place_forget()
                    back.destroy()

                back = Button(w, text="Back", font=("Algerian", 17), bg="red", fg="Black", command=back)
                back.place(x=10, y=60)

            B5 = Button(w, text="Live Images", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black", relief="raised",
                        command=Img)
            B5.place(x=580, y=215)

            def rew():
                if r1 == Li1[0]:
                    Back1.place(x=227, y=250)
                    B21.place(x=1225, y=100)
                elif r1 == Li1[1]:
                    Back2.place(x=227, y=250)
                    B41.place(x=1225, y=100)
                elif r1 == Li1[2]:
                    Back3.place(x=227, y=250)
                    B51.place(x=1225, y=100)
                elif r1 == Li1[3]:
                    Back4.place(x=227, y=250)
                    B61.place(x=1225, y=100)

                Re = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                Re.place(x=225, y=250, height=100, width=1000)
                Re1 = Label(w, text="\nRated By people\t\tPost your Review", font=("Times New Roman", 17), bg="#d0f9f9",
                            fg="Black")
                Re1.place(x=230, y=250)
                Re2 = Label(w, text="4 Star", font=("Times New Roman", 17), bg="#d0f9f9", fg="Black")
                Re2.place(x=230, y=310)

                def Like():
                    Re3.destroy()
                    Re4.destroy()

                    ch1 = Checkbutton(w, text="Cleanliness", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black")
                    ch1.place(x=750, y=270)
                    ch2 = Checkbutton(w, text="Boarding\npoint", font=("Lucida Calligraphy", 10), bg="#d0f9f9",
                                      fg="Black")
                    ch2.place(x=750, y=300)
                    ch3 = Checkbutton(w, text="AC ", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black")
                    ch3.place(x=860, y=270)
                    ch4 = Checkbutton(w, text="Driving ", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black")
                    ch4.place(x=860, y=300)
                    ch5 = Checkbutton(w, text="Staff behavior ", font=("Lucida Calligraphy", 10), bg="#d0f9f9",
                                      fg="Black")
                    ch5.place(x=960, y=270)
                    ch6 = Checkbutton(w, text="Live tracking  ", font=("Lucida Calligraphy", 10), bg="#d0f9f9",
                                      fg="Black")
                    ch6.place(x=960, y=300)

                    def Sub():
                        Re5.destroy()
                        Re1.destroy()
                        Re2.destroy()
                        ch1.destroy()
                        ch2.destroy()
                        ch3.destroy()
                        ch4.destroy()
                        ch5.destroy()
                        ch6.destroy()
                        Sub.destroy()
                        Th = Label(w, text="Thanks for your Feedback", font=("Lucida Calligraphy", 22), bg="#d0f9f9",
                                   fg="Black")
                        Th.place(x=250, y=280)
                        Th1 = Label(w, text="We'd Surely look upoon the same", font=("Lucida Calligraphy", 15),
                                    bg="#d0f9f9", fg="Black")
                        Th1.place(x=680, y=310)

                    Sub = Button(w, text="Submit", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black",
                                 command=Sub)
                    Sub.place(x=1110, y=290)

                Re3 = Button(w, text="Like it", font=("Times New Roman", 17), bg="#d0f9f9", fg="Black", command=Like)
                Re3.place(x=750, y=270)

                def dislike():
                    Re3.destroy()
                    Re4.destroy()

                    ch11 = Checkbutton(w, text="Punctuality", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black")
                    ch11.place(x=740, y=270)
                    ch21 = Checkbutton(w, text="Seat comfort ", font=("Lucida Calligraphy", 10), bg="#d0f9f9",
                                       fg="Black")
                    ch21.place(x=740, y=300)
                    ch31 = Checkbutton(w, text="Rest\nstop hygiene  ", font=("Lucida Calligraphy", 8), bg="#d0f9f9",
                                       fg="Black")
                    ch31.place(x=855, y=260)
                    ch41 = Checkbutton(w, text="Change\nof bus ", font=("Lucida Calligraphy", 8), bg="#d0f9f9",
                                       fg="Black")
                    ch41.place(x=860, y=300)
                    ch51 = Checkbutton(w, text="Blanket", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black")
                    ch51.place(x=960, y=270)
                    ch61 = Checkbutton(w, text="Live tracking  ", font=("Lucida Calligraphy", 10), bg="#d0f9f9",
                                       fg="Black")
                    ch61.place(x=960, y=300)

                    def Sub1():
                        Re5.destroy()
                        Re1.destroy()
                        Re2.destroy()
                        ch11.destroy()
                        ch21.destroy()
                        ch31.destroy()
                        ch41.destroy()
                        ch51.destroy()
                        ch61.destroy()
                        Sub.destroy()
                        Th1 = Label(w, text="Thanks for your Feedback", font=("Lucida Calligraphy", 22), bg="#d0f9f9",
                                    fg="Black")
                        Th1.place(x=250, y=280)
                        Th11 = Label(w, text="We'd Surely look upoon the same", font=("Lucida Calligraphy", 15),
                                     bg="#d0f9f9", fg="Black")
                        Th11.place(x=680, y=310)
                        Re.after(5000, lambda: Re.destroy())
                        Th1.after(5000, lambda: Th1.destroy())
                        Th11.after(5000, lambda: Th11.destroy())

                    Sub = Button(w, text="Submit", font=("Lucida Calligraphy", 10), bg="#d0f9f9", fg="Black",
                                 command=Sub1)
                    Sub.place(x=1110, y=290)

                Re4 = Button(w, text="Could Be Better", font=("Times New Roman", 17), bg="#d0f9f9", fg="Black",
                             command=dislike)
                Re4.place(x=900, y=270)
                Re5 = Label(w, text="We Love your Feedback", font=("Lucida Calligraphy", 15), bg="#d0f9f9", fg="Black")
                Re5.place(x=450, y=315)

            B6 = Button(w, text="Drop A review", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black",
                        relief="raised", command=rew)
            B6.place(x=675, y=215)

            def cancel():
                if r1 == Li1[0]:
                    Back1.place(x=227, y=250)
                    B21.place(x=1225, y=100)
                elif r1 == Li1[1]:
                    Back2.place(x=227, y=250)
                    B41.place(x=1225, y=100)
                elif r1 == Li1[2]:
                    Back3.place(x=227, y=250)
                    B51.place(x=1225, y=100)
                elif r1 == Li1[3]:
                    Back4.place(x=227, y=250)
                    B61.place(x=1225, y=100)
                Cp = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                Cp.place(x=225, y=250, height=100, width=1000)
                cp1 = Label(w,
                            text="* Cancellation charges are computed on a per seat basis. Above cancellation fare is calculated based on seat fare of 399",
                            font=("Arial Bold", 10), bg="#d0f9f9", fg="Black")
                cp1.place(x=240, y=280)
                cp2 = Label(w,
                            text="* Cancellation charges are calculated based on service start date + time at :11-06-2020 06:00",
                            font=("Arial Bold", 10), bg="#d0f9f9", fg="Black")
                cp2.place(x=240, y=300)
                cp3 = Label(w,
                            text="* Ticket cannot be cancelled after scheduled bus departure time from the first boarding point",
                            font=("Arial Bold", 10), bg="#d0f9f9", fg="Black")
                cp3.place(x=240, y=320)

                def back():
                    back.destroy()
                    Back1.place_forget()
                    Back2.place_forget()
                    Back3.place_forget()
                    Back4.place_forget()
                    B21.place_forget()
                    B41.place_forget()
                    B51.place_forget()
                    B61.place_forget()
                    Back11.place_forget()
                    Back21.place_forget()
                    Back31.place_forget()
                    Back41.place_forget()

                    Cp.place_forget()
                    cp1.place_forget()
                    cp3.place_forget()
                    cp2.place_forget()
                    B7.place_forget()
                    back.destroy()

                back = Button(w, text="Back", font=("Algerian", 17), bg="red", fg="Black", command=back)
                back.place(x=10, y=60)

            B7 = Button(w, text="Cancellation Policy", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black",
                        relief="raised", command=cancel)
            B7.place(x=785, y=215)

            def cont():
                Co = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                Co.place(x=1222, y=642, height=150, width=306)
                if r1 == Li1[0]:
                    Back1.place(x=227, y=250)
                    B21.place(x=1225, y=100)
                    co1 = Label(w, text="Contact -\n Nationaltravels.india\n@gmail.com",
                                font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                    co1.place(x=1237, y=665)
                    co2 = Label(w, text="Eagerly waitiong for your response", font=("Lucida Handwriting", 10),
                                bg="#d0f9f9", fg="Black")
                    co2.place(x=1237, y=730)

                elif r1 == Li1[1]:
                    Back2.place(x=227, y=250)
                    B41.place(x=1225, y=100)
                    co1 = Label(w, text="Contact - Evacaytravels.india\n@gmail.com", font=("Lucida Handwriting", 12),
                                bg="#d0f9f9", fg="Black")
                    co1.place(x=1227, y=665)
                    co2 = Label(w, text="Eagerly waitiong for your response", font=("Lucida Handwriting", 10),
                                bg="#d0f9f9", fg="Black")
                    co2.place(x=1237, y=730)
                elif r1 == Li1[2]:
                    Back3.place(x=227, y=250)
                    B51.place(x=1225, y=100)
                    co1 = Label(w, text="Contact - Sharmatravels.india\n@gmail.com", font=("Lucida Handwriting", 12),
                                bg="#d0f9f9", fg="Black")
                    co1.place(x=1227, y=665)
                    co2 = Label(w, text="Eagerly waitiong for your response", font=("Lucida Handwriting", 10),
                                bg="#d0f9f9", fg="Black")
                    co2.place(x=1237, y=730)
                elif r1 == Li1[3]:
                    Back4.place(x=227, y=250)
                    B61.place(x=1225, y=100)
                    co1 = Label(w, text="Contact - asianexpress.india\n@gmail.com", font=("Lucida Handwriting", 12),
                                bg="#d0f9f9", fg="Black")
                    co1.place(x=1227, y=665)
                    co2 = Label(w, text="Eagerly waitiong for your response", font=("Lucida Handwriting", 10),
                                bg="#d0f9f9", fg="Black")
                    co2.place(x=1237, y=730)

                def back():
                    back.destroy()
                    Back1.place_forget()
                    Back2.place_forget()
                    Back3.place_forget()
                    Back4.place_forget()
                    B21.place_forget()
                    B41.place_forget()
                    B51.place_forget()
                    B61.place_forget()
                    Back11.place_forget()
                    Back21.place_forget()
                    Back31.place_forget()
                    Back41.place_forget()

                    co1.place_forget()
                    co2.place_forget()
                    Co.place_forget()
                    back.destroy()

                back = Button(w, text="Back", font=("Algerian", 17), bg="red", fg="Black", command=back)
                back.place(x=10, y=60)

            B8 = Button(w, text="Contact", font=("Times New Roman", 13), bg="#d0f9f9", fg="Black", relief="raised",
                        command=cont)
            B8.place(x=932, y=215)

            def seats():
                ss1 = ["Gray", "#d0f9f9"]
                rs1 = random.choice(ss1)
                ss2 = ["Gray", "#d0f9f9"]
                rs2 = random.choice(ss2)
                ss3 = ["Gray", "#d0f9f9"]
                rs3 = random.choice(ss3)
                ss31 = ["Gray", "#d0f9f9"]
                rs31 = random.choice(ss31)
                ss4 = ["Gray", "#d0f9f9"]
                rs4 = random.choice(ss4)
                ss5 = ["Gray", "#d0f9f9"]
                rs5 = random.choice(ss5)
                ss6 = ["Gray", "#d0f9f9"]
                rs6 = random.choice(ss6)
                ss7 = ["Gray", "#d0f9f9"]
                rs7 = random.choice(ss7)
                ss8 = ["Gray", "#d0f9f9"]
                rs8 = random.choice(ss8)
                ss9 = ["Gray", "#d0f9f9"]
                rs9 = random.choice(ss9)
                ss10 = ["Gray", "#d0f9f9"]
                rs10 = random.choice(ss10)
                ss11 = ["Gray", "#d0f9f9"]
                rs11 = random.choice(ss11)
                ss12 = ["Gray", "#d0f9f9"]
                rs12 = random.choice(ss12)
                ss13 = ["Gray", "#d0f9f9"]
                rs13 = random.choice(ss13)
                ss14 = ["Gray", "#d0f9f9"]
                rs14 = random.choice(ss14)
                ss15 = ["Gray", "#d0f9f9"]
                rs15 = random.choice(ss15)
                ss16 = ["Gray", "#d0f9f9"]
                rs16 = random.choice(ss16)
                ss17 = ["Gray", "#d0f9f9"]
                rs17 = random.choice(ss17)
                ss18 = ["Gray", "#d0f9f9"]
                rs18 = random.choice(ss18)
                ss19 = ["Gray", "#d0f9f9"]
                rs19 = random.choice(ss19)
                ss20 = ["Gray", "#d0f9f9"]
                rs20 = random.choice(ss20)
                ss21 = ["Gray", "#d0f9f9"]
                rs21 = random.choice(ss21)
                ss22 = ["Gray", "#d0f9f9"]
                rs22 = random.choice(ss22)
                s = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                s.place(x=5, y=100, height=690, width=215)
                steer = Label(w, text="Driver", font=("Lucida Handwriting", 11), bg="#d0f9f9", fg="Black", bd=1,
                              relief="solid")
                steer.place(x=135, y=210)
                line = Label(w, text="----------------------------------", bg="#d0f9f9")
                line.place(x=20, y=240)
                pa = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                pa.place(x=75, y=270, height=475, width=25)
                gr = Label(w, bd=1, relief="solid", bg="Gray")
                gr.place(x=30, y=755, height=15, width=15)
                gr1 = Label(w, text="Booked", font=("Lucida Handwriting", 10), bg="#d0f9f9", fg="Black")
                gr1.place(x=50, y=750)
                ngr = Label(w, bd=1, relief="solid", bg="#d0f9f9")
                ngr.place(x=120, y=755, height=15, width=15)
                ngr1 = Label(w, text="Vacant", font=("Lucida Handwriting", 10), bg="#d0f9f9", fg="Black")
                ngr1.place(x=140, y=750)
                sel = Label(w, text="Choose your \nSeats", font=("Lucida Handwriting", 16), bg="#d0f9f9", fg="Black")
                sel.place(x=30, y=120)
                p = Label(w, text="P", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                p.place(x=78, y=300)
                a = Label(w, text="A", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                a.place(x=78, y=370)
                s = Label(w, text="S", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                s.place(x=78, y=430)
                s1 = Label(w, text="S", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                s1.place(x=78, y=500)
                a1 = Label(w, text="A", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                a1.place(x=78, y=570)
                g = Label(w, text="G", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                g.place(x=78, y=630)
                e = Label(w, text="E", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black")
                e.place(x=78, y=700)

                def pro():
                    pr1 = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                    pr1.place(x=227, y=250, height=542, width=1000)
                    e1 = Label(w, text="Choose your Boarding & dropping points", font=("Script Mt bold", 18),
                               bg="#d0f9f9", fg="Black")
                    e1.place(x=235, y=265)
                    pr2 = Label(w, text="<----- Enter Boarding Point", font=("Script Mt bold", 15), bg="#d0f9f9",
                                fg="Black")
                    pr2.place(x=520, y=315)
                    tn = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                    tn.place(x=235, y=315, height=35)

                    def her():
                        nonlocal tn
                        yx = tn.get()
                        pr4231 = Label(w, text="Done", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                        pr4231.place(x=735, y=350)

                    pr421 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black", command=her)
                    pr421.place(x=235, y=350)

                    def here():
                        nonlocal tn
                        yx = tn.get()
                        pr4232 = Label(w, text="Done", font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                        pr4232.place(x=735, y=450)

                    pr422 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black", command=here)
                    pr422.place(x=235, y=450)

                    pr3 = Label(w, text="<----- Enter Dropping Point", font=("Script Mt bold", 15), bg="#d0f9f9",
                                fg="Black")
                    pr3.place(x=520, y=415)
                    tn1 = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                    tn1.place(x=235, y=415, height=35)
                    tn1.focus()

                    y2 = tn1.get()

                    def click():
                        y = "You have Choosed Seats  - " + combof.get()
                        ap = combof.get()

                        L.remove(ap)
                        pr42 = Label(w, text=y, font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                        pr42.place(x=235, y=515)

                    x = ""
                    combof = Combobox(w, textvariable=x)
                    combof['values'] = L
                    combof.place(x=685, y=515)
                    combo1 = Button(w, text="Select", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black", bd=2,
                                    relief="solid", command=click)
                    combo1.place(x=835, y=515)
                    x1 = "Please Confirm your Seats - "
                    pr4 = Label(w, text=x1, font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                    pr4.place(x=235, y=515)

                    def more():
                        pr5a.destroy()

                        def click():
                            y = "You have Choosed Seats now - " + comboff.get() + " & " + combof.get()
                            pr42 = Label(w, text=y, font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                            pr42.place(x=235, y=690)
                            pr51 = Label(w, text="Maximum 2 seats can be chosed at a time", font=("Algerian", 15),
                                         bg="#d0f9f9", fg="Black")
                            pr51.place(x=235, y=730)

                            def ppr():
                                nonlocal tn
                                yx = tn.get()
                                nonlocal tn1
                                yy = tn1.get()
                                pr1a = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                                pr1a.place(x=227, y=250, height=542, width=1000)
                                pr61 = Label(w, text="Fill your Personal Details", font=("Script Mt bold", 18),
                                             bg="#d0f9f9", fg="Black")
                                pr61.place(x=235, y=265)
                                pr4211 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                                command=her)
                                pr4211.place(x=235, y=350)

                                def here1():
                                    nonlocal Number
                                    yx1 = Number.get()
                                    N = yx1
                                    l = len(N)
                                    if l == 12:
                                        if N[3] == "-" and N[7] == "-":
                                            pr4232 = Label(w, text="Correct Format", font=("Algerian", 15),
                                                           bg="#d0f9f9", fg="Black")
                                            pr4232.place(x=535, y=500)
                                            pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15),
                                                            bg="#d0f9f9", fg="Black")
                                            pr4232a.place(x=535, y=530)
                                            Number.config(state="disabled")
                                            Number.after(3000, lambda: Number.config(state="normal"))
                                            pr4232.after(3000, lambda: pr4232.destroy())
                                            pr4232a.destroy()
                                        else:
                                            pr4232 = Label(w, text="Dashes At Unexpected Places", font=("Algerian", 15),
                                                           bg="#d0f9f9", fg="Black")
                                            pr4232.place(x=535, y=500)
                                            pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15),
                                                            bg="#d0f9f9", fg="Black")
                                            pr4232a.place(x=535, y=530)
                                            Number.config(state="disabled")
                                            Number.after(3000, lambda: Number.config(state="normal"))
                                            pr4232.after(3000, lambda: pr4232.destroy())
                                            pr4232a.destroy()
                                        if N[0:3].isdigit():
                                            if N[4:7].isdigit():
                                                if N[8:12].isdigit():
                                                    pr4232 = Label(w, text="Done!!!! Now Proceed",
                                                                   font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                                                    pr4232.place(x=535, y=500)
                                                    pr4232.after(3000, lambda: pr4232.destroy())
                                                    pr42322.destroy()
                                                    pr7 = Label(w, text="<----- Please Enter your Contact Number",
                                                                font=("Script Mt bold", 18), bg="#d0f9f9", fg="Black")
                                                    pr7.place(x=520, y=415)
                                                    pr42322x = Label(w, text=" Fare - 650 INR", font=("Algerian", 15),
                                                                     bg="#d0f9f9", fg="Black")
                                                    pr42322x.place(x=235, y=580)

                                                    def Thank():

                                                        pr1ax = Label(w, text="Making the Magic Happen...",
                                                                      font=("Algerian", 40), bd=2, relief="solid",
                                                                      bg="#d0f9f9")
                                                        pr1ax.place(x=227, y=250, height=542, width=1000)
                                                        pr1axx = Label(w,
                                                                       text="Kindly take the screenshot of the invoice for further references",
                                                                       font=("Algerian", 15), bg="#d0f9f9")
                                                        pr1axx.place(x=230, y=400)

                                                        def thnk():
                                                            nonlocal Name
                                                            k1 = Name.get()
                                                            nonlocal Number
                                                            k2 = Number.get()
                                                            nonlocal tn
                                                            k3 = tn.get()
                                                            nonlocal tn1
                                                            k4 = tn1.get()
                                                            nonlocal lat
                                                            k5 = lat
                                                            nonlocal lat1
                                                            k6 = lat1

                                                            w3 = Tk()
                                                            w3 = Toplevel()

                                                            w3.geometry('2000x1000')
                                                            w3.config(bg="White")
                                                            k = photo
                                                            l = Button(w3, text='Let Some Memories Be forever', image=k,
                                                                       ).place(x=1, y=1)
                                                            a = Label(w3, text=k1, font=("Lucida Handwriting", 40),
                                                                      bg="#f1f1ee", fg="#242222")
                                                            a.place(x=210, y=200)
                                                            a1 = Label(w3, text=k2, font=("Lucida Handwriting", 35),
                                                                       bg="#f1f1ee", fg="#242222")
                                                            a1.place(x=430, y=270)
                                                            a1 = Label(w3, text=k3, font=("Lucida Handwriting", 28),
                                                                       bg="#f1f1ee", fg="#242222")
                                                            a1.place(x=345, y=380)
                                                            a1 = Label(w3, text=k4, font=("Lucida Handwriting", 28),
                                                                       bg="#f1f1ee", fg="#242222")
                                                            a1.place(x=345, y=490)
                                                            a2 = Label(w3, text=k5, font=("Lucida Handwriting", 28),
                                                                       bg="#f1f1ee", fg="#242222")
                                                            a2.place(x=870, y=380)
                                                            a3 = Label(w3, text=k6, font=("Lucida Handwriting", 28),
                                                                       bg="#f1f1ee", fg="#242222")
                                                            a3.place(x=870, y=490)
                                                            if r1 == Li1[0]:
                                                                a4 = Label(w3, text=Li1[0],
                                                                           font=("Lucida Handwriting", 28),
                                                                           bg="#f1f1ee", fg="#242222")
                                                                a4.place(x=250, y=580)
                                                            elif r1 == Li1[1]:
                                                                a4 = Label(w3, text=Li1[1],
                                                                           font=("Lucida Handwriting", 28),
                                                                           bg="#f1f1ee", fg="#242222")
                                                                a4.place(x=250, y=580)
                                                            elif r1 == Li1[2]:
                                                                a4 = Label(w3, text=Li1[2],
                                                                           font=("Lucida Handwriting", 28),
                                                                           bg="#f1f1ee", fg="#242222")
                                                                a4.place(x=250, y=580)
                                                            elif r1 == Li1[3]:
                                                                a4 = Label(w3, text=Li1[3],
                                                                           font=("Lucida Handwriting", 28),
                                                                           bg="#f1f1ee", fg="#242222")
                                                                a4.place(x=250, y=580)
                                                            a5 = Label(w3, text="650 INR",
                                                                       font=("Lucida Handwriting", 28), bg="#f1f1ee",
                                                                       fg="#242222")
                                                            a5.place(x=200, y=650)
                                                            k7 = "650 INR"
                                                            a6 = Label(w3,
                                                                       text="For Security Provisions Number will be sent to your Registered Mobile Number",
                                                                       font=("Lucida Handwriting", 15), bg="#f1f1ee",
                                                                       fg="#242222")
                                                            a6.place(x=210, y=720)
                                                            nonlocal combof

                                                            combo = combof.get()
                                                            combox = comboff.get()

                                                            s1 = Label(w3, text="A", bg="Light Blue")
                                                            s1.place(x=1125, y=270, height=20, width=25)
                                                            s2 = Label(w3, text="B", bg="Light Blue")
                                                            s2.place(x=1125, y=310, height=20, width=25)
                                                            s3 = Label(w3, text="C", bg="Light Blue")
                                                            s3.place(x=1125, y=350, height=20, width=25)
                                                            s4 = Label(w3, text="D", bg="Light Blue")
                                                            s4.place(x=1125, y=390, height=20, width=25)
                                                            s5 = Label(w3, text="E", bg="Light Blue")
                                                            s5.place(x=1125, y=430, height=20, width=25)
                                                            s6 = Label(w3, text="F", bg="Light Blue")
                                                            s6.place(x=1125, y=470, height=20, width=25)
                                                            s7 = Label(w3, text="G", bg="Light Blue")
                                                            s7.place(x=1125, y=510, height=20, width=25)
                                                            s8 = Label(w3, text="H", bg="Light Blue")
                                                            s8.place(x=1125, y=550, height=20, width=25)
                                                            s1r = Label(w3, text="1", bg="Light Blue")
                                                            s1r.place(x=1235, y=270, height=20, width=25)
                                                            s2r = Label(w3, text="3", bg="Light Blue")
                                                            s2r.place(x=1235, y=310, height=20, width=25)
                                                            s3r = Label(w3, text="5", bg="Light Blue")
                                                            s3r.place(x=1235, y=350, height=20, width=25)
                                                            s4r = Label(w3, text="7", bg="Light Blue")
                                                            s4r.place(x=1235, y=390, height=20, width=25)
                                                            s5r = Label(w3, text="9", bg="Light Blue")
                                                            s5r.place(x=1235, y=430, height=20, width=25)
                                                            s6r = Label(w3, text="11", bg="Light Blue")
                                                            s6r.place(x=1235, y=470, height=20, width=25)
                                                            s7r = Label(w3, text="13", bg="Light Blue")
                                                            s7r.place(x=1235, y=510, height=20, width=25)
                                                            s8r = Label(w3, text="15", bg="Light Blue")
                                                            s8r.place(x=1235, y=550, height=20, width=25)
                                                            s1rr = Label(w3, text="2", bg="Light Blue")
                                                            s1rr.place(x=1290, y=270, height=20, width=25)
                                                            s2rr = Label(w3, text="4", bg="Light Blue")
                                                            s2rr.place(x=1290, y=310, height=20, width=25)
                                                            s3rr = Label(w3, text="6", bg="Light Blue")
                                                            s3rr.place(x=1290, y=350, height=20, width=25)
                                                            s4rr = Label(w3, text="8", bg="Light Blue")
                                                            s4rr.place(x=1290, y=390, height=20, width=25)
                                                            s5rr = Label(w3, text="10", bg="Light Blue")
                                                            s5rr.place(x=1290, y=430, height=20, width=25)
                                                            s6rr = Label(w3, text="12", bg="Light Blue")
                                                            s6rr.place(x=1290, y=470, height=20, width=25)
                                                            s7rr = Label(w3, text="14", bg="Light Blue")
                                                            s7rr.place(x=1290, y=510, height=20, width=25)
                                                            s8rr = Label(w3, text="16", bg="Light Blue")
                                                            s8rr.place(x=1290, y=550, height=20, width=25)
                                                            pa = Label(w3, bd=2, relief="solid", bg="Light Blue")
                                                            pa.place(x=1180, y=270, height=300, width=25)
                                                            p = Label(w3, text="P", font=("Lucida Handwriting", 11),
                                                                      bg="Light Blue", fg="Black")
                                                            p.place(x=1185, y=300)
                                                            a = Label(w3, text="A", font=("Lucida Handwriting", 11),
                                                                      bg="Light Blue", fg="Black")
                                                            a.place(x=1185, y=330)
                                                            s = Label(w3, text="S", font=("Lucida Handwriting", 11),
                                                                      bg="Light Blue", fg="Black")
                                                            s.place(x=1185, y=360)
                                                            s1 = Label(w3, text="S", font=("Lucida Handwriting", 11),
                                                                       bg="Light Blue", fg="Black")
                                                            s1.place(x=1185, y=390)
                                                            a1 = Label(w3, text="A", font=("Lucida Handwriting", 11),
                                                                       bg="Light Blue", fg="Black")
                                                            a1.place(x=1185, y=420)
                                                            g = Label(w3, text="G", font=("Lucida Handwriting", 11),
                                                                      bg="Light Blue", fg="Black")
                                                            g.place(x=1185, y=450)
                                                            e = Label(w3, text="E", font=("Lucida Handwriting", 11),
                                                                      bg="Light Blue", fg="Black")
                                                            e.place(x=1185, y=480)
                                                            if combo == "A":
                                                                s1.config(bg="Orange")
                                                            if combo == "B":
                                                                s2.config(bg="Orange")
                                                            if combo == "C":
                                                                s3.config(bg="Orange")
                                                            if combo == "D":
                                                                s4.config(bg="Orange")
                                                            if combo == "E":
                                                                s5.config(bg="Orange")
                                                            if combo == "F":
                                                                s6.config(bg="Orange")
                                                            if combo == "G":
                                                                s7.config(bg="Orange")
                                                            if combo == "H":
                                                                s8.config(bg="Orange")
                                                            if combo == "1":
                                                                s1r.config(bg="Orange")
                                                            if combo == "2":
                                                                s1rr.config(bg="Orange")
                                                            if combo == "3":
                                                                s2r.config(bg="Orange")
                                                            if combo == "4":
                                                                s2rr.config(bg="Orange")
                                                            if combo == "5":
                                                                s3r.config(bg="Orange")
                                                            if combo == "6":
                                                                s3rr.config(bg="Orange")
                                                            if combo == "7":
                                                                s4r.config(bg="Orange")
                                                            if combo == "8":
                                                                s4rr.config(bg="Orange")
                                                            if combo == "9":
                                                                s5r.config(bg="Orange")
                                                            if combo == "10":
                                                                s5rr.config(bg="Orange")
                                                            if combo == "11":
                                                                s6r.config(bg="Orange")
                                                            if combo == "12":
                                                                s6rr.config(bg="Orange")
                                                            if combo == "13":
                                                                s7r.config(bg="Orange")
                                                            if combo == "14":
                                                                s7rr.config(bg="Orange")
                                                            if combo == "15":
                                                                s8r.config(bg="Orange")
                                                            if combo == "16":
                                                                s8rr.config(bg="Orange")

                                                            if combox == "A":
                                                                s1.config(bg="Orange")
                                                            if combox == "B":
                                                                s2.config(bg="Orange")
                                                            if combox == "C":
                                                                s3.config(bg="Orange")
                                                            if combox == "D":
                                                                s4.config(bg="Orange")
                                                            if combox == "E":
                                                                s5.config(bg="Orange")
                                                            if combox == "F":
                                                                s6.config(bg="Orange")
                                                            if combox == "G":
                                                                s7.config(bg="Orange")
                                                            if combox == "H":
                                                                s8.config(bg="Orange")
                                                            if combox == "1":
                                                                s1r.config(bg="Orange")
                                                            if combox == "2":
                                                                s1rr.config(bg="Orange")
                                                            if combox == "3":
                                                                s2r.config(bg="Orange")
                                                            if combox == "4":
                                                                s2rr.config(bg="Orange")
                                                            if combox == "5":
                                                                s3r.config(bg="Orange")
                                                            if combox == "6":
                                                                s3rr.config(bg="Orange")
                                                            if combox == "7":
                                                                s4r.config(bg="Orange")
                                                            if combox == "8":
                                                                s4rr.config(bg="Orange")
                                                            if combox == "9":
                                                                s5r.config(bg="Orange")
                                                            if combox == "10":
                                                                s5rr.config(bg="Orange")
                                                            if combox == "11":
                                                                s6r.config(bg="Orange")
                                                            if combox == "12":
                                                                s6rr.config(bg="Orange")
                                                            if combox == "13":
                                                                s7r.config(bg="Orange")
                                                            if combox == "14":
                                                                s7rr.config(bg="Orange")
                                                            if combox == "15":
                                                                s8r.config(bg="Orange")
                                                            if combox == "16":
                                                                s8rr.config(bg="Orange")

                                                            BusNo = ["MH-43-AS-1000", "MH-43-AS-1100", "MH-43-AS-1200",
                                                                     "MH-43-AS-1050", "MH-43-AS-1005", "MH-43-AS-5000",
                                                                     "MH-03-AS-1000", "MH-43-AS-1540", "MH-43-AS-1054"
                                                                                                       "MH-43-AS-8989",
                                                                     "MH-43-AS-1555", "MH-43-AS-1654", "MH-43-AS-1564",
                                                                     "MH-43-AS-1464", "MH-43-AS-4654", "MH-43-AS-1050",
                                                                     "MH-43-AZ-1000", "MH-43-AS-1505"]
                                                            bn = random.choice(BusNo)
                                                            combo = combof.get()
                                                            combox = comboff.get()
                                                            j = Number.get()
                                                            jx = j[0:3] + j[4:7] + j[8:]
                                                            print(jx)
                                                            d = combo + " & " + combox
                                                            m = "\nTravel India \nThis is Your Invoice\nName - " + k1 + " \nSource - " + k3 + " \nDestination - " + k4 + " \n On - " + k5 + " \nReturn - " + k6 + "\nFare - " + k7 + " \nBus No - " + bn + "\nSeat No - " + d + " \n Thanks for Booking \nAn Effort By Kailash's Creation"
                                                            m1 = "sender_id=FSTSMS&message=" + m + "&language=english&route=p&numbers=" + jx
                                                            import requests
                                                            url = "https://www.fast2sms.com/dev/bulk"
                                                            payload = m1
                                                            headers = {
                                                                'authorization': "k0jB9RUYogPnCitNscAwd7zXZ5MVh28SfJ6yrLKETaIlbquDx4paeSDzTlso8cr2Rm9Ad7G5yqgJKtYk",
                                                                'Content-Type': "application/x-www-form-urlencoded",
                                                                'Cache-Control': "no-cache",
                                                            }
                                                            response = requests.request("POST", url, data=payload,
                                                                                        headers=headers)
                                                            print(response.text)
                                                            w3.geometry('2000x1000')
                                                            w3.mainloop()

                                                        thnkx = Button(w, text=" View my receipt",
                                                                       font=("Algerian", 18), bg="#d0f9f9", fg="Black",
                                                                       command=thnk)
                                                        thnkx.place(x=650, y=650)
                                                        thnkx.config(state="disabled")
                                                        thnkx.after(4000, lambda: thnkx.config(state="active"))

                                                    pr4221x = Button(w, text=" I aggre to Rules \nProceed to BOOK",
                                                                     font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                                                     command=Thank)
                                                    pr4221x.place(x=235, y=650)
                                    elif l != 12:
                                        pr4232 = Label(w, text="Number Exceeds the Limited characters allowed",
                                                       font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                                        pr4232.place(x=535, y=500)
                                        pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15),
                                                        bg="#d0f9f9", fg="Black")
                                        pr4232a.place(x=535, y=530)
                                        Number.config(state="disabled")
                                        Number.after(3000, lambda: Number.config(state="normal"))
                                        pr4232.after(3000, lambda: pr4232.destroy())
                                        pr4232a.after(3000, lambda: pr4232a.destroy())
                                    else:
                                        pr4232 = Label(w, text="You Entered Something other than a Number. Right??",
                                                       font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                                        pr4232.place(x=535, y=500)
                                        pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15),
                                                        bg="#d0f9f9", fg="Black")
                                        pr4232a.place(x=535, y=530)
                                        Number.config(state="disabled")
                                        Number.after(3000, lambda: Number.config(state="normal"))
                                        pr4232.after(3000, lambda: pr4232.destroy())
                                        pr4232a.after(3000, lambda: pr4232a.destroy())

                                pr42322 = Label(w, text="Correct Format is XXX-XXX-XXXX", font=("Algerian", 15),
                                                bg="#d0f9f9", fg="Black")
                                pr42322.place(x=235, y=580)
                                pr4221 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                                command=here1)
                                pr4221.place(x=235, y=450)
                                pr6 = Label(w, text="<----- Please Enter Your Name", font=("Script Mt bold", 18),
                                            bg="#d0f9f9", fg="Black")
                                pr6.place(x=520, y=315)
                                pr7 = Label(w, text="<----- Please Enter your Contact Number",
                                            font=("Script Mt bold", 18), bg="#d0f9f9", fg="Black")
                                pr7.place(x=520, y=415)
                                Name = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                                Name.place(x=235, y=315, height=35)
                                Number = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                                Number.place(x=235, y=415, height=35)
                                Number.focus()

                            pr52 = Button(w, text="Lets Proceed", font=("Algerian", 15), bg="Light Green", fg="Black",
                                          command=ppr)
                            pr52.place(x=835, y=730)

                        pr41 = Label(w, text="Please Select from Options Below", font=("Algerian", 15), bg="#d0f9f9",
                                     fg="Black")
                        pr41.place(x=235, y=605)
                        x = ""
                        comboff = Combobox(w, textvariable=x)
                        comboff['values'] = L
                        comboff.place(x=235, y=650)
                        combo1 = Button(w, text="Select", font=("Lucida Handwriting", 12), bg="#d0f9f9", fg="Black",
                                        bd=2, relief="solid", command=click)
                        combo1.place(x=385, y=650)

                    pr5 = Button(w, text="Wanna choose More Seats", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                 command=more)
                    pr5.place(x=235, y=550)

                    def ppr():

                        nonlocal tn
                        yx = tn.get()
                        nonlocal tn1
                        yy = tn1.get()

                        pr1a = Label(w, bd=2, relief="solid", bg="#d0f9f9")
                        pr1a.place(x=227, y=250, height=542, width=1000)
                        pr61 = Label(w, text="Fill your Personal Details", font=("Script Mt bold", 18), bg="#d0f9f9",
                                     fg="Black")
                        pr61.place(x=235, y=265)
                        pr42322 = Label(w, text="Correct Format is XXX-XXX-XXXX", font=("Algerian", 15), bg="#d0f9f9",
                                        fg="Black")
                        pr42322.place(x=235, y=580)
                        pr61 = Label(w, text="Fill your Personal Details", font=("Script Mt bold", 18), bg="#d0f9f9",
                                     fg="Black")
                        pr61.place(x=235, y=265)
                        pr4211 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                        command=her)
                        pr4211.place(x=235, y=350)

                        def here1():
                            nonlocal Number
                            yx1 = Number.get()
                            N = yx1
                            l = len(N)
                            pr52.destroy()
                            if l == 12:
                                if N[3] == "-" and N[7] == "-":
                                    pr4232 = Label(w, text="Correct Format", font=("Algerian", 15), bg="#d0f9f9",
                                                   fg="Black")
                                    pr4232.place(x=535, y=500)
                                    pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15), bg="#d0f9f9",
                                                    fg="Black")
                                    pr4232a.place(x=535, y=530)
                                    Number.config(state="disabled")
                                    Number.after(3000, lambda: Number.config(state="normal"))
                                    pr4232.after(3000, lambda: pr4232.destroy())
                                    pr4232a.destroy()
                                else:
                                    pr4232 = Label(w, text="Dashes At Unexpected Places", font=("Algerian", 15),
                                                   bg="#d0f9f9", fg="Black")
                                    pr4232.place(x=535, y=500)
                                    pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15), bg="#d0f9f9",
                                                    fg="Black")
                                    pr4232a.place(x=535, y=530)
                                    Number.config(state="disabled")
                                    Number.after(3000, lambda: Number.config(state="normal"))
                                    pr4232.after(3000, lambda: pr4232.destroy())
                                    pr4232a.destroy()
                                if N[0:3].isdigit():
                                    if N[4:7].isdigit():
                                        if N[8:12].isdigit():
                                            pr4232 = Label(w, text="Done!!!! Now Proceed", font=("Algerian", 15),
                                                           bg="#d0f9f9", fg="Black")
                                            pr4232.place(x=535, y=500)
                                            pr4232.after(3000, lambda: pr4232.destroy())
                                            pr42322.destroy()
                                            pr7 = Label(w, text="<----- Please Enter your Contact Number",
                                                        font=("Script Mt bold", 18), bg="#d0f9f9", fg="Black")
                                            pr7.place(x=520, y=415)
                                            pr42322x = Label(w, text=" Fare - 650 INR", font=("Algerian", 15),
                                                             bg="#d0f9f9", fg="Black")
                                            pr42322x.place(x=235, y=580)

                                            def Thank():

                                                pr1ax = Label(w, text="Making the Magic Happen...",
                                                              font=("Algerian", 40), bd=2, relief="solid", bg="#d0f9f9")
                                                pr1ax.place(x=227, y=250, height=542, width=1000)
                                                pr1axx = Label(w,
                                                               text="Kindly take the screenshot of the invoice for further references",
                                                               font=("Algerian", 15), bg="#d0f9f9")
                                                pr1axx.place(x=230, y=400)

                                                def thnk():
                                                    nonlocal Name
                                                    k1 = Name.get()
                                                    nonlocal Number
                                                    k2 = Number.get()
                                                    nonlocal tn
                                                    k3 = tn.get()
                                                    nonlocal tn1
                                                    k4 = tn1.get()
                                                    nonlocal lat

                                                    k5 = lat
                                                    nonlocal lat1
                                                    k6 = lat1

                                                    w3 = Tk()
                                                    w3 = Toplevel()

                                                    w3.geometry('2000x1000')
                                                    w3.config(bg="White")
                                                    k = photo
                                                    l = Button(w3, text='Let Some Memories Be forever', image=k,
                                                               ).place(x=1, y=1)
                                                    a = Label(w3, text=k1, font=("Lucida Handwriting", 40),
                                                              bg="#f1f1ee", fg="#242222")
                                                    a.place(x=210, y=200)
                                                    a1 = Label(w3, text=k2, font=("Lucida Handwriting", 35),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a1.place(x=430, y=270)
                                                    a1 = Label(w3, text=k3, font=("Lucida Handwriting", 28),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a1.place(x=345, y=380)
                                                    a1 = Label(w3, text=k4, font=("Lucida Handwriting", 28),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a1.place(x=345, y=490)
                                                    a2 = Label(w3, text=k5, font=("Lucida Handwriting", 28),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a2.place(x=870, y=380)
                                                    a3 = Label(w3, text=k6, font=("Lucida Handwriting", 28),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a3.place(x=870, y=490)

                                                    if r1 == Li1[0]:
                                                        a4 = Label(w3, text=Li1[0], font=("Lucida Handwriting", 28),
                                                                   bg="#f1f1ee", fg="#242222")
                                                        a4.place(x=250, y=580)
                                                    elif r1 == Li1[1]:
                                                        a4 = Label(w3, text=Li1[1], font=("Lucida Handwriting", 28),
                                                                   bg="#f1f1ee", fg="#242222")
                                                        a4.place(x=250, y=580)
                                                    elif r1 == Li1[2]:
                                                        a4 = Label(w3, text=Li1[2], font=("Lucida Handwriting", 28),
                                                                   bg="#f1f1ee", fg="#242222")
                                                        a4.place(x=250, y=580)
                                                    elif r1 == Li1[3]:
                                                        a4 = Label(w3, text=Li1[3], font=("Lucida Handwriting", 28),
                                                                   bg="#f1f1ee", fg="#242222")
                                                        a4.place(x=250, y=580)
                                                    a5 = Label(w3, text="650 INR", font=("Lucida Handwriting", 28),
                                                               bg="#f1f1ee", fg="#242222")
                                                    a5.place(x=200, y=650)
                                                    k7 = "650 INR"
                                                    a6 = Label(w3,
                                                               text="For Security Provisions Number will be sent to your Registered Mobile Number",
                                                               font=("Lucida Handwriting", 15), bg="#f1f1ee",
                                                               fg="#242222")
                                                    a6.place(x=210, y=720)
                                                    combo = combof.get()
                                                    combox = comboff.get()

                                                    s1 = Label(w3, text="A", bg="Light Blue")
                                                    s1.place(x=1125, y=270, height=20, width=25)
                                                    s2 = Label(w3, text="B", bg="Light Blue")
                                                    s2.place(x=1125, y=310, height=20, width=25)
                                                    s3 = Label(w3, text="C", bg="Light Blue")
                                                    s3.place(x=1125, y=350, height=20, width=25)
                                                    s4 = Label(w3, text="D", bg="Light Blue")
                                                    s4.place(x=1125, y=390, height=20, width=25)
                                                    s5 = Label(w3, text="E", bg="Light Blue")
                                                    s5.place(x=1125, y=430, height=20, width=25)
                                                    s6 = Label(w3, text="F", bg="Light Blue")
                                                    s6.place(x=1125, y=470, height=20, width=25)
                                                    s7 = Label(w3, text="G", bg="Light Blue")
                                                    s7.place(x=1125, y=510, height=20, width=25)
                                                    s8 = Label(w3, text="H", bg="Light Blue")
                                                    s8.place(x=1125, y=550, height=20, width=25)
                                                    s1r = Label(w3, text="1", bg="Light Blue")
                                                    s1r.place(x=1235, y=270, height=20, width=25)
                                                    s2r = Label(w3, text="3", bg="Light Blue")
                                                    s2r.place(x=1235, y=310, height=20, width=25)
                                                    s3r = Label(w3, text="5", bg="Light Blue")
                                                    s3r.place(x=1235, y=350, height=20, width=25)
                                                    s4r = Label(w3, text="7", bg="Light Blue")
                                                    s4r.place(x=1235, y=390, height=20, width=25)
                                                    s5r = Label(w3, text="9", bg="Light Blue")
                                                    s5r.place(x=1235, y=430, height=20, width=25)
                                                    s6r = Label(w3, text="11", bg="Light Blue")
                                                    s6r.place(x=1235, y=470, height=20, width=25)
                                                    s7r = Label(w3, text="13", bg="Light Blue")
                                                    s7r.place(x=1235, y=510, height=20, width=25)
                                                    s8r = Label(w3, text="15", bg="Light Blue")
                                                    s8r.place(x=1235, y=550, height=20, width=25)
                                                    s1rr = Label(w3, text="2", bg="Light Blue")
                                                    s1rr.place(x=1290, y=270, height=20, width=25)
                                                    s2rr = Label(w3, text="4", bg="Light Blue")
                                                    s2rr.place(x=1290, y=310, height=20, width=25)
                                                    s3rr = Label(w3, text="6", bg="Light Blue")
                                                    s3rr.place(x=1290, y=350, height=20, width=25)
                                                    s4rr = Label(w3, text="8", bg="Light Blue")
                                                    s4rr.place(x=1290, y=390, height=20, width=25)
                                                    s5rr = Label(w3, text="10", bg="Light Blue")
                                                    s5rr.place(x=1290, y=430, height=20, width=25)
                                                    s6rr = Label(w3, text="12", bg="Light Blue")
                                                    s6rr.place(x=1290, y=470, height=20, width=25)
                                                    s7rr = Label(w3, text="14", bg="Light Blue")
                                                    s7rr.place(x=1290, y=510, height=20, width=25)
                                                    s8rr = Label(w3, text="16", bg="Light Blue")
                                                    s8rr.place(x=1290, y=550, height=20, width=25)
                                                    pa = Label(w3, bd=2, relief="solid", bg="Light Blue")
                                                    pa.place(x=1180, y=270, height=300, width=25)
                                                    p = Label(w3, text="P", font=("Lucida Handwriting", 11),
                                                              bg="Light Blue", fg="Black")
                                                    p.place(x=1185, y=300)
                                                    a = Label(w3, text="A", font=("Lucida Handwriting", 11),
                                                              bg="Light Blue", fg="Black")
                                                    a.place(x=1185, y=330)
                                                    s = Label(w3, text="S", font=("Lucida Handwriting", 11),
                                                              bg="Light Blue", fg="Black")
                                                    s.place(x=1185, y=360)
                                                    s1 = Label(w3, text="S", font=("Lucida Handwriting", 11),
                                                               bg="Light Blue", fg="Black")
                                                    s1.place(x=1185, y=390)
                                                    a1 = Label(w3, text="A", font=("Lucida Handwriting", 11),
                                                               bg="Light Blue", fg="Black")
                                                    a1.place(x=1185, y=420)
                                                    g = Label(w3, text="G", font=("Lucida Handwriting", 11),
                                                              bg="Light Blue", fg="Black")
                                                    g.place(x=1185, y=450)
                                                    e = Label(w3, text="E", font=("Lucida Handwriting", 11),
                                                              bg="Light Blue", fg="Black")
                                                    e.place(x=1185, y=480)
                                                    if combo == "A":
                                                        s1.config(bg="Orange")
                                                    if combo == "B":
                                                        s2.config(bg="Orange")
                                                    if combo == "C":
                                                        s3.config(bg="Orange")
                                                    if combo == "D":
                                                        s4.config(bg="Orange")
                                                    if combo == "E":
                                                        s5.config(bg="Orange")
                                                    if combo == "F":
                                                        s6.config(bg="Orange")
                                                    if combo == "G":
                                                        s7.config(bg="Orange")
                                                    if combo == "H":
                                                        s8.config(bg="Orange")
                                                    if combo == "1":
                                                        s1r.config(bg="Orange")
                                                    if combo == "2":
                                                        s1rr.config(bg="Orange")
                                                    if combo == "3":
                                                        s2r.config(bg="Orange")
                                                    if combo == "4":
                                                        s2rr.config(bg="Orange")
                                                    if combo == "5":
                                                        s3r.config(bg="Orange")
                                                    if combo == "6":
                                                        s3rr.config(bg="Orange")
                                                    if combo == "7":
                                                        s4r.config(bg="Orange")
                                                    if combo == "8":
                                                        s4rr.config(bg="Orange")
                                                    if combo == "9":
                                                        s5r.config(bg="Orange")
                                                    if combo == "10":
                                                        s5rr.config(bg="Orange")
                                                    if combo == "11":
                                                        s6r.config(bg="Orange")
                                                    if combo == "12":
                                                        s6rr.config(bg="Orange")
                                                    if combo == "13":
                                                        s7r.config(bg="Orange")
                                                    if combo == "14":
                                                        s7rr.config(bg="Orange")
                                                    if combo == "15":
                                                        s8r.config(bg="Orange")
                                                    if combo == "16":
                                                        s8rr.config(bg="Orange")

                                                    if combox == "A":
                                                        s1.config(bg="Orange")
                                                    if combox == "B":
                                                        s2.config(bg="Orange")
                                                    if combox == "C":
                                                        s3.config(bg="Orange")
                                                    if combox == "D":
                                                        s4.config(bg="Orange")
                                                    if combox == "E":
                                                        s5.config(bg="Orange")
                                                    if combox == "F":
                                                        s6.config(bg="Orange")
                                                    if combox == "G":
                                                        s7.config(bg="Orange")
                                                    if combox == "H":
                                                        s8.config(bg="Orange")
                                                    if combox == "1":
                                                        s1r.config(bg="Orange")
                                                    if combox == "2":
                                                        s1rr.config(bg="Orange")
                                                    if combox == "3":
                                                        s2r.config(bg="Orange")
                                                    if combox == "4":
                                                        s2rr.config(bg="Orange")
                                                    if combox == "5":
                                                        s3r.config(bg="Orange")
                                                    if combox == "6":
                                                        s3rr.config(bg="Orange")
                                                    if combox == "7":
                                                        s4r.config(bg="Orange")
                                                    if combox == "8":
                                                        s4rr.config(bg="Orange")
                                                    if combox == "9":
                                                        s5r.config(bg="Orange")
                                                    if combox == "10":
                                                        s5rr.config(bg="Orange")
                                                    if combox == "11":
                                                        s6r.config(bg="Orange")
                                                    if combox == "12":
                                                        s6rr.config(bg="Orange")
                                                    if combox == "13":
                                                        s7r.config(bg="Orange")
                                                    if combox == "14":
                                                        s7rr.config(bg="Orange")
                                                    if combox == "15":
                                                        s8r.config(bg="Orange")
                                                    if combox == "16":
                                                        s8rr.config(bg="Orange")

                                                    BusNo = ["MH-43-AS-1000", "MH-43-AS-1100", "MH-43-AS-1200",
                                                             "MH-43-AS-10050", "MH-43-AS-1005", "MH-43-AS-5000",
                                                             "MH-03-AS-1000", "MH-43-AS-1540", "MH-43-AS-1054"
                                                                                               "MH-43-AS-8989",
                                                             "MH-43-AS-1555", "MH-43-AS-1654", "MH-43-AS-1564",
                                                             "MH-43-AS-1464", "MH-43-AS-4654", "MH-43-AS-1050",
                                                             "MH-43-AZ-1000", "MH-43-AS-1505"]
                                                    bn = random.choice(BusNo)
                                                    combo = combof.get()
                                                    combox = comboff.get()
                                                    d = combo + " & " + combox
                                                    j = Number.get()
                                                    jx = j[0:3] + j[4:7] + j[8:]
                                                    print(jx)
                                                    m = "\nTravel India \nThis is Your Invoice\nName - " + k1 + " \nSource - " + k3 + " \nDestination - " + k4 + " \n On - " + k5 + " \nReturn - " + k6 + "\nFare - " + k7 + " \nBus No - " + bn + "\nSeat No - " + d + " \n Thanks for Booking \nAn Effort By Kailash's Creation"
                                                    m1 = "sender_id=FSTSMS&message=" + m + "&language=english&route=p&numbers=" + jx
                                                    import requests
                                                    url = "https://www.fast2sms.com/dev/bulk"
                                                    payload = m1
                                                    headers = {
                                                        'authorization': "k0jB9RUYogPnCitNscAwd7zXZ5MVh28SfJ6yrLKETaIlbquDx4paeSDzTlso8cr2Rm9Ad7G5yqgJKtYk",
                                                        'Content-Type': "application/x-www-form-urlencoded",
                                                        'Cache-Control': "no-cache",
                                                    }
                                                    response = requests.request("POST", url, data=payload,
                                                                                headers=headers)
                                                    print(response.text)
                                                    w3.geometry('2000x1000')
                                                    w3.mainloop()

                                                thnkx = Button(w, text=" View my receipt", font=("Algerian", 18),
                                                               bg="#d0f9f9", fg="Black", command=thnk)
                                                thnkx.place(x=650, y=650)
                                                thnkx.config(state="disabled")
                                                thnkx.after(4000, lambda: thnkx.config(state="active"))

                                            pr4221x = Button(w, text=" I aggre to Rules \nProceed to BOOK",
                                                             font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                                             command=Thank)
                                            pr4221x.place(x=235, y=650)
                            elif l != 12:
                                pr4232 = Label(w, text="Number Exceeds the Limited characters allowed",
                                               font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                                pr4232.place(x=535, y=500)
                                pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15), bg="#d0f9f9",
                                                fg="Black")
                                pr4232a.place(x=535, y=530)
                                Number.config(state="disabled")
                                Number.after(3000, lambda: Number.config(state="normal"))
                                pr4232.after(3000, lambda: pr4232.destroy())
                                pr4232a.after(3000, lambda: pr4232a.destroy())
                            else:
                                pr4232 = Label(w, text="You Entered Something other than a Number. Right??",
                                               font=("Algerian", 15), bg="#d0f9f9", fg="Black")
                                pr4232.place(x=535, y=500)
                                pr4232a = Label(w, text="Try again in 3 secs", font=("Algerian", 15), bg="#d0f9f9",
                                                fg="Black")
                                pr4232a.place(x=535, y=530)
                                Number.config(state="disabled")
                                Number.after(3000, lambda: Number.config(state="normal"))
                                pr4232.after(3000, lambda: pr4232.destroy())
                                pr4232a.after(3000, lambda: pr4232a.destroy())

                        pr42322 = Label(w, text="Correct Format is XXX-XXX-XXXX", font=("Algerian", 15), bg="#d0f9f9",
                                        fg="Black")
                        pr42322.place(x=235, y=580)
                        pr4221 = Button(w, text="Click Here", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                        command=here1)
                        pr4221.place(x=235, y=450)
                        pr6 = Label(w, text="<----- Please Enter Your Name", font=("Script Mt bold", 18), bg="#d0f9f9",
                                    fg="Black")
                        pr6.place(x=520, y=315)
                        pr7 = Label(w, text="<----- Please Enter your Contact Number", font=("Script Mt bold", 18),
                                    bg="#d0f9f9", fg="Black")
                        pr7.place(x=520, y=415)
                        Name = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                        Name.place(x=235, y=315, height=35)
                        Number = Entry(w, font=("Lucida Handwriting", 15), bg="#d0f9f9", fg="Black")
                        Number.place(x=235, y=415, height=35)
                        Number.focus()

                        pr52 = Button(w, text="Lets Proceed", font=("Algerian", 15), bg="Light Green", fg="Black",
                                      command=ppr)
                        pr52.place(x=835, y=730)

                    pr5a = Button(w, text="No Proceed Further", font=("Algerian", 15), bg="#d0f9f9", fg="Black",
                                  command=ppr)
                    pr5a.place(x=235, y=610)

                t = "A"
                s1 = Button(w, text="A", bd=2, relief="solid", bg=rs1, command=pro, textvar=t)
                s1.place(x=25, y=270, height=50, width=25)
                t = "B"
                s2 = Button(w, text="B", bd=2, relief="solid", bg=rs2, command=pro, textvar=t)
                s2.place(x=25, y=330, height=50, width=25)
                t = "C"
                s3 = Button(w, text="C", bd=2, relief="solid", bg=rs3, command=pro, textvar=t)
                s3.place(x=25, y=390, height=50, width=25)
                t = "D"
                s4 = Button(w, text="D", bd=2, relief="solid", bg=rs4, command=pro, textvar=t)
                s4.place(x=25, y=450, height=50, width=25)
                t = "E"
                s5 = Button(w, text="E", bd=2, relief="solid", bg=rs5, command=pro, textvar=t)
                s5.place(x=25, y=510, height=50, width=25)
                t = "F"
                s6 = Button(w, text="F", bd=2, relief="solid", bg=rs6, command=pro, textvar=t)
                s6.place(x=25, y=570, height=50, width=25)
                t = "G"
                s7 = Button(w, text="G", bd=2, relief="solid", bg=rs7, command=pro, textvar=t)
                s7.place(x=25, y=630, height=50, width=25)
                t = "H"
                s8 = Button(w, text="H", bd=2, relief="solid", bg=rs8, command=pro, textvar=t)
                s8.place(x=25, y=690, height=50, width=25)
                t = "1"
                s1r = Button(w, text="1", bd=2, relief="solid", bg=rs9, command=pro, textvar=t)
                s1r.place(x=125, y=270, height=50, width=25)
                t = "3"
                s2r = Button(w, text="3", bd=2, relief="solid", bg=rs10, command=pro, textvar=t)
                s2r.place(x=125, y=330, height=50, width=25)
                t = "5"
                s3r = Button(w, text="5", bd=2, relief="solid", bg=rs11, command=pro, textvar=t)
                s3r.place(x=125, y=390, height=50, width=25)
                t = "7"
                s4r = Button(w, text="7", bd=2, relief="solid", bg=rs11, command=pro, textvar=t)
                s4r.place(x=125, y=450, height=50, width=25)
                t = "9"
                s5r = Button(w, text="9", bd=2, relief="solid", bg=rs12, command=pro, textvar=t)
                s5r.place(x=125, y=510, height=50, width=25)
                t = "11"
                s6r = Button(w, text="11", bd=2, relief="solid", bg=rs13, command=pro, textvar=t)
                s6r.place(x=125, y=570, height=50, width=25)
                t = "13"
                s7r = Button(w, text="13", bd=2, relief="solid", bg=rs14, command=pro, textvar=t)
                s7r.place(x=125, y=630, height=50, width=25)
                t = "15"
                s8r = Button(w, text="15", bd=2, relief="solid", bg=rs15, command=pro, textvar=t)
                s8r.place(x=125, y=690, height=50, width=25)
                t = "2"
                s1rr = Button(w, text="2", bd=2, relief="solid", bg=rs16, command=pro, textvar=t)
                s1rr.place(x=165, y=270, height=50, width=25)
                t = "4"
                s2rr = Button(w, text="4", bd=2, relief="solid", bg=rs17, command=pro, textvar=t)
                s2rr.place(x=165, y=330, height=50, width=25)
                t = "6"
                s3rr = Button(w, text="6", bd=2, relief="solid", bg=rs18, command=pro, textvar=t)
                s3rr.place(x=165, y=390, height=50, width=25)
                t = "8"
                s4rr = Button(w, text="8", bd=2, relief="solid", bg=rs19, command=pro, textvar=t)
                s4rr.place(x=165, y=450, height=50, width=25)
                t = "10"
                s5rr = Button(w, text="10", bd=2, relief="solid", bg=rs20, command=pro, textvar=t)
                s5rr.place(x=165, y=510, height=50, width=25)
                t = "12"
                s6rr = Button(w, text="12", bd=2, relief="solid", bg=rs21, command=pro, textvar=t)
                s6rr.place(x=165, y=570, height=50, width=25)
                t = "14"
                s7rr = Button(w, text="14", bd=2, relief="solid", bg=rs22, command=pro, textvar=t)
                s7rr.place(x=165, y=630, height=50, width=25)
                t = "18"
                s8rr = Button(w, text="16", bd=2, relief="solid", bg=rs17, command=pro, textvar=t)
                s8rr.place(x=165, y=690, height=50, width=25)
                if rs1 == ss1[0]:
                    s1.config(state="disabled")
                    L.remove("A")
                if rs2 == ss1[0]:
                    s2.config(state="disabled")
                    L.remove("B")
                if rs3 == ss1[0]:
                    s3.config(state="disabled")
                    L.remove("C")
                if rs4 == ss1[0]:
                    s4.config(state="disabled")
                    L.remove("D")
                if rs5 == ss1[0]:
                    s5.config(state="disabled")
                    L.remove("E")
                if rs6 == ss1[0]:
                    s6.config(state="disabled")
                    L.remove("F")
                if rs7 == ss1[0]:
                    s7.config(state="disabled")
                    L.remove("G")
                if rs8 == ss1[0]:
                    s8.config(state="disabled")
                    L.remove("H")
                if rs9 == ss1[0]:
                    s1r.config(state="disabled")
                    L.remove("1")
                if rs10 == ss1[0]:
                    s2r.config(state="disabled")
                    L.remove("3")
                if rs11 == ss1[0]:
                    s3r.config(state="disabled")
                    L.remove("5")
                if rs11 == ss1[0]:
                    s4r.config(state="disabled")
                    L.remove("7")
                if rs12 == ss1[0]:
                    s5r.config(state="disabled")
                    L.remove("9")
                if rs13 == ss1[0]:
                    s6r.config(state="disabled")
                    L.remove("11")
                if rs14 == ss1[0]:
                    s7r.config(state="disabled")
                    L.remove("13")
                if rs15 == ss1[0]:
                    s8r.config(state="disabled")
                    L.remove("15")
                if rs16 == ss1[0]:
                    s1rr.config(state="disabled")
                    L.remove("2")
                if rs17 == ss1[0]:
                    s2rr.config(state="disabled")
                    L.remove("4")
                if rs18 == ss1[0]:
                    s3rr.config(state="disabled")
                    L.remove("6")
                if rs19 == ss1[0]:
                    s4rr.config(state="disabled")
                    L.remove("8")
                if rs20 == ss1[0]:
                    s5rr.config(state="disabled")
                    L.remove("10")
                if rs21 == ss1[0]:
                    s6rr.config(state="disabled")
                    L.remove("12")
                if rs22 == ss1[0]:
                    s7rr.config(state="disabled")
                    L.remove("14")
                if rs17 == ss1[0]:
                    s8rr.config(state="disabled")
                    L.remove("16")

            B9 = Button(w, text="View & Book Seats", font=("Lucida Handwriting", 14), bg="#f7e3ec", fg="#00277e",
                        relief="raised", command=seats)
            B9.place(x=229, y=205)

            tip = Label(w, text="! Tip \nClick on Bus to view its images", font=("Bahnscript", 10), bg="Light Yellow",
                        fg="Dark Blue")
            tip.place(x=1300, y=10)
            tip.after(5000, lambda: tip.destroy())

        Search = Button(w, text="Search", font=("Algerian", 20), bg="#f3c5e6", fg="Dark Blue", command=Search)
        Search.place(x=1140, y=260, height=53)

    P = Button(w, text="Proceed", font=("Algerian", 20), bg="#f3c5e6", fg="Dark Blue", command=proceed)
    P.place(x=1140, y=260, height=53)


B1 = Button(w, text="Lets Proceed for Booking >>>>", font=("Algerian", 25), bg="#a2f1ec", fg="Dark Blue", command=Book)
B1.place(x=978, y=630)
w.mainloop()
