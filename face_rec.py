import cv2, sys, numpy, os, time
from tkinter import messagebox
def eigentrn():
    global images
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    print('Training eigen...')

    (images, lables, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(fn_dir):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                lable = id
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1
    (im_width, im_height) = (112, 92)
    print(names)
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    start = time.time_ns()
    model = cv2.face.EigenFaceRecognizer_create()
    model.train(images, lables)
    model.save("abc.yml")
    end = time.time_ns()
    tm = end - start
    messagebox.showinfo("Process Complete", (str(names) + " have been trained by Eigen in " + str(tm) + "ns"))
    return names


def fishertrn():
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    print('Training fisher...')

    (images, lables, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(fn_dir):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                lable = id
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1
    (im_width, im_height) = (112, 92)
    print(names)
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    start = time.time_ns()
    model = cv2.face.FisherFaceRecognizer_create()
    model.train(images, lables)
    end = time.time_ns()
    tm = end - start
    messagebox.showinfo("Process Complete", (str(names) + " have been trained by Fisher in " + str(tm) + "ns"))


def lbphtrn():
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'
    (im_width, im_height) = (112, 92)

    print('Training lbph...')

    (images, lables, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(fn_dir):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                lable = id
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1
    (im_width, im_height) = (112, 92)
    print(names)
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]
    start = time.time_ns()
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, lables)
    end = time.time_ns()
    tm = end - start
    messagebox.showinfo("Process Complete", (str(names) + " have been trained by LBPH in " + str(tm) + "ns"))

