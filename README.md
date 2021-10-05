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
Below are the progress reports for each meeting the team had, broken down by date to include the progress of the day, the issues, and the next steps.

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

Our team added the LED and volume reduction to the code. We learned to publish the github rather than just send the edit link. We also created the prototypes out of old tissue boxes for the perosnal vehicle and the emergency vehicle. Finally, we worked more on integrating the sound sensor to our code. We made some progress in understanding what the source code is doing (low output = high sound intensity), but need to continue working. 

### Problems Encountered
October 1, 2021

The group had to talk for a bit about where to start with the project as there were a lot of tasks to work through. Also, the group forgot to plug in the Raspberry Pi, which caused some obvious issues when trying to make the LED flash.

October 3, 2021

At the beginning of Sunday's meeting, the group had to rewrite SD card. The monitors were displaying the message that no HDMI input was detected, but once it was rewritten there were no additional problems.
When editing all of the source code, we had to determine what sampling frequency we should be using. This was estimated based on the source code, but will be played with during the experimental phase of the project. Similarly, when writing the light intensity codes, we had to determine what difference in light intensity would be considered flashing. Using the source code, we ran a short experiment using the flashing light on an Apple Watch and went with 15% difference. However, this will continue to be edited during the full experiment phase. 
Finally, the code for the sound and light detection is still a work in progress because our group is trying to understand how the sound sensor works with 'bouncetime' as found in the source code and whether a return of True/1 or False/0 means sound was detected. 

October 5, 2021

We struggled to determine the sampling frequency we should be using for the sound sensor. By running experiments using a music notes app, we determined that the sensor could only occasionally detect 440 Hz. This means that our sampling rate will need to be at least 880 Hz, or one sample every 0.0011 seconds. 

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

In our next meeting we will finish the sound code, likely with the help of the instructor, and incorporate the light filter on to the sensor. This will allow us to begin running the experiments. 

## Methodology

### Phenomena of Interest
1. Light
We are interested in knowing the intensity of the light in the surrounding environment as there will almost always be ambient light. When intensity is significantly higher than the surrounding light (15% greater) for multiple sensed periods of time, this is an indicator that an emergency vehicle could be approaching.
Similarly, the filter created to only allow red light through indicates that there is both a color red and a high intensity light, sensed multiple times in a row.  

2. Sound  
We are interested in knowing the intensity of the sound in the surrounding envrionment as again there will almost always be background noise around the vehicle. However, our sensor cannot determine the intensity of sound and rather can only sense whether a sound above the threshold is present. We set the sampling frequency to 880 Hz and the threshold to XXX decibels to represent the typical decibel level of an emergency vehicle (in reality this level is 130 decibels). When sound above the threshold is sesnsed multiple times in a row, it indicates that an emergency vehicle could be approaching.

3. Distance
We are interested in knowing the distance to the nearest object behind the personal vehicle. When this distance is less than XXX meters, we know that something is behind the car. This is an indicator than an emergency vehicle could be approaching.

Overall, each of these phenomena individually will pick up on many stimuli that are not actually emergency vehicles. However, combnining all three and using repeated sampling helps to decrease the number of false positives of approaching emergency vehicles. While annoying and incorrect from our project's standpoint, it is important to note that false positives will not be harmful to anyone.

### Sensor(s) Used
- sound
- ultrasonic
- light intensity

### Signal Conditioning and Processing
- use of difference of intensity for light
- use of multiple EV sense conditions
- use of multiple TRUE of EV sensed to decrease the rate of false positives

## Experiments and Results

## Discussion


