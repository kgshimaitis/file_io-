numbers = [1, 2, 3, 4, 5]
#f = open("numberfile/txt", "w+")
with open ("numberfile.txt", "w+") as f:
    for x in numbers:
        data = str(x)
        f.write(data)
#f.close()
