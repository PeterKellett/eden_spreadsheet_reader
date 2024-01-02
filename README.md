![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Workspace Purpose  
For connection to Edens Schoolwork Google sheets.

## Project Setup  
https://developers.google.com/sheets/api/quickstart/python  
### Google Sheets
- Confirm the Google project folder folder - Eden Schoolwork  
  - Click Enable  
- Configure the OAuth consent screen  
  - User Type - External  
  - Click Create  
- App information  
  - App Name: eden_spreadsheet_reader
  - User support Email: peterwkellett@gmail.com  
  - Developer contact information: peterwkellett@gmail.com  
  - Click Save and Continue  
- Scopes  
  - Skip, click Save and Continue  
- Test users - Required bescause User Type above is set as External  
  - Add Users  
  - peterwkellett@gmail.com  

- Authorize credentials for a desktop application  
  - Create Credentials > OAuth client ID  
  - Application Type: Desktop App  
  - Name: eden_spreadsheet_reader  
  - Click Create  
  - Download the credentials.json file and move to project directory  
- Install the Google client library  
  - pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib  
- Configure the sample  
  - In your working directory, create a file named read.py  
  - Copy code

#### Enable the Google Projects API's  
- On the Google project dashboard, click Explore and Enable API's  
  - Select Google Sheets API  
  - Click Enable  
- Add a Service Account  
  - Click Manage Service Accounts and Create Service Account  
  - Name: eden schoolwork reader  
  - Copy the email address address created for the Service Account and share the Google sheets folder with that email  
- Add a key for this Service Account  
  - Open the Service Account and go  to Keys  
  - Click Add Key  
  - Create a credentials.json file  
  - Move this file to GitPod project root directory and rename it keys.json  
#### Preparing to make a delegated API call  
- Docs: https://developers.google.com/identity/protocols/oauth2/service-account#python  
- Copy python code and paste to read.py file  
- Change the SERVICE_ACCOUNT_FILE path to keys.json  
- Remove the copied SCOPES list and use the readonly SCOPES list already in the code and remove the .readonly text in the string  
- Remove SAMPLE_DATA_RANGE from code  
- Get SAMPLE_SPREADSHEET_ID string from the Google Sheets project
  - Go to Google Sheets and copy url
  - Paste url string for SAMPLE_SPREADSHEET_ID, remove https://docs.google.com/spreadsheets/d/ and /edit#gid=1737658404 from the url string  
- See video from 13mins for code changes to read.py  








https://www.youtube.com/watch?v=4ssigWmExak&t=2s

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Heroku
To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.




## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
