import cv2
import numpy as np
import math


class hello():


    def detect(im):
        BLACK_THRESHOLD = 200
        THIN_THRESHOLD = 10
        ret2,thresh = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #cv2.imshow('image_2',thresh)
        contours, hierarchy = cv2.findContours(thresh, 1, 3)
        idx = 0

        xmax = 0
        ymax = 0
        wmax = 0
        hmax = 0

        for cnt in contours:
            idx += 1
            x, y, w, h = cv2.boundingRect(cnt)
            #roi = im[y:y + h, x:x + w]

            if (h < THIN_THRESHOLD) or (w < THIN_THRESHOLD):

                continue

            #cv2.imwrite(str(idx) + '.png', roi)

            if (w > wmax) and (h > hmax):
                xmax = x
                ymax = y
                wmax = w
                hmax = h

        #cropim = crop(thresh ,ymax , xmax , hmax , wmax)
        #cv2.rectangle(im, (xmax, ymax), (xmax + wmax, ymax + hmax), (200, 0, 0), 2)

        return thresh,xmax,ymax,wmax,hmax

    def crop(im , xmax , ymax , wmax , hmax):
        crop = im[ ymax:ymax+hmax,xmax:xmax+wmax]
        #cv2.imshow("crop", crop)
        #print('X Y W H', wmax*hmax)
        return crop

    def count(im):


        n_white_pix = np.sum(im == 255)
        #print('Number of white pixels:', n_white_pix)
        n_black_pix = np.sum(im == 0)
        #  print('Number of black pixels:', n_black_pix)



        return n_white_pix,n_black_pix



    def middlecut(img):
        dimensions = img.shape

        #print(dimensions)
        height = img.shape[0]
        width = img.shape[1]
        #channels = img.shape[2]
        #print('Image Dimension    : ',dimensions)
        #print('Image Height       : ',height)
        #print('Image Width        : ',width)
        h = height / 3
        w = width / 3

        h = math.ceil(h)
        w = math.ceil(w)

        #print('Image Height       : ',h)
        #print('Image Width        : ',w)

        middlecut = img[h:h+h , w:w+w]
        #cv2.imshow("middlecut", middlecut)
        return middlecut

    def cal(white,black,all):

        whitepreall = white / all * 100

        return whitepreall

    def show(Brain_Per_All,Hole_Pre_Brain):
        brain = False
        hold = False
        Per_brain = 55
        Per_hold = 4
        good = "good"
        bad = "bad"
        uncertain =  "don't sure"
        result = "NULL"
        if (Brain_Per_All > Per_brain) :
            brain = True


        if (Hole_Pre_Brain < Per_hold) :
            hold = True


        if (brain == True) and (hold == True):
            result = good



        elif (brain == False) and (hold == False):
            result = bad


        else:
            result =  uncertain

        # else
        #     result =  "don't sure"
        #    pass

        print(result)

        return result

    def fix(picname):
        length = len(picname)
        picname_cut = ""
        for x in range(length):
            if x == 0:
                continue
            picname_cut = picname_cut + picname[x]
            #print(x)

        return picname_cut


    def run(picname):
        picname_cut = hello.fix(picname)


        path = picname_cut
        #path = r'C:\Users\porsc\Desktop\OAS30145_2.PNG'
        r_pic = cv2.imread(path, 0)

        result,x,y,w,h = hello.detect(r_pic)

        cropp = hello.crop(result,x,y,w,h)
        w,b = hello.count(cropp)
        Brain_Per_All = hello.cal(w,b,w+b)


        piccut = hello.middlecut(cropp)



        piccut = ~piccut
        #cv2.imshow("Original", r_pic)
        #cv2.imshow("detect", cropp)
        #cv2.imshow("middlecut", piccut)
        #cv2.imshow("inverse", piccut)

        w_H,b_H = hello.count(piccut)
        Hole_Pre_Brain = hello.cal(w_H,b_H,w)

        ans = hello.show(Brain_Per_All,Hole_Pre_Brain)

        print("Brain_Per_All : ",Brain_Per_All)
        print("Hole_Pre_Brain : ",Hole_Pre_Brain)
        print("Ture / False : ",ans)


        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


        return ans,Brain_Per_All,Hole_Pre_Brain
