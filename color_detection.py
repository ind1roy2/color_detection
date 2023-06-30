
import pandas as pd
import numpy as np

import cv2

df = pd.read_csv("E:/color_detection_cc/colors.csv")

df.head()

df.info()

img = cv2.imread("E:/color_detection_cc/colorpic.jpg") # this returns the image as an array

# global variables which will be required later
clicked = False
r = g = b = x_pos = y_pos = 0

col = ['col_id','color','hex','R','G','B']

df.columns = col

df.head()

def draw(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    global b,g,r,x_pos,y_pos,clicked
    clicked = True
    x_pos = x
    y_pos = y
    b,g,r = img[y,x]
    b = int(b)
    g = int(g)
    r = int(r)

def color_name(R,G,B):
  l = []
  threshold = 10000
  for i in range(len(df)):
    diff = abs(R - int(df.loc[i,"R"])) + abs(G - int(df.loc[i,"G"])) + abs(B - int(df.loc[i,"B"]))
    if diff<threshold:
      threshold = diff
      col = df.loc[i,"color"]
  return col

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while True:

    cv2.imshow("image", img)
    if clicked == True:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black color
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()