# QCF Quantum Computing Web Simulator

## Overview

This project is a web-based Quantum Computing Simulator built using the QCF (Quantum Computing Functions) toolkit for MATLAB/Octave. The application integrates Octave-based quantum algorithms with a Flask web interface, allowing users to execute quantum computing functions directly from a browser.

The project demonstrates the practical implementation of quantum computing concepts through an easy-to-use web interface.

---

## Features

* Web-based interface for running quantum algorithms
* Flask backend integrated with Octave
* Real-time execution of QCF functions
* Interactive output display
* Support for multiple quantum computing functions

---

## Technologies Used

* Python 3
* Flask
* GNU Octave
* HTML5
* CSS3
* JavaScript
* QCF (Quantum Computing Functions)

---

## Supported Quantum Algorithms

### Quantum Algorithms

* Grover's Search Algorithm
* Deutsch Algorithm
* Deutsch-Jozsa Algorithm
* Quantum Fourier Transform (QFT)
* GHZ State Generation

### Quantum Utility Functions

* Hadamard Gate
* Measure
* Identity Matrix
* Renormalise
* Build U
* Dec2Vec
* Bin2Vec
* Struct2Vec
* Vec2Struct
* CF Assert
* CF Rescale
* CF Approx

---

## Project Structure

```text
qcf-master/
│
├── webapp/
│   ├── app.py
│   ├── index.html
│   └── venv/
│
├── grover.m
├── deutsch.m
├── deutsch_jozsa.m
├── qft.m
├── genghz.m
├── hadamard.m
├── measure.m
├── identity.m
└── ...
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/qcf-quantum-simulator.git
cd qcf-quantum-simulator
```

### Install Octave

Ubuntu:

```bash
sudo apt update
sudo apt install octave
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Flask

```bash
pip install flask
```

---

## Running the Application

Navigate to the web application directory:

```bash
cd webapp
```

Start Flask:

```bash
python3 app.py
```

Open the browser:

```text
http://127.0.0.1:5002
```

---

## How It Works

1. User selects a quantum algorithm from the webpage.
2. Flask receives the request.
3. Flask executes the corresponding Octave command.
4. QCF processes the quantum operation.
5. Output is returned to Flask.
6. Results are displayed on the webpage.

---

## Sample Output

```text
Quantum Search Completed
Peak Probability Found
State = 5
```

---

## Applications

* Quantum Computing Education
* Academic Mini Projects
* Research Demonstrations
* Algorithm Visualization
* Learning Quantum Gates and Operations

---

## Future Enhancements

* Quantum Circuit Visualization
* Probability Graphs
* Multi-Qubit Simulation
* User Authentication
* Cloud Deployment
* Advanced Quantum Algorithms

---

## Author

Sarada Maheswari

B.Tech Computer Science and Engineering

Narayana Engineering College, Nellore

---

## License

This project is developed for educational and academic purposes.
