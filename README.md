# What is CalPal?

CalPal utilizes the GPT-3 OpenAI API to create calendar events out of a schedule.

For instance, consider a schedule like this:

<img width="790" alt="Screenshot 2023-05-15 at 1 54 06 AM" src="https://github.com/harshithadurai/CalPal/assets/76853136/ef6b9a82-f739-466f-9e59-e8c93ea9b8c7">

You can simply copy and paste this onto the CalPal App:

<img width="1437" alt="Screenshot 2023-05-14 at 11 46 18 PM" src="https://github.com/harshithadurai/CalPal/assets/76853136/1c2e349d-5654-4a67-b9a6-3df02265d9ac">

Now you can download the corresponding calendar events!

<img width="1440" alt="Screenshot 2023-05-14 at 11 47 05 PM" src="https://github.com/harshithadurai/CalPal/assets/76853136/7605d6ca-e415-451b-ab4a-e29373138427">

The file is an iCal file with a .ics extension. To add to Google Calendar, this file can be directly 
<a href="https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop">imported</a> or the file can be opened on an Apple device to be directly added to the Apple calendar.

## Setup

Note that in order to run this app, you would need an [API key from OpenAI](https://beta.openai.com/account/api-keys)

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd CalPal
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)
