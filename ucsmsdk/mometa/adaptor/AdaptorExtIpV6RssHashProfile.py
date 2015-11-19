"""This module contains the general information for AdaptorExtIpV6RssHashProfile ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorExtIpV6RssHashProfileConsts():
    IP_HASH_DISABLED = "disabled"
    IP_HASH_ENABLED = "enabled"
    TCP_HASH_DISABLED = "disabled"
    TCP_HASH_ENABLED = "enabled"


class AdaptorExtIpV6RssHashProfile(ManagedObject):
    """This is AdaptorExtIpV6RssHashProfile class."""

    consts = AdaptorExtIpV6RssHashProfileConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorExtIpV6RssHashProfile", "adaptorExtIpV6RssHashProfile", "ext-ipv6-rss-hash", VersionMeta.Version101e, "InputOutput", 0xfL, [], ["admin", "ls-config-policy", "ls-network", "ls-server-policy"], [u'adaptorHostEthIf', u'adaptorHostEthIfProfile', u'adaptorUsnicConnDef'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "ip_hash": MoPropertyMeta("ip_hash", "ipHash", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "tcp_hash": MoPropertyMeta("tcp_hash", "tcpHash", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "ipHash": "ip_hash", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "tcpHash": "tcp_hash", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.ip_hash = None
        self.sacl = None
        self.status = None
        self.tcp_hash = None

        ManagedObject.__init__(self, "AdaptorExtIpV6RssHashProfile", parent_mo_or_dn, **kwargs)
