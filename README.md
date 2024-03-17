# Face Recognition Employee Attandance System

### Recognize The faces And Take Automatic Employee Attandance. :

## Installation

### create enviroment (highly suggested)

recommended python version == 3.7

miniconda installation
https://docs.anaconda.com/free/miniconda/index.html

after successful installation create. conda environment
```bash
conda create -n attendance -all -y
```

activate the environment
```bash
conda activate attendance
```


git clone the repo

```bash
git clone https://github.com/srinick007/attendance_system.git
```

change directory to FRAS

```bash
cd FRAS
```

install requirements
```bash
pip install -r requirements.txt
```

create three folders inside FRAS with the following names:

```bash
TrainingImage
ImagesUnknown
Attendance
```


## running

change directory to FRAS
```bash
cd FRAS
```
run main.py

```bash
python main.py
```


1 - check camera is functional

2 - capture training images of person for attendance. enter unique name(without spaces and special characters) and unique id.
    camera open and wait for 20 seconds for each person.for each person 101 images are captured and stores in TrainingImages folder. after capturing open TrainingImages and check no images other then faces are there . if random image is present delete it.

3 - train the model after capturing images of person

4 - run attentance system. the attendace list will be saved in attendance folder. click on camera and press q to stop taking attendance

6 - quit the program

