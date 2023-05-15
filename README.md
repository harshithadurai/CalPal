# What is CalPal?

CalPal utilizes the GPT-3 OpenAI API to create calendar events out of a schedule.

For instance, consider a schedule like this:

<img width="909" alt="Screenshot 2023-05-15 at 1 31 10 AM" src="https://github.com/harshithadurai/CalPal/assets/76853136/77afb448-f7ae-4b8b-bb7f-8fcc9dda2103">

You can simply copy and paste this onto the CalPal App:

<img width="1437" alt="Screenshot 2023-05-14 at 11 46 18 PM" src="https://github.com/harshithadurai/CalPal/assets/76853136/321f785e-b3a1-4408-9a92-e587b7450007">

Now you can download the corresponding calendar events!

<img width="1440" alt="Screenshot 2023-05-14 at 11 47 05 PM" src="https://github.com/harshithadurai/CalPal/assets/76853136/6fbaf8a9-ae9f-4487-96b2-81b73aa802a0">

The file is an iCal file with a .ics extension. To add to Google Calendar, this file can be directly 
<a href="https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop">imported</a> or the file can be opened on an Apple device to be directly added to the Apple calendar.

## Setup

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
