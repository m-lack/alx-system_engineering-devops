#0x19-postmortem task using webstack debugging #1 #By Me

#Issue Summary
Duration of the Outage: The disruption began at 11:45 AM and was restored by 12:45 PM GMT.

#Impact
The website was unresponsive on port 80, preventing all users from accessing the site.

#Root Cause
The Nginx server's site configurations were not properly linked. The sites-available configuration was not connected to sites-enabled, which meant the configuration was correct but inactive, preventing users from accessing the site.

#Timeline
11:45 AM: The issue was identified when ALX (the platform) tried to access the website and found it unresponsive.

11:50 AM: ALX monitoring alerts showed the site was down, and the issue was escalated to me.

11:55 AM: The initial investigation focused on reviewing the Nginx configuration files for errors, but no issues were found in the configuration itself.

12:15 PM: Further investigation involved checking the service listening on port 80. It was discovered that the Nginx configuration in sites-available wasn’t linked to sites-enabled.

12:30 PM: The default configuration was correctly linked in sites-enabled, and Nginx was restarted to apply the changes.

12:45 PM: The issue was resolved, and the site was restored online.

#Root Cause and Resolution
#Root Cause
The root cause was the failure to link the sites-available configuration to sites-enabled, which resulted in the Nginx server configuration being correct but inactive.

#Resolution
The issue was fixed by linking the default configuration from sites-available to sites-enabled and restarting the Nginx service.

#Corrective and Preventative Measures
#Improvements
Implement a script or automated check to verify that necessary configurations are correctly linked and active after any changes. Additionally, enhance the monitoring system to detect such issues earlier and alert the team proactively.

#Task List
Create and execute a script that automatically links the configuration from sites-available to sites-enabled following any configuration changes. Additionally, implement a monitoring system to verify that Nginx is correctly listening on port 80, ensuring early detection of potential issues.

#Example Script
Here is the script i mentioned to ensure the configuration is always active:

[bash] (Copy code) #!/usr/bin/env bash

#Ensure Nginx is properly configured and listening on port 80
cat /etc/nginx/sites-available/default > /etc/nginx/sites-enabled/default sudo service nginx restart
