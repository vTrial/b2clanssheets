How to operate b2 clans sheets

### Step 1: Download Packages

Copy and paste the following command into your terminal to download and install the required packages mentioned in the `requirements.txt` file. This will also ensure that the packages are updated to their latest versions.

```bash
pip install -r requirements.txt --upgrade
```

Certainly! Before creating the `credentials.json` file, you need to set up a Google Sheets API account and generate the necessary credentials. Here are the steps to do that:

### Step 2: Set Up a Google Sheets API Account

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. If you don't have a project, create one by clicking on the project drop-down menu at the top of the page and selecting "New Project." Follow the prompts to create a new project.
3. Once your project is created, ensure it is selected from the project drop-down menu.
4. In the left sidebar, click on "APIs & Services" > "Dashboard."
5. Click on the "+ ENABLE APIS AND SERVICES" button at the top of the page.
6. Search for "Google Sheets API" and click on it in the results.
7. Click the "Enable" button to enable the Google Sheets API for your project.

### Step 3: Create Credentials

1. In the left sidebar, click on "APIs & Services" > "Credentials."
2. Click on the "Create Credentials" button and select "Service Account."
3. Fill in the necessary details for the service account, such as name and role. You can choose "Editor" as the role if you want full access to Google Sheets. You can also create a new key pair by selecting "Create new key" and choosing the key type (JSON is recommended).
4. Click the "Continue" button, and a JSON file containing your credentials will be downloaded to your computer.

### Step 4: Rename and Move the Credentials

1. Rename the downloaded JSON file to `credentials.json`.
2. Move the `credentials.json` file to the same directory as your Python script.
