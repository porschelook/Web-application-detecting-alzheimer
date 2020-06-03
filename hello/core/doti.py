import cv2
import numpy as np
import math


class hello():

    def detect(im):
        BLACK_THRESHOLD = 200
        THIN_THRESHOLD = 10
        ret2,thresh = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(thresh, 1, 3)
        idx = 0
        xmax = 0
        ymax = 0
        wmax = 0
        hmax = 0

        for cnt in contours:
            idx += 1
            x, y, w, h = cv2.boundingRect(cnt)
            if (h < THIN_THRESHOLD) or (w < THIN_THRESHOLD):
                continue
            if (w > wmax) and (h > hmax):
                xmax = x
                ymax = y
                wmax = w
                hmax = h
        return thresh,xmax,ymax,wmax,hmax

    def crop(im , xmax , ymax , wmax , hmax):
        crop = im[ ymax:ymax+hmax,xmax:xmax+wmax]
        return crop

    def count(im):
        n_white_pix = np.sum(im == 255)
        n_black_pix = np.sum(im == 0)
        return n_white_pix,n_black_pix



    def middlecut(img):
        dimensions = img.shape
        height = img.shape[0]
        width = img.shape[1]
        h = height / 3
        w = width / 3

        h = math.ceil(h)
        w = math.ceil(w)
        middlecut = img[h:h+h , w:w+w]

        return middlecut

    def cal(white,black,all):
        whitepreall = white / all * 100
        return whitepreall

    def show(Brain_Per_All,Hole_Pre_Brain):
        brain = False
        hold = False
        Per_brain = 63.239662
        Per_hold = 3.904078
        good = "ไม่มีโอกาศเสี่ยเป็นโรคอัลไซเมอร์"
        bad = "มีโอกาศเสี่ยเป็นโรคอัลไซเมอร์"
        uncertain =  "มีโอกาศเสี่ยเป็นโรคอัลไซเมอร์ ควรไปพบแพทย์"
        result = "NULL"

        if (Hole_Pre_Brain > Per_hold) :
            if (Brain_Per_All > Per_brain) :
                if (Hole_Pre_Brain > 4.636591) :
                    hold = True
                    brain = True
                else :
                    brain = True
                    hold = False
            else:
                brain = False
                hold = False
        else :
            hold = True
            brain = True

        if (brain == True) and (hold == True):
            result = good

        elif (brain == False) and (hold == False):
            result = bad

        else:
            result =  uncertain
        print(result)

        return result

    def fix(picname):
        length = len(picname)
        picname_cut = ""
        for x in range(length):
            if x == 0:
                continue
            picname_cut = picname_cut + picname[x]
        return picname_cut


    def run(picname):
        picname_cut = hello.fix(picname)
        path = picname_cut
        r_pic = cv2.imread(path, 0)
        result,x,y,w,h = hello.detect(r_pic)
        cropp = hello.crop(result,x,y,w,h)
        w,b = hello.count(cropp)
        Brain_Per_All = hello.cal(w,b,w+b)
        piccut = hello.middlecut(cropp)
        piccut = ~piccut
        result_2,x_2,y_2,w_2,h_2 = hello.detect(piccut)
        cropp_2 = hello.crop(result_2,x_2,y_2,w_2,h_2)
        w_H,b_H = hello.count(cropp_2)
        Hole_Pre_Brain = hello.cal(w_H,b_H,w)
        ans = hello.show(Brain_Per_All,Hole_Pre_Brain)

        # cv2.imshow("orginal", r_pic)
        # cv2.imshow("brain", result)
        # cv2.imshow("BW", cropp)
        # cv2.imshow("hold", piccut)
        # cv2.imshow("orginal_2", piccut)
        # cv2.imshow("BW_2", result_2)
        # cv2.imshow("hold_2", cropp_2)

        print("Brain_Per_All : ",Brain_Per_All)
        print("Hole_Pre_Brain : ",Hole_Pre_Brain)
        print("Ture / False : ",ans)

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


        return ans,Brain_Per_All,Hole_Pre_Brain
