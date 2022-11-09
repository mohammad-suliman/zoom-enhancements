# regexs.py
# A part of zoomEnhancements add-on
#This file is covered by the GNU General Public License
#See the file COPYING for more details

import re


"""Some regular expressions to determine the type of the alert"""
joinedLeftMeetingRegEx = re.compile("^.+ (has|have) (joined|left) the meeting$")
joinedLeftWaitingRoomRegEx = re.compile(
    "^.+ (has|have) (entered|left) the Waiting Room for this meeting.*$")
audioMutedByHostRegEx = re.compile("The host muted you.")
videoStoppedByHostRegEx = re.compile("Host has stopped your video")
screenSharingStartedStoppedByParticipantRegEx = re.compile(
    "^.+has (started|stopped) screen share")
recordingPermissionGrantedRevokedRegEx = re.compile(
    "Host (dis)?allows you to record this meeting.")
publicInMeetingChatReceivedRegEx = re.compile("^From .* to Everyone: .*$")
privateInMeetingChatReceivedRegEx = re.compile("^From .* to Me: .*$")
inMeetingChatReceivedPrefixRegEx = re.compile("^From .* to (Everyone|Me)$")
inMeetingFileUploadCompletedRegEx = re.compile(
    "File \(.*\) sent successfully.")
hostPrivilegeGrantedRevokedRegEx = re.compile(
    "(^You are the host now$|^.+is the host now$)")
remoteControlPermissionGrantedRevokedRegEx = re.compile(
    "^You can control .+'s screen$")
raisedLoweredHandRegEx = re.compile("^.* (has )?(raised|lowered) hand$")
iMChatReceivedRegEx = re.compile(r"^.+, \d+ unread messages?")
