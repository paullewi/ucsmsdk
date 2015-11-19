"""This module contains the general information for FabricVlanGroupReq ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricVlanGroupReqConsts():
    TYPE_LAN = "lan"
    TYPE_SAN = "san"


class FabricVlanGroupReq(ManagedObject):
    """This is FabricVlanGroupReq class."""

    consts = FabricVlanGroupReqConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("FabricVlanGroupReq", "fabricVlanGroupReq", "vlan-group-req-[name]", VersionMeta.Version211a, "InputOutput", 0x1fL, [], ["admin", "ls-network"], [u'orgOrg'], [u'faultInst'], ["Add", "Get", "Remove"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "config_issues": MoPropertyMeta("config_issues", "configIssues", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """((defaultValue|not-applicable|permit-unresolved),){0,2}(defaultValue|not-applicable|permit-unresolved){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x4L, None, None, """[\-\.:_a-zA-Z0-9]{1,32}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lan", "san"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "configIssues": "config_issues", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.config_issues = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "FabricVlanGroupReq", parent_mo_or_dn, **kwargs)
