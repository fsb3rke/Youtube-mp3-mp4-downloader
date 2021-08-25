import os
from pytube import YouTube
import Brango
import os
while True:
    def true():
        return True
    def false():
        return False
    true = true()
    false = false()
    iss:bool = true
    issList:bool = false
    listMode = []
    link = str(input("link(çıkmak:Q/q||liste:L/l): "))
    if link == "Q" or link == "q":
        break
    if link == "L" or link == "l":
        while True:
            issList = true
            link2 = str(input("liste/link(çıkmak:Q/q||liste:L/l): "))
            if link2 == "Q" or link2 == "q":
                break
            if link2 == "L" or link2 == "l":
                ssadf:int = 0
                for l in listMode:
                    ssadf += 1
                    print(f"{ssadf}. = {l}")
            else:
                listMode.append(link2)
    mp = int(input("mp4/mp3(1|2): "))
    try:
        if mp == 1:
            if issList:
                for one in listMode:
                    YouTube(one).streams.filter(mime_type="video/mp4").first().download()
            else:
                YouTube(link).streams.filter(mime_type="video/mp4").first().download()
        elif mp == 2:
            if issList:
                for two in listMode:
                    video = YouTube(two).streams.filter(only_audio=true).first()
                    filex = video.download()
                    base, ext = os.path.splitext(filex)
                    filey = base + ".mp3"
                    os.rename(filex, filey)
            else:
                video = YouTube(link).streams.filter(only_audio=true).first()
                filex = video.download()
                base, ext = os.path.splitext(filex)
                filey = base + ".mp3"
                os.rename(filex, filey)
    except:
        iss = false
    if iss:
        print("indirildi")
    else:
        print("indirilemedi")

    def wrt():
        print(f"Video ismi: {videoTitle}\nThumbnail Url: {thumbnailUrl}")
        Brango.Brango("editor.js", "a").WriteFile(f"""
asd('{videoTitle.replace("'", "")}')
dsa('{thumbnailUrl}')
        """)
    try:
        if issList:
            for i in listMode:
                videoTitle = str(YouTube(i).title)
                thumbnailUrl = str(YouTube(i).thumbnail_url)
                wrt()
        else:
            videoTitle = str(YouTube(link).title)
            thumbnailUrl = str(YouTube(link).thumbnail_url)
            wrt()
    except:
        pass
    def jsClear():
        Brango.Brango("editor.js", "w").WriteFile("""
function asd(x="normal") {
    var a = document.createElement("div")
    a.innerHTML = x
    document.body.appendChild(a)
}
function dsa(x="https://i2.milimaj.com/i/milliyet/75/0x0/5ea3069155428010fc7475da.jpg") {
    var b = document.createElement("img")
    b.src = x
    document.body.appendChild(b)
}
        """)