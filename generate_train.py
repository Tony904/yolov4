import os

image_files = []
os.chdir("/darknet/data/obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(tuple([".jpg", "JPG"])):
        image_files.append("/darknet/data/obj/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
