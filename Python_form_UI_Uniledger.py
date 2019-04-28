# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:23:28 2019

@author: mathi
"""

import tkinter
#import tkinter.ttk
from tkinter import *


def NewPatient():
    login_screen.destroy()
    patient_screen = tkinter.Tk()
    patient_screen.geometry("700x500")
    patient_screen.title("Create New Patient ID")
    patient_heading = Label(text = "Create New Patient ID", bg = "grey", fg = "black", width = "700", height = "3")
    patient_heading.pack()
    
# form content
    patient_form_text = Label(text = "New Patient Form",)
    patient_name_text = Label(text = "Name: ",)
    patient_DOB_text = Label(text = "Date of Birth: ",)
    patient_bloodtype_text = Label(text = "Blood Type: ",)
    #patient_date_text = Label(text = "Date: ",)
    #patient_Diagnosis_text = Label(text = "Diagnosis: ",)
    #patient_Prescription_text = Label(text = "Prescription: ",)
    patient_email_text = Label(text = "Email: ",)
    
    
    
    patient_form_text.place(x = 35, y = 70)
    patient_name_text.place(x = 35, y = 110)
    patient_DOB_text.place(x = 35, y = 150)
    patient_bloodtype_text.place(x = 35, y = 190)
   # patient_date_text.place(x = 35, y = 230)
   # patient_Diagnosis_text.place(x = 35, y = 270)
   # patient_Prescription_text.place(x = 35, y = 310)
    patient_email_text.place(x = 35, y = 230)
    
#Data input
    patient_name = StringVar()
    patient_DOB = StringVar()
    patient_bloodtype = StringVar()
   # patient_date = StringVar()
    #patient_Diagnosis = StringVar()
    #patient_Prescription = StringVar()
    patient_email = StringVar()
    
   
 #Textbox   
    patient_name_entry = Entry(textvariable = patient_name, width = "30")
    patient_DOB_entry = Entry(textvariable = patient_DOB, width = "30")
    patient_bloodtype_entry = Entry(textvariable = patient_bloodtype, width = "30")
    #patient_date_entry = Entry(textvariable = patient_date, width = "30")
    #patient_Diagnosis_entry = Entry(textvariable = patient_Diagnosis, width = "30")
    #patient_Prescription_entry = Entry(textvariable = patient_Prescription, width = "30")
    patient_email_entry = Entry(textvariable = patient_email, width = "30")
    
    patient_name_entry.place(x = 170, y = 110)
    patient_DOB_entry.place(x = 170, y = 150)
    patient_bloodtype_entry.place(x = 170, y = 190)
    #patient_date_entry.place(x = 170, y = 230)
    #patient_Diagnosis_entry.place(x = 170, y = 270)
    #patient_Prescription_entry.place(x = 170, y = 310)
    patient_email_entry.place(x = 170, y = 230)
    
    patient_create = Button(patient_screen, text = "Register Patient", width = "20", height = "2")
    patient_create.place(x = 35, y = 400)
    
    patient_create = Button(patient_screen, text = "Back", width = "20", height = "2")
    patient_create.place(x = 235, y = 400)

def NewDoctor():
    login_screen.destroy()
    doctor_screen = tkinter.Tk()
    doctor_screen.geometry("700x400")
    doctor_screen.title("Create New Doctor ID")
    doctor_heading = Label(text = "Create New Doctor ID", bg = "blue", fg = "white", width = "700", height = "3")
    doctor_heading.pack()
    
    # form content
    doctor_form_text = Label(text = "New Doctor Form",)
    doctor_name_text = Label(text = "Name: ",)
    doctor_specialisation_text = Label(text = "Specialisation: ",)
    doctor_email_text = Label(text = "Email: ",)
    
    doctor_form_text.place(x = 35, y = 70)
    doctor_name_text.place(x = 35, y = 110)
    doctor_specialisation_text.place(x = 35, y = 150)
    doctor_email_text.place(x = 35, y = 190)
    
    doctor_name = StringVar()
    doctor_specialisation = StringVar()
    doctor_email = StringVar()
    
    doctor_name_entry = Entry(textvariable = doctor_name, width = "30")
    doctor_specialisation_entry = Entry(textvariable = doctor_specialisation, width = "30")
    doctor_email_entry = Entry(textvariable = doctor_email, width = "30")
    
    doctor_name_entry.place(x = 170, y = 110)
    doctor_specialisation_entry.place(x = 170, y = 150)
    doctor_email_entry.place(x = 170, y = 190)

    doctor_create = Button(doctor_screen, text = "Register Doctor", width = "20", height = "2")
    doctor_create.place(x = 35, y = 240)

    doctor_create = Button(doctor_screen, text = "Back", width = "20", height = "2")
    doctor_create.place(x = 235, y = 240)

def LogIn():
    login_screen.destroy()
    doctor_screen = tkinter.Tk()
    doctor_screen.geometry("700x500")
    doctor_screen.title("Log In")
    doctor_heading = Label(text = "Medical Record", bg = "blue", fg = "white", width = "700", height = "3")
    doctor_heading.pack()
    
    # form content
    patient_id_text = Label(text = "Patient ID",)
    patient_age_text = Label(text = "Age: ",)
    patient_weight_text = Label(text = "Weight: ",)
    patient_height_text = Label(text = "Height: ",)
    patient_heartrate_text = Label(text = "Heart rate: ",)
    patient_bloodpressure_text = Label(text = "Blood pressure: ",)
    patient_diagnosis_text = Label(text = "Diagnosis: ",)
    patient_prescription_text = Label(text = "Prescription: ",)
    
    patient_id_text.place(x = 35, y = 70)
    patient_age_text.place(x = 35, y = 110)
    patient_weight_text.place(x = 35, y = 150)
    patient_height_text.place(x = 35, y = 190)
    patient_heartrate_text.place(x = 35, y = 230)
    patient_bloodpressure_text.place(x = 35, y = 270)
    patient_diagnosis_text.place(x = 35, y = 310)
    patient_prescription_text.place(x = 35, y = 350)
    
    patient_id = StringVar()
    patient_weight = StringVar()
    patient_height = StringVar()
    patient_heartrate = StringVar()
    patient_bloodpressure = StringVar()
    patient_diagnosis = StringVar()
    patient_prescription = StringVar()
    
    patient_id_entry = Entry(textvariable = patient_id, width = "30")
    patient_weight_entry = Entry(textvariable = patient_weight, width = "30")
    patient_height_entry = Entry(textvariable = patient_height, width = "30")
    patient_heartrate_entry = Entry(textvariable = patient_heartrate, width = "30")
    patient_bloodpressure_entry = Entry(textvariable = patient_bloodpressure, width = "30")
    patient_diagnosis_entry = Entry(textvariable = patient_diagnosis, width = "30")
    patient_prescription_entry = Entry(textvariable = patient_prescription, width = "30")
    
    patient_id_entry.place(x = 170, y = 110)
    patient_weight_entry.place(x = 170, y = 150)
    patient_height_entry.place(x = 170, y = 190)
    patient_heartrate_entry.place(x = 170, y = 230)
    patient_bloodpressure_entry.place(x = 170, y = 270)
    patient_diagnosis_entry.place(x = 170, y = 310)
    patient_prescription_entry.place(x = 170, y = 350)

    doctor_create = Button(doctor_screen, text = "Register Doctor", width = "20", height = "2")
    doctor_create.place(x = 35, y = 390)

    doctor_create = Button(doctor_screen, text = "Back", width = "20", height = "2")
    doctor_create.place(x = 235, y = 390)

#def login():
login_screen = tkinter.Tk()
login_screen.geometry("700x400")
login_screen.title("YouRecord Login")
login_heading = Label(text = "YouRecord Login", bg = "light green", fg = "black", width = "700", height = "3")
login_heading.pack()

# Login using existing ID
patient_id_text = Label(text = "Patient ID",)
doctor_id_text = Label(text = "Doctor ID",)
patient_id_text.place(x = 15, y = 70)
doctor_id_text.place(x = 365, y = 70)

# Submit Button
log_in_register = Button(login_screen, text = "Medical Record", width = "20", height = "2", command = LogIn)
log_in_register.place(x = 270, y = 110)

# If new user wants to sign in
new_user_warning = Label(text = "*If you are a new user, please select the option below ",)
new_user_warning.place(x = 15, y = 180)

new_patient_register = Button(login_screen, text = "Create new patient ID", width = "20", height = "2", command = NewPatient)
new_doctor_register = Button(login_screen, text = "Create new doctor ID", width = "20", height = "2", command = NewDoctor)
new_patient_register.place(x = 55, y = 250)
new_doctor_register.place(x = 415, y = 250)

patient_id = StringVar()
doctor_id = StringVar()

patient_id_entry = Entry(textvariable = patient_id, width = "30")
doctor_id_entry = Entry(textvariable = doctor_id, width = "30")
patient_id_entry.place(x = 115, y = 70)
doctor_id_entry.place(x = 465, y = 70)

login_screen.mainloop()

#login()



#%%

# New Patient Window

patient_screen.mainloop()

patient_data = list()



#%%

# New Doctor Window

doctor_screen.mainloop()


 