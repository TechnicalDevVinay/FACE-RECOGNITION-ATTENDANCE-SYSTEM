import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("C:/SEM 6 PROJECT/")
firebase_admin.initialize_app(cred,{
    'databaseURL':"",
    'storageBucket':""
})

bucket=storage.bucket()




cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,360)

imgBackground = cv2.imread('C:/SEM 6 PROJECT/RESOURCES/BACKGROUND1.png')

folderModePath = ('C:/SEM 6 PROJECT/RESOURCES/MODES')
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

modeType = 0
counter = 0
id = -1
imgStudent = []


while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)


    imgBackground[155:155 + 360, 250:250 + 640] = img
    imgBackground[70:70+ 482, 904:904 + 262] = imgModeList[modeType]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print("matches", matches)
        #print("faceDis", faceDis)
        
        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 250 + x1, 125 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
            id = studentIds[matchIndex]
            if counter == 0:
                counter = 1
                modeType = 1

    if counter != 0:

        if counter ==1:
            studentInfo = db.reference(f'STUDENTS/{id}').get()
            print(studentInfo)
            blob = bucket.get_blob(f'C:/SEM 6 PROJECT/IMAGES/{id}.png')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgStudent = cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
            datetimeObject = datetime.strptime(studentInfo['LAST_ATTENDENCE_TIME'],"%Y-%m-%d %H:%M:%S")
            secondsElapsed = (datetime.now()-datetimeObject).total_seconds()
            print(secondsElapsed)
            if secondsElapsed >25:
                ref = db.reference(f'STUDENTS/{id}')
                studentInfo['TOTAL_ATTENDENCE'] +=1
                ref.child('TOTAL_ATTENDENCE').set(studentInfo['TOTAL_ATTENDENCE'])
                ref.child('LAST_ATTENDENCE_TIME').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                modeType = 3
                counter = 0
                imgBackground[141:141+ 220, 922:922+ 220] = imgStudent


        if modeType != 3:

            if 10<counter<20:
                modeType= 2
            imgBackground[70:70+ 482, 904:904 + 262] = imgModeList[modeType]    

            if counter<=10:
                cv2.putText(imgBackground, str(studentInfo['TOTAL_ATTENDENCE']), (990, 120),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.putText(imgBackground, str(studentInfo['BACHELORS']), (935, 454),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(id), (1050, 391),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(studentInfo['RANKING']), (952, 530),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
                cv2.putText(imgBackground, str(studentInfo['YEAR']), (1030, 530),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
                cv2.putText(imgBackground, str(studentInfo['STARTING_YEAR']), (1085, 530),
                cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 1)
                (w, h), _ = cv2.getTextSize(studentInfo['NAME'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414 - w) // 2
                cv2.putText(imgBackground, str(studentInfo['NAME']), (915 + offset, 412),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                imgBackground[141:141+ 220, 922:922+ 220] = imgStudent

                


            counter+=1
            
            if counter>=20:
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
                imgBackground[70:70+ 482, 904:904 + 262] = imgModeList[modeType]

                   




    cv2.imshow("STANFORD TECHNOLOGY UNIVERSITY FACE ATTENDENCE",imgBackground)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


     