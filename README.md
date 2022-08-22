CAP
===

CDI Analysis Platform


# Steps:

Open an empty directory in VS Code

Open a new terminal and clone this repository with the following command:

`git clone https://github.com/NASA-IMPACT/CDI-Dashboard.git .`

Install the requirements with the following command:

`pip install -r requirements/cloud.txt`

In the ".env.txt" file, add environement variables and save as ".env"

If using the NSSTC network, use Pulse VPN to get on the main campus network. (https://chargerware.uah.edu/all-software/pulse-vpn)

## To run CAP (generate new report):

Run cap from the django shell by entering the command

`from dashboard.cap import *`

followed by

`run_cap()`

exit the shell with 

`quit()`

## To view reports in the dashboard:

`python3 manage.py runserver`

## To view database tables in the dashboard:

Create a superuser

`python3 manage.py createsuperuser`

Start the server

`python3 manage.py runserver`

Navigate to the admin console by clickcing on the shield in the upper right-hand corner and login with the superuser role