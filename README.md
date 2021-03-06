# Automated Response to Emergency Vehicles

<img src="https://user-images.githubusercontent.com/78807472/135682706-1d6bb726-967b-4284-af72-caa876460891.png" height = "300">

[Project Video](https://youtu.be/1EThtkh3gLU)

### Introduction

#### Motivation
Emergency vehicle response times are critical to saving lives of those in need both in arrival to the scene and transportation to the hospital or emergency care after an accident. By reducing emergency vehicle response time by just 1 minute, patient survival rate increases by over 2% (Bürger). Everyday vehicles on the road are often a hindrance to the emergency vehicles reaching their destinations. To make this less of an issue, our team created an autoamted response system when emergency vehicles are detected. 

When the flashing lights and loud siren sounds of an emergency vehicle is sensed approaching the vehicle from behind, the radio volume is automatically reduced and a dashboard message is displayed 'Emergency Vehicle Approaching'. With the reduction in noise and visual cue, drivers will be able to react more quickly to make room on the road for emergency vehicles en route to an active scene or hospital.

#### Goals

Our team aims to simulate this project idea by creating a scaled model of a personal vehicle and an emergency vehicle. We will sense based on three stimuli in the surrounding environment.
1. Light detected
2. Sound detected
3. Distance to nearest object behind.

The stimuli are combined using various conditional statements to determine when the emergency vehicle is approaching versus when there are other stimuli such as headlights, background noise, and perosnal vehicles approaching from behind. 

For the to scale model, print statements will be used to show the volume reduction of the radio and a flashing LED will be used to show the dashboard message that would be displayed.


## Progress Report

### Current Progress
#### October 1, 2021

A plan and schedule was created for the next two weeks until the project is due. The additional sensors were acquired from Amazon and most of the hardware was set up and ready to use. As a team, starter code for the light, sound, and distance sensors was added to the shared Google Drive for use in the next meeting. Finally, the team walked through the LED Tutorial on the course website for use as our dashboard display in the scaled model.

#### October 3, 2021

The team completed hardware setup of all of the sensors and the LED light.

<img src="https://user-images.githubusercontent.com/49326756/135782207-aafcd84f-e19b-41ab-9677-c0523eb0ba7f.JPG" height = "250">

Together, we edited code for the following test cases that will be combined to determine if an emergency vehicle is approaching. We incorporated the ADC into the light sensor to show intensity rather than only light/no light.
1. Sound Detection only (SoundTest.py)
2. Light Detection only (LightandLED.py)
3. Distance Detection only (Distance.py)
4. Distance and Light Detection (LightDistanceTest103.py)
5. Sound and Light Detection (SoundLightTest103.py)

The first four test cases are fully working, yet the last is still a work in progress.

#### October 5, 2021

Our team added the LED and volume reduction to the code. We learned to publish the github rather than just send the edit link. We also created the prototypes out of boxes for the perosnal vehicle. Finally, we worked more on integrating the sound sensor to our code. We made some progress in understanding what the source code is doing (low output = high sound intensity), but need to continue working. We determined the correct sampling frequency to use based on light and sound.

<img src="https://user-images.githubusercontent.com/49326756/137036053-c6ed93a6-5ddb-4330-b168-b440a6c83b83.JPG" height = "350">

#### October 7, 2021

Currently working on obtaining the spec sheets for all of our sensors used. Our team also met with Professor Berges to disccuss our code and found that putting the while loop inside the callback function rather than the other way around solves our problem. Additionally, the professor explained to us how the aliasing is occuring in the light frequency; discussed below.

#### Octboer 8, 2021

We ran all of our experiments and videod some of the trials. In our code (FinalCodeWithPrintOuts.py), we added a write to text file section so that we would be able to do statistical analysis on the outputs to determine the number of false positives and false negatives we encountered in each trial. 

#### October 12, 2021

We finished assigning tasks for the Github report writing and created the voiceovers for our video.


### Problems Encountered
#### October 1, 2021

The group had to talk for a bit about where to start with the project as there were a lot of tasks to work through. Also, the group forgot to plug in the Raspberry Pi, which caused some obvious issues when trying to make the LED flash.

#### October 3, 2021

At the beginning of Sunday's meeting, the group had to rewrite SD card. The monitors were displaying the message that no HDMI input was detected, but once it was rewritten there were no additional problems.
When editing all of the source code, we had to determine what sampling frequency we should be using. This was estimated based on the source code, but will be played with during the experimental phase of the project. Similarly, when writing the light intensity codes, we had to determine what difference in light intensity would be considered flashing. Using the source code, we ran a short experiment using the flashing light on an Apple Watch and went with 15% difference. However, this will continue to be edited during the full experiment phase. 
Finally, the code for the sound and light detection is still a work in progress because our group is trying to understand how the sound sensor works with 'bouncetime' as found in the source code and whether a return of True/1 or False/0 means sound was detected. 

#### October 5, 2021

We struggled to determine the sampling frequency we should be using for the sound sensor. By running experiments using a music notes app, we determined that the sensor could only occasionally detect 440 Hz. This means that our sampling rate will need to be at least 880 Hz, or one sample every 0.0011 seconds.

Below are a list of questions to ask at our meeting with the professor: 
1. How to get sound sensor to work, do we need bouncetime
2. How to use two different sampling frequencies to measure sound and light at same time (orders of magnitude difference between sound and light frequencies
3. How to justify sampling frequency of light (see LightDistanceLED105.py)

#### October 7, 2021
LED light was turning off at the beginning of each sample test
where should we place the initializing in the code with callback and while loop

#### October 8, 2021
During our experiments, we struggled to have the light intensity difference be strong enough while there were other people in the room. We decided to add an umbrella on top of the sensor to increase the difference in intensity before we were able to turn off the lights when other groups left. 

<img src="https://user-images.githubusercontent.com/91758370/136990524-3fe045f4-857f-4764-847d-5ae601a304cd.jpeg" height = "350">

We also ran into a problem of recieving a 'none' value for every time the first sample was run. To fix this, we coded out our first sample as we knew it was always going to be wrong. Finally, it took us a bit to debug our code in writing the text files for the statistical analysis we would create.

#### Octboer 12, 2021

Over the weekend, one of our wires got chewed by a group member's cat. Since we had already filmed our experiments, we didn't have a huge problem but we did replace the wire. 

### Future Plan
#### October 1, 2021

At the next meeting, we would like to edit the source code to make as we need for the 7 cases we will be testing. Additionally, we'd like to finish assembling the hardware and create a scaled personal vehicle model.

#### October 3, 2021

At the next meeting, we will finish creating the  personal vehicle scaled model and continue editing the code. For the code, our specific tasks are to include:
1. Complete Sound and Light detection code
2. Create Distance and Sound detection code
3. Create Distance, Light, and Sound detection code
4. Create a master code that uses the return from 7 cases to determine if an emergency vehicle is actually approaching
5. Include radio reduction print statements

#### October 5, 2021

In our next meeting we will finish the sound code, likely with the help of the instructor, and incorporate it to the light and distance code. This will allow us to begin running the experiments. 

#### October 7, 2021

In our next meeting we plan to run the actual experiments with recording data and video.

#### October 8, 2021

In our next meeting we plan to edit and voiceover the videos from the meeting today and incorporate additional video / instructional and presentation information.

#### October 12, 2021

This was our final meeting and all other small details for the class will be communicated over our Whatsapp group chat!

## Methodology

### Phenomena of Interest
1. Light <br />
We are interested in knowing the intensity of the light in the surrounding environment as there will almost always be ambient light. When intensity is significantly higher than the surrounding light (5% greater) for multiple sensed periods of time, this is an indicator that an emergency vehicle could be approaching.  Because we are only looking for if a light is flashing or not, we only care about the relative intensity of visible light rather than the frequency of the light's wavelength.

2. Sound  <br />
We are interested in knowing the intensity of the sound in the surrounding envrionment as again there will almost always be background noise around the vehicle. However, our sensor cannot determine the intensity of sound and rather can only sense whether a sound above the threshold is present. When sound above the threshold is sesnsed multiple times in a row, it indicates that an emergency vehicle could be approaching.

3. Distance <br />
We are interested in knowing the distance to the nearest object behind the personal vehicle. When this distance is less than a certain number of meters, we know that something is behind the car. This is an indicator than an emergency vehicle could be approaching. Note that on a smaller scale, our distance was only set at 25 cm.

Overall, each of these phenomena individually will pick up on many stimuli that are not actually emergency vehicles. However, combnining all three and using repeated sampling helps to decrease the number of false positives of approaching emergency vehicles. While annoying, it is important to note that false positives will not be harmful to anyone.

### Sensor(s) Used
<img width="565" alt="Screen Shot 2021-10-12 at 11 54 43 AM" src="https://user-images.githubusercontent.com/91758370/136989464-ca08c1a8-442a-4949-be41-8d27258d1b39.png">

#### Light

As shown in the table above, the light sensor has both a digital and an analog output. We used the analog output in conjuction with the ADC described below in our project. This sensor works using the photoresistors onboard and sensing the change in ambient lighting based on the threshold. A series of resistance electrical signals is conveyed once this is detected.  The photoresistors contain semicondutors, which when struck by light, allow electrons in the material to enter the conductance band.  This causes a drop in the resistance, with higher intensities of light meaning a greater drop in resistance.  Low light conditions with mean the sensor will output a high resistance.  This resistance can then be converted into intensity using a known conversion formula. (Keim)  

#### Sound

The sound sensor only has an analog output, showing LOW when the sound detected is above the threshold and HIGH when the sound is below the threshold (or not detected). When the sensitivity of the sensor is increased, it takes less sound to trigger a LOW, or sound detected, output. (Banggod)

#### Distance

The distance sensor only has a digital output, showing the distance to the nearest object in centimeters. To do this, the sensor sends out a high frequency sound pulse and determine the time it takes for the wave to bounce back to the sensor, as shown in the image below (Arduino). Since sound travels at approximately the same speed no matter the surrounding environment on Earth (temperature dependent, but we are not testing extreme conditions), the distance sensor can calculate the space between itself and the nearest object, thus outputting the digital number of the echo time.

![ultrasonic_sensor_radiations](https://user-images.githubusercontent.com/49326756/137359036-b37e4613-237c-45c2-8504-d426d8a1b41e.jpeg)

#### Analog to Digital Converter

As mentioned, the ADC was used in conjuction with the light sensor in our project. It takes the continuous signal of light from the environment and breaks it down into readable digitized signals as intensities. With a 10-bit resoultion and 8 channels, there are 1024 different levels that can be output as voltages. This leaves the light intensity readings relatively specific in terms of the needs of our project. (Sklar)

The sensor and Raspberry Pi configuration can be found below, and the written out pin configuration can be found in PinConfiguration.

<img src = "https://user-images.githubusercontent.com/49326756/136623919-8b73a6c2-4dd8-4ff6-b9f3-76a94cdeb79b.jpg" height = "500">

### Signal Conditioning and Processing
The signal conditioning and processing in our project was mostly based on the light sensor. We had to use the ADC as described above to convert the analog output to the digital intensity needed. Using the difference in these sampled intensities, we were able to determine if a light was actually flashing or if it was just the detection of one longer bright light.

Our project experienced aliasing in the light sensing we completed. Our tests were completed at either (1) a flashing frequency of 150 bpm (2.5 Hz) and a sleep time of 1 second or (2) a flashing frequency of 200 bpm (3.33 Hz) and a sleep time of 0.75 seconds. For this explanation, we will use the second frequency (3.33 Hz) as an example.

The sampling frequency for the flashing of 3.33 Hz is based on the sleep time of 0.75 seconds which equals a sampling frequency of 1.33 Hz. Given the Nyquist theorem, the maximum frequency we should be able to read is 0.67 Hz (f<sub>n</sub>). From here, we know that k = fs / f<sub>n</sub> = 3.33 Hz / 0.67 Hz = 5.0  

Using the folding diagram shown below from Class Reference 15, we know that the aliased k<sub>a</sub> = 1 and the aliased frequency = k<sub>a</sub> * f<sub>n</sub> = 0.67 Hz; which happens to be equal to the Nyquist frequency.

<img width="401" alt="Screen Shot 2021-10-12 at 12 32 48 PM" src="https://user-images.githubusercontent.com/91758370/136995267-a63c93dd-a388-4715-bf0e-7105fa54f34f.png">

#### Code
Our fully commented and working code can be found in the file FinalCodeWithComments.py.  The source code we used is cited in the final section of the report. The most important part of code is within the callback function, which is called when the sound sensor detects a sound intensity that is greater than our set threshold.  We set the sound sensor threshold using a video playing regular traffic sounds (https://www.youtube.com/watch?v=fh3EdeGNKus).  Once the callback function is called, we test to see if the light conditions are a flashing light.  This is done by comparing consecutive light intensity readings.  If the difference in the consecutive readings is high, then the light went from high intensity to low intensity, which could mean a flashing light.  We calculated two differences in consecutive readings to verify that a light is flashing multiple times rather than just once.  The callback function also calls the function distance, which calculates the distance between the car and any object behind it.  If the object behind the car is within a certain distance, we determined that it meant the object was approaching.

```ruby
def callback(channel):
         musicVolume = 10
         i1 = 0
         i2 = 0
         i3 = 0
         del1 = 0
         del2 = 0
         if GPIO.input(channel): 
             init()
             counter = 0
             print 'sound'
             while counter < 5:
                 counter += 1
                 photo_value = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
                 i1 = i2
                 i2 = i3
                 #equation converts output photo_value to intensity, check what the output is
                 i3 = (1024-photo_value)/1024.*100
                 
                 #see the difference between two flashes, depends on the sampling frequency
                 del1 = del2
                 del2 = abs(i3-i2)

                 #get current distance
                 dist = distance()


                 if (dist <= tooClose) and (del1>lightDiffThreshold) and \
                 (del2>lightDiffThreshold):
                     #turn on LED
                     GPIO.output(red_led, GPIO.HIGH)
                     #Turn down music
                     musicVolume = 1
                     print('EV!     Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2))
                     time.sleep(sampleFreq)
                 elif (counter == 1):
                     print('Sound Detected')
                     time.sleep(sampleFreq)
                 elif (counter > 1):
                     print('None,   Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2))
                     #turn off LED
                     GPIO.output(red_led, GPIO.LOW)
                     time.sleep(sampleFreq)
         
                 
GPIO.add_event_detect(channel, GPIO.BOTH)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

while True:
        time.sleep(1)
```

Overall, our code works on a simple hierarchy: first it must detect the siren.  The system then checks for flashing lights and an approaching object.  If all three of these conditions are met, then it outputs that an emergency vehicle is approaching and turns on the LED and reduces the music volume.

## Experiments and Results
To test the effectiveness of our emergency vehicle detection system, we completed the seven test trials.  Each trial represents a potential real life scenario that could either mean an emergency vehicle or trigger a false negative.
- Scenario 1: There is a regular vehicle approaching from behind with normal traffic sounds.  This is expected to trigger the distance sensor.
- Scenario 2:  There is a construction/oversized vehicle approaching with a flashing light, and regular traffic sounds.  This is expected to trigger the distance and light sensors.
- Scenario 3: There is an emergency vehicle in the area that you can hear and see, and there are no cars approaching from behind.  This is expected to trigger the sound and light sensors.
- Scenario 4: There is an emergency vehicle in the area that you can hear but cannot see, and there are cars approaching from behind.  This is expected to trigger the distance and light sensors.
- Scenario 5: There is a source of flashing lights such as a malfunctioning street lamp or storefront, no cars approaching from behind, and regular traffic sounds.  This is expected to trigger the light sensor.
- Scenario 6: There is a siren or loud source of sound in the general vicinity that you cannot see, and there are no cars approaching from behind.  This is expected to trigger the sound sensor.
- Scenario 7: There is an emergency vehicel approaching from behind.  This should trigger all three sensors and turn on the LED and reduce the music volume.

The video linked at the top of this page shows how the system responds appropriately to each scenario, with the detection of an approaching emergency vehicle and the LED turning on only for Scenario 7.

Statistical Analysis:
To determine how accurate our system is at detecting emergency vehicles, we performed a series tests to determine how often there is a false positive or negative.  A false positive is defined as the system outputting an emergency vehicle (LED on and music volume reduced) when there is no emergency vehicle.  A false negative is the system not detecting an emergency vehicle even when there is one.  We tested the system by playing a siren and having a vehicle within the trigger distance, but turning the flashing light on and off.  The experimental results can be found below.  The false negatives are difficult to verify as real false negatives because it could have resulted in a miscommunication between the recorder and the person controlling the flashing lights.

<img width="373" alt="Screen Shot 2021-10-12 at 12 40 12 PM" src="https://user-images.githubusercontent.com/49326756/136996177-b3c4eb48-eb41-4edd-9fcf-af2538e314e9.png">

## Discussion
Future work would include adding the color filter that we were unable to get to due to resources and time constraints.  This would help reduce false positives due to construction/oversized vehicles approaching, which have flashing lights and loud noises.  The flashing lights on these vehicle types are orange, so filtering for only red and blue would reduce false positives.  We would also include sampling for more light flashing frequencies due to emergency vehicles having more than one flashing light at different frequencies and colors.

We also expect there will be difficulties implementing our system into full scales vehicles, but we were able to find that it worked on the model scale.

## Sources

Arduino Forum. (2018). “How to convert sound sensor output reading to decibel value?” Arduino Forum, <https://forum.arduino.cc/t/how-to-convert-sound-sensor-output-reading-to-decibel-value/513239> (Oct. 14, 2021).

Arduino. (2021). "Ultrasonic Sensor" Tutorials Point,  <https://www.tutorialspoint.com/arduino/arduino_ultrasonic_sensor.htm> (Oct 14, 2021).

Banggood.com. (2021). “3Pcs Microphone Sound Sensor Module Voice Sensor High Sensitivity Sound Detection Module.” www.banggood.com, <https://usa.banggood.com/3Pcs-Microphone-Sound-Sensor-Module-Voice-Sensor-High-Sensitivity-Sound-Detection-Module-p-1254928.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=US&utm_content=minha&utm_campaign=minha-usg-pc¤cy=USD&cur_warehouse=CN&createTmp=1&utm_source=googleshopping&utm_medium=cpc_bgcs&utm_content=sandra&utm_campaign=sandra-ssc-usg-all-newcustom-ncv90-0420-19cov&ad_id=432153545270&gclid=CjwKCAjwqeWKBhBFEiwABo_XBqywUlY0gQ2NyC9dYwZM_aSot1bLFAsDhlg-or-2dWL1Ni5KukmZ_BoC1YsQAvD_BwE> (Oct. 14, 2021).

Bürger, A., Wnent, J., Bohn, A., Jantzen, T., Brenner, S., Lefering, R., Seewald, S., Gräsner, J.-T., and Fischer, M. (2018). “The Effect of Ambulance Response Time on Survival Following Out-of-Hospital Cardiac Arrest.” Deutsches Aerzteblatt Online.

‌“Design sound light switch throught raspberry pi and sound light sensor – kookye.com.” (2017). Kookye.com, <https://kookye.com/2017/06/01/design-sound-light-switch-throught-raspberry-pi-and-sound-light-sensor/> (Oct. 14, 2021).

‌Felix. (2015). “Using a Raspberry Pi distance sensor (ultrasonic sensor HC-SR04).” Raspberry Pi Tutorials, Raspberry Pi Tutorials, <https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/> (Oct. 14, 2021).

‌“Home.” (2021). Idahotc.com, <https://idahotc.com/> (Oct. 14, 2021).

Instructables. (2017). “Sound Sensor (Raspberry Pi).” Instructables, Instructables, <https://www.instructables.com/Sound-Sensor-Raspberry-Pi/> (Oct. 14, 2021).

‌Keim, R. (2021). “Photoresistor.” Eepower.com, eepower.com, <https://eepower.com/resistor-guide/resistor-types/photo-resistor/#> (Oct. 14, 2021).

‌Sklar, M. (2012). “Analog Inputs for Raspberry Pi Using the MCP3008.” Adafruit Learning System, <https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/connecting-the-cobbler-to-a-mcp3008> (Oct. 14, 2021).

“Using the Pi to measure Decibels - Raspberry Pi Forums.” (2012). Raspberrypi.com, <https://forums.raspberrypi.com/viewtopic.php?t=18014> (Oct. 14, 2021).
