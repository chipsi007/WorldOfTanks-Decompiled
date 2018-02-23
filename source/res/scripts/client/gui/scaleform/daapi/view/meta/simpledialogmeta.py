# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleDialogMeta.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleDialogMeta(AbstractWindowView):

    def onButtonClick(self, buttonId):
        self._printOverrideError('onButtonClick')

    def as_setTextS(self, text):
        return self.flashObject.as_setText(text) if self._isDAAPIInited() else None

    def as_setTitleS(self, title):
        return self.flashObject.as_setTitle(title) if self._isDAAPIInited() else None

    def as_setButtonsS(self, buttonNames):
        """
        :param buttonNames: Represented by Array (AS)
        """
        return self.flashObject.as_setButtons(buttonNames) if self._isDAAPIInited() else None

    def as_setButtonEnablingS(self, id, isEnabled):
        return self.flashObject.as_setButtonEnabling(id, isEnabled) if self._isDAAPIInited() else None

    def as_setButtonFocusS(self, id):
        return self.flashObject.as_setButtonFocus(id) if self._isDAAPIInited() else None
