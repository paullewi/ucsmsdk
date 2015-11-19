"""This module contains the general information for ExtpolRegistryFsmStage ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ExtpolRegistryFsmStageConsts():
    LAST_UPDATE_TIME_ = ""
    NAME_CROSS_DOMAIN_CONFIG_BEGIN = "crossDomainConfigBegin"
    NAME_CROSS_DOMAIN_CONFIG_FAIL = "crossDomainConfigFail"
    NAME_CROSS_DOMAIN_CONFIG_SET_LOCAL = "crossDomainConfigSetLocal"
    NAME_CROSS_DOMAIN_CONFIG_SET_PEER = "crossDomainConfigSetPeer"
    NAME_CROSS_DOMAIN_CONFIG_SUCCESS = "crossDomainConfigSuccess"
    NAME_CROSS_DOMAIN_DELETE_BEGIN = "crossDomainDeleteBegin"
    NAME_CROSS_DOMAIN_DELETE_FAIL = "crossDomainDeleteFail"
    NAME_CROSS_DOMAIN_DELETE_SET_LOCAL = "crossDomainDeleteSetLocal"
    NAME_CROSS_DOMAIN_DELETE_SET_PEER = "crossDomainDeleteSetPeer"
    NAME_CROSS_DOMAIN_DELETE_SUCCESS = "crossDomainDeleteSuccess"
    NAME_NOP = "nop"
    STAGE_STATUS_FAIL = "fail"
    STAGE_STATUS_IN_PROGRESS = "inProgress"
    STAGE_STATUS_NOP = "nop"
    STAGE_STATUS_PENDING = "pending"
    STAGE_STATUS_SKIP = "skip"
    STAGE_STATUS_SUCCESS = "success"
    STAGE_STATUS_THROTTLED = "throttled"


class ExtpolRegistryFsmStage(ManagedObject):
    """This is ExtpolRegistryFsmStage class."""

    consts = ExtpolRegistryFsmStageConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ExtpolRegistryFsmStage", "extpolRegistryFsmStage", "stage-[name]", VersionMeta.Version211a, "OutputOnly", 0x7L, [], [""], [u'extpolRegistryFsm'], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, None, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x1L, 0, 256, None, [], []), 
        "last_update_time": MoPropertyMeta("last_update_time", "lastUpdateTime", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, """([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [""], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, None, None, None, None, ["crossDomainConfigBegin", "crossDomainConfigFail", "crossDomainConfigSetLocal", "crossDomainConfigSetPeer", "crossDomainConfigSuccess", "crossDomainDeleteBegin", "crossDomainDeleteFail", "crossDomainDeleteSetLocal", "crossDomainDeleteSetPeer", "crossDomainDeleteSuccess", "nop"], []), 
        "order": MoPropertyMeta("order", "order", "ushort", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "retry": MoPropertyMeta("retry", "retry", "byte", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "stage_status": MoPropertyMeta("stage_status", "stageStatus", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["fail", "inProgress", "nop", "pending", "skip", "success", "throttled"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "lastUpdateTime": "last_update_time", 
        "name": "name", 
        "order": "order", 
        "retry": "retry", 
        "rn": "rn", 
        "sacl": "sacl", 
        "stageStatus": "stage_status", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.last_update_time = None
        self.order = None
        self.retry = None
        self.sacl = None
        self.stage_status = None
        self.status = None

        ManagedObject.__init__(self, "ExtpolRegistryFsmStage", parent_mo_or_dn, **kwargs)
