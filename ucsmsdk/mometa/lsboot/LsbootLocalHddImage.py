"""This module contains the general information for LsbootLocalHddImage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsbootLocalHddImageConsts():
    TYPE_LOCAL_ANY = "local-any"
    TYPE_LOCAL_JBOD = "local-jbod"
    TYPE_LOCAL_LUN = "local-lun"
    TYPE_SD_CARD = "sd-card"
    TYPE_USB_EXTERN = "usb-extern"
    TYPE_USB_INTERN = "usb-intern"


class LsbootLocalHddImage(ManagedObject):
    """This is LsbootLocalHddImage class."""

    consts = LsbootLocalHddImageConsts()
    naming_props = set([])

    mo_meta = MoMeta("LsbootLocalHddImage", "lsbootLocalHddImage", "local-hdd", VersionMeta.Version221b, "InputOutput", 0x1fL, [], ["admin", "ls-compute", "ls-config", "ls-config-policy", "ls-server", "ls-server-policy", "ls-storage", "ls-storage-policy"], [u'lsbootLocalStorage'], [u'lsbootLocalLunImagePath', u'lsbootUEFIBootParam'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-16"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["local-any", "local-jbod", "local-lun", "sd-card", "usb-extern", "usb-intern"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "order": "order", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.order = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "LsbootLocalHddImage", parent_mo_or_dn, **kwargs)
