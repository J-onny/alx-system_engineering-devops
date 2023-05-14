Issue Summary:
Duration: The outage occurred on May 12, 2023, from 3:00 PM to 8:00 PM
Impact: The outage mostly affected our online booking platform which was generally completely unavailable to our users, resulting in a 100% downtime for the duration of the outage and as a result, close to 8000 customers were affected.
The root cause of the outage was a hardware failure in the primary database server.
Timeline: The Issue was detected on May 12, 2023, 3:00 PM and it lasted for 5 Hours
Issue Detection: A sudden drop in database connectivity triggered a monitoring alert 
Action Taken: The team responsible immediately started investigating the issue by examining server logs and network connectivity.
The team initially suspected a network issue and spent time troubleshooting routers and switches, leading to a delay in identifying the root cause.
When the incident persisted, the incident was escalated to the database engineering team for further investigation and resolution.
Resolution: After identifying the hardware failure in the primary database server, the team performed an emergency failover to the secondary database server, restoring service availability by 8:00 PM.
Root Cause: The root cause of the outage was a critical hardware failure in the primary database server which was caused by a faulty power supply unit that led to an unexpected shutdown of the server.
Resolution: The team initiated an emergency failover to the secondary database server. They redirected all traffic to the secondary server after ensuring its synchronization with the primary server. The faulty power supply unit was replaced, and the primary server was brought back online once stability was confirmed. Additionally, the team implemented proactive monitoring to detect similar hardware failures in the future.
Corrective and Preventative Measures:
Improvements/Fixes:
Improve incident response procedures to streamline the identification and resolution process.
Enhance monitoring capabilities to quickly detect hardware failures and power supply issues.
Implement redundant power supply units to minimize the risk of downtime caused by a single point of failure.
Replace power supply units in all database servers with more reliable models.
Review and update failover procedures to ensure seamless transitions during critical incidents.
Enhance monitoring system to actively monitor power supply health and alert the operations team in case of abnormalities.
In implementing these measures, we seek to improve system reliability, reduce the impact of potential failures, and minimize downtime in the future.
We sincerely apologize for the inconvenience caused by this outage. Our online booking platform is very crucial to our customers and we are committed to preventing reoccurrence similar incidents in the future. Thank you for your patience and understanding. In case you have further concerns, please don't hesitate to reach out to our support team.


The unexpected Server outage that led to astronomical

Issue Summary:

Duration: From the disgraceful hours of May 12, 2023, at 3:00 PM to the sweet release of recovery at 8:00 PM.

Impact: Hold on tight, folks! Our online booking platform went on an unplanned vacation, leaving our dear users stranded in a sea of error messages. The entire service was down, resulting in a 100% downtime. Talk about a grand adventure! Approximately 8000 customers were affected, and we apologize for the unexpected rise in blood pressure it involuntary adrenaline rush caused.

Root Cause: Oops! The root cause of this wild escapade was a misbehaving pirate—no, wait, a hardware failure in the primary database server. Oh God!!!

Timeline:

X marks the spot! May 12, 2023, at 3:00 PM (the fateful hour!)

S.O.S signal! A monitoring alert frantically waved its digital arms, signaling the sudden drop in database connectivity.

Oops, me hearties! The crew sprang into action, scouring server logs and examining network connectivity, trying to unravel the mystery.

A wild goose chase! We chased shadows, suspecting a network issue, and wasted precious time unraveling the tangled webs of routers and switches. Avast! The culprit eluded us!

Calling for reinforcements! We finally raised the black flag and escalated the incident to the mighty database engineering team. Alas, we needed their expertise to navigate these treacherous waters!

Victory looms! After intense investigation, we discovered the actual culprit—the primary database server's hardware failure. The damn power supply unit had led to sudden shutdown.

Root Cause and Resolution:

Root Cause: A faulty power supply unit caused the hardware failure in the primary database server. It be like walking the plank for our poor server.

Resolution: hooray! We initiated an emergency failover to the secondary database server, guiding our users to safe shores. We replaced the treacherous power supply unit, and the primary server was resurrected once stability was confirmed. Yo ho ho! To avoid future mishaps, we implemented proactive monitoring to detect similar hardware failures before they can make us walk the plank again.

Improvements/Fixes:

We shall improve incident response procedures, making them as swift as a sword's strike, to streamline the identification and resolution process.

Enhancing our monitoring capabilities will help us spot misbehaving hardware and power supply issues quicker than Blackbeard can grow his beard.

We will implement redundant power supply units, making sure a single failure doesn't plunge us into darkness.

Trade your cutlasses! Replacing power supply units in all database servers with more reliable models will ensure smoother sailing.

Sharpen your blades! Reviewing and updating failover procedures will allow us to navigate stormy waters with finesse, ensuring seamless transitions during critical incidents.

Enhancing our monitoring system to actively monitor power supply health and raise the alarm if any abnormalities are spotted.

With these measures in place, we aim to conquer the seven seas of system reliability, steering clear of future outages and keeping our treasure-seeking users happy. 

We offer our sincerest apologies for this unexpected cruise. We understand the importance of our online booking platform to all the adventurous souls out there. Should ye have any further queries or concerns, don't hesitate to send a message in a bottle to our support team. Serene gales 


