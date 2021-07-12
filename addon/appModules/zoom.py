# An app module for Zoom
# A part of zoomEnhancements add-on
#This file is covered by the GNU General Public License
#See the file COPYING for more details

from nvdaBuiltin.appModules.zoom import *
import appModuleHandler
import eventHandler
import tones
from scriptHandler import script
import ui
from logHandler import log
import re
import config
import gui
from gui import guiHelper
from gui.settingsDialogs import NVDASettingsDialog
from gui.nvdaControls import DPIScaledDialog
import wx
import api
import controlTypes
import mouseHandler
import winUser
import addonHandler
import datetime

def initConfiguration():
    confspec = {
        "alertsReportingMode": "string(default=Custom)",
        "ParticipantHasJoined/LeftMeeting": "boolean(default=True)",
        "ParticipantHasJoined/LeftWaitingRoom": "boolean(default=True)",
        "AudioMutedByHost": "boolean(default=True)",
        "VideoStoppedByHost": "boolean(default=True)",
        "ScreenSharingStarted/StoppedByParticipant": "boolean(default=True)",
        "RecordingPermissionGranted/Revoked": "boolean(default=True)",
        "PublicIn-meetingChatReceived": "boolean(default=True)",
        "PrivateIn-meetingChatReceived": "boolean(default=True)",
        "In-meetingFileUploadCompleted": "boolean(default=True)",
        "HostPrivilegeGranted/Revoked": "boolean(default=True)",
        "ParticipantHasRaised/LoweredHand": "boolean(default=True)",
        "RemoteControlPermissionGranted/Revoked": "boolean(default=True)",
        "IMChatReceived": "boolean(default=True)",
        # "Co-hostPrivilegeGranted/Revoked": "boolean(default=True)",
        # "LivestreamStarted/Stopped": "boolean(default=True)",
        # "Q&AQuestionReceived": "boolean(default=True)",
        # "Q&AAnswerReceived": "boolean(default=True)",
        # "RoleChangedToPanelist": "boolean(default=True)",
        # "RoleChangedToAttendee": "boolean(default=True)",
    }
    config.conf.spec["zoomEnhancements"] = confspec


# Execute on init
addonHandler.initTranslation()


class SettingsPanel(gui.SettingsPanel):
    # Translators: Title for the settings dialog
    title = _("Zoom Enhancements settings")
    
    def makeSettings(self, settingsSizer):
        settingsSizerHelper = guiHelper.BoxSizerHelper(
            self, sizer=settingsSizer)
        modeChoices = [item[1] for item in alertModeToLabel.items()]
        self.alertsReportingMode = settingsSizerHelper.addLabeledControl(
            # Translators: the lable of the combobox in the settings dialog
            _("Alerts reporting mode"), wx.Choice, choices=modeChoices)
        currentModeLabel = config.conf["zoomEnhancements"]["alertsReportingMode"]
        currentMode = 0
        for item in alertModeToLabel.items():
            if (item[1] == currentModeLabel):
                currentMode = item[0]
        self.alertsReportingMode.SetSelection(currentMode)
        alertsGroupText = _(
        # Translators: the text of the grouping in the settings dialog
            "Choose which alerts should be reported (effective only when custom mode is selected)")
        alertsGroup = guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(
            wx.StaticBox(self, label=alertsGroupText), wx.VERTICAL))
        settingsSizerHelper.addItem(alertsGroup)
        # Translators: a label of a checkbox in the settings dialog
        self.ParticipantHasJoinedLeftMeetingCheckbox = wx.CheckBox(
            self, label=_("Participant Has Joined/Left Meeting"))
        self.ParticipantHasJoinedLeftMeetingCheckbox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"])
        alertsGroup.addItem(
            self.ParticipantHasJoinedLeftMeetingCheckbox)
        # Translators: a label of a checkbox in the settings dialog
        self.ParticipantHasJoinedLeftWaitingRoomCheckBox = wx.CheckBox(
            self, label=_("Participant Has Joined/Left Waiting Room"))
        self.ParticipantHasJoinedLeftWaitingRoomCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"])
        alertsGroup.addItem(
            self.ParticipantHasJoinedLeftWaitingRoomCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.AudioMutedByHostCheckBox = wx.CheckBox(
            self, label=_("Audio Muted by Host"))
        self.AudioMutedByHostCheckBox.SetValue(
            config.conf["zoomEnhancements"]["AudioMutedByHost"])
        alertsGroup.addItem(self.AudioMutedByHostCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.VideoStoppedByHostCheckBox = wx.CheckBox(
            self, label=_("Video Stopped by Host"))
        self.VideoStoppedByHostCheckBox.SetValue(
            config.conf["zoomEnhancements"]["VideoStoppedByHost"])
        alertsGroup.addItem(self.VideoStoppedByHostCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.ScreenSharingStartedStoppedByParticipantCheckBox = wx.CheckBox(
            self, label=_("Screen Sharing Started/Stopped by a Participant"))
        self.ScreenSharingStartedStoppedByParticipantCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"])
        alertsGroup.addItem(
            self.ScreenSharingStartedStoppedByParticipantCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.RecordingPermissionGrantedRevokedCheckBox = wx.CheckBox(
            self, label=_("Recording Permission Granted/Revoked"))
        self.RecordingPermissionGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"])
        alertsGroup.addItem(
            self.RecordingPermissionGrantedRevokedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.PublicInMeetingChatReceivedCheckBox = wx.CheckBox(
            self, label=_("Public In-meeting Chat Received"))
        self.PublicInMeetingChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"])
        alertsGroup.addItem(self.PublicInMeetingChatReceivedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.PrivateInMeetingChatReceivedCheckBox = wx.CheckBox(
            self, label=_("Private In-meeting Chat Received"))
        self.PrivateInMeetingChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"])
        alertsGroup.addItem(self.PrivateInMeetingChatReceivedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.InMeetingFileUploadCompletedCheckBox = wx.CheckBox(
            self, label=_("In-meeting File Upload Completed"))
        self.InMeetingFileUploadCompletedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"])
        alertsGroup.addItem(self.InMeetingFileUploadCompletedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.HostPrivilegeGrantedRevokedCheckBox = wx.CheckBox(
            self, label=_("Host Privilege Granted/Revoked"))
        self.HostPrivilegeGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"])
        alertsGroup.addItem(self.HostPrivilegeGrantedRevokedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.ParticipantHasRaisedLoweredHandCheckBox = wx.CheckBox(
            self, label=_("Participant Has Raised/Lowered Hand (Host Only)"))
        self.ParticipantHasRaisedLoweredHandCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"])
        alertsGroup.addItem(
            self.ParticipantHasRaisedLoweredHandCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.RemoteControlPermissionGrantedRevokedCheckBox = wx.CheckBox(
            self, label=_("Remote Control Permission Granted/Revoked"))
        self.RemoteControlPermissionGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"])
        alertsGroup.addItem(
            self.RemoteControlPermissionGrantedRevokedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.IMChatReceivedCheckBox = wx.CheckBox(
            self, label=_("IM Chat Received"))
        self.IMChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["IMChatReceived"])
        alertsGroup.addItem(self.IMChatReceivedCheckBox)
        """
        # Translators: a label of a checkbox in the settings dialog
        self.CoHostPrivilegeGrantedRevokedCheckBox = wx.CheckBox(
            self, label=_("Co-host Privilege Granted/Revoked"))
        self.CoHostPrivilegeGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["Co-hostPrivilegeGranted/Revoked"])
        alertsGroup.addItem(self.CoHostPrivilegeGrantedRevokedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.LivestreamStartedStoppedCheckBox = wx.CheckBox(
            self, label=_("Livestream Started/Stopped"))
        self.LivestreamStartedStoppedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["LivestreamStarted/Stopped"])
        alertsGroup.addItem(self.LivestreamStartedStoppedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.QAndAQuestionReceivedCheckBox = wx.CheckBox(
            self, label=_("Q And A Question Received"))
        self.QAndAQuestionReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["Q&AQuestionReceived"])
        alertsGroup.addItem(self.QAndAQuestionReceivedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.QAndAAnswerReceivedCheckBox = wx.CheckBox(
            self, label=_("Q And A AnswerReceived"))
        self.QAndAAnswerReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["Q&AAnswerReceived"])
        alertsGroup.addItem(self.QAndAAnswerReceivedCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.RoleChangedToPanelistCheckBox = wx.CheckBox(
            self, label=_("Role Changed to Panelist"))
        self.RoleChangedToPanelistCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RoleChangedToPanelist"])
        alertsGroup.addItem(self.RoleChangedToPanelistCheckBox)
        # Translators: a label of a checkbox in the settings dialog
        self.RoleChangedToAttendeeCheckBox = wx.CheckBox(
            self, label=_("Role Changed to Attendee"))
        self.RoleChangedToAttendeeCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RoleChangedToAttendee"])
        alertsGroup.addItem(self.RoleChangedToAttendeeCheckBox)
        """

    def onSave(self):
        newMode = [x[1] for x in alertModeToLabel.items()][self.alertsReportingMode.GetSelection()]
        config.conf["zoomEnhancements"]["alertsReportingMode"] = newMode
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] = self.ParticipantHasJoinedLeftMeetingCheckbox.IsChecked()
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] = self.ParticipantHasJoinedLeftWaitingRoomCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["AudioMutedByHost"] = self.AudioMutedByHostCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["VideoStoppedByHost"] = self.VideoStoppedByHostCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] = self.ScreenSharingStartedStoppedByParticipantCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] = self.RecordingPermissionGrantedRevokedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] = self.PublicInMeetingChatReceivedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] = self.PrivateInMeetingChatReceivedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] = self.InMeetingFileUploadCompletedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] = self.HostPrivilegeGrantedRevokedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] = self.ParticipantHasRaisedLoweredHandCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] = self.RemoteControlPermissionGrantedRevokedCheckBox.IsChecked()
        config.conf["zoomEnhancements"]["IMChatReceived"] = self.IMChatReceivedCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["Co-hostPrivilegeGranted/Revoked"] = self.CoHostPrivilegeGrantedRevokedCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["LivestreamStarted/Stopped"] = self.LivestreamStartedStoppedCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["Q&AQuestionReceived"] = self.QAndAQuestionReceivedCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["Q&AAnswerReceived"]= self.QAndAAnswerReceivedCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["RoleChangedToPanelist"] = self.RoleChangedToPanelistCheckBox.IsChecked()
        # config.conf["zoomEnhancements"]["RoleChangedToAttendee"] = self.RoleChangedToAttendeeCheckBox.IsChecked()


class DialogWithList(DPIScaledDialog):

    def __init__(self, title, items, appModule):
        windowStyle = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX
        super().__init__(gui.mainFrame, title = title, style = windowStyle)
        mainSizer=wx.BoxSizer(wx.VERTICAL)
        sHelper = guiHelper.BoxSizerHelper(self, wx.VERTICAL)
        self.itemList = wx.ListBox(self)
        if items:
            self.itemList.InsertItems(items, 0)
        sHelper.addItem(self.itemList)
        sHelper.addDialogDismissButtons(wx.CLOSE, True)
        mainSizer.Add(sHelper.sizer, border = guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL | wx.EXPAND, proportion=1)
        mainSizer.Fit(self)
        self.SetSizer(mainSizer)
        self.SetMinSize(self.scaleSize(self.MIN_SIZE))
        self.SetSize(self.scaleSize(self.INITIAL_SIZE))
        self.CentreOnScreen()
        self.appModule = appModule
        self.Bind(wx.EVT_CLOSE, self.onClose)

    INITIAL_SIZE = (800, 480)
    MIN_SIZE = (470, 240)

    def onClose(self, event):
        self.appModule.raisedHandDialog = None
        event.Skip()


# Some regular expressions to determine the type of the alert
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
# coHostPrivilegeGrantedRevoked = re.compile("")
# livestreamStartedStoppedRegEx = re.compile("")
# qAndAQuestionReceivedRegEx = re.compile("")
# qAndAAnswerReceivedRegEx = re.compile("")
# roleChangedToPanelistRegEx = re.compile("")
# roleChangedToAttendeeRegEx = re.compile("")


# A script category for the add -on
# Translators: the name of the add-on category in input gestures
SCRCAT_ZOOMENHANCEMENTS = _("Zoom Enhancements")


# Alert reporting mode to label dict
alertModeToLabel = {
    # Translators: a lable for alerts reporting mode
    0: _("Report all alerts"),
    # Translators: a lable for alerts reporting mode
    1: _("Beep for alerts"),
    # Translators: a lable for alerts reporting mode
    2: _("Silence all alerts"),
    # Translators: a lable for alerts reporting mode
    3: _("Custom")
}


class AppModule(AppModule):

    def __init__(self, processID, appName):
        super(AppModule, self).__init__(processID, appName)
        eventHandler.requestEvents("nameChange",processId=self.processID,windowClassName="zBubbleBaseClass")
        initConfiguration()
        categoryClasses = gui.settingsDialogs.NVDASettingsDialog.categoryClasses
        if not (SettingsPanel in categoryClasses):
            categoryClasses.append(SettingsPanel)
        self.chatHistoryDialog = None
        self.chatHistoryList = []
        self.ricievedChatPrefix = False
        self.chatPrefixText = ""

    def terminate(self):
        super(AppModule, self).terminate()
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsPanel)

    def event_alert(self, obj, nextHandler):
        if publicInMeetingChatReceivedRegEx.fullmatch(obj.name) or privateInMeetingChatReceivedRegEx.fullmatch(obj.name):
            self._handleChatMessage(obj.name)
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] == "Report all alerts"):
            nextHandler()
            return
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] == "Beep for alerts"):
            tones.beep(1000, 50)
            return
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] == "Silence all alerts"):
            return
        alert = obj.name
        if (publicInMeetingChatReceivedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"]):
                nextHandler()
            return
        elif(privateInMeetingChatReceivedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"]):
                nextHandler()
            return
        elif(joinedLeftMeetingRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"]):
                nextHandler()
            return
        elif(joinedLeftWaitingRoomRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"]):
                nextHandler()
            return
        elif(audioMutedByHostRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["AudioMutedByHost"]):
                nextHandler()
            return
        elif(videoStoppedByHostRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["VideoStoppedByHost"]):
                nextHandler()
            return
        elif(screenSharingStartedStoppedByParticipantRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"]):
                nextHandler()
            return
        elif(recordingPermissionGrantedRevokedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"]):
                nextHandler()
            return
        elif(inMeetingFileUploadCompletedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"]):
                nextHandler()
            return
        elif(hostPrivilegeGrantedRevokedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"]):
                nextHandler()
            return
        elif(raisedLoweredHandRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"]):
                nextHandler()
            return
        elif(iMChatReceivedRegEx.fullmatch(alert)):
            if (config.conf["zoomEnhancements"]["IMChatReceived"]):
                nextHandler()
            return
        else:
            nextHandler()

    def event_nameChange(self, obj, nextHandler):
        nextHandler()
        if obj.role == controlTypes.ROLE_STATICTEXT and obj.windowClassName == "zBubbleBaseClass":
            if self.ricievedChatPrefix:
                obj.name = self.chatPrefixText + ": " + obj.name
                self.ricievedChatPrefix = False
                self.chatPrefixText = ""
            elif inMeetingChatReceivedPrefixRegEx.fullmatch(obj.name):
                self.chatPrefixText = obj.name
                self.ricievedChatPrefix = True
                return
            obj.role = controlTypes.ROLE_ALERT
            log.debug(obj.devInfo)
            eventHandler.queueEvent("alert", obj)

    scriptCategory = SCRCAT_ZOOMENHANCEMENTS

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting joined / left meeting alerts on / off"),
        gestures=[
            "kb:NVDA+control+1",
            "kb(desktop):NVDA+control+numpad1"
        ]
    )
    def script_participantJoinedLeftMeeting(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] = not config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Participant Has Joined/Left Meeting is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting joined / left Waiting Room alerts on / off"),
        gestures=[
            "kb:NVDA+control+2",
            "kb(desktop):NVDA+control+numpad2"
        ]
    )
    def script_participantJoinedLeftWaitingRoom(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] = not config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] else _("off")
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            "Reporting Participant Has Joined/Left Waiting Room is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting audio muted by host alerts on / off"),
        gestures=[
            "kb:NVDA+control+3",
            "kb(desktop):NVDA+control+numpad3"
        ]
    )
    def script_audioMutedByHost(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["AudioMutedByHost"] = not config.conf["zoomEnhancements"]["AudioMutedByHost"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["AudioMutedByHost"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Audio Muted By Host is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting video stopped by host alerts on / off"),
        gestures=[
            "kb:NVDA+control+4",
            "kb(desktop):NVDA+control+numpad4"
        ]
    )
    def script_videoStoppedByHost(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["VideoStoppedByHost"] = not config.conf["zoomEnhancements"]["VideoStoppedByHost"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["VideoStoppedByHost"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Video Stopped By Host is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting screen sharing started / stopped by participant alerts on / off"),
        gestures=[
            "kb:NVDA+control+5",
            "kb(desktop):NVDA+control+numpad5",
        ]
    )
    def script_screenSharingStartedStopped(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] = not config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] else _("off")
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            "Reporting Screen Sharing Started/Stopped By Participant is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting recording permission granted / revoked alerts on / off"),
        gestures=[
            "kb:NVDA+control+6",
            "kb(desktop):NVDA+control+numpad6"
        ]
    )
    def script_recordingPermissionGrantedRevoked(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] = not config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Recording Permission Granted/Revoked is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting public in-meeting chat received alerts on / off"),
        gestures=[
            "kb:NVDA+control+7",
            "kb(desktop):NVDA+control+numpad7"
        ]
    )
    def script_publicInMeetingChatReceived(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] = not config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Public In-meeting Chat Received is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting private in-meeting chat received alerts on / off"),
        gestures=[
            "kb:NVDA+control+8",
            "kb(desktop):NVDA+control+numpad8"
        ]
    )
    def script_privateInMeetingChatReceived(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] = not config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Private In-meeting Chat Received is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting in-meeting file upload completed alerts on / off"),
        gestures=[
            "kb:NVDA+control+9",
            "kb(desktop):NVDA+control+numpad9"
        ]
    )
    def script_inMeetingFileUploadCompleted(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] = not config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting In-meeting File Upload Completed is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting host privilege granted / revoked alerts on / off"),
        gestures=[
            "kb:NVDA+control+0",
            "kb(desktop):NVDA+control+numpad0"
        ]
    )
    def script_hostPrivilegeGrantedRevoked(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] = not config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Host Privilege Granted/Revoked is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting participant raised / lowered hand alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+1",
            "kb(desktop):NVDA+shift+control+numpad1"
        ]
    )
    def script_participantRaisedLoweredHand(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] = not config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting Participant Has Raised/Lowered Hand is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting remote control permission granted /revoked alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+2",
            "kb(desktop):NVDA+shift+control+numpad2"
        ]
    )
    def script_remoteControlPermissionGrantedRevoked(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] = not config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] else _("off")
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            "Reporting Remote Control Permission Granted/Revoked is %s" % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description = _("Toggles reporting IM chat received alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+3",
            "kb(desktop):NVDA+shift+control+numpad3"
        ]
    )
    def script_iMChatReceived(self, gesture):
        if (config.conf["zoomEnhancements"]["alertsReportingMode"] != "custom"):
            return
        config.conf["zoomEnhancements"]["IMChatReceived"] = not config.conf["zoomEnhancements"]["IMChatReceived"]
        # Translators: a label for on / off states for reporting a spicific alert
        state = _(
            "on") if config.conf["zoomEnhancements"]["IMChatReceived"] else _("off")
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message("Reporting IM Chat Received is %s" % state)

    @script(
        # Translators: a description for a command to cycle between alerts reporting modes
        description = _("Toggles between reporting alerts as usual, beeping for the alert, silencing alerts completely, or custom mode, where you can choose which alerts are reported and which aren't."),
        gesture="kb:NVDA+Shift+a"
    )
    def script_toggleAlertsMode(self, gesture):
        currentModeLabel = config.conf["zoomEnhancements"]["alertsReportingMode"]
        currentMode = 3
        for item in alertModeToLabel.items():
            if (item[1] == currentModeLabel):
                currentMode = item[0]
        currentMode = (currentMode + 1) % 4
        config.conf["zoomEnhancements"]["alertsReportingMode"] = alertModeToLabel[currentMode]
        ui.message(alertModeToLabel[currentMode])

    @script(
        # Translators: a description for a command to move the focus in / out of the remote controlled screen
        description = _("Moves focus in / out of the remote controlled screen"),
        gesture="kb:NVDA+o"
    )
    def script_remoteControl(self, gesture):
        focus = api.getFocusObject()
        if (focus.windowClassName.startswith("CASView_0x") and focus.role == controlTypes.ROLE_UNKNOWN):
            try:
                newFocus = focus.parent.parent.parent.parent.parent.previous.firstChild.firstChild.firstChild
                self._clickObject(newFocus)
                return
            except:
                return
        shareContentWindow = self._getShareContentWindow()
        if (shareContentWindow):
            self._clickObject(shareContentWindow)
        else:
            log.debugWarning("Couldn't find share content window")

    def _clickObject(self, obj):
        api.moveMouseToNVDAObject(obj)
        mouseHandler.executeMouseEvent(
            winUser.MOUSEEVENTF_LEFTDOWN, 0, 0)
        mouseHandler.executeMouseEvent(
            winUser.MOUSEEVENTF_LEFTUP, 0, 0)

    def _getShareContentWindow(self):
        focus = api.getFocusObject()
        try:
            shareContentWindow = focus.parent.parent
            if (shareContentWindow.name == "Share Content" and shareContentWindow.role == controlTypes.ROLE_WINDOW):
                return shareContentWindow
        except:
            pass
        try:
            meetingToolsWindow = focus.parent.parent.parent
            if (meetingToolsWindow.name != "Meeting Tools"):
                meetingToolsWindow = focus.parent.parent.parent.parent.parent
            return meetingToolsWindow.next.firstChild.firstChild
        except:
            pass

    def _handleChatMessage(self, alert):
        now = datetime.datetime.now()
        now = str(now.hour) + ":" + str(now.minute)
        alert += ", " + now
        self.chatHistoryList.append(alert)
        if self.chatHistoryDialog:
            self.chatHistoryDialog.itemList.InsertItems([alert], self.chatHistoryDialog.itemList.GetCount())

    @script(
        # Translators: a description for a command to show the add-on settings dialog
        description = _("Shows Zoom enhancements settings dialog"),
        gesture="kb:NVDA+z"
    )
    def script_showSettingsDialog(self, gesture):
        gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, SettingsPanel)

    @script(
        # Translators: a description for a command to show chat history dialog
        description = _("Shows chat history dialog"),
        gesture="kb:NVDA+control+h"
    )
    def script_showChatHistoryDialog(self, gesture):
        gui.mainFrame.prePopup()
        # Translaters: the title of the chat history dialog
        self.chatHistoryDialog = DialogWithList(_("Chat history"), self.chatHistoryList, self)
        self.chatHistoryDialog.Show()
        gui.mainFrame.postPopup()
