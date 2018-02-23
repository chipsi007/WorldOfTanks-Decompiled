# Python 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/dossiers2/common/utils.py
import struct

def getDossierVersion(dossierCompDescr, versionFormat, latestVersion):
    if dossierCompDescr == '':
        return latestVersion
    return struct.unpack_from(versionFormat, dossierCompDescr)[0]
