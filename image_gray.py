import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import matplotlib.cm as cm

IMG_DIR = '/Users/christopherjohnson/Desktop/Shed/'
originalImage = cv2.imread(IMG_DIR+ 'treering.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)


(thresh3, blackAndWhiteImage3) = cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY)

blur = cv2.GaussianBlur((blackAndWhiteImage3),(3,3),0)

y,x = blur.shape


#circle vars
xcen = int(x/2)
ycen = int(y/2)
rad = 50
cwidth = 1

#line vars
xbeg = 0
ybeg = int(y/2)
xend = int(x)   
yend = int(y/2)
lwidth = 1

#draw shapes
#cv2.circle(originalImage,(xcen,ycen), rad, (0,0,255), cwidth)
cv2.line(originalImage,(xbeg,ybeg),(xend,yend),(255,0,0),lwidth)
cv2.line(originalImage,(xbeg,ybeg+2),(xend,yend+2),(255,0,0),lwidth)
cv2.line(originalImage,(xbeg,ybeg-2),(xend,yend-2),(255,0,0),lwidth)
cv2.line(originalImage,(xbeg,ybeg+6),(xend,yend+6),(0,0,255),lwidth)
cv2.line(originalImage,(xbeg,ybeg-6),(xend,yend-6),(0,0,255),lwidth)


#print(blur[yend])
xblur = np.arange(x)
print(yend)


images1 = {'Orig': originalImage,
        'Blur': blur,  
          }

fig = plt.figure(figsize=(10,10))
ax = []

rows = 2
columns = 1
keys = list(images1.keys())
#for i in range(rows*columns):
#    ax.append( fig.add_subplot(rows, columns, i+1) )
#    ax[-1].set_title('Original - ' + keys[i]) 
#    plt.imshow(images1[keys[i]], origin='lower')#,cmap=cm.gray,vmin=0, vmax=255)
#plt.show()
ax.append( fig.add_subplot(3, 1, 1) )
plt.imshow(images1[keys[0]], origin='lower')
ax.append( fig.add_subplot(3, 1, 2) )
plt.imshow(images1[keys[1]], origin='lower')
ax.append( fig.add_subplot(3, 1, 3) )
#plt.plot(xblur,blur[yend],'k')
#plt.plot(xblur,blur[yend+2],'g')
#plt.plot(xblur,blur[yend-2],'r')
plt.plot(xblur,blur[yend+6],'b')
#plt.plot(xblur,blur[yend-4],'c')
plt.show()