# import this to create messages in the bika domain.
from zope.i18nmessageid import MessageFactory
bikaMessageFactory = MessageFactory('bika.batches')

import logging
logger = logging.getLogger('bika.batches')

from bika.lims.validators import *
from bika.lims.config import *
from bika.lims.permissions import *
from bika.batches.config import *
from bika.batches.permissions import *

from AccessControl import ModuleSecurityInfo, allow_module
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFCore.utils import ContentInit, ToolInit, getToolByName
from Products.CMFPlone import PloneMessageFactory
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.GenericSetup import EXTENSION, profile_registry

allow_module('AccessControl')
allow_module('bika.lims')
allow_module('bika.lims.permissions')
allow_module('bika.lims.utils')
allow_module('bika.batches')
allow_module('bika.batches.permissions')
allow_module('bika.batches.utils')
allow_module('json')
allow_module('pdb')
allow_module('zope.i18n.locales')


def initialize(context):
    ""

    # from content. import
    # from controlpanel.bika_. import

    # content_types, constructors, ftis = process_types(
    #     listTypes(PROJECTNAME),
    #     PROJECTNAME)

    # allTypes = zip(content_types, constructors)
    # for atype, constructor in allTypes:
    #     kind = "%s: Add %s" % (config.PROJECTNAME, atype.portal_type)
    #     perm = ADD_CONTENT_PERMISSIONS.get(atype.portal_type, ADD_CONTENT_PERMISSION)
    #     utils.ContentInit(kind,
    #                       content_types      = (atype,),
    #                       permission         = perm,
    #                       extra_constructors = (constructor,),
    #                       fti                = ftis,
    #                       ).initialize(context)
