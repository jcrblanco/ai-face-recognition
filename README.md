Real-Time Face Detection and Similarity Comparison

This project demonstrates a simple application using Python, OpenCV, and the `face_recognition` library to detect faces via webcam and compare their similarity in real-time. The project is provided in a Jupyter Notebook format (`.ipynb`), making it easy to run and experiment with.

 Overview

The application captures video from the webcam, detects faces in each frame, and compares their similarity in real-time. If multiple faces are detected, the similarity percentage between them is displayed on the screen along with a visual representation (boxes around faces and lines between similar faces).

 Features

- Face Detection: Real-time face detection using `face_recognition` and OpenCV.
- Face Similarity Comparison: Calculates the similarity percentage between detected faces.
- Live Video Feed: Displays the live video feed with real-time annotations (face boxes and similarity lines).
- Interactive Jupyter Notebook: The code is provided in a Jupyter Notebook for easy experimentation and modification.

 Technology Stack

- Python: The main programming language used for this project.
- OpenCV: Used for capturing video from the webcam and image processing.
- face_recognition: Utilized for face detection and encoding, as well as for calculating the distance between face encodings to determine similarity.
- Jupyter Notebook: Provides an interactive environment to run and modify the code easily.

 How It Works

1. Video Capture: The program opens the webcam to capture real-time video.
2. Face Detection: The `face_recognition` library detects faces in each frame.
3. Face Encoding: The detected faces are converted into encodings, which can then be compared.
4. Similarity Calculation: If two or more faces are detected, the similarity between them is calculated and displayed as a percentage.
5. Real-Time Display: The video feed shows the detected faces with boxes around them, along with lines connecting similar faces.

 Challenges

One of the main challenges during development was optimizing the real-time performance of the face detection and similarity calculation, ensuring the system remains responsive while handling multiple faces in a single frame.

 Requirements

- Python 3.x
- Jupyter Notebook
- OpenCV
- face_recognition

Install the required libraries with:

bash
pip install opencv-python face_recognition numpy jupyter

Usage

To run the notebook:

1. Clone this repository.
2. Install the required libraries.
3. Open the notebook:

bash
jupyter notebook face_comparison.ipynb

4. Run all the cells in the notebook to start the face detection and comparison process. Press `q` within the video window to stop the webcam feed.

Next Steps

- Improving performance for larger groups of faces.
- Extending the application to include face recognition from a pre-trained database of known faces.

Contributing

Feel free to contribute by forking the repository, submitting issues, or suggesting improvements via pull requests. I am always open to feedback and collaboration!


