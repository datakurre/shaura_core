# -*- coding: utf-8 -*-
"""Base implementations"""

from zope.interface import implements

from shaura_core.interfaces import IObjectManager
from shaura_core.events import\
    ObjectCreatedEvent, ObjectModifiedEvent, ObjectObsoletedEvent

from pyramid.threadlocal import get_current_registry


class ObjectManagerBase(object):
    """Database access utility"""
    implements(IObjectManager)

    def __call__(self, **kwargs):
        """Query for objects on datastore"""
        raise NotImplementedError

    def add(self, obj):
        """Add object to datastore"""
        registry = get_current_registry()
        event = ObjectCreatedEvent(obj)
        registry.notify(event)

    def update(self, obj):
        """Update object on datastore"""
        registry = get_current_registry()
        event = ObjectModifiedEvent(obj)
        registry.notify(event)

    def delete(self, obj):
        """Delete object from datastore"""
        registry = get_current_registry()
        event = ObjectObsoletedEvent(obj)
        registry.notify(event)
