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

The team completed hardware setup of all of the sensors and the LED light. *insert photo*

Together, we edited code for the following test cases that will be combined to determine if an emergency vehicle is approaching.
1. Sound Detection only
2. Light Detection only
3. Distance Detection only
4. Distance and Light Detection
5. Sound and Light Detection

The first four test cases are fully working, yet the last is still a work in progress.

### Problems Encountered
October 1, 2021

The group had to talk for a bit about where to start with the project as there were a lot of tasks to work through. Also, the group forgot to plug in the Raspberry Pi, which caused some obvious issues when trying to make the LED flash.

October 3, 2021

At the beginning of Sunday's meeting, the group had to rewrite SD card. The monitors were displaying the message that no HDMI input was detected, but once it was rewritten there were no additional problems.
When editing all of the source code, we had to determine what sampling frequency we should be using. This was estimated based on the source code, but will be played with during the experimental phase of the project. Similarly, when writing the light intensity codes, we had to determine what difference in light intensity would be considered flashing. Using the source code, we ran a short experiment using the flashing light on an Apple Watch and went with 15% difference. However, this will continue to be edited during the full experiment phase. 
Finally, the code for the sound and light detection is still a work in progress because our group is trying to understand how the sound sensor works with 'bouncetime' as found in the source code and whether a return of True/1 or False/0 means sound was detected. 

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

## Methodology

### Phenomena of Interest
- light intensity
- sound intensity 
- distance to nearest object behind

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


