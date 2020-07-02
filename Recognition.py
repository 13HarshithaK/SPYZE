import cv2, sys, numpy, os, time
from tkinter import messagebox
import face_rec

def eigrec(names):
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    (images, lables, namess, id) = ([], [], {}, 0)
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)
    model = cv2.face.EigenFaceRecognizer_create()
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        model.read("abc.yml")
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
        faces = haar_cascade.detectMultiScale(mini)
        cv2.imshow("recogniser",im)
        print(names)
        print(faces)
        name=""
        for face in faces:
            print("1")
            (x, y, w, h) = [v * size for v in face]
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            cv2.imshow("Image", gray[y:y + h, x:x + w])
            face_resize = cv2.resize(face, (im_width, im_height))
            label, confidence = model.predict(face_resize)
            print(label)
            name=names[label]
            print(confidence)

            if int(confidence) > 3500:
                return "unknown"
                exit()
            else:
                return name
            cv2.imshow('video', face)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    print("eigenvector")


def fisrec():
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    (images, lables, names, id) = ([], [], {}, 0)
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)
    model = cv2.face.FisherFaceRecognizer_create()
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
        faces = haar_cascade.detectMultiScale(mini)
        print(faces)
        for face in faces:
            print("1")
            (x, y, w, h) = [v * size for v in face]
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            cv2.imshow("Image", gray[y:y + h, x:x + w])
            face_resize = cv2.resize(face, (im_width, im_height))
            label, confidence = model.predict(face_resize)
            print(label)
            print(confidence)

            if int(confidence) > 3000:
                return "unknown"
                exit()
            else:
                return (names[label])
            cv2.imshow('video', face)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    print(eigenvector)


def lbphrec():
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    (images, lables, names, id) = ([], [], {}, 0)
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)
    model = cv2.face.LBPHFaceRecognizer_create()
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))
        faces = haar_cascade.detectMultiScale(mini)
        print(faces)
        for face in faces:
            print("1")
            (x, y, w, h) = [v * size for v in face]
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            cv2.imshow("Image", gray[y:y + h, x:x + w])
            face_resize = cv2.resize(face, (im_width, im_height))
            label, confidence = model.predict(face_resize)
            print(label)
            print(confidence)

            if int(confidence) > 3000:
                return "unknown"
                exit()
            else:
                return names[label]
            cv2.imshow('video', face)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    print(eigenvector)



