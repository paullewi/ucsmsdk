"""This module contains the general information for AdaptorFcWorkQueueProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorFcWorkQueueProfileConsts():
    pass


class AdaptorFcWorkQueueProfile(ManagedObject):
    """This is AdaptorFcWorkQueueProfile class."""

    consts = AdaptorFcWorkQueueProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFcWorkQueueProfile", "adaptorFcWorkQueueProfile", "fc-work-q", VersionMeta.Version101e, "InputOutput", 0x1fL, [], ["admin", "ls-config-policy", "ls-server-policy", "ls-storage"], [u'adaptorHostFcIf', u'adaptorHostFcIfProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "count": MoPropertyMeta("count", "count", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-1"]), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "ring_size": MoPropertyMeta("ring_size", "ringSize", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["64-128"]), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "ringSize": "ring_size", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.count = None
        self.ring_size = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AdaptorFcWorkQueueProfile", parent_mo_or_dn, **kwargs)
