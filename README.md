## Password Checker and Generator
I vibe coded this simple Python tool that allows users to check if their password has been exposed in data breaches using the **Have I Been Pwned** API. 
If a password is found in breaches, the tool generates a strong, randomly suggested password for the user.

To ensure privacy, the tool uses k-anonymity, meaning only a hashed prefix of the password is sent to the API, keeping the full password secure as it never leaves your computer.

This is a lightweight and effective way to improve password security while maintaining user privacy.

A great use case for this tool is system administrators dealing with the stress of managing password rotations, I had exactly them in mind when creating this tool; as ensuring that employees don’t reuse compromised passwords is a constant challenge, and this tool easily solves that problem.

With this, system admins can streamline password policies, reduce security risks, and improve overall password hygiene- read more on secure deployment to Cloud on my medium article here! 



## Run on your local machine

1. Clone Repo to your Machine
2. Skip **Step 3** if deploying to production, or if you already have **port 5000** open and free on your local machine.
3. Edit **app.py**, navigate to line 83 in app.py;  83. `app.run(host="0.0.0.0", port=5000)` remove **port 5000** and edit to **port 8000**. 
4. Install Python on your local machine if you haven't done so already; to check if Python is available on your machine, run `python --version` or `python3 --version`
5. Open your terminal and navigate to your project directory; `cd password_checker`
6. In the terminal, to run this application on your local machine, you need to **install venv**, run `python3 -m venv venv` this will create a new folder "venv" in your project root directory.
7. Next, run `source venv/bin/activate`, this opens a virtual environment in your terminal for you to safely deploy your code on your machine.
8. Now, to install the project dependencies, run `pip install -r requirements.txt`, this installs all the dependencies found in your **requirements.txt** file.
9. Now that your environment is set, to run your application, run `python app.py`, your application should be live on your localhost port `5000` or `8000`, depending on your **Steps 2&3**.
