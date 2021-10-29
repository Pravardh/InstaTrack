import instaloader
import tkinter as tk
import sys

def getFollowers(username,password,window):
    L = instaloader.Instaloader()

    L.login(username, password)  # (login)

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, username)

    # Print list of followees
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file = open(f"{username} Followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1

    tk.Label(window,text = f"Task completed. File has been saved to:{username} Followers.txt \n",font = ('Calibri',14)).pack()

def compareFollowers(username,password):
    f =  open(f'{username} Followers.txt')
    a = f.read().splitlines()
    f.close()

    L = instaloader.Instaloader()

    L.login(username, password)  # (login)

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, username)

    # Print list of followees
    follow_list = []
    for followee in profile.get_followers():
        follow_list.append(followee.username)

    for i in a:
        if i not in follow_list:
            print(f'{i} has unfollowed you!')

    print('done!')

window = tk.Tk()
window.geometry("500x500")
window.resizable(False,False)
window.title("InstaTrack")

Title = tk.Label(window,text = "InstaTrack",font = ('Calibri',20)).pack()

Username = tk.Label(window,text = "Username\n",font = ('Calibri',10)).pack()
ue = tk.Entry(window)
ue.pack()
Password = tk.Label(window,text = "Password\n",font = ('Calibri',10)).pack()
pe = tk.Entry(window,show = '*')
pe.pack()

GetFollowers = tk.Button(window,text = "Get Followers List",command = lambda: getFollowers(ue.get(),pe.get(),window),font = ('Calibri',16))
GetFollowers.pack()

tk.Button(window,text = "Compare Followers",command = lambda: compareFollowers(ue.get(),pe.get()),font = ('Calibri',10)).pack()

tk.Button(window,text = "Exit",command = lambda: sys.exit(),font = ('Calibri',16)).pack()
window.mainloop()

