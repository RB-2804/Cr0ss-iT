# Cr0ss_iT

Lisez ce document en [français](README.md)

**An application to simplify the organization of school sports events made with pygame!**

## Description

Cr0ss_iT is an application developed with Pygame, designed to simplify the organization of school sports events. It offers a range of features aimed at facilitating the management of sports events, including student registration via a form or CSV data import, creation and tracking of various races, and a departure system integrating QR Code for precise timing. This application represents a comprehensive and user-friendly solution for schools looking to optimize the management of their sports events.

![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/c8376baf-5168-407c-b3a1-b00164f57ca7)

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Demo 

https://github.com/RB-2804/Cr0ss-iT/assets/130835974/b6c15007-ce9d-48fe-8e3f-544e5c0826fa

### Example of our Database 

![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/5d2b2a8c-09b9-4b8f-bc8c-609b529b6ee4)

## Features

### Sports Events Management

  - Student registration for various events
    
  - Data import via CSV file for more efficient management
    
  - Creation and tracking of various races
    
  - Departure system with QR Code for precise timing and effective finish line ranking

## Installation

### Windows 

After installing Python3 (version 3.7 or higher), run the following command:

![image](https://github.com/RB-2804/Cross-iT/assets/130835974/6962260a-cf2f-48dc-9272-37c0a6294404)

Also, install the qrocde and cv2 modules for proper functionality:

- pip install opencv-python-headless qrcode

### Ubuntu

After installing the SOL2 package ( IIbsd12-dev for Ubuntu), Python3 (version 3.7 or higher), run the following command:

- sudo pip3 install pygame opencv-python-headless qrcode

## Usage

When you launch the application, a window will open with multiple tabs:

### Tabs
- Home

  - This first tab is a home screen with the only button "Quit" to close the application.
  
- Registration

  ![image_2024-03-24_224447974](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/c9b555a8-0299-4b48-b28f-043a293d23a6)

  - This tab allows manual registration of a student using a form.
  - It also offers a "Create QR Code" button to generate unique QR codes associated with each student.
  - The "Import a file" button allows you to import a CSV file to automatically register students in the database.

  ⚠️The cursor must be on the text box otherwise there will be no input

- Departure

  ![image_2024-03-24_235831441](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/f2230dcf-7290-4396-9f04-02ec9855e549)

    - In this tab, you can select a race from those available.
    - It displays the list of students participating in the selected race.
    - You can also enter the camera number to use in a text box.
    - The "Start" button will start the camera and start an internal timer in the code.

  ⚠️You must enter the number of the camera you want to use

- Race

  ![image_2024-03-28_205247761](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/4f0ad291-29cf-48a1-91b9-a31ae9a8c2ed)
  
    - This tab provides a form to create a new race.
    - You can select the class, gender, and distance of the race, which will be saved in the database.
    - The "Reset ALL" button allows resetting all tables in the database.
    - The "Reset course" button allows resetting the course table.
    - The "Reset participate" button allows resetting the participate table.
    - The "Reset students" button allows resetting the students' table.
 
  ℹ️Hover over to find out the correct format to enter!
    
- Ranking

  - Once the race is finished, this tab allows you to select the ranking of the race and display the times of the top 3.
 
  ![Screenshot 2024-03-28 204253 (1)](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/92aea944-4513-4083-a33e-5a0ecc601ce1)
  

## Photo License 

© 2024 Lycée La Bourdonnais. All rights reserved.
