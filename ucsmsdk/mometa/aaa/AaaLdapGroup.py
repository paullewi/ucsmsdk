"""This module contains the general information for AaaLdapGroup ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AaaLdapGroupConsts():
    pass


class AaaLdapGroup(ManagedObject):
    """This is AaaLdapGroup class."""

    consts = AaaLdapGroupConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("AaaLdapGroup", "aaaLdapGroup", "ldapgroup-[name]", VersionMeta.Version141i, "InputOutput", 0x3fL, [], ["aaa", "admin"], [u'aaaLdapEp'], [u'aaaUserLocale', u'aaaUserRole'], ["Add", "Get", "Remove", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version141i, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x2L, None, None, """[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version141i, MoPropertyMeta.NAMING, 0x8L, None, None, """[\t\n\x0b\x0c\r !""#$%&'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{1,240}""", [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version141i, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version141i, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.descr = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "AaaLdapGroup", parent_mo_or_dn, **kwargs)
