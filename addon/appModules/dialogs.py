# dialogs.py
# A part of zoomEnhancements add-on
# This file is covered by the GNU General Public License
# See the file COPYING for more details

import gui
from gui import guiHelper
from gui.settingsDialogs import NVDASettingsDialog
from gui.nvdaControls import DPIScaledDialog
import wx
import config
import addonHandler


addonHandler.initTranslation()


class SettingsPanel(gui.SettingsPanel):
    # Translators: Title for the settings dialog
    title = _("Zoom Enhancements settings")

    def makeSettings(self, settingsSizer):
        settingsSizerHelper = guiHelper.BoxSizerHelper(
            self, sizer=settingsSizer)
        from .zoom import alertModeToLabel
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
        self.ParticipantHasJoinedLeftMeetingCheckbox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Participant Has Joined/Left Meeting"))
        self.ParticipantHasJoinedLeftMeetingCheckbox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"])
        alertsGroup.addItem(
            self.ParticipantHasJoinedLeftMeetingCheckbox)
        self.ParticipantHasJoinedLeftWaitingRoomCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Participant Has Joined/Left Waiting Room"))
        self.ParticipantHasJoinedLeftWaitingRoomCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"])
        alertsGroup.addItem(
            self.ParticipantHasJoinedLeftWaitingRoomCheckBox)
        self.AudioMutedByHostCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Audio Muted by Host"))
        self.AudioMutedByHostCheckBox.SetValue(
            config.conf["zoomEnhancements"]["AudioMutedByHost"])
        alertsGroup.addItem(self.AudioMutedByHostCheckBox)
        self.VideoStoppedByHostCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Video Stopped by Host"))
        self.VideoStoppedByHostCheckBox.SetValue(
            config.conf["zoomEnhancements"]["VideoStoppedByHost"])
        alertsGroup.addItem(self.VideoStoppedByHostCheckBox)
        self.ScreenSharingStartedStoppedByParticipantCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Screen Sharing Started/Stopped by a Participant"))
        self.ScreenSharingStartedStoppedByParticipantCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"])
        alertsGroup.addItem(
            self.ScreenSharingStartedStoppedByParticipantCheckBox)
        self.RecordingPermissionGrantedRevokedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Recording Permission Granted/Revoked"))
        self.RecordingPermissionGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"])
        alertsGroup.addItem(
            self.RecordingPermissionGrantedRevokedCheckBox)
        self.PublicInMeetingChatReceivedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Public In-meeting Chat Received"))
        self.PublicInMeetingChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"])
        alertsGroup.addItem(self.PublicInMeetingChatReceivedCheckBox)
        self.PrivateInMeetingChatReceivedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Private In-meeting Chat Received"))
        self.PrivateInMeetingChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"])
        alertsGroup.addItem(self.PrivateInMeetingChatReceivedCheckBox)
        self.InMeetingFileUploadCompletedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("In-meeting File Upload Completed"))
        self.InMeetingFileUploadCompletedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"])
        alertsGroup.addItem(self.InMeetingFileUploadCompletedCheckBox)
        self.HostPrivilegeGrantedRevokedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Host Privilege Granted/Revoked"))
        self.HostPrivilegeGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"])
        alertsGroup.addItem(self.HostPrivilegeGrantedRevokedCheckBox)
        self.ParticipantHasRaisedLoweredHandCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Participant Has Raised/Lowered Hand (Host Only)"))
        self.ParticipantHasRaisedLoweredHandCheckBox.SetValue(
            config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"])
        alertsGroup.addItem(
            self.ParticipantHasRaisedLoweredHandCheckBox)
        self.RemoteControlPermissionGrantedRevokedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("Remote Control Permission Granted/Revoked"))
        self.RemoteControlPermissionGrantedRevokedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"])
        alertsGroup.addItem(
            self.RemoteControlPermissionGrantedRevokedCheckBox)
        self.IMChatReceivedCheckBox = wx.CheckBox(
            # Translators: a label of a checkbox in the settings dialog
            self, label=_("IM Chat Received"))
        self.IMChatReceivedCheckBox.SetValue(
            config.conf["zoomEnhancements"]["IMChatReceived"])
        alertsGroup.addItem(self.IMChatReceivedCheckBox)

    def onSave(self):
        from .zoom import alertModeToLabel
        newMode = [x[1] for x in alertModeToLabel.items()][
            self.alertsReportingMode.GetSelection()
        ]
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


class ChatHistoryDialog(DPIScaledDialog):

    def __init__(self, title, items):
        windowStyle = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX
        super().__init__(gui.mainFrame, title=title, style=windowStyle)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        sHelper = guiHelper.BoxSizerHelper(self, wx.VERTICAL)
        self.itemList = wx.ListBox(self)
        if items:
            self.itemList.InsertItems(items, 0)
        sHelper.addItem(self.itemList)
        sHelper.addDialogDismissButtons(wx.CLOSE, True)
        mainSizer.Add(sHelper.sizer, border=guiHelper.BORDER_FOR_DIALOGS,
                      flag=wx.ALL | wx.EXPAND, proportion=1)
        mainSizer.Fit(self)
        self.SetSizer(mainSizer)
        self.SetMinSize(self.scaleSize(self.MIN_SIZE))
        self.SetSize(self.scaleSize(self.INITIAL_SIZE))
        self.CentreOnScreen()

    INITIAL_SIZE = (800, 480)
    MIN_SIZE = (470, 240)
