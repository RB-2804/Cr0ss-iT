# Technical Description of the Project

Lisez ce document en [français](doc.md)

## Display

The application's display is achieved using Pygame. The Pygame library offers Rect objects for drawing rectangles. By creating functions, we can create rectangles with pre-defined text by calling the function. Moreover, we have the ability to input text into a defined area by a rectangle thanks to the Pygame module.

## Database

In this project, the use of a database is crucial for structuring student data, courses, and participation in courses. It ensures data integrity, facilitates their manipulation, and guarantees the application's sustainability. Through it, operations such as displaying lists of students or calculating rankings are efficient and secure. In summary, our database offers a solid and flexible solution for managing information effectively.

The principle of primary keys and foreign keys is used in our database to ensure proper functioning and uniquely identify each record.

Our database uses primary keys and foreign keys. The identifier of each table is defined as the primary key. In the "participates" table, the "id_course" and "id_student" columns serve as a composite key to ensure the uniqueness of relationships. Furthermore, the foreign key "id_student" of the "participates" table refers to the primary key "id_student" of the "students" table, and the foreign key "id_course" refers to the primary key "id_course" of the "courses" table.

Thanks to the database, we can insert student names but also retrieve them using functions that allow us to execute SQL queries in Python. This is how we can display the list of students participating in a course or the ranking when a course is completed.

- ### Conceptual Schema (unfinished)

  ![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/8b9f2090-18c7-446a-aef5-8e6a9d193e28)

The use of the Tkinter module allows us to select the CSV file of our choice. When importing students into the database, we must also specify UTF-8 encoding to avoid the presence of special characters in names.

- ### CSV File
  ![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/82d55768-fcd8-48af-9c92-39b79900e3cf)

## Camera

The OpenCV-Python module is a widely used open-source library for image processing. It provides functionalities for real-time image manipulation, object detection, motion tracking, facial recognition, camera calibration, and much more.

In our case, we used it to detect students' QR Codes.

You can choose the camera you want to use, and we used the Iriun application, which allows, if the computer running the application and the mobile phone are connected to the same Wi-Fi network, to access the mobile phone's camera to obtain a wireless "webcam" semblance. You can also directly use a webcam connected to the computer.

### Stop camera
![image](https://github.com/RB-2804/Cr0ss-iT/assets/130835974/6d0d92a4-0995-45c4-bfba-738180cd7434)


## App Design

### Tabs

The application is composed of several tabs such as the home tab, start tab, course tab, and ranking tab. To switch tabs, simply click on the tab name.
