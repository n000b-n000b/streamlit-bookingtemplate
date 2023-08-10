from time import sleep, strftime
import time
import streamlit as a
import smtplib,ssl
from email.mime.text import MIMEText
import datetime
import requests as b
from datetime import date

def main():
    a.markdown("""<style>
               h1 {
               text-align: center;
               }
               h4 {
               text-align: center;
               }
               </style>""",unsafe_allow_html=True)
    a.markdown("""
               <h1>Dont Just Look, Book!</h1>
               <h4>Please book today!</h4>""", unsafe_allow_html=True)
    all_booked=["8:00am","8:30am","9:00am","9:30am","10:00am","10:30am","11:00am","11:30am","2:00pm","2:30pm","3:00pm","3:30pm","4:00pm","4:30pm"]
    display_avail=["8:00am","8:30am","9:00am","9:30am","10:00am","10:30am","11:00am","11:30am","2:00pm","2:30pm","3:00pm","3:30pm","4:00pm","4:30pm"]
    book00=open('sched.csv', 'r')
    book01=book00.readlines()
    chek_date=''
    avail_times=[]
    avail_times.clear()
    with a.form("Home"):
        a00=a.text_input("First Name:")
        a01=a.text_input("Last Name:")
        a04=a.text_input("Phone Number: ")
        a05=a.text_input("Email address: ")
        a02=a.date_input("Please select date that works best for you:")
        shift00=a.form_submit_button("Next")
    if shift00:
        if len(a00)==0:
            a.warning("Please enter a first name!")
            a.stop()
        elif len(a01)==0:
            a.warning("Please enter a last name!")
            a.stop()
        elif len(a04)<10:
            a.warning("Please enter a valid phone number!")
            a.stop()
        elif len(a05)==0:
            a.warning("Please enter an email address!")
        else:
            for f in all_booked:
                chek_date="'"+str(a02)+"'"+', '+"'"+f+"'"
                for g in book01:
                    g=g.strip()
                    g=g.split(',')
                    if chek_date==str(g[-2:]).replace('[','').replace(']',''):
                        try:
                            display_avail.remove(f)
                        except:
                            pass
            if len(display_avail)==0:
                a.warning("Sorry but all times for the date selected have been booked! Please chose another date.\n Thank you.")
                a.stop()
            else:
                with a.spinner():
                    sleep(2.7)
                    a03=a.selectbox("Please select time that works best for you:",
                                (display_avail))   
            sleep(3.7)
            a.markdown('<div style="border-style=solid;"><h4>Please wait confirming your booking for</h4></div>',unsafe_allow_html=True)
            a.markdown('<div><h4>'+str(a02) +' at '+a03+'. . .</h4></div>',unsafe_allow_html=True)
            if a03:
                book00=open('sched.csv', 'a')
                book00.write(str(a00)+','+str(a01)+','+str(a02)+','+a03+'\n')
                try:
                    port=587
                    subject="NEW BOOKING FOR "+str(a00)+' '+str(a01)
                    body="Booking request for "+str(a02)+' at '+str(a03)+'.'+"\nClient Name: "+a00+' '+a01+"\nPhone Number: "+str(a04)+"\nEmail:"+' '+a05+"\n"+"\nSincerely,\nSystems Team."
                    sender="YOUR OUTLOOK EMAIL HERE"
                    receiv="RECEIVERS EMAIL HERE"
                    with smtplib.SMTP('smtp-mail.outlook.com',port) as serv:
                        passw="YOUR OUTLOOK EMAIL PASSWORD HERE"
                        msg=MIMEText(body)
                        msg['Subject']=subject
                        msg['From']=sender
                        msg['To']=receiv
                        serv.connect('smtp-mail.outlook.com',port)
                        serv.ehlo()
                        serv.starttls()
                        serv.ehlo()
                        serv.login(sender,passw)
                        serv.sendmail(sender,receiv,msg.as_string())
                        serv.quit()
                        a.markdown('<div style="border-style=solid;"><h4>Thank you for booking!</h4></div>',unsafe_allow_html=True)
                        a.balloons()
                except:
                    a.error("""Sorry there is an issue on our end. Please try giving us a call,
                            we have raised the issue to our systems team. Thank you for your
                            understanding.
                            """)
                    sleep(2.5)
                    a.experimental_rerun()
                    a.stop()
main()
