with open("layouts/default.html","r") as f:
       data = f.read()
data = data.replace("../css", "css")

data = data.replace("../images", "images")
data = data.replace("../js", "js")


data = data.replace("blossom1", "moon")

data = data.replace("blossom2", "sea")

with open("layouts/shan.html", "w", newline = "\n") as f:
       f.write(data)