import subprocess, json

ideaPath = "C:/Users/pressos/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/"
officeFolder = "C:/Program Files/Microsoft Office/root/Office16"

with open(ideaPath + ".channel.settings.json") as f:
    data = json.load(f)

ideaPath += data["active-application"]["builds"][0]
ideaPath += "/bin/idea64"

# print("/n" + ideaPath)
subprocess.Popen([ideaPath])
subprocess.Popen(officeFolder + "/OUTLOOK")
subprocess.Popen(officeFolder + "/lync")
subprocess.Popen("C:/Program Files (x86)/Microsoft/Skype for Desktop/Skype")
subprocess.Popen("C:/Program Files/Google/Drive/googledrivesync")
subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/Chrome")
