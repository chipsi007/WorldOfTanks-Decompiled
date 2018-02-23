# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/Lib/plat-unixware7/IN.py


def IN_CLASSA(i):
    return long(i) & 2147483648L == 0


IN_CLASSA_NET = 4278190080L
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 16777215
IN_CLASSA_MAX = 128

def IN_CLASSB(i):
    return long(i) & 3221225472L == 2147483648L


IN_CLASSB_NET = 4294901760L
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 65535
IN_CLASSB_MAX = 65536

def IN_CLASSC(i):
    return long(i) & 3758096384L == 3221225472L


IN_CLASSC_NET = 4294967040L
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 255

def IN_CLASSD(i):
    return long(i) & 4026531840L == 3758096384L


IN_CLASSD_NET = 4026531840L
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 268435455

def IN_MULTICAST(i):
    return IN_CLASSD(i)


def IN_EXPERIMENTAL(i):
    return long(i) & 3758096384L == 3758096384L


def IN_BADCLASS(i):
    return long(i) & 4026531840L == 4026531840L


INADDR_ANY = 0
INADDR_LOOPBACK = 2130706433
INADDR_BROADCAST = 4294967295L
INADDR_NONE = 4294967295L
IN_LOOPBACKNET = 127
INADDR_UNSPEC_GROUP = 3758096384L
INADDR_ALLHOSTS_GROUP = 3758096385L
INADDR_ALLRTRS_GROUP = 3758096386L
INADDR_MAX_LOCAL_GROUP = 3758096639L

def quad_low(x):
    return x.val[0]


ADT_EMASKSIZE = 8
SHRT_MIN = -32768
SHRT_MAX = 32767
INT_MIN = -2147483648
INT_MAX = 2147483647
LONG_MIN = -2147483648
LONG_MAX = 2147483647
OFF32_MAX = LONG_MAX
ISTAT_ASSERTED = 0
ISTAT_ASSUMED = 1
ISTAT_NONE = 2
OFF_MAX = OFF32_MAX
CLOCK_MAX = LONG_MAX
P_MYID = -1
P_MYHOSTID = -1
FD_SETSIZE = 4096
NBBY = 8
NULL = 0

def IN6_IS_ADDR_UNSPECIFIED(a):
    return IN6_ADDR_EQUAL_L(a, 0, 0, 0, 0)


def IN6_SET_ADDR_UNSPECIFIED(a):
    return IN6_ADDR_COPY_L(a, 0, 0, 0, 0)


def IN6_IS_ADDR_ANY(a):
    return IN6_ADDR_EQUAL_L(a, 0, 0, 0, 0)


def IN6_SET_ADDR_ANY(a):
    return IN6_ADDR_COPY_L(a, 0, 0, 0, 0)


def IN6_IS_ADDR_LOOPBACK(a):
    return IN6_ADDR_EQUAL_L(a, 0, 0, 0, 16777216)


def IN6_SET_ADDR_LOOPBACK(a):
    return IN6_ADDR_COPY_L(a, 0, 0, 0, 16777216)


IN6_MC_FLAG_PERMANENT = 0
IN6_MC_FLAG_TRANSIENT = 1
IN6_MC_SCOPE_NODELOCAL = 1
IN6_MC_SCOPE_LINKLOCAL = 2
IN6_MC_SCOPE_SITELOCAL = 5
IN6_MC_SCOPE_ORGLOCAL = 8
IN6_MC_SCOPE_GLOBAL = 14

def IN6_IS_ADDR_MC_NODELOCAL(a):
    pass


def IN6_IS_ADDR_MC_LINKLOCAL(a):
    pass


def IN6_IS_ADDR_MC_SITELOCAL(a):
    pass


def IN6_IS_ADDR_MC_ORGLOCAL(a):
    pass


def IN6_IS_ADDR_MC_GLOBAL(a):
    pass


__NETLIB_UW211_SVR4 = 1
__NETLIB_UW211_XPG4 = 2
__NETLIB_GEMINI_SVR4 = 3
__NETLIB_GEMINI_XPG4 = 4
__NETLIB_FP1_SVR4 = 5
__NETLIB_FP1_XPG4 = 6
__NETLIB_BASE_VERSION__ = __NETLIB_UW211_SVR4
__NETLIB_VERSION__ = __NETLIB_FP1_SVR4
__NETLIB_VERSION__ = __NETLIB_FP1_XPG4
__NETLIB_VERSION__ = __NETLIB_GEMINI_SVR4
__NETLIB_VERSION__ = __NETLIB_GEMINI_XPG4
__NETLIB_VERSION__ = __NETLIB_UW211_SVR4
__NETLIB_VERSION__ = __NETLIB_UW211_XPG4
__NETLIB_VERSION__ = __NETLIB_FP1_XPG4
LITTLE_ENDIAN = 1234
BIG_ENDIAN = 4321
PDP_ENDIAN = 3412
BYTE_ORDER = LITTLE_ENDIAN

def htonl(hl):
    return __htonl(hl)


def ntohl(nl):
    return __ntohl(nl)


def htons(hs):
    return __htons(hs)


def ntohs(ns):
    return __ntohs(ns)


def ntohl(x):
    return x


def ntohs(x):
    return x


def htonl(x):
    return x


def htons(x):
    return x


def __NETLIB_VERSION_IS_XPG4(version):
    return version % 2 == 0


def __NETLIB_VERSION_HAS_SALEN(version):
    return version >= __NETLIB_GEMINI_SVR4


def __NETLIB_VERSION_IS_IKS(version):
    return version >= __NETLIB_FP1_SVR4


def SA_FAMILY_GET(sa):
    pass


INET6_ADDRSTRLEN = 46
IPV6_UNICAST_HOPS = 3
IPV6_ADDRFORM = 24
IPV6_MULTICAST_HOPS = 25
IPV6_MULTICAST_IF = 26
IPV6_MULTICAST_LOOP = 27
IPV6_ADD_MEMBERSHIP = 28
IPV6_DROP_MEMBERSHIP = 29

def LIST_INIT(head):
    pass


def LIST_INIT(head):
    pass


def remque(a):
    return REMQUE(a)


SHUT_RD = 0
SHUT_WR = 1
SHUT_RDWR = 2

def __P(protos):
    return protos


def __STRING(x):
    pass


def __P(protos):
    pass


def __STRING(x):
    pass


NETCONFIG = '/etc/netconfig'
NETPATH = 'NETPATH'
NC_TPI_CLTS = 1
NC_TPI_COTS = 2
NC_TPI_COTS_ORD = 3
NC_TPI_RAW = 4
NC_NOFLAG = 0
NC_VISIBLE = 1
NC_BROADCAST = 2
NC_NOPROTOFMLY = '-'
NC_LOOPBACK = 'loopback'
NC_INET = 'inet'
NC_INET6 = 'inet6'
NC_IMPLINK = 'implink'
NC_PUP = 'pup'
NC_CHAOS = 'chaos'
NC_NS = 'ns'
NC_NBS = 'nbs'
NC_ECMA = 'ecma'
NC_DATAKIT = 'datakit'
NC_CCITT = 'ccitt'
NC_SNA = 'sna'
NC_DECNET = 'decnet'
NC_DLI = 'dli'
NC_LAT = 'lat'
NC_HYLINK = 'hylink'
NC_APPLETALK = 'appletalk'
NC_NIT = 'nit'
NC_IEEE802 = 'ieee802'
NC_OSI = 'osi'
NC_X25 = 'x25'
NC_OSINET = 'osinet'
NC_GOSIP = 'gosip'
NC_NETWARE = 'netware'
NC_NOPROTO = '-'
NC_TCP = 'tcp'
NC_UDP = 'udp'
NC_ICMP = 'icmp'
NC_IPX = 'ipx'
NC_SPX = 'spx'
NC_TPI_CLTS = 1
NC_TPI_COTS = 2
NC_TPI_COTS_ORD = 3
NC_TPI_RAW = 4
SOCK_STREAM = 2
SOCK_DGRAM = 1
SOCK_RAW = 4
SOCK_RDM = 5
SOCK_SEQPACKET = 6
SO_DEBUG = 1
SO_ACCEPTCONN = 2
SO_REUSEADDR = 4
SO_KEEPALIVE = 8
SO_DONTROUTE = 16
SO_BROADCAST = 32
SO_USELOOPBACK = 64
SO_LINGER = 128
SO_OOBINLINE = 256
SO_ORDREL = 512
SO_IMASOCKET = 1024
SO_MGMT = 2048
SO_REUSEPORT = 4096
SO_LISTENING = 8192
SO_RDWR = 16384
SO_SEMA = 32768
SO_DONTLINGER = ~SO_LINGER
SO_SNDBUF = 4097
SO_RCVBUF = 4098
SO_SNDLOWAT = 4099
SO_RCVLOWAT = 4100
SO_SNDTIMEO = 4101
SO_RCVTIMEO = 4102
SO_ERROR = 4103
SO_TYPE = 4104
SO_PROTOTYPE = 4105
SO_ALLRAW = 4106
SOL_SOCKET = 65535
AF_UNSPEC = 0
AF_UNIX = 1
AF_LOCAL = AF_UNIX
AF_INET = 2
AF_IMPLINK = 3
AF_PUP = 4
AF_CHAOS = 5
AF_NS = 6
AF_NBS = 7
AF_ECMA = 8
AF_DATAKIT = 9
AF_CCITT = 10
AF_SNA = 11
AF_DECnet = 12
AF_DLI = 13
AF_LAT = 14
AF_HYLINK = 15
AF_APPLETALK = 16
AF_NIT = 17
AF_802 = 18
AF_OSI = 19
AF_ISO = AF_OSI
AF_X25 = 20
AF_OSINET = 21
AF_GOSIP = 22
AF_YNET = 23
AF_ROUTE = 24
AF_LINK = 25
pseudo_AF_XTP = 26
AF_INET6 = 27
AF_MAX = 27
AF_INET_BSWAP = 512
PF_UNSPEC = AF_UNSPEC
PF_UNIX = AF_UNIX
PF_LOCAL = AF_LOCAL
PF_INET = AF_INET
PF_IMPLINK = AF_IMPLINK
PF_PUP = AF_PUP
PF_CHAOS = AF_CHAOS
PF_NS = AF_NS
PF_NBS = AF_NBS
PF_ECMA = AF_ECMA
PF_DATAKIT = AF_DATAKIT
PF_CCITT = AF_CCITT
PF_SNA = AF_SNA
PF_DECnet = AF_DECnet
PF_DLI = AF_DLI
PF_LAT = AF_LAT
PF_HYLINK = AF_HYLINK
PF_APPLETALK = AF_APPLETALK
PF_NIT = AF_NIT
PF_802 = AF_802
PF_OSI = AF_OSI
PF_ISO = PF_OSI
PF_X25 = AF_X25
PF_OSINET = AF_OSINET
PF_GOSIP = AF_GOSIP
PF_YNET = AF_YNET
PF_ROUTE = AF_ROUTE
PF_LINK = AF_LINK
pseudo_PF_XTP = pseudo_AF_XTP
PF_INET6 = AF_INET6
PF_MAX = AF_MAX
SOMAXCONN = 5
SCM_RIGHTS = 1
MSG_OOB = 1
MSG_PEEK = 2
MSG_DONTROUTE = 4
MSG_CTRUNC = 8
MSG_TRUNC = 16
MSG_EOR = 48
MSG_WAITALL = 32
MSG_MAXIOVLEN = 16

def OPTLEN(x):
    return (x + sizeof(long) - 1) / sizeof(long) * sizeof(long)


GIARG = 1
CONTI = 2
GITAB = 4
SOCKETSYS = 88
SOCKETSYS = 83
SO_ACCEPT = 1
SO_BIND = 2
SO_CONNECT = 3
SO_GETPEERNAME = 4
SO_GETSOCKNAME = 5
SO_GETSOCKOPT = 6
SO_LISTEN = 7
SO_RECV = 8
SO_RECVFROM = 9
SO_SEND = 10
SO_SENDTO = 11
SO_SETSOCKOPT = 12
SO_SHUTDOWN = 13
SO_SOCKET = 14
SO_SOCKPOLL = 15
SO_GETIPDOMAIN = 16
SO_SETIPDOMAIN = 17
SO_ADJTIME = 18
SIGNBIT = 2147483648L
DIVERR = 0
SGLSTP = 1
NMIFLT = 2
BPTFLT = 3
INTOFLT = 4
BOUNDFLT = 5
INVOPFLT = 6
NOEXTFLT = 7
DBLFLT = 8
EXTOVRFLT = 9
INVTSSFLT = 10
SEGNPFLT = 11
STKFLT = 12
GPFLT = 13
PGFLT = 14
EXTERRFLT = 16
ALIGNFLT = 17
MCEFLT = 18
USERFLT = 256
TRP_PREEMPT = 512
TRP_UNUSED = 513
PF_ERR_MASK = 1
PF_ERR_PAGE = 0
PF_ERR_PROT = 1
PF_ERR_WRITE = 2
PF_ERR_USER = 4
EVT_STRSCHED = 4
EVT_GLOBCALLOUT = 8
EVT_LCLCALLOUT = 16
EVT_SOFTINTMASK = EVT_STRSCHED | EVT_GLOBCALLOUT | EVT_LCLCALLOUT
PL0 = 0
PL1 = 1
PL2 = 2
PL3 = 3
PL4 = 4
PL5 = 5
PL6 = 6
PLHI = 8
PL7 = PLHI
PLBASE = PL0
PLTIMEOUT = PL1
PLDISK = PL5
PLSTR = PL6
PLTTY = PLSTR
PLMIN = PL0
PLMIN = PL1
MAX_INTR_LEVELS = 10
MAX_INTR_NESTING = 50
STRSCHED = EVT_STRSCHED
GLOBALSOFTINT = EVT_GLOBCALLOUT
LOCALSOFTINT = EVT_LCLCALLOUT

def GET_TIME(timep):
    pass


LK_THRESHOLD = 500000

def remque_null(e):
    pass


def LS_ISEMPTY(listp):
    pass


LK_BASIC = 1
LK_SLEEP = 2
LK_NOSTATS = 4

def CYCLES_SINCE(c):
    return CYCLES_BETWEEN(c, CYCLES())


LSB_NLKDS = 92
EVT_RUNRUN = 1
EVT_KPRUNRUN = 2
SP_UNLOCKED = 0
SP_LOCKED = 1
KS_LOCKTEST = 1
KS_MPSTATS = 2
KS_DEINITED = 4
KS_NVLTTRACE = 8
RWS_READ = ord('r')
RWS_WRITE = ord('w')
RWS_UNLOCKED = ord('u')
RWS_BUSY = ord('b')

def SLEEP_LOCKOWNED(lkp):
    pass


def SLEEP_DISOWN(lkp):
    pass


KS_NOPRMPT = 1
__KS_LOCKTEST = KS_LOCKTEST
__KS_LOCKTEST = 0
__KS_MPSTATS = KS_MPSTATS
__KS_MPSTATS = 0
__KS_NVLTTRACE = KS_NVLTTRACE
__KS_NVLTTRACE = 0
KSFLAGS = __KS_LOCKTEST | __KS_MPSTATS | __KS_NVLTTRACE
KSVUNIPROC = 1
KSVMPDEBUG = 2
KSVMPNODEBUG = 3
KSVFLAG = KSVUNIPROC
KSVFLAG = KSVMPDEBUG
KSVFLAG = KSVMPNODEBUG
_A_SP_LOCKED = 1
_A_SP_UNLOCKED = 0
_A_INVPL = -1

def _ATOMIC_INT_INCR(atomic_intp):
    pass


def _ATOMIC_INT_DECR(atomic_intp):
    pass


def ATOMIC_INT_READ(atomic_intp):
    return _ATOMIC_INT_READ(atomic_intp)


def ATOMIC_INT_INCR(atomic_intp):
    return _ATOMIC_INT_INCR(atomic_intp)


def ATOMIC_INT_DECR(atomic_intp):
    return _ATOMIC_INT_DECR(atomic_intp)


def FSPIN_INIT(lp):
    pass


def FSPIN_LOCK(l):
    return DISABLE()


def FSPIN_TRYLOCK(l):
    return (DISABLE(), B_TRUE)


def FSPIN_UNLOCK(l):
    return ENABLE()


def LOCK_DEINIT(lp):
    pass


def LOCK_DEALLOC(lp):
    pass


def LOCK_OWNED(lp):
    return B_TRUE


def RW_DEINIT(lp):
    pass


def RW_DEALLOC(lp):
    pass


def RW_OWNED(lp):
    return B_TRUE


def IS_LOCKED(lockp):
    return B_FALSE


def LOCK_PLMIN(lockp):
    pass


def TRYLOCK_PLMIN(lockp):
    return LOCK_PLMIN(lockp)


def LOCK_SH_PLMIN(lockp):
    return LOCK_PLMIN(lockp)


def RW_RDLOCK_PLMIN(lockp):
    return LOCK_PLMIN(lockp)


def RW_WRLOCK_PLMIN(lockp):
    return LOCK_PLMIN(lockp)


def LOCK_DEINIT(l):
    pass


def LOCK_PLMIN(lockp):
    return LOCK(lockp, PLMIN)


def TRYLOCK_PLMIN(lockp):
    return TRYLOCK(lockp, PLMIN)


def LOCK_SH_PLMIN(lockp):
    return LOCK_SH(lockp, PLMIN)


def RW_RDLOCK_PLMIN(lockp):
    return RW_RDLOCK(lockp, PLMIN)


def RW_WRLOCK_PLMIN(lockp):
    return RW_WRLOCK(lockp, PLMIN)


def FSPIN_IS_LOCKED(fsp):
    return B_FALSE


def SPIN_IS_LOCKED(lockp):
    return B_FALSE


def FSPIN_OWNED(l):
    return B_TRUE


CR_MLDREAL = 1
CR_RDUMP = 2

def crhold(credp):
    return crholdn(credp, 1)


def crfree(credp):
    return crfreen(credp, 1)


def str_aligned(X):
    return uint(X) & sizeof(int) - 1 == 0


DST_NONE = 0
DST_USA = 1
DST_AUST = 2
DST_WET = 3
DST_MET = 4
DST_EET = 5
DST_CAN = 6
DST_GB = 7
DST_RUM = 8
DST_TUR = 9
DST_AUSTALT = 10
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
FD_SETSIZE = 4096
FD_NBBY = 8
NULL = 0
CLOCKS_PER_SEC = 1000000
CGBITS = 4
IDBITS = 28

def toid_unpackcg(idval):
    return idval >> IDBITS & 15


def toid_unpackid(idval):
    return idval & 268435455


def toid_unpackcg(idval):
    pass


def toid_unpackid(idval):
    return idval


NCALLOUT_HASH = 1024
CALLOUT_MAXVAL = 2147483647
TO_PERIODIC = 2147483648L
TO_IMMEDIATE = 2147483648L
SEC = 1
MILLISEC = 1000
MICROSEC = 1000000
NANOSEC = 1000000000
SECHR = 3600
SECDAY = 24 * SECHR
SECYR = 365 * SECDAY

def TIME_OWNED_R(cgnum):
    return B_TRUE


LOOPSECONDS = 1800
LOOPMICROSECONDS = LOOPSECONDS * MICROSEC

def TICKS_SINCE(t):
    return TICKS_BETWEEN(t, TICKS())


MAXRQS = 2
E_OFFLINE = 1
E_BAD = 2
E_SHUTDOWN = 4
E_DRIVER = 8
E_DEFAULTKEEP = 256
E_DRIVERBOUND = 512
E_EXCLUSIVE = 1024
E_CGLEADER = 2048
E_NOWAY = E_OFFLINE | E_BAD | E_SHUTDOWN
E_BOUND = 1
E_GLOBAL = 0
E_UNAVAIL = -1
ENGINE_ONLINE = 1

def PROCESSOR_UNMAP(e):
    return e - engine


BOOTENG = 0
QMOVED = 1
QWANTR = 2
QWANTW = 4
QFULL = 8
QREADR = 16
QUSE = 32
QNOENB = 64
QUP = 128
QBACK = 256
QINTER = 512
QPROCSON = 1024
QTOENAB = 2048
QFREEZE = 4096
QBOUND = 8192
QDEFCNT = 16384
QENAB = 1
QSVCBUSY = 2
STRM_PUTCNT_TABLES = 31

def STRM_MYENG_PUTCNT(sdp):
    return STRM_PUTCNT(l.eng_num, sdp)


QB_FULL = 1
QB_WANTW = 2
QB_BACK = 4
NBAND = 256
DB_WASDUPED = 1
DB_2PIECE = 2
STRLEAKHASHSZ = 1021
MSGMARK = 1
MSGNOLOOP = 2
MSGDELIM = 4
MSGNOGET = 8
MSGLOG = 16
M_DATA = 0
M_PROTO = 1
M_BREAK = 8
M_PASSFP = 9
M_SIG = 11
M_DELAY = 12
M_CTL = 13
M_IOCTL = 14
M_SETOPTS = 16
M_RSE = 17
M_TRAIL = 18
M_IOCACK = 129
M_IOCNAK = 130
M_PCPROTO = 131
M_PCSIG = 132
M_READ = 133
M_FLUSH = 134
M_STOP = 135
M_START = 136
M_HANGUP = 137
M_ERROR = 138
M_COPYIN = 139
M_COPYOUT = 140
M_IOCDATA = 141
M_PCRSE = 142
M_STOPI = 143
M_STARTI = 144
M_PCCTL = 145
M_PCSETOPTS = 146
QNORM = 0
QPCTL = 128
STRCANON = 1
RECOPY = 2
SO_ALL = 63
SO_READOPT = 1
SO_WROFF = 2
SO_MINPSZ = 4
SO_MAXPSZ = 8
SO_HIWAT = 16
SO_LOWAT = 32
SO_MREADON = 64
SO_MREADOFF = 128
SO_NDELON = 256
SO_NDELOFF = 512
SO_ISTTY = 1024
SO_ISNTTY = 2048
SO_TOSTOP = 4096
SO_TONSTOP = 8192
SO_BAND = 16384
SO_DELIM = 32768
SO_NODELIM = 65536
SO_STRHOLD = 131072
SO_LOOP = 262144
DRVOPEN = 0
MODOPEN = 1
CLONEOPEN = 2
OPENFAIL = -1
BPRI_LO = 1
BPRI_MED = 2
BPRI_HI = 3
INFPSZ = -1
FLUSHALL = 1
FLUSHDATA = 0
STRHIGH = 5120
STRLOW = 1024
MAXIOCBSZ = 1024

def straln(a):
    return caddr_t(long(a) & ~(sizeof(int) - 1))


IPM_ID = 200
ICMPM_ID = 201
TCPM_ID = 202
UDPM_ID = 203
ARPM_ID = 204
APPM_ID = 205
RIPM_ID = 206
PPPM_ID = 207
AHDLCM_ID = 208
MHDLCRIPM_ID = 209
HDLCM_ID = 210
PPCID_ID = 211
IGMPM_ID = 212
IPIPM_ID = 213
IPPROTO_IP = 0
IPPROTO_HOPOPTS = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_IPIP = 4
IPPROTO_TCP = 6
IPPROTO_EGP = 8
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
IPPROTO_TP = 29
IPPROTO_IPV6 = 41
IPPROTO_ROUTING = 43
IPPROTO_FRAGMENT = 44
IPPROTO_ESP = 50
IPPROTO_AH = 51
IPPROTO_ICMPV6 = 58
IPPROTO_NONE = 59
IPPROTO_DSTOPTS = 60
IPPROTO_HELLO = 63
IPPROTO_ND = 77
IPPROTO_EON = 80
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPORT_ECHO = 7
IPPORT_DISCARD = 9
IPPORT_SYSTAT = 11
IPPORT_DAYTIME = 13
IPPORT_NETSTAT = 15
IPPORT_FTP = 21
IPPORT_TELNET = 23
IPPORT_SMTP = 25
IPPORT_TIMESERVER = 37
IPPORT_NAMESERVER = 42
IPPORT_WHOIS = 43
IPPORT_MTP = 57
IPPORT_TFTP = 69
IPPORT_RJE = 77
IPPORT_FINGER = 79
IPPORT_TTYLINK = 87
IPPORT_SUPDUP = 95
IPPORT_EXECSERVER = 512
IPPORT_LOGINSERVER = 513
IPPORT_CMDSERVER = 514
IPPORT_EFSSERVER = 520
IPPORT_BIFFUDP = 512
IPPORT_WHOSERVER = 513
IPPORT_ROUTESERVER = 520
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 65535
IPPORT_RESERVED_LOW = 512
IPPORT_RESERVED_HIGH = 1023
IPPORT_USERRESERVED_LOW = 32768
IPPORT_USERRESERVED_HIGH = 65535
INET_ADDRSTRLEN = 16
IP_OPTIONS = 1
IP_TOS = 2
IP_TTL = 3
IP_HDRINCL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_MULTICAST_IF = 9
IP_MULTICAST_LOOP = 10
IP_ADD_MEMBERSHIP = 11
IP_DROP_MEMBERSHIP = 12
IP_BROADCAST_IF = 14
IP_RECVIFINDEX = 15
IP_MULTICAST_TTL = 16
MRT_INIT = 17
MRT_DONE = 18
MRT_ADD_VIF = 19
MRT_DEL_VIF = 20
MRT_ADD_MFC = 21
MRT_DEL_MFC = 22
MRT_VERSION = 23
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IP_MAX_MEMBERSHIPS = 20
INADDR_UNSPEC_GROUP = 3758096384L
INADDR_ALLHOSTS_GROUP = 3758096385L
INADDR_ALLRTRS_GROUP = 3758096386L
INADDR_MAX_LOCAL_GROUP = 3758096639L
IP_HIER_BASE = 20

def ASSERT_LOCK(x):
    pass


def ASSERT_WRLOCK(x):
    pass


def ASSERT_UNLOCK(x):
    pass


def CANPUT(q):
    return canput(q)


def CANPUTNEXT(q):
    return canputnext(q)


INET_DEBUG = 1
