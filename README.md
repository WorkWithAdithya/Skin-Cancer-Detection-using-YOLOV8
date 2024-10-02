<h1>Skin-Cancer-Detection-using-YOLOV8</h1> 
<h1>Introduction</h1>
<p>Melanoma is a type of skin cancer that originates from the pigment producing cells known as melanocytes. Melanoma is considered more dangerous than other types of skin cancer due to its ability to spread to other parts of the body. With modern technology, it is feasible to detect skin cancer at an early stage and treat it effectively. Traditional methods of melanoma detection rely on visual inspection, checking the biopsy results by dermatologists which is time consuming and is prone to human errors. Leveraging the advancements using deep learning technology.  </p>

<h1>Language used</h1>
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

<h1>Tools used</h1>
<li>Ultralytics : It is a library used for real time object detection and classification with high accuracy . </li>
<li>Cuda : It enables the power of GPU for general-purpose processing </li>
<li>Python Tkinter : Python library used for creating GUI.</li>
<li>LabelImge :LabelImg is a graphical image annotation tool.</li>
<li>Simple Mail Transfer Protocol : Simple Mail Transfer mechanism (SMTP) is a mechanism for exchanging email messages between servers. It is an essential component of the email communication process and operates at the application layer of the TCP/IP protocol stack.</li>


 <h1>Problem statemnt</h1>
 <p>The aim of the project is to detect the Melanoma Skin Cancer from dermoscopic images using Deep Learning CNN algorithm. Train and validate the model on a dataset of malignant melanomas and benign non-melanomas.  Evaluate its performance using metrics like F1 curve and precision, recall curves. Deploy the model as a user-friendly application for patients. Aim to enhance early detection and improve patient outcomes in melanoma diagnosis
</p>

<h1>Figure representing Melanoma</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/melanoma.png  width="600" height="450">

<h1>Objectives</h1>
<li>To collect the dataset containing dermascopic images .</li>
<li>To pre-process the image.</li>
<li>Using the pre-processed image to train the model using YOLO</li>
<li>To evaluate the trained model using the image present for validation.</li>
<li>To classify the image if it is melanoma or non-melanoma.</li>

<h1>Technology used</h1>
<h1>Deep Learning(CNN)</h1>
<p>A Convolutional Neural Network (CNN) is a type of Deep Learning neural network architecture commonly used in Computer Vision. Computer vision is a field of Artificial Intelligence that enables a computer to understand and interpret the image or visual data. </p>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/CNN%20architecture.png  width="1000" height="450">

<h1>YOLO (You look only once)</h1>
<p>YOLO is a real-time object detection algorithm that efficiently processes images and divides them into a grid, predicting bounding boxes and class probabilities for objects within each grid cell. Unlike traditional methods that classify and locate objects in multiple stages, YOLO performs both tasks simultaneously in a single pass. This makes YOLO well- suited for applications requiring fast and accurate object detection.
</p>
<p>Some of the important features of YOLO include </p>
<li>Single shot detection</li>
<li>Grid-based detection</li>
<li>Features extraction using CNN</li>
<li>Efficient</li>
<li>Scalable</li>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/YOLO%20working.png  width="800" height="800">

<h1>System architecture</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/System%20Architecture.png  width="800" height="1000">
<li>The dataset which is collected is divided into training data(70%) and testing data(30%)</li>
<li>Annotations are each image performed for each of the images present in the dataset and classes are defined for each of the images .</li>
<li>Training data thus generated will undergo training under YOLO where YOLO recognizes each of the images  characteristics and features.</li>
<li>The trained model generated will undergo evaluation using the testing data and prediction is made for each of the images .</li>

<h1>Result and Snapshots</h1>
<h1>Introduction Page</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/intro%20page.png  width="1000" height="800">

<h1>Prediction Page</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/prediction%20page.png  width="1000" height="800">

<h1>Output page</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/output.png  width="500" height="500">

<h1>Contact Page</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/contact%20page.png  width="1000" height="800">

<h1>Mail message</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/Mail%20page.png width="800" height="800">

<h1>Confusion Matrix</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/Confusion%20matrix.png  width="500" height="500">

<h1>F1-Confidence curve</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/F1%20confidence%20curve.png width="500" height="500">

<h1>Precision-Confidence curve</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/precision%20confidence.png  width="500" height="500">

<h1>Precision-Recall curve</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/precision%20recall.png  width="500" height="500">

<h1>Recall-Confidence curve</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/recall%20confidence.png  width="500" height="500">


<h1>Graphical Representaion of accuracy comparision</h1>
<img src=https://github.com/WorkWithAdithya/Skin-Cancer-Detection-using-YOLOV8/blob/main/Final%20Images/Accuracy%20acheived.png  width="1000" height="800">


