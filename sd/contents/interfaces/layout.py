# -*- coding: utf-8 -*-

from zope.schema import Choice, Bool
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from base import IStructuredItem
_ = MessageFactory("sd")


class IDynamicStructuredItem(IStructuredItem):
    """The elements implementing this interface are considered as
    structured item. It adds a notion of layout that can be selected
    by the user. A layout is a certain form of rendering. While implementing
    this interface, the content type will provide a form allowing the user
    to choose between the existing registered renderers.
    """
    show_title = Bool(
        default=True,
        title=_(u"show_title", default="Enable title rendering"),
        description=_(u"show_title_desc",
                      default=u"Show the item description in the rendering.")
        )

    show_description = Bool(
        default=True,
        title=_(u"show_description", default="Enable description rendering"),
        description=_(u"show_description_desc",
                      default=u"Show the item description in the rendering.")
        )

    sd_layout = Choice(
        required=True,
        title=_(u"Layout"),
        vocabulary="sd.rendering.layout",
        default=u"default",
        description=_(u"sd_layout_desc",
                      default=u"Layout used to render the item."),
        )

    
class IUndirectLayoutProvider(Interface):
    """An object providing layout informations through its context.
    """

class ILayoutProvider(IUndirectLayoutProvider):
    """Adapting items to be layout aware.
    """
