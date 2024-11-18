# Secret Santa SMS
Automated SMS app that assigns people to secret santa randomly and send each person an SMS

# Note to user:
This project currently requires you to clone down the repo and modify code and run it. You should have basic knowledge of python to use this project. You will also need to buy credits through Text Belt. (Though you can modify the code to use the SMS service of your choice). At the time of writing text belt is 3 dollars for 50 messages and is overall pretty affordable for small scale. 

Do not use this project for malicious purposes. Please use this project responsibly and ensure all parties consent to receive text messages for your Secret Santa. 

A user friently version of this project will be worked on that will include a UI so you don't have to worry about modifying python files or running scripts. 

# How to set up
## Step 1: Populate the arrays
The following arrays must be populate:
- participants
- hat
- particpantsPhone

The particpants and hat arrays should look the exact same and contain each person that is part of your secret santa.
The particpantsPhone should be each person's phone number. An automated text will best sent to them with the person they are assigned to.

## Step 2: Set up a Text Belt Token 
This project is currently using text belt to send automatted messages. You can pay for message using this link:
- [Text Belt](https://textbelt.com/purchase/?generateKey=1)

## Step 3: Create an env file with your token
Set up a `.env` file in the root directory and add TEXTBELT_AUTH_TOKEN=<Replace with your token from step 2>

## Step 4: Run the script!
To run this script, ensure you have installed and setup python3 and run:
`python3 secret-santa-sms.py`
