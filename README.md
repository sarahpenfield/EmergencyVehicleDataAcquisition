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
- created plan/schedule
- acquired additional sensors
- most of the hardware setup
- found code sources for light, distance, and sound sensors
- completed LED tutorial for use as the dashboard

October 3, 2021
- edited code for:
1. sound
2. light
3. distance
4. sound&light
5. distance&light

- hardware assembly of entire setup

### Problems Encountered
October 1, 2021
- forgot to plug in the board
- where should we start

October 3, 2021
- had to rewrite SD card
- we dont' understand bouncetime for the sound sensor / it is not consistent
- decide how big the difference in light intensity should be (will be part of experiments section)
- decide sampling frequency

### Future Plan
October 1, 2021
- edit code for 7 cases
- create personal vehicle scaled model
- assemble remaining hardware

October 3, 2021
- create personal vehicle scaled model
- edit code for 3 cases (completed 4; one in progress, need 2 more)
1. distance&sound
2. distance&light&sound
- include radio reduction print statemnts
- filter out false positives with an overarching if all TRUE code

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


