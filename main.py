import time

import cv2

cap = cv2.VideoCapture(str(input("VideoFile: ")))


letters = open("lValue.txt","r").readlines()
print(letters)



print(cap.get(cv2.CAP_PROP_FPS))

def turnTo(x):
    return int((x/256)*len(letters))
def convert(frame):
    c = (frame+"#").strip()

    nowC = []


    curltr = c[0]
    curcount = 0
    for g in range(len(c)):
        if curltr != c[g]:
            if curcount <= len("#" + curltr + str(curcount) + "+"):
            #if curcount == 1:
                for _ in range(curcount):
                    nowC.append(curltr)
            else:
                nowC.append( "#"+curltr +str(curcount)+"+")
            curcount = 0
            curltr = c[g]
        if curltr == c[g]:
            curcount += 1

    return "".join(nowC)



succ = True

video = open("Video.txt","w",encoding="utf-8")

frm = 0
print()




#SIZE = (int(120/2/2),int(90/2/2))
SIZE = (int(input("SizeX: ")),int(input("SizeY: ")))
skip = int(input("SkipFrames: "))

video.write(str(SIZE[0])+"\n")
video.write(str(SIZE[1])+"\n")

video.write(str(skip)+"\n")
video.write(str(cap.get(cv2.CAP_PROP_FPS))[:-2]+"\n")
prevFrame = ""
while succ:
    for _ in range(skip):
        succ, image = cap.read()
        #_,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
        if not succ:
            quit(0)
    frm += skip

    #print(image.shape)
    image = cv2.resize(image,SIZE)

    frame = ""
    for m in range(image.shape[2]):
        for j in range(image.shape[0]):
            for k in range(image.shape[1]):
                cr = letters[turnTo(image[j,k,m])][0]
                frame += cr
        frame +="-"


    frame = convert(frame)


    print(image.shape[0] * image.shape[1] * image.shape[2], cap.get(cv2.CAP_PROP_FRAME_COUNT) - frm, frm,
          cap.get(cv2.CAP_PROP_FRAME_COUNT),len(frame))

    #cv2.imwrite("A.png",image)
    #open("A.txt","w").write(frame)
    #print(frame)
    if prevFrame == frame:
        video.write(".\n")
    else:
        video.write(frame + "\n")
    prevFrame = frame