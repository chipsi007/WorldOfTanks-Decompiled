# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/PattonValleyAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class PattonValleyAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value=None):
        super(PattonValleyAchievement, self).__init__('pattonValley', _AB.TOTAL, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'fragsPatton')
