import cv2
import numpy as np
import os

data_folder = "C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\face_recog\\data"

def authenticate():
    # Load the face recognition models for each person
    models = {}
    for person_name in os.listdir(data_folder):
        person_folder = os.path.join(data_folder, person_name)
        if os.path.isdir(person_folder):
            model = cv2.face.EigenFaceRecognizer_create()
            faces = []
            labels = []

            # Read images from the person's folder
            for file in os.listdir(person_folder):
                if file.endswith(".jpg"):
                    image_path = os.path.join(person_folder, file)
                    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    faces.append(cv2.resize(image, (100, 100)))
                    labels.append(1)  # Assuming label 1 represents the person

            # Train the face recognition model
            model.train(faces, np.array(labels))
            models[person_name] = model

    # Start capturing video from the webcam
    cap = cv2.VideoCapture(1)

    while True:
        # Read the current frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Check the number of detected faces
        num_faces = len(faces)

        # If more than one face is detected, prompt to add someone
        if num_faces > 1:
            add_person = input("Multiple faces detected. Do you want to add someone to the data folder? (y/n): ")
            if add_person.lower() == "y":
                new_person_name = input("Enter the name of the person to add: ")
                new_person_folder = os.path.join(data_folder, new_person_name)
                os.makedirs(new_person_folder, exist_ok=True)
                print("Collecting face photos for", new_person_name)
                capture_face_photos(new_person_folder)
                continue

        # Iterate over detected faces
        for (x, y, w, h) in faces:
            # Extract the face region
            face = gray[y:y+h, x:x+w]

            # Resize the face image for recognition
            face_resized = cv2.resize(face, (100, 100))

            # Recognize the face using each model
            for person_name, model in models.items():
                # Predict the label and confidence for the face
                label, confidence = model.predict(face_resized)

                # Check if the predicted label matches the current person's label with a confidence threshold
                if label == 1 and confidence < 4000:
                    # Draw a rectangle around the face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                    # Put the name as text on the rectangle
                    cv2.putText(frame, person_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    break  # Exit the loop if a match is found

        # Display the frame with the bounding box and labels
        cv2.imshow("Face Recognition", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()


def capture_face_photos(person_folder):
    # Start capturing video from the webcam
    cap = cv2.VideoCapture(0)

    # Counter for captured photos
    photo_count = 0

    while photo_count < 10:  # Capture 10 photos
        # Read the current frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

        # Check if a face is detected
        if len(faces) == 1:
            # Extract the face region
            (x, y, w, h) = faces[0]
            face = gray[y:y+h, x:x+w]

            # Resize the face image for saving
            face_resized = cv2.resize(face, (100, 100))

            # Save the face image
            photo_count += 1
            photo_filename = f"{person_folder}/{person_folder}_{photo_count}.jpg"
            cv2.imwrite(photo_filename, face_resized)

            # Display the frame with the bounding box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Capturing: {photo_count}/10", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        elif len(faces) > 1:
            # Display warningmessage if multiple faces are detected
            cv2.putText(frame, "Multiple faces detected. Please align with a single face.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the frame with the bounding box and capturing progress
        cv2.imshow("Capture Face Photos", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()


# Call the authenticate function to start the face recognition
authenticate()
