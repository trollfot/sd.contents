# -*- coding: utf-8 -*-

from zope.interface import Interface
from plone.portlets.interfaces import ILocalPortletAssignable


class IStructuredItem(Interface):
    """Marker interface
    """

class IStructuredContainer(IStructuredItem):
    """Marker interface
    """

class IStructuredDocument(IStructuredContainer, ILocalPortletAssignable):
    """Marker interface
    """

class IStructuredBlock(Interface):
    """Marker interface
    """

class IExternalStructuredItem(IStructuredItem):
    """Marker interface for contents that have no layout attributes.
    It's used to mark non-native contents that need to be rendered in
    the structured document.
    """
