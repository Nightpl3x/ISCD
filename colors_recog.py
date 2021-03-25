import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import variables as v

'''
Setup:
'''
#img = v.image_sharp
img = cv2.imread("images/_rainbow.jpeg") # read test image

index=["color", "color_name", "hex", "R", "G", "B"] # index colors
csv = pd.read_csv('colors.csv', names=index, header=None) # and read csv file

'''
Globals:
'''
clicked = False
r = g = b = xpos = ypos = 0

'''
Function:
'''
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"])) # Get RGB value trough simple absolute subtraction
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
'''
Showcase:
'''
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Detection')
cv2.setMouseCallback('Color Detection', mouse_click)

while(1):
    cv2.imshow("Color Detection",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)#Creating text string to display( Color name and RGB values )
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)#For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()