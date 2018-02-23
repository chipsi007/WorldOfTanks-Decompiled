# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/boosters_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import battle_booster
from gui.shared.tooltips import boosters
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders',)

def getTooltipBuilders():
    return (DataBuilder(TOOLTIPS_CONSTANTS.INVENTORY_BATTLE_BOOSTER, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_booster.BattleBoosterBlockTooltipData(contexts.InventoryBattleBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_BOOSTER, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_booster.BattleBoosterBlockTooltipData(contexts.HangarContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SHOP_BATTLE_BOOSTER, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_booster.BattleBoosterBlockTooltipData(contexts.ShopBattleBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_BOOSTER_COMPARE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_booster.BattleBoosterBlockTooltipData(contexts.VehCmpConfigurationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO, TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI, boosters.BoosterTooltipData(contexts.BoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BOOSTERS_SHOP, TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI, boosters.BoosterTooltipData(contexts.ShopBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BOOSTERS_QUESTS, TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI, boosters.BoosterTooltipData(contexts.QuestsBoosterContext())))
