# swe-business-management
Business Management Software
  
Team Members:  
Gabriel Walsh  
Javier Velasquez  
Katie Garner  
Matheus Mendes  
Natnael Yonas  

# Deployed Website
No local installation is required to use the deployed version of the application. The project is deployed through Render and can be accessed here:

https://maryland-contracting-company-353p.onrender.com

# Required Software for Local Hosting
To run this project locally, the following software is needed:

- Python 3
- A code editor such as Visual Studio Code
- A web browser

# Required Packages for Local Hosting
These can be installed individually or by running "pip install -r requirements.txt" 
- Flask
- google-genai
- sendgrid

# Environment Variables
The project is fully available through the deployed Render link, which already has the required environment variables configured. For security reasons, the actual API keys and email credentials are not included in the submitted files. Running the project locally requires the user to provide their own environment variable values.
- GEMINI_API_KEY
- SENDGRID_API_KEY
- SENDER_EMAIL
- TEST_EMAIL

# How to Run the Project Locally
1. Download or clone the project files.
2. Open the project folder in Visual Studio Code or other IDE.
3. Install the required packages.
4. Set the required environment variables such that a Gemini and SendGrid API key is provided and a sender/receiver email is set.
5. Run python app.py in the terminal.
6. Open link in browser: http://127.0.0.1:5000.

# Demonstration Login Information
- Employee Login: username: admin password: temp123
- Customer Login: username: cwilson password: temp123
