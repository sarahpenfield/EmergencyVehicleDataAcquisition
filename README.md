# Automated Response to Emergency Vehicles

![image](https://user-images.githubusercontent.com/78807472/135682706-1d6bb726-967b-4284-af72-caa876460891.png)


### Introduction

### Motivation
Emergency vehicle response times are critical to saving lives of those in need both in arrival to the scene and transportation to the hospital or emergency care after an accident. By reducing emergency vehicle response time by just 1 minute, patient survival rate increases by over 2%. Everyday vehicles on the road are often a hindrance to the emergency vehicles reaching their destinations. To make this less of an issue, our team created an autoamted response system when emergency vehicles are detected. 

When the flashing lights and loud siren sounds of an emergency vehicle is sensed approaching the vehicle from behind, the radio volume is automatically reduced and a dashboard message is displayed 'Emergency Vehicle Approaching'. With the reduction in noise and visual cue, drivers will be able to react more quickly to make room on the road for emergency vehicles en route to an active scene or hospital.

### Goals

Our team aims to simulate this project idea by creating a scaled model of a personal vehicle and an emergency vehicle. We will sense based on three stimuli in the surrounding environment.
1. Light detected
2. Sound detected
3. Distance to nearest object behind.

The stimuli are combined using various conditional statements to determine when the emergency vehicle is approaching versus when there are other stimuli such as headlights, background noise, and perosnal vehicles approaching from behind. 

For the to scale model, print statements will be used to show the volume reduction of the radio and a flashing LED will be used to show the dashboard message that would be displayed.


## Progress Report

### Current Progress
October 1, 2021

A plan and schedule was created for the next two weeks until the project is due. The additional sensors were acquired from Amazon and most of the hardware was set up and ready to use. As a team, starter code for the light, sound, and distance sensors was added to the shared Google Drive for use in the next meeting. Finally, the team walked through the LED Tutorial on the course website for use as our dashboard display in the scaled model.

October 3, 2021

The team completed hardware setup of all of the sensors and the LED light.

![Oct3Circuit](https://user-images.githubusercontent.com/49326756/135782207-aafcd84f-e19b-41ab-9677-c0523eb0ba7f.JPG)

Together, we edited code for the following test cases that will be combined to determine if an emergency vehicle is approaching. We incorporated the ADC into the light sensor to show intensity rather than only light/no light.
1. Sound Detection only (SoundTest.py)
2. Light Detection only (LightandLED.py)
3. Distance Detection only (Distance.py)
4. Distance and Light Detection (LightDistanceTest103.py)
5. Sound and Light Detection (SoundLightTest103.py)

The first four test cases are fully working, yet the last is still a work in progress.

October 5, 2021

Our team added the LED and volume reduction to the code. We learned to publish the github rather than just send the edit link. We also created the prototypes out of boxes for the perosnal vehicle. Finally, we worked more on integrating the sound sensor to our code. We made some progress in understanding what the source code is doing (low output = high sound intensity), but need to continue working. We determined the correct sampling frequency to use based on light and sound.

October 7, 2021

Currently working on obtaining the spec sheets for all of our sensors used. Our team also met with Professor Berges to disccuss our code and found that putting the while loop inside the callback function rather than the other way around solves our problem. Additionally, the professor explained to us how the aliasing is occuring in the light frequency; discussed below.

Octboer 8, 2021

We ran all of our experiments and videod some of the trials. In our code, we added a write to text file section so that we would be able to do statistical analysis on the outputs to determine the number of false positives and false negatives we encountered in each trial. 


### Problems Encountered
October 1, 2021

The group had to talk for a bit about where to start with the project as there were a lot of tasks to work through. Also, the group forgot to plug in the Raspberry Pi, which caused some obvious issues when trying to make the LED flash.

October 3, 2021

At the beginning of Sunday's meeting, the group had to rewrite SD card. The monitors were displaying the message that no HDMI input was detected, but once it was rewritten there were no additional problems.
When editing all of the source code, we had to determine what sampling frequency we should be using. This was estimated based on the source code, but will be played with during the experimental phase of the project. Similarly, when writing the light intensity codes, we had to determine what difference in light intensity would be considered flashing. Using the source code, we ran a short experiment using the flashing light on an Apple Watch and went with 15% difference. However, this will continue to be edited during the full experiment phase. 
Finally, the code for the sound and light detection is still a work in progress because our group is trying to understand how the sound sensor works with 'bouncetime' as found in the source code and whether a return of True/1 or False/0 means sound was detected. 

October 5, 2021

We struggled to determine the sampling frequency we should be using for the sound sensor. By running experiments using a music notes app, we determined that the sensor could only occasionally detect 440 Hz. This means that our sampling rate will need to be at least 880 Hz, or one sample every 0.0011 seconds.

Below are a list of questions to ask at our meeting with the professor: 
1. How to get sound sensor to work, do we need bouncetime
2. How to use two different sampling frequencies to measure sound and light at same time (orders of magnitude difference between sound and light frequencies
3. How to justify sampling frequency of light (see LightDistanceLED105.py)

October 7, 2021
LED light was turning off at the beginning of each sample test
where should we place the initializing in the code with callback and while loop

October 8, 2021
light intensity difference = umbrella
recieving a none for every time the first sample was run
had to ask Brian for scissors
error in how to create text file

### Future Plan
October 1, 2021

At the next meeting, we would like to edit the source code to make as we need for the 7 cases we will be testing. Additionally, we'd like to finish assembling the hardware and create a scaled personal vehicle model.

October 3, 2021

At the next meeting, we will finish creating the  personal vehicle scaled model and continue editing the code. For the code, our specific tasks are to include:
1. Complete Sound and Light detection code
2. Create Distance and Sound detection code
3. Create Distance, Light, and Sound detection code
4. Create a master code that uses the return from 7 cases to determine if an emergency vehicle is actually approaching
5. Include radio reduction print statements

October 5, 2021

In our next meeting we will finish the sound code, likely with the help of the instructor, and incorporate it to the light and distance code. This will allow us to begin running the experiments. 

October 7, 2021

In our next meeting we plan to run the actual experiments with recording data and video.

October 8, 2021

In our next meeting we plan to edit and voiceover the videos from the meeting today and incorporate additional video / instructional and presentation information.

## Methodology

### Phenomena of Interest
1. Light
We are interested in knowing the intensity of the light in the surrounding environment as there will almost always be ambient light. When intensity is significantly higher than the surrounding light (5% greater) for multiple sensed periods of time, this is an indicator that an emergency vehicle could be approaching.

2. Sound  
We are interested in knowing the intensity of the sound in the surrounding envrionment as again there will almost always be background noise around the vehicle. However, our sensor cannot determine the intensity of sound and rather can only sense whether a sound above the threshold is present. When sound above the threshold is sesnsed multiple times in a row, it indicates that an emergency vehicle could be approaching.

3. Distance
We are interested in knowing the distance to the nearest object behind the personal vehicle. When this distance is less than a certain number of meters, we know that something is behind the car. This is an indicator than an emergency vehicle could be approaching. Note that on a smaller scale, our distance was only set at 50 cm.

Overall, each of these phenomena individually will pick up on many stimuli that are not actually emergency vehicles. However, combnining all three and using repeated sampling helps to decrease the number of false positives of approaching emergency vehicles. While annoying, it is important to note that false positives will not be harmful to anyone.

### Sensor(s) Used
1. Light (Photosensitive LM 393)
This sensor has both analog and digital outputs, depending on which way the switch is turned. Our group used the analog output and then utilized and ADC to convert to the digital information needed in the code. It also includes an onboard potentiometer for sensitivity adjustment, which we used depending on how bright the room was. Finally, its input voltage range is 3.3 - 5.0 V.

2. Sound (1PCS 3 Pin)
This sensor has an analog output in which a LOW value indicates a sound higher than the threshold and a HIGH value indicates that a louder sound has not been detected. Similar to the light sensor, it includes an adjustable potentiometer for sensitivity which we used a lot in trial and error. Again, its input voltage is 3.3 - 5.0 V.

3. Distance (Ultrasonic HC-SR04)
This sensor has a digital output and displays the distance to the nearest object within a 2 - 400 cm range. The accuracy of this measurement is up to 3 mm. On board, there is a transmitter, receiver, and a control circuit and the voltage range is 3.0 - 5.0 V

### Signal Conditioning and Processing
- use of difference of intensity for light
  - Establish an ambient setting for light, test approximately how much intensity reading will change when flashing light is added, use that change as a baseline       for expected difference in light intensity for a flashing light
- use of multiple EV sense conditions
- use of multiple TRUE of EV sensed to decrease the rate of false positives
  - We are only looking for EV that are behind the car, so the distane sensor must detect an approaching or close object in addition to the sensed flashing lights      and high sound 

## Experiments and Results
Did the following trial types:

Statistical Analysis:

## Discussion


