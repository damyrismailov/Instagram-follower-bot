# Instagram Follower Bot – Selenium Automation

Python Selenium script that logs into Instagram, opens the followers list of a target account, and then automatically follows users you are not already following or haven’t already requested. It skips any rows where the button already says “Following” or “Requested”.

## Main features

- Uses a class-based design `InstagramFollower` with clear methods:
  - `login()` – opens Instagram, fills in email and password, submits the form, and clicks “Not now” on the save-login popup.
  - `find_followers()` – navigates to a chosen account’s followers page (e.g. `https://www.instagram.com/<similar_acc>/`), clicks the “followers” link, and scrolls the modal so more users load.
  - `follow_user()` – iterates through the follower rows, checks each follow button’s text, and:
    - **skips** if the text is `"Following"` or `"Requested"` (already handled)
    - **clicks** only when the text is `"Follow"`, then waits briefly before moving on.
- Uses `ChromeOptions` with `detach=True` so the browser stays open after the script finishes.
- Uses `WebDriverWait` and XPath/CSS selectors to:
  - wait for login inputs and buttons
  - wait for the followers modal and its scrollable area
  - locate each follower row and corresponding follow button.
- Uses `execute_script` to scroll the followers modal a few times so new rows are loaded before iterating.
- Prints simple log lines (e.g. “Following <username> now”, “Already following <username>, skipping this person”) so you can see what the bot is doing in real time.
- Keeps a counter of how many users were actually followed in this run.

## What I learned

- How to structure Selenium automation into a reusable class with clear responsibilities per method.
- How to log into a site with dynamic content (Instagram) using `WebDriverWait` instead of only `sleep()`.
- How to work with scrollable modals (not the full page) by targeting the correct element and using `execute_script` to scroll it.
- How to read button text and make decisions based on its current state (“Follow”, “Following”, “Requested”) instead of blindly clicking everything.
- How to iterate over dynamic lists of elements where rows are loaded as you scroll.
- Why Instagram (and similar sites) change HTML/XPath frequently and how that can break brittle locators.
- The importance of respecting platform rate limits and terms of service when automating any social media interaction.

## How to run

1. Clone the repo:

   git clone https://github.com/<your-username>/instagram-follower-bot.git  
   cd instagram-follower-bot  

2. (Optional) Create and activate a virtual environment:

   python -m venv venv  
   source venv/bin/activate   (Windows: venv\Scripts\activate)  

3. Install dependencies:

   pip install -r requirements.txt  

4. Configure your credentials and target account:

   - In `main.py`, set:
     - `instagram_email` – your Instagram login email/username  
     - `instagram_password` – your Instagram password  
     - `similar_acc` – the account whose followers you want to follow (e.g. `"some_public_account"`)  
   - Alternatively, read these values from environment variables if you’ve set the code up that way.

5. Run the bot:

   python main.py  

   - The script will:
     - open Chrome and Instagram  
     - log in with your credentials  
     - open the followers list for `similar_acc`  
     - scroll the modal to load followers  
     - loop through the follower rows and:
       - click “Follow” only on users you’re not already following / haven’t requested  
       - skip rows where the button text is “Following” or “Requested”.  

6. Important notes:

   - Instagram has rules and rate limits around automation. Use this script for learning purposes and at a sensible speed to avoid having your account restricted.  
   - If Instagram changes its HTML or class names, you may need to update the XPath/CSS selectors in the code.
