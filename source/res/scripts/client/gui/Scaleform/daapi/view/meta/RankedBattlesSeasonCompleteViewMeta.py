# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesSeasonCompleteViewMeta.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""
from gui.Scaleform.daapi.view.meta.RankedCompleteViewMeta import RankedCompleteViewMeta

class RankedBattlesSeasonCompleteViewMeta(RankedCompleteViewMeta):

    def closeView(self):
        self._printOverrideError('closeView')

    def showRating(self):
        self._printOverrideError('showRating')

    def onSoundTrigger(self, trigerName):
        self._printOverrideError('onSoundTrigger')

    def as_setDataS(self, data):
        """
        :param data: Represented by RankedBattlesSeasonCompleteVO (AS)
        """
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None
