# zoom.py
# A part of zoomEnhancements add-on
# This file is covered by the GNU General Public License
# See the file COPYING for more details

from nvdaBuiltin.appModules.zoom import *
import appModuleHandler
import eventHandler
import tones
from scriptHandler import script
import ui
from logHandler import log
import config
import api
import controlTypes
try:
    from controlTypes import role
except ImportError:
    pass
import mouseHandler
import winUser
import addonHandler
from .dialogs import SettingsPanel, ChatHistoryDialog
from .regexs import *
import datetime
import gui
from gui import NVDASettingsDialog


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
    }
    config.conf.spec["zoomEnhancements"] = confspec


# Execute on init
addonHandler.initTranslation()


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


# Translators: the label of the off state for reporting an alert
offLabel = _("off")


# Translators: the label of on state for reporting an alert
onLable = _("on")


class AppModule(AppModule):

    def __init__(self, processID, appName):
        super(AppModule, self).__init__(processID, appName)
        eventHandler.requestEvents(
            "nameChange", processId=self.processID, windowClassName="zBubbleBaseClass")
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
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(
            SettingsPanel)

    def event_alert(self, obj, nextHandler):
        if publicInMeetingChatReceivedRegEx.fullmatch(obj.name) or privateInMeetingChatReceivedRegEx.fullmatch(obj.name):
            self._handleChatMessage(obj.name)
        if config.conf["zoomEnhancements"]["alertsReportingMode"] == "Report all alerts":
            nextHandler()
            return
        if config.conf["zoomEnhancements"]["alertsReportingMode"] == "Beep for alerts":
            tones.beep(1000, 50)
            return
        if config.conf["zoomEnhancements"]["alertsReportingMode"] == "Silence all alerts":
            return
        alert = obj.name
        if publicInMeetingChatReceivedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"]:
                nextHandler()
            return
        elif privateInMeetingChatReceivedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"]:
                nextHandler()
            return
        elif joinedLeftMeetingRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"]:
                nextHandler()
            return
        elif joinedLeftWaitingRoomRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"]:
                nextHandler()
            return
        elif audioMutedByHostRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["AudioMutedByHost"]:
                nextHandler()
            return
        elif videoStoppedByHostRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["VideoStoppedByHost"]:
                nextHandler()
            return
        elif screenSharingStartedStoppedByParticipantRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"]:
                nextHandler()
            return
        elif recordingPermissionGrantedRevokedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"]:
                nextHandler()
            return
        elif inMeetingFileUploadCompletedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"]:
                nextHandler()
            return
        elif hostPrivilegeGrantedRevokedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"]:
                nextHandler()
            return
        elif raisedLoweredHandRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"]:
                nextHandler()
            return
        elif iMChatReceivedRegEx.fullmatch(alert):
            if config.conf["zoomEnhancements"]["IMChatReceived"]:
                nextHandler()
            return
        else:
            nextHandler()

    def event_nameChange(self, obj, nextHandler):
        nextHandler()
        try:
            ROLE_STATICTEXT = role.Role.STATICTEXT
        except NameError:
            ROLE_STATICTEXT = controlTypes.ROLE_STATICTEXT
        if obj.role == ROLE_STATICTEXT and obj.windowClassName == "zBubbleBaseClass":
            if self.ricievedChatPrefix:
                obj.name = self.chatPrefixText + ": " + obj.name
                self.ricievedChatPrefix = False
                self.chatPrefixText = ""
            elif inMeetingChatReceivedPrefixRegEx.fullmatch(obj.name):
                self.chatPrefixText = obj.name
                self.ricievedChatPrefix = True
                return
            try:
                obj.role = role.Role.ALERT
            except NameError:
                obj.role = controlTypes.ROLE_ALERT
            eventHandler.queueEvent("alert", obj)

    scriptCategory = SCRCAT_ZOOMENHANCEMENTS

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting joined / left meeting alerts on / off"),
        gestures=[
            "kb:NVDA+control+1",
            "kb(desktop):NVDA+control+numpad1"
        ]
    )
    def script_participantJoinedLeftMeeting(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] = not config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"]
        state = onLable if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Participant Has Joined/Left Meeting is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting joined / left Waiting Room alerts on / off"),
        gestures=[
            "kb:NVDA+control+2",
            "kb(desktop):NVDA+control+numpad2"
        ]
    )
    def script_participantJoinedLeftWaitingRoom(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] = not config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"]
        state = onLable if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Participant Has Joined/Left Waiting Room is %s") % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description=_("Toggles reporting audio muted by host alerts on / off"),
        gestures=[
            "kb:NVDA+control+3",
            "kb(desktop):NVDA+control+numpad3"
        ]
    )
    def script_audioMutedByHost(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["AudioMutedByHost"] = not config.conf["zoomEnhancements"]["AudioMutedByHost"]
        state = onLable if config.conf["zoomEnhancements"]["AudioMutedByHost"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting Audio Muted By Host is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting video stopped by host alerts on / off"),
        gestures=[
            "kb:NVDA+control+4",
            "kb(desktop):NVDA+control+numpad4"
        ]
    )
    def script_videoStoppedByHost(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["VideoStoppedByHost"] = not config.conf["zoomEnhancements"]["VideoStoppedByHost"]
        state = onLable if config.conf["zoomEnhancements"]["VideoStoppedByHost"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting Video Stopped By Host is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting screen sharing started / stopped by participant alerts on / off"),
        gestures=[
            "kb:NVDA+control+5",
            "kb(desktop):NVDA+control+numpad5",
        ]
    )
    def script_screenSharingStartedStopped(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] = not config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"]
        state = onLable if config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Screen Sharing Started/Stopped By Participant is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting recording permission granted / revoked alerts on / off"),
        gestures=[
            "kb:NVDA+control+6",
            "kb(desktop):NVDA+control+numpad6"
        ]
    )
    def script_recordingPermissionGrantedRevoked(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] = not config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"]
        state = onLable if config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Recording Permission Granted/Revoked is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting public in-meeting chat received alerts on / off"),
        gestures=[
            "kb:NVDA+control+7",
            "kb(desktop):NVDA+control+numpad7"
        ]
    )
    def script_publicInMeetingChatReceived(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] = not config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"]
        state = onLable if config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting Public In-meeting Chat Received is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting private in-meeting chat received alerts on / off"),
        gestures=[
            "kb:NVDA+control+8",
            "kb(desktop):NVDA+control+numpad8"
        ]
    )
    def script_privateInMeetingChatReceived(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] = not config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"]
        state = onLable if config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting Private In-meeting Chat Received is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting in-meeting file upload completed alerts on / off"),
        gestures=[
            "kb:NVDA+control+9",
            "kb(desktop):NVDA+control+numpad9"
        ]
    )
    def script_inMeetingFileUploadCompleted(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] = not config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"]
        state = onLable if config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting In-meeting File Upload Completed is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting host privilege granted / revoked alerts on / off"),
        gestures=[
            "kb:NVDA+control+0",
            "kb(desktop):NVDA+control+numpad0"
        ]
    )
    def script_hostPrivilegeGrantedRevoked(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] = not config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"]
        state = onLable if config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] else offLabel
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting Host Privilege Granted/Revoked is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting participant raised / lowered hand alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+1",
            "kb(desktop):NVDA+shift+control+numpad1"
        ]
    )
    def script_participantRaisedLoweredHand(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] = not config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"]
        state = onLable if config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Participant Has Raised/Lowered Hand is %s") % state)

    @script(
        description=_(
            # Translators: a description for a command to toggle reporting a spicific alert
            "Toggles reporting remote control permission granted /revoked alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+2",
            "kb(desktop):NVDA+shift+control+numpad2"
        ]
    )
    def script_remoteControlPermissionGrantedRevoked(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] = not config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"]
        state = onLable if config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] else offLabel
        ui.message(
            # Translators: a message reported for the user when toggling reporting a spicific alert
            _("Reporting Remote Control Permission Granted/Revoked is %s") % state)

    @script(
        # Translators: a description for a command to toggle reporting a spicific alert
        description=_("Toggles reporting IM chat received alerts on / off"),
        gestures=[
            "kb:NVDA+shift+control+3",
            "kb(desktop):NVDA+shift+control+numpad3"
        ]
    )
    def script_iMChatReceived(self, gesture):
        if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
            return
        config.conf["zoomEnhancements"]["IMChatReceived"] = not config.conf["zoomEnhancements"]["IMChatReceived"]
        state = onLable if config.conf["zoomEnhancements"]["IMChatReceived"] else offLabel
        ui.message(state)
        # Translators: a message reported for the user when toggling reporting a spicific alert
        ui.message(_("Reporting IM Chat Received is %s") % state)

    @script(
        # Translators: a description for a command to cycle between alerts reporting modes
        description=_("Toggles between reporting alerts as usual, beeping for the alert, silencing alerts completely, or custom mode where the user can choose which alerts are reported and which aren't."),
        gesture="kb:NVDA+Shift+a"
    )
    def script_toggleAlertsMode(self, gesture):
        currentModeLabel = config.conf["zoomEnhancements"]["alertsReportingMode"]
        currentMode = 3
        for item in alertModeToLabel.items():
            if item[1] == currentModeLabel:
                currentMode = item[0]
        currentMode = (currentMode + 1) % 4
        config.conf["zoomEnhancements"]["alertsReportingMode"] = alertModeToLabel[currentMode]
        ui.message(alertModeToLabel[currentMode])

    @script(
        # Translators: a description for a command to move the focus in / out of the remote controlled screen
        description=_("Moves focus in / out of the remote controlled screen"),
        gesture="kb:NVDA+o"
    )
    def script_remoteControl(self, gesture):
        focus = api.getFocusObject()
        try:
            ROLE_UNKNOWN = role.Role.UNKNOWN
        except NameError:
            ROLE_UNKNOWN = controlTypes.ROLE_UNKNOWN
        if focus.windowClassName.startswith("CASView_0x") and focus.role == ROLE_UNKNOWN:
            try:
                newFocus = focus.parent.parent.parent.parent.parent.previous.firstChild.firstChild.firstChild
                self._clickObject(newFocus)
                return
            except:
                return
        shareContentWindow = self._getShareContentWindow()
        if shareContentWindow:
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
            ROLE_WINDOW = role.Role.WINDOW
        except NameError:
            ROLE_WINDOW = controlTypes.ROLE_WINDOW
        try:
            shareContentWindow = focus.parent.parent
            if shareContentWindow.name == "Share Content" and shareContentWindow.role == ROLE_WINDOW:
                return shareContentWindow
        except:
            pass
        try:
            meetingToolsWindow = focus.parent.parent.parent
            if meetingToolsWindow.name != "Meeting Tools":
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
            self.chatHistoryDialog.itemList.InsertItems(
                [alert], self.chatHistoryDialog.itemList.GetCount())

    @script(
        # Translators: a description for a command to show the add-on settings dialog
        description=_("Shows Zoom enhancements settings dialog"),
        gesture="kb:NVDA+z"
    )
    def script_showSettingsDialog(self, gesture):
        gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, SettingsPanel)

    @script(
        # Translators: a description for a command to show chat history dialog
        description=_("Shows chat history dialog"),
        gesture="kb:NVDA+control+h"
    )
    def script_showChatHistoryDialog(self, gesture):
        gui.mainFrame.prePopup()
        self.chatHistoryDialog = ChatHistoryDialog(
            # Translaters: the title of the chat history dialog
            _("Chat history"), self.chatHistoryList)
        self.chatHistoryDialog.Show()
        gui.mainFrame.postPopup()
