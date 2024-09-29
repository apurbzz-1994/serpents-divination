# :snake: :magic_wand: Serpent's Divination
Automating documentation and insights procurement for your local Python scripts

![first version screenshot](/git_assets/sgrab_1.png)

# Introduction
Serpent's Divinition (excuse the super dramatic name!) is a nifty tool that can be used to procure documentation and insights for a collection of Python scripts in your local directory. The goal is to use the resultant documentation for knowledge sharing between teams, drafting README.md files, assisting those who are just starting out with Python with running your scripts etc. 

## What does it do (for now)?

Given that you've written a script in the following manner...

![code grab](/git_assets/f1.png)


...the tool will render the following row in the Documentation table:

![rendered html](/git_assets/f2.png)

For more information, click on the "How does it work" button while using the tool.


## How to run
1. Install the latest version of Python from [https://www.python.org/downloads](https://www.python.org/downloads/), ensuring that you've added Python to your `PATH` (more on this here: [https://realpython.com/add-python-to-path](https://realpython.com/add-python-to-path/)). 

2. Clone this repository in your machine or download the project files via `Code > Download ZIP`. It is recommended to use a Python virtual environment (like [venv](https://docs.python.org/3/library/venv.html)) so that all modules and dependencies can be housed neatly in one place.

3. Open your terminal and `cd` to the repository directory and run the following command:

    ```
    pip install -r requirements.txt
    ```

    This will install all necessary modules. 

4. Create a folder called `scripts` and place all your scripts there. 

5. To run the application, open a terminal, `cd` to the correct directory and run the following command:

    ```
    python3 app.py
    ```

    Depending on your system, you may need to use `python` or `python3` in the above command. 

6. The command in step 4 will launch a Flask development server (usally on http://127.0.0.1:5000), but check the command line as it might be running on a different localhost ip address. 


## Upcoming features
- Ability to print documentation table and generate markdown for different platforms
- Automating the generation of instructions on how to run each script and what to look out for to minimise error during script run(e.g a script taking an argument or requires a csv file)
 