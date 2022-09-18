<html>

<body>
<h1>Cat & Dog Detector: </h1>
<h2>cat dog neural network implemented into website using flask</h2>
<p>Convolutional Neural Network (CNN) is an algorithm taking an image as input then assigning weights and biases to all the aspects of an image and thus differentiates one from the other. Neural networks can be trained by using batches of images, each of them having a label to identify the real nature of the image (cat or dog here). A batch can contain few tenths to hundreds of images. For each and every image, the network prediction is compared with the corresponding existing label, and the distance between network prediction and the truth is evaluated for the whole batch. Then, the network parameters are modified to minimize the distance and thus the prediction capability of the network is increased. The training process continues for every batch similarly.The main goal of this project is to develop a system that can identify images of cats and dogs. The input image will be analyzed and then the output is predicted. The model that is implemented can be extended to a website or any mobile device as per the need. The Dogs vs Cats dataset can be downloaded from the Kaggle website. The dataset contains a set of images of cats and dogs. Our main aim here is for the model to learn various distinctive features of cat and dog. Once the training of the model is done it will be able to differentiate images of cat and dog.</p>
<h1>Libraries Used: </h1>
<ul>
<li>Numpy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>tensorflow</li>
<li>keras</li>
<li>flask</li>
</ul>
<h1><b>WorkFlow</b></h1>

<ol>
<li>Data Preprocessing</li>
<li>Rescale & assign categorical designs</li>
<li>CNN Model</li>
<li>Splitting Data Into Training and Test Set</li>
<li>Visulazing Dataset and Determining Training Loss</li>
</ol>
<img src="./files/smsSpamImage.png" width="700" height="400">
<video width="320" height="240" controls src="./files/smsSpamDetector.mp4">
  <source src="./files/smsSpamDetector.mp4" type="video/mp4">
Video: 
</video>
<a href="https://cat-dogimagepredictoravijit.herokuapp.com/">Livelink</a>
<a href="#">Custom Dataset</a>
</body>

</html>
