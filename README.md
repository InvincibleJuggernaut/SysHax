# VelFitTest-6

<h2>Introduction</h2>

<p> This is an application aimed at automating Vehicle Fitness Test process in India. As per Motor Vehicle act, all commercial vehicles are mandated to undergo fitness test periodically, depending on vehicle age. The vehicles are to be brought to designated fitness centres (which are normally one centre per district in most states) for inspection and certification. There are normally long queues and the process is hassle some. An innovative solution is required to 
ease this process for all.</p>
<p>Therefore, fitness test procedure needs to be automated. The testing also needs to be done transparently. Wherever possible, the parameters are to be tested automatically (obtain the image / video for selected test, analyze and 
rate the test as pass / fail. For the tests where manual intervention is required (checking the brakes, etc.), the authorized personnel will key-in the details (online). </p>

<h2> Technology Stack</h2>
<ul type="disc">
  <li>sqlite3 in the back-end</li>
  <li>Flask for the front-end</li>
  <li>Keras modelling for the DL models</li>
  <li>TensorFlow for ML models</li>
  <li>OpenCV for real-time computer vision capabilities</li>
  </ul>

<h2> Working</h2>
<p> The application first initiates login for an RTO Officer. Then, they make proceed to test the vehicle for features like external damage, condition of wipers, condition of windshield. All these tasks are automated. Some evaluation need human interaction like evaluating engine, tyres, seatbelts etc. These can be keyed-in by the RTO officer and then they may proceed to generate the final report for the vehcile fitness certificate.</p>

<h2> Datasets</h2>

<p>It was quite a challenging task to obtain a ready-made dataset for training the models. Other than the dataset for external body damage which can be viewed <a href="https://github.com/neokt/car-damage-detective">here</a>, we had to resort to synthesizing our own dataset by scraping the web. All the datasets used for training the models can be found <a href="https://drive.google.com/drive/folders/1ttZocSV1DpBV7V5vMpp1ZrSl_BDASVYD?usp=sharing">here</a>.</p>

<h2> Pre-requisistes</h2>

<p> All the dependencies can be found <a href="requirements.txt">here</a>.</p>

<h2>Setup</h2>

<p> Clone or download the repository in your preferred directory using:</p>

```
git clone https://github.com/InvincibleJuggernaut/VelFitTest-6.git
```

<p> To begin with the setup, first install all the dependencies using:</p>

```
cd VelFitTest-6
pip3 install -r requirements.txt
```

<h2>Usage</h2>

<p> The application can be run locally by using:</p>

```
python3 main.py
```
