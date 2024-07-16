import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


HOST = "2.tcp.eu.ngrok.io"
PORT = 18016
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



LIGHT_GREY = "#D3D3D3"
DARK_GREY = "#A9A9A9"
WHITE = "white"
BLACK = "black"
BLUE = "aqua"

FONT = ("Helvetica", 17)
CHAT_FONT = ("Helvetica", 13)
BUTTON_FONT = ("Helvetica",12)

def add_message_to_scrolledtext(message):
    chat_scrolledtext.config(state=tk.NORMAL)
    chat_scrolledtext.insert(tk.END, message + '\n')
    chat_scrolledtext.config(state=tk.DISABLED)

def join():
    try:
        client.connect((HOST,PORT))
        add_message_to_scrolledtext("[SERVER] You joined the chat.")
        username_textbox.config(state=tk.DISABLED)
        username_button.config(state=tk.DISABLED)
    except:
        messagebox.showerror("SERVER","Server is off.")
        exit(0)
    
    send_username_to_server(client)

def send_message():
    message = message_textbox.get().strip()
    print(message)
    if(message != ""):
        client.sendall(message.encode())
    else:
        add_message_to_scrolledtext("[SERVER] empty message can not be send to the chat")
    
    message_textbox.delete(0,tk.END)

root = tk.Tk()
root.title("Msg App")
root.geometry("500x500")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame = tk.Frame(root,bg=DARK_GREY,height=100, width=500)
top_frame.grid(row=0,column=0,sticky=tk.NSEW)

middle_frame = tk.Frame(root,bg=LIGHT_GREY,height=300, width=500)
middle_frame.grid(row=1,column=0,sticky=tk.NSEW)


bottom_frame = tk.Frame(root,bg=DARK_GREY,height=100, width=500)
bottom_frame.grid(row=2,column=0,sticky=tk.NSEW)


username_label = tk.Label(top_frame,text="Username :",font=FONT,bg=DARK_GREY,fg=WHITE)
username_label.pack(side=tk.LEFT,padx=10)

username_textbox = tk.Entry(top_frame,font=FONT,bg=WHITE,fg=BLACK,width=15)
username_textbox.pack(side=tk.LEFT,padx=1)

username_button = tk.Button(top_frame,text="join",font=FONT,bg=BLUE,fg=BLACK,command=join)
username_button.pack(side=tk.LEFT,padx=10)

message_textbox = tk.Entry(bottom_frame,font=FONT,bg=WHITE,fg=BLACK,width=24)
message_textbox.pack(side=tk.LEFT,padx=10)

message_button = tk.Button(bottom_frame,text="Send",font=BUTTON_FONT,bg=BLUE,fg=BLACK,command=send_message)
message_button.pack(side=tk.LEFT,padx=10)

chat_scrolledtext = scrolledtext.ScrolledText(middle_frame,font=CHAT_FONT,bg=LIGHT_GREY,fg=BLACK,width=40,height=15.5)
chat_scrolledtext.config(state=tk.DISABLED)
chat_scrolledtext.pack(side=tk.TOP)



def listen_messages_from_server(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                username, content = message.split('~')
                add_message_to_scrolledtext(f"[{username}] {content}")
            else:
                print("Empty message received.")
        except:
            print("Error receiving message from server.")
            break


def send_username_to_server(client):
    username = username_textbox.get().strip()
    if username:
        client.sendall(username.encode())
        threading.Thread(target=listen_messages_from_server, args=(client,)).start()
    else:
        messagebox.showerror("Username Error!", "Username cannot be empty!")
        exit(0)



def main():
    root.mainloop()
    



if __name__ == "__main__":
    main()