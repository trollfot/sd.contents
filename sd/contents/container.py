# -*- coding: utf-8 -*-
from zope.interface import implements
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.lib.autosort import AutoOrderSupport
from Products.ATContentTypes.content.base import ATCTOrderedFolder
from Products.ATContentTypes.content.folder  import ATFolderSchema
from Products.Archetypes.AllowedTypesByIface import AllowedTypesByIfaceMixin
from interfaces import IStructuredContainer


class StructuredContainer( AllowedTypesByIfaceMixin,
                           AutoOrderSupport, ATCTOrderedFolder ):
    """Base container, implemented by a document and a chapter
    """
    implements(IStructuredContainer)
    schema = ATFolderSchema.copy()
    security = ClassSecurityInfo()


    security.declarePublic('canSetDefaultPage')
    def canSetDefaultPage(self):
        """No Default Page can be set for this folderish type
        """
        return False


    security.declarePublic('getDefaultAddableTypes')
    def getDefaultAddableTypes(self, context=None):
        """Returns a list of normally allowed objects as ftis.
        Exactly like PortalFolder.allowedContentTypes except this
        will check in a specific context.
        """
        if context is None:
            context = self

        pt = getToolByName(self, 'portal_types')
        at = getToolByName(self, 'archetype_tool')
        
        allow   = at.listPortalTypesWithInterfaces(self.allowed_interfaces)
        allowed = [item.getId() for item in allow]
        result  = [ contentType for contentType in pt.listTypeInfo(context)
                    if contentType.getId() in allowed]

        return [t for t in result if t.isConstructionAllowed(context)]


    security.declareProtected(View, 'getNextPreviousParentValue')
    def getNextPreviousParentValue(self):
        """We disable the next-previous inheritage.
        """
        return False
        

    def manage_afterAdd(self, item, container):
        ATCTOrderedFolder.manage_afterAdd(self, item, container)
        AutoOrderSupport.manage_afterAdd(self, item, container)
