# Hospital AI Chatbot using Python and NLTK

## Project Description

The **Hospital AI Chatbot** is a Python-based chatbot developed to provide basic hospital-related information to users through natural language conversations. The chatbot can answer common questions about doctors, departments, appointments, emergency services, laboratory, pharmacy, visiting hours, ambulance services, and other hospital facilities.

The project uses **Natural Language Processing (NLP)** techniques with the **NLTK** library and a custom **intents.json** dataset to understand user queries and provide predefined responses.

---

# Objective

The main objective of this project is to develop an intelligent hospital assistant that can:

* Answer frequently asked hospital-related questions.
* Help patients find the appropriate doctor.
* Provide doctor schedules and consultation fees.
* Provide emergency and ambulance information.
* Reduce the workload of hospital reception staff.
* Demonstrate the use of Natural Language Processing in healthcare applications.

---

# Features

* Interactive command-line chatbot
* Natural Language Processing using NLTK
* Custom hospital dataset
* Doctor information
* Department information
* Appointment guidance
* Emergency services
* Pharmacy information
* Laboratory information
* ICU information
* Blood Bank information
* Hospital visiting hours
* Parking information
* Cafeteria information
* Health tips
* First aid guidance
* Symptom-based responses
* Easy to customize

---

# Technologies Used

* Python 3.11
* NLTK
* NumPy
* JSON
* Pickle
* Visual Studio Code

---

# Project Structure

```
Hospital-AI-Chatbot
│
├── data
│   └── intents.json
│
├── model
│   ├── words.pkl
│   └── classes.pkl
│
├── src
│   ├── chatbot.py
│   ├── inf.py
│   └── train.py
│
├── requirements.txt
└── README.md
```

---

# Installation Steps

## Step 1

Install Python 3.11.

---

## Step 2

Clone or download the project.

---

## Step 3

Install the required libraries.

```bash
pip install -r requirements.txt
```

---

## Step 4

Generate the vocabulary.

```bash
python inf.py
```

---

## Step 5

Train the chatbot.

```bash
python train.py
```

---

## Step 6

Run the chatbot.

```bash
python chatbot.py
```

---

# Required Libraries

* nltk
* numpy

---

# Dataset

The chatbot uses a custom **intents.json** file containing hospital-related intents and training sentences.

The dataset includes:

* Greetings
* Doctor Information
* Departments
* Emergency
* Ambulance
* Laboratory
* Pharmacy
* ICU
* Blood Bank
* Appointment
* Fees
* Visiting Hours
* Health Tips
* First Aid
* Diseases
* Symptoms
* General Hospital Information

---

# Model

The chatbot creates the following trained files:

* words.pkl
* classes.pkl

These files store the generated vocabulary and intent classes used during chatbot execution.

---

# How the Chatbot Works

1. User enters a message.
2. The message is tokenized using NLTK.
3. Words are converted into a Bag-of-Words representation.
4. The chatbot compares the input with the trained vocabulary.
5. The matching intent is identified.
6. A suitable response is selected from the dataset.
7. The chatbot displays the response.

---

# Expected Output

Example:

```
====================================
 CITY CARE HOSPITAL AI CHATBOT
====================================

You : Hello

Bot : Welcome to CityCare Hospital.
How may I help you today?

----------------------------------

You : I have fever

Bot :
Please consult Dr. Ahmed Raza.
Timing:
9:00 AM - 2:00 PM

Consultation Fee:
PKR 2,000
```

---

# Advantages

* Easy to use
* Fast response
* User-friendly
* Reduces receptionist workload
* Can be customized
* Low resource requirements
* Offline execution

---

# Limitations

* Rule-based responses
* Cannot answer questions outside the dataset
* No database connectivity
* No voice support

---

# Future Improvements

Future versions of this project may include:

* Web Interface
* Mobile Application
* Voice Assistant
* Database Integration
* Appointment Booking
* User Authentication
* AI-based Response Generation
* Integration with Hospital Management Systems

---

# Conclusion

The Hospital AI Chatbot successfully demonstrates the application of Natural Language Processing for answering common hospital-related queries. The chatbot provides quick responses using a custom intent-based dataset and can be extended with additional AI techniques in future versions.

---

# Developed By

**Muhammad Ibrahim**

Seat No: **B23110006103**

Department of Computer Science (UBIT)

University of Karachi

Course: Artificial Intelligence

Semester: 5th

Instructor: **Zaeem Tariq**
