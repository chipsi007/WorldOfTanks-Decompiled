# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/items/components/shared_components.py
from collections import namedtuple
from constants import IS_CLIENT, IS_WEB
from items.components import component_constants
from items.components import path_builder
from soft_exception import SoftException
if IS_CLIENT:
    from helpers import i18n
elif IS_WEB:
    from web_stubs import i18n
else:

    class i18n(object):

        @classmethod
        def makeString(cls, key):
            raise SoftException('Unexpected call "i18n.makeString"')


__all__ = ('MaterialInfo', 'DEFAULT_MATERIAL_INFO', 'EmblemSlot', 'LodSettings', 'NodesAndGroups', 'Camouflage', 'DEFAULT_CAMOUFLAGE', 'SwingingSettings', 'I18nComponent', 'DeviceHealth', 'ModelStatesPaths')
MaterialInfo = namedtuple('MaterialInfo', ('kind', 'armor', 'extra', 'vehicleDamageFactor', 'useArmorHomogenization', 'useHitAngle', 'useAntifragmentationLining', 'mayRicochet', 'collideOnceOnly', 'checkCaliberForRichet', 'checkCaliberForHitAngleNorm', 'damageKind', 'chanceToHitByProjectile', 'chanceToHitByExplosion', 'continueTraceIfNoHit'))
DEFAULT_MATERIAL_INFO = MaterialInfo(0, 0, None, 0.0, False, False, False, False, False, False, False, 0, 0.0, 0.0, False)
EmblemSlot = namedtuple('EmblemSlot', ('rayStart', 'rayEnd', 'rayUp', 'size', 'hideIfDamaged', 'type', 'isMirrored', 'isUVProportional', 'emblemId'))
LodSettings = namedtuple('LodSettings', ('maxLodDistance', 'maxPriority'))
NodesAndGroups = namedtuple('NodesAndGroups', ('nodes', 'groups'))
Camouflage = namedtuple('Camouflage', ('tiling', 'exclusionMask'))
DEFAULT_CAMOUFLAGE = Camouflage(None, None)
SwingingSettings = namedtuple('SwingingSettings', ('lodDist', 'sensitivityToImpulse', 'pitchParams', 'rollParams'))

class I18nString(object):
    __slots__ = ('__value',)

    def __init__(self, key):
        super(I18nString, self).__init__()
        self.__value = i18n.makeString(key)

    @property
    def value(self):
        return self.__value


class I18nComponent(object):
    __slots__ = ('__userString', '__shortString', '__description')

    def __init__(self, userStringKey, descriptionKey, shortStringKey=''):
        super(I18nComponent, self).__init__()
        self.__userString = i18n.makeString(userStringKey)
        if shortStringKey:
            self.__shortString = i18n.makeString(shortStringKey)
        else:
            self.__shortString = component_constants.EMPTY_STRING
        self.__description = i18n.makeString(descriptionKey)

    @property
    def userString(self):
        return self.__userString

    @property
    def shortString(self):
        return self.__shortString or self.__userString

    @property
    def description(self):
        return self.__description


class I18nExposedComponent(I18nComponent):
    __slots__ = ('__userKey', '__shortKey', '__descriptionKey')

    def __init__(self, userStringKey, descriptionKey, shortStringKey=''):
        super(I18nExposedComponent, self).__init__(userStringKey, descriptionKey, shortStringKey='')
        self.__userKey = userStringKey
        self.__descriptionKey = descriptionKey
        self.__shortKey = shortStringKey

    @property
    def userKey(self):
        return self.__userKey

    @property
    def descriptionKey(self):
        return self.__descriptionKey

    @property
    def shortKey(self):
        return self.__shortKey


class DeviceHealth(object):
    __slots__ = ('maxHealth', 'repairCost', 'maxRegenHealth', 'healthRegenPerSec', 'healthBurnPerSec', 'chanceToHit', 'hysteresisHealth')

    def __init__(self, maxHealth, repairCost=component_constants.ZERO_FLOAT, maxRegenHealth=component_constants.ZERO_INT):
        super(DeviceHealth, self).__init__()
        self.maxHealth = maxHealth
        self.repairCost = repairCost
        self.maxRegenHealth = maxRegenHealth
        self.healthRegenPerSec = component_constants.ZERO_FLOAT
        self.healthBurnPerSec = component_constants.ZERO_FLOAT
        self.chanceToHit = None
        self.hysteresisHealth = None
        return

    def __repr__(self):
        return 'DeviceHealth(maxHealth={}, repairCost={}, maxRegenHealth={})'.format(self.maxHealth, self.repairCost, self.maxRegenHealth)

    @property
    def maxRepairCost(self):
        return (self.maxHealth - self.maxRegenHealth) * self.repairCost


DEFAULT_DEVICE_HEALTH = DeviceHealth(1)

class ModelStatesPaths(object):
    __slots__ = ('__undamaged', '__destroyed', '__exploded')

    def __init__(self, undamaged, destroyed, exploded):
        super(ModelStatesPaths, self).__init__()
        self.__undamaged = tuple(path_builder.makeIndexes(undamaged))
        self.__destroyed = tuple(path_builder.makeIndexes(destroyed))
        self.__exploded = tuple(path_builder.makeIndexes(exploded))

    def __repr__(self):
        return 'ModelStatesPaths(undamaged={}, destroyed={}, exploded={})'.format(self.undamaged, self.destroyed, self.exploded)

    @property
    def undamaged(self):
        return path_builder.makePath(*self.__undamaged)

    @property
    def destroyed(self):
        return path_builder.makePath(*self.__destroyed)

    @property
    def exploded(self):
        return path_builder.makePath(*self.__exploded)

    def getPathByStateName(self, stateName):
        path = getattr(self, stateName, None)
        if path is None:
            raise SoftException('State {} is not found'.format(stateName))
        return path
