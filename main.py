import smtplib
password="abc1234"
my_email="mvuyandre@gmail.com"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # transport layer security
connection.login(user=my_email,password=password)






#  The lecture focuses on sending emails using Python's SMTP protocol. Here are the main points:

# Email Transmission Basics: It compares mail servers to post offices and SMTP to a postman, explaining how emails are routed from sender to recipient.
#
# Setting Up Email Accounts: Viewers are encouraged to create test accounts with Gmail and Yahoo to practice safely.
#
# Using smtplib Module: This module is essential for Python to communicate with email servers.
#
# Creating an SMTP Connection: Demonstrates creating an SMTP object using the provider's server address.
#
# Securing the Connection: Explains using starttls() for encrypting email content.
#
# Logging In: Shows how to log in using connection.login(), requiring an email and app password for security.
#
# Sending Emails: Covers composing and sending the email with sender, recipient, and message specified.
#
# Error Handling: Discusses common errors with security settings in Gmail and Yahoo, advising on enabling two-step verification and app passwords.
#
# Improving Delivery: Tips on avoiding spam filters by including a subject line and proper formatting.
#
# Using Context Managers: Recommends the "with" statement for managing SMTP connections effectively.
#
# Overall, it provides a comprehensive guide on sending emails in Python with practical tips and troubleshooting techniques. If you have any specific questions or need further clarification on any point, feel free to ask!