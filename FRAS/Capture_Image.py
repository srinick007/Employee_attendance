import csv
import cv2
import os

# Function to check if a string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# Function to take images
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if is_number(Id) and name.isalpha():
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        # Check if TrainingImages folder exists, if not, create it
        if not os.path.exists("TrainingImage"):
            os.makedirs("TrainingImage")

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                sampleNum += 1
                cv2.imwrite(f"TrainingImage/{name}.{Id}.{sampleNum}.jpg", gray[y:y + h, x:x + w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q') or sampleNum > 100:
                break

        cam.release()
        cv2.destroyAllWindows()

        res = f"Images Saved for ID : {Id} Name : {name}"
        header = ["Id", "Name"]
        row = [Id, name]

        csv_file_path = "EmployeeDetails/EmployeeDetails.csv"
        if os.path.isfile(csv_file_path):
            with open(csv_file_path, 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        else:
            with open(csv_file_path, 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(header)
                writer.writerow(row)
    else:
        if is_number(Id):
            print("Enter Alphabetical Name")
        if name.isalpha():
            print("Enter Numeric ID")
