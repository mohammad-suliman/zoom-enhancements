# Zoom Accessibility enhancements add-on for NVDA

By: Mohamad Suliman and Eilana Benish

This add-on will improve the experience of using Zoom for NVDA users by providing keyboard shortcuts to Handle alerts for Different events While In a meeting, make the process of remote control much more accessible and smoother, and more...

## keyboard shortcuts for controlling alerts In meetings 

* NVDA + Shift + A: cycles between different modes of reporting alerts. The following modes are available:
    * Report all alerts mode, where all alerts are reported as usual
    * Beep for alerts, where NVDA will play a short beep for every alert displayed in Zoom
    * Silence all alerts, where NVDA will ignore all alerts
    * Custom mode, Where the user can customize which alerts they want to have and which not. This can be done using the settings dialog of the add-on, or by using the dedicated keyboard shortcuts for that

The following shortcuts can be used to toggle on / off the announcements of each type of alert (note that this will be effective when custom mode is selected):

* NVDA + Ctrl + 1: Participant Has Joined/Left Meeting (Host Only)
* NVDA + Ctrl + 2: Participant Has Joined/Left Waiting Room (Host Only)
* NVDA + Ctrl + 3: Audio Muted by Host
* NVDA + Ctrl + 4: Video Stopped by Host
* NVDA + Ctrl + 5: Screen Sharing Started/Stopped by a Participant
* NVDA + Ctrl + 6: Recording Permission Granted/Revoked
* NVDA + Ctrl + 7:  Public In-meeting Chat Received
* NVDA + Ctrl + 8: Private In-meeting Chat Received
* NVDA + Ctrl + 9: In-meeting File Upload Completed
* NVDA + Ctrl + 0: Host Privilege Granted/Revoked
* NVDA + Shift + Ctrl + 1: Participant Has Raised/Lowered Hand (Host Only)
* NVDA + Shift + Ctrl + 2: Remote Control Permission Granted/Revoked
* NVDA + Shift + Ctrl + 3: IM chat message received


Note that you need to leave reporting all alert types selected (in Zoom accessibility settings) to have the add-on function as expected.

## Keyboard shortcut for Opening add on Dialogue 

NVDA + Z Opens the add-on dialog !

Using this dialog you can :

* See which alerts are announced and which aren't
* Select the types of the alerts you want to be announced
* Choose alerts reporting mode
* Save custom changes 

## Remote control 

after a remote control permission is granted,  NVDA + O will move the focus in /Out of  the remote controlled screen

Note that the focus should be on one of the meeting controls to be able to remote control the other screen