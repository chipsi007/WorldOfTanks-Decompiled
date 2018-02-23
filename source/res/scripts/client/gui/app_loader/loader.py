# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/app_loader/loader.py
import BigWorld
import Event
from constants import ARENA_GUI_TYPE
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG
from debug_utils import LOG_DEBUG
from gui.app_loader.interfaces import IAppFactory
from gui.shared import g_eventBus, events
from gui.app_loader.settings import GUI_GLOBAL_SPACE_ID as _SPACE_ID
from gui.app_loader.settings import APP_STATE_ID as _STATE_ID
from gui.app_loader.settings import DISCONNECT_REASON as _DSN_REASON
from gui.app_loader.states import StartState
from gui.shared.utils.decorators import ReprInjector
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager

@ReprInjector.simple('guiSpaceID', 'appsStates', 'dsnReason', 'dsnDesc')
class _GlobalCtx(object):
    __slots__ = ('guiSpaceID', 'arenaGuiType', 'appsStates', 'dsnReason', 'dsnDesc')
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        super(_GlobalCtx, self).__init__()
        self.guiSpaceID = _SPACE_ID.UNDEFINED
        self.arenaGuiType = ARENA_GUI_TYPE.UNKNOWN
        self.appsStates = {}
        self.dsnReason = _DSN_REASON.UNDEFINED
        self.dsnDesc = ()

    @classmethod
    def isConnected(cls):
        return cls.connectionMgr.isConnected()

    def resetDsn(self):
        self.dsnReason = _DSN_REASON.UNDEFINED
        self.dsnDesc = ()


class _EmptyFactory(IAppFactory):
    pass


class _AppLoader(object):
    __slots__ = ('__state', '__ctx', '__appFactory', 'onGUISpaceLeft', 'onGUISpaceEntered')
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self):
        super(_AppLoader, self).__init__()
        self.__state = StartState()
        self.__ctx = _GlobalCtx()
        self.__appFactory = _EmptyFactory()
        self.onGUISpaceLeft = Event.Event()
        self.onGUISpaceEntered = Event.Event()

    def init(self, appFactory):
        self.__appFactory = appFactory
        add = g_eventBus.addListener
        appEvent = events.AppLifeCycleEvent
        spaceEvent = events.GlobalSpaceEvent
        add(appEvent.INITIALIZING, self.__onAppInitializing)
        add(appEvent.INITIALIZED, self.__onAppInitialized)
        add(appEvent.DESTROYED, self.__onAppDestroyed)
        add(spaceEvent.GO_NEXT, self.__onGoNextSpace)

    def fini(self):
        if self.__appFactory:
            self.__appFactory.destroy()
            self.__appFactory = None
        remove = g_eventBus.removeListener
        appEvent = events.AppLifeCycleEvent
        spaceEvent = events.GlobalSpaceEvent
        remove(appEvent.INITIALIZING, self.__onAppInitializing)
        remove(appEvent.INITIALIZED, self.__onAppInitialized)
        remove(appEvent.DESTROYED, self.__onAppDestroyed)
        remove(spaceEvent.GO_NEXT, self.__onGoNextSpace)
        return

    def getSpaceID(self):
        return self.__ctx.guiSpaceID

    def getPackageImporter(self):
        importer = None
        if self.__appFactory:
            importer = self.__appFactory.getPackageImporter()
        return importer

    def getAppStateID(self, appNS):
        return self.__ctx.appsStates.get(appNS, _STATE_ID.NOT_CREATED)

    def getApp(self, appNS=None):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getApp(appNS=appNS)
        return app

    def getDefLobbyApp(self):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getDefLobbyApp()
        return app

    def getDefBattleApp(self):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getDefBattleApp()
        return app

    def startLobby(self):
        self.__appFactory.createLobby()
        self.__updateState()

    def changeSpace(self, spaceID):
        self.__ctx.guiSpaceID = spaceID
        return self.__updateState()

    def showLogin(self):
        return self.changeSpace(_SPACE_ID.LOGIN)

    def showLobby(self):
        return self.changeSpace(_SPACE_ID.LOBBY)

    def switchAccountEntity(self):
        self.changeSpace(_SPACE_ID.WAITING)
        self.__appFactory.destroyLobby()
        self.__appFactory.createLobby()

    def createBattle(self, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        self.__ctx.arenaGuiType = arenaGuiType
        self.__appFactory.createBattle(arenaGuiType)

    def showBattleLoading(self):
        return self.changeSpace(_SPACE_ID.BATTLE_LOADING)

    def showBattlePage(self):
        return self.changeSpace(_SPACE_ID.BATTLE)

    def destroyBattle(self):
        self.__ctx.arenaGuiType = ARENA_GUI_TYPE.UNKNOWN
        return False if self.__ctx.dsnReason != _DSN_REASON.UNDEFINED else self.changeSpace(_SPACE_ID.WAITING)

    def goToLoginByRQ(self, forced=False):
        if self.__ctx.dsnReason != _DSN_REASON.REQUEST or forced:
            LOG_DEBUG('Disconnects from server by request')
            self.__ctx.dsnReason = _DSN_REASON.REQUEST
            self.connectionMgr.disconnect()
        return self.showLogin()

    def goToLoginByEvent(self):
        if self.__ctx.dsnReason not in (_DSN_REASON.REQUEST, _DSN_REASON.KICK):
            LOG_DEBUG('Disconnects from server by connection manager event')
            if self.__ctx.guiSpaceID != _SPACE_ID.LOGIN:
                self.__ctx.dsnReason = _DSN_REASON.EVENT
            return self.showLogin()
        else:
            return False

    def goToLoginByKick(self, reason, isBan, expiryTime):
        if self.__ctx.dsnReason != _DSN_REASON.KICK:
            LOG_DEBUG('Disconnects from server by kick')
            self.__ctx.dsnReason = _DSN_REASON.KICK
            self.__ctx.dsnDesc = (reason, isBan, expiryTime)
        return self.showLogin()

    def goToLoginByError(self, reason):
        LOG_DEBUG('Disconnects from server by client error')
        self.__ctx.dsnReason = _DSN_REASON.ERROR
        self.__ctx.dsnDesc = (reason, False, 0)
        self.connectionMgr.disconnect()
        return self.showLogin()

    @staticmethod
    def quitFromGame():
        BigWorld.quit()

    def attachCursor(self, appNS, flags=_CTRL_FLAG.CURSOR_VISIBLE):
        self.__appFactory.attachCursor(appNS, flags=flags)

    def detachCursor(self, appNS):
        self.__appFactory.detachCursor(appNS)

    def syncCursor(self, appNS, flags=_CTRL_FLAG.CURSOR_VISIBLE):
        self.__appFactory.syncCursor(appNS, flags=flags)

    def handleKey(self, appNS, isDown, key, mods):
        return self.__appFactory.handleKey(appNS, isDown, key, mods)

    def __updateState(self):
        result = False
        newState = self.__state.goNext(self.__ctx)
        if newState:
            LOG_DEBUG('State is changed (from, to)', self.__state, newState)
            self.onGUISpaceLeft(self.__state.getSpaceID())
            self.__state.fini(self.__ctx)
            self.__state.hideGUI(self.__appFactory)
            self.__state = newState
            self.__state.init(self.__ctx)
            for appNS, appState in self.__getCreatedApps():
                self.__state.showGUI(self.__appFactory, appNS, appState)

            result = True
            self.onGUISpaceEntered(self.__ctx.guiSpaceID)
        else:
            LOG_DEBUG('State is updated ctx:', self.__ctx)
            for appNS, appState in self.__getCreatedApps():
                self.__state.update(self.__ctx)
                self.__state.updateGUI(self.__appFactory, appNS)

        return result

    def __getCreatedApps(self):
        for appNS, appState in self.__ctx.appsStates.iteritems():
            if appState != _STATE_ID.NOT_CREATED:
                yield (appNS, appState)

    def __onAppInitializing(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            LOG_DEBUG('App is initializing', appNS)
            self.__ctx.appsStates[appNS] = _STATE_ID.INITIALIZING
            self.__state.showGUI(self.__appFactory, appNS, _STATE_ID.INITIALIZING)

    def __onAppInitialized(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            LOG_DEBUG('App is initialized', appNS)
            self.__ctx.appsStates[appNS] = _STATE_ID.INITIALIZED
            self.__state.showGUI(self.__appFactory, appNS, _STATE_ID.INITIALIZED)

    def __onAppDestroyed(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            LOG_DEBUG('App is destroyed', appNS)
            self.__ctx.appsStates[appNS] = _STATE_ID.NOT_CREATED

    def __onGoNextSpace(self, _):
        self.__updateState()


g_appLoader = _AppLoader()
