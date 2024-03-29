# Zoom Accessibility enhancements add-on for NVDA

By: Mohamad Suliman and Eilana Benish

This add-on improves the experience of using Zoom for NVDA users by providing keyboard shortcuts to Handle alerts for Different events While In a meeting, provides an alternative way to view the chat history in a meeting to overcome accessibility issues found sometimes in the native chat view of Zoom, and more...

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

## Keyboard shortcut for Opening the add on Dialogue 

NVDA + Z Opens the add-on dialog !

Using this dialog you can :

* See which alerts are announced and which aren't
* Select the types of the alerts you want to be announced
* Choose alerts reporting mode
* Save custom changes 

## Remote control 

It has ben found out that Zoom now has a dedicated keyboard shortcuts to handle the remote control in an accessible manar. Use the following keyboard shortcuts to:

* Alt + Shift + r: to start remote control. Note that you need to have the permision of the remote controlled computer user to be able to proceed
* Alt + Shift + g: to give up remote control or to revoke it

## Chat history dialog

The add-on has a custom dialog where you can see all chat messages sent during the meeting and while the add-on was running.
To open this dialog, use NVDA + Ctrl + h.
The dialog is very simplistic, it has a list of the sent chat messages with their timestamps also.

## An Important note

Currently, the feature of custom alerts mode (where the user can choose which alerts they want to have and which not) works with Zoom only when the user interface language is set to english.