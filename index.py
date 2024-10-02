import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter import filedialog
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from ultralytics import YOLO
import os, shutil
import cv2
from PIL import ImageTk, Image
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
root = tk.Tk()
root.title("Image in Tab Example")
root.title("Melanoma disease Detection")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}+0+0")

# Create a notebook (tabbed menu)
style = ttk.Style()
style.configure("TNotebook.Tab", font=('Times New Roman', 14), foreground="red")

# Set the background color of tabs
style.configure("TNotebook", background="white")  # Change the background color of the entire notebook
style.map("TNotebook.Tab", background=[("selected", "white")])

notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill='both', expand=True)



# Create tabs


# Create frames for each tab
tab1 = tk.Frame(notebook,bg='white')
tab2 = tk.Frame(notebook,bg='white')
tab3 = tk.Frame(notebook,bg='white')
tab2.configure(background='white')
# Add tabs to the notebook
notebook.add(tab2, text="About Melanoma disease")
notebook.add(tab1, text="Predict Disease")
notebook.add(tab3, text="Contact us")





def classify(file_path):
    shutil.rmtree("output")
    # os.mkdir("D:\YoloProjects\HumanFallDetction\output")
    model = YOLO("best1.pt")
    model.predict(mode="predict", model="best1.pt", project='output', save=True, show=False,save_txt=True, conf=0.1, source=file_path)
    filename = os.path.basename(file_path).split('/')[-1]
    print(filename)
    emailfile=os.path.basename(file_path).split('/')[-1]
    im = Image.open(r"output/predict/" + filename)

    im.show()

    Melonoma = 0
    Nevus = 0
    Keratoses = 0
    predictedclass = ""
    feeds=""
    labelpath = "output/predict/labels/"+filename
    file_name_without_extension = os.path.splitext(os.path.basename(labelpath))[0]
    print(file_name_without_extension)
    label_file_path = "output/predict/labels/" + file_name_without_extension + ".txt"  # Update with your file path
    try:
        with open(label_file_path, "r") as file:
            for line in file:
                if line.strip():  # Check if the line is not empty
                    first_char = line[0]
                    if (first_char == "0"):
                        Melonoma = Melonoma + 1;

                    if (first_char == "1"):
                        Nevus = Nevus + 1
                    if (first_char == "2"):
                        Keratoses = Keratoses + 1


                else:
                    print("Empty line detected")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)
    print("Melanoma :", Melonoma)
    print("Nevus :", Nevus)
    print("Keratoses :", Keratoses)
    if ((Melonoma > Nevus) and (Melonoma > Keratoses)):
        predictedclass = "Detected as Melanoma please visit the doctor more confirmation."
        feeds += " Please meet the doctor this is very serious condition"

    elif ((Nevus > Melonoma) and (Nevus > Keratoses)):
        predictedclass = "Nevus (Non Melanoma)."
        feeds += "This is not fatal, kindly visit a doctor for your confirmation."

    elif ((Keratoses > Melonoma) and (Keratoses > Nevus)):
        predictedclass = " Seborrehic Keratosis(Non Melanoma)."
        feeds += " This is not fatal, please visit the doctor for confirmation"


    print(feeds)
    name = name_entry.get()
    email = email_entry.get()
    print("Name:", name)
    print("Email:", email)

    image_path = "output/predict/"+emailfile

    # Email details
    sender_email = "ourprojectemails@gmail.com"
    password = "oxipcucyayarblht"
    receiver_email =email
    subject = "Melanoma Results:"
    message = "The predicted Result is "+predictedclass+" and "+feeds

    image_path = image_path  # Path to the image file
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Open the image file
    with open(image_path, 'rb') as attachment:
        # Add image as application/octet-stream
        # Email clients can usually display it inline
        img = MIMEImage(attachment.read())
        img.add_header('Content-Disposition', 'attachment', filename=image_path)
        msg.attach(img)

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Login to the SMTP server
    server.login(sender_email, password)
    # Send email
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    # Close the SMTP session
    print("mail Sent")
    server.quit()
    messagebox.showinfo("MessageBox",'Email sent successfully.')


    text_to_append = "Name:"+name+" email:"+email+"  predicted Disease is:"+predictedclass+"\n"
    file_path = "example.txt"

    # Open the file in append mode
    with open(file_path, "a") as file:
        # Append the text to the file
        file.write(text_to_append)

    print("Text appended to the file successfully.")


def show_classify_button(file_path):

    classify_b = Button(tab1, text="Classify Image", command=lambda: checkEmail(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('Times New Roman', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def checkEmail(file_path):
    emailval = email_entry.get()
    res = validate_email(emailval)
    if res == "true":
        classify(file_path)


def validate_email(addrs):
    flag="true"
    email = email_entry.get()
    if len(email)==0:
        flag="Please fill the email"
        messagebox.showinfo("Alert", "Please fill the email")

    # Regular expression for validating an email address
    regex = r'^[a-z0-9]+[._-]?[a-z0-9]+[@]\w+[.]\w{2,}$'


    if not re.match(regex, email):
        email_entry.config(bg="red")
        flag="invalid Email address"
        messagebox.showinfo("Alert","invalid Email address")
    else:
        email_entry.config(bg="green")
    return flag

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((tab2.winfo_width() / 2.25), (tab1.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

def livecam():
    model = YOLO("best1.pt")
    model.predict(mode="predict", model="best1.pt", show=True, conf=0.1, source=0)

def send_email():
    sender_email = "ourprojectemails@gmail.com"  # Enter your email
    sender_password = "oxipcucyayarblht"      # Enter your email password

    #receiver_email = receiver_entry.get()
    receiver_email = "enteryouemainl@gmail.com"  #here enter your email
    #subject = subject_entry.get()
    subject = "Feedback of the project"
    message = message_text.get("1.0", "end")

    # Constructing the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Establishing a connection to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Logging in to the email account
        server.login(sender_email, sender_password)
        # Sending the email
        server.send_message(msg)
        # Quitting the server
        server.quit()
        messagebox.showinfo("Success", "Feedback sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def open_link():
    webbrowser.open_new_tab("https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884")

def open_link_Neaves():
    webbrowser.open_new_tab("https://www.healthline.com/health/nevus")

def open_link_sk():
    webbrowser.open_new_tab("https://www.mayoclinic.org/diseases-conditions/seborrheic-keratosis/symptoms-causes/syc-20353878")
# Add widgets to each tab

upload = Button(tab1, text="Upload an image", padx=10, pady=5)
webcam = Button(tab1, text="Live  Detection", command=livecam, padx=10, pady=5,bg='black',foreground='white',font=('Times New Roman',10,'bold'))
upload.configure(background='#000000', foreground='white', command=upload_image,  font=('Times New Roman', 10, 'bold'))
webcam.pack(side=BOTTOM,pady=70)
upload.pack(side=BOTTOM, pady=50)

label = Label(tab1)
label = Label(tab1, background='white', font=('Times New Roman', 15, 'bold'))
sign_image = Label(tab1)
sign_image.pack(side=BOTTOM, expand=True)




label1 = tk.Label(tab1, text="Predict Image", font=('Times New Roman', 24, 'bold'),bg='white' )
label1.pack(padx=20, pady=20)

label2 = tk.Label(tab2, text="About Melanoma Disease",font=('Times New Roman', 24, 'bold'),bg='white')
label2.pack(padx=20, pady=20)

label8 = tk.Label(tab2, text="Disclaimer ! This model is trained for Melanoma images. So user should select only the images containing Melanoma.",font=('Times New Roman', 20, 'bold'),bg='white',foreground='red')
label8.place(relx=0.05, rely=0.75)
multi_line_info = "Melanoma is a type of skin cancer that originates from melanocytes" \
                  " the cells that produce melanin, the pigment responsible for skin color \n" \
                  "It can also develop in other parts of the body where melanocytes are found " \
                  "such as the eyes and the intestines, although this is less common"+""

aboutlabel2 = tk.Label(tab2, text=multi_line_info,font=('Times New Roman', 16),bg='white')
aboutlabel2.pack(padx=20, pady=20)

image_path = "ALL1.jpeg"
image1 = Image.open(image_path)
resized_image = image1.resize((300, 200))
photo1 = ImageTk.PhotoImage(resized_image)
label4 = tk.Label(tab2, image=photo1)
label4.place(relx=0.10, rely=0.20)
nevslinkbutton = tk.Button(tab2, text="Click here for more Information on Melanoma",bg='white', command=open_link)
nevslinkbutton.place(relx=0.12, rely=0.55)

image_path = "ALL2.jpeg"
image2 = Image.open(image_path)
resized_image = image2.resize((300, 200))
photo2 = ImageTk.PhotoImage(resized_image)
label5 = tk.Label(tab2, image=photo2)
label5.place(relx=0.40, rely=0.20)
linkbutton = tk.Button(tab2, text="Click here for more Information on Nevus", command=open_link_Neaves)
linkbutton.place(relx=0.42, rely=0.55)


image_path = "ALL3.jpeg"
image3 = Image.open(image_path)
resized_image = image3.resize((300, 200))
photo3 = ImageTk.PhotoImage(resized_image)
label6 = tk.Label(tab2, image=photo3)
label6.place(relx=0.70, rely=0.20)
sklinkbutton = tk.Button(tab2, text="click here for more Information on Seborrheic keratosis",bg='white', command=open_link_sk)
sklinkbutton.place(relx=0.72, rely=0.55)





label3 = tk.Label(tab3, text="Project By",font=('Times New Roman', 24, 'bold'),bg='white')
label3.pack(padx=20, pady=20)
label4 = tk.Label(tab3, text="JNNCE CSE Students", font=('Times New Roman', 24, 'bold'),bg='white')
label4.pack(padx=20, pady=20)
label5 = tk.Label(tab3, text="Computer Science and Engineering",font=('Times New Roman', 24, 'bold'),bg='white')
label5.pack(padx=20, pady=20)
message_label = tk.Label(tab3, text="Send your valuable Feedback:",bg='white',font=('Times New Roman', 16))
message_label.pack(padx=20, pady=20)

message_text = tk.Text(tab3, width=50, height=10,bg='white')
message_text.pack(padx=20, pady=20)

send_button = tk.Button(tab3, text="Send",command=send_email,bg='black',foreground='white',font=('Times New Roman', 10))
send_button.pack(padx=30, pady=30)

# Pack the notebook
notebook.pack(expand=True, fill="both")


name_label = tk.Label(tab1, text="Enter Name:",font=('Times New Roman', 14, 'bold'),bg='white')
name_label.place(relx=0.70, rely=0.26)

name_entry = tk.Entry(tab1,width=40)
name_entry.place(relx=0.80, rely=0.26)

# Email Label and Entry
email_label = tk.Label(tab1, text="Enter Email:",bg='white',font=('Times New Roman', 14, 'bold'))
email_label.place(relx=0.70, rely=0.36)

email_entry = tk.Entry(tab1,width=40)
email_entry.place(relx=0.80, rely=0.36)
root.mainloop()


