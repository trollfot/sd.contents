# -*- coding: utf-8 -*-

from zope.schema import Choice, Bool, Int
from zope.interface import Interface, Attribute
from zope.i18nmessageid import MessageFactory
from zope.annotation.interfaces import IAttributeAnnotatable
from Products.ATContentTypes.interface.interfaces import IATContentType

_ = MessageFactory("sd")


# Basic markers
class IStructuredItem(IATContentType):
    """Marker interface
    """

class IStructuredContainer(IATContentType):
    """Marker interface
    """

class IStructuredDocument(IStructuredContainer):
    """Marker interface
    """

class IStructuredChapter(IStructuredItem):
    """While implementing this interface, the content type will
    be considered as a chapter and therefore, will be granted in a
    structured document."""

class IStructuredParagraph(IStructuredItem):
    """While implementing this interface, the content type will
    be considered as a paragraph and therefore, will be granted in a
    structured chapter."""

class IStructuredBlock(Interface):
    """Marker interface
    """

# Markers for non native content
class IExternalStructuredChapter(IStructuredChapter, IAttributeAnnotatable):
    """Marker interface for chapter-ish contents that have
    no layout-aware attributes. This should be used for basic
    ATCT, for instance.
    """

class IExternalStructuredParagraph(IStructuredParagraph, IAttributeAnnotatable):
    """Marker interface for paragraph-ish contents that have
    no layout-aware attributes. This should be used for basic
    ATCT, for instance.
    """


# Used for dynamic layouts
class IPossibleBatchProvider(Interface):
    """Marker interface for items that can provide their contents in
    a batch way.
    """

class IBatchProvider(IPossibleBatchProvider):
    """Can provide a batch with a given number of item.
    """
    batch_size = Int(title=_(u"batch_size", default="Size of the batch"),
                      default=0,
                      description=_(u"batch_size_desc",
                                    default=(u"Number of items rendered."
                                             u"Zero means no batch."))
                     )

class IDynamicStructuredChapter(IStructuredChapter):
    """The elements implementing this interface are considered as
    structured chapters. It adds a notion of layout that can be selected
    by the user. A layout is a certain form of rendering. While implementing
    this interface, the content type will provide a form allowing the user
    to choose between the existing registered renderers."""

    show_title = Bool(title=_(u"show_title",
                              default="Enable title rendering"),
                      default=True,
                      description=_(u"show_title_desc",
                                    default=(u"Unticked, the title "
                                             u"won't be rendered in "
                                             u"the page.")))

    show_description = Bool(title=_(u"show_description",
                                    default="Enable description rendering"),
                            default=True,
                            description=_(u"show_description_desc",
                                          default=(u"Unticked, the description"
                                                   u" won't be rendered in "
                                                   u"the page.")))

    sd_layout = Choice(title=_(u"Layout"),
                       vocabulary="sd.rendering.chapter_layout",
                       default=u"default",
                       description=_(u"chapter_layout_desc",
                                     default=(u"Layout used to render the "
                                              u"chapter")),
                       required=True)


class IDynamicStructuredParagraph(IStructuredParagraph):
    """The elements implementing this interface are considered as
    structured paragraphs. It adds a notion of layout that can be selected
    by the user. A layout is a certain form of rendering. While implementing
    this interface, the content type will provide a form allowing the user
    to choose between the existing registered renderers."""
    
    show_title = Bool(title=_(u"show_title",
                              default="Enable title rendering"),
                      default=True,
                      description=_(u"show_title_desc",
                                    default=(u"Unticked, the title "
                                             u"won't be rendered in "
                                             u"the page.")))

    show_description = Bool(title=_(u"show_description",
                                    default="Enable description rendering"),
                            default=True,
                            description=_(u"show_description_desc",
                                          default=(u"Unticked, the description"
                                                   u" won't be rendered in "
                                                   u"the page.")))

    sd_layout = Choice(title=_(u"Layout"),
                       default=u"default",
                       vocabulary="sd.rendering.paragraph_layout",
                       description=_(u"paragraph_layout_desc",
                                     default=(u"Layout used to render the "
                                              u"paragraph")),
                       required=True)
    

class IUndirectLayoutProvider(Interface):
    """An object providing layout informations through its context.
    """
    context = Attribute('The objet providing the layout informations')

class IDynamicLayoutAdapter(IUndirectLayoutProvider):
    """Adapting items to be layout aware.
    """
