'''
Created on May 8, 2015

@author: DC (http://cramer.io/)
'''
from django.db.models.signals import post_init

def track_changes(*fields):
    """
    Tracks property changes on a model instance.
    
    The changed list of properties is refreshed on model initialization
    and save.
    
    >>> @track_changes('name')
    >>> class Post(models.Model):
    >>>     name = models.CharField(...)
    >>> 
    >>>     @classmethod
    >>>     def pre_save(cls, sender, instance, created, **kwargs):
    >>>         if instance.has_changed('name'):
    >>>             print "Hooray!"
    """
    
    UNSAVED = dict()

    def _store_original(self):
        "Updates a local copy of attributes values"
        if self.id:
            self.__original = dict((f, getattr(self, f)) for f in fields)
        else:
            self.__original = UNSAVED

    def inner(cls):
        # contains a local copy of the previous values of attributes
        cls.__data = {}

        def has_changed(self, field):
            "Returns ``True`` if ``field`` has changed since initialization."
            if self.__original is UNSAVED:
                return False
            return self.__original.get(field) != getattr(self, field)
        cls.has_changed = has_changed

        def old_value(self, field):
            "Returns the previous value of ``field``"
            return self.__original.get(field)
        cls.old_value = old_value

        def whats_changed(self):
            "Returns a list of changed attributes."
            changed = {}
            if self.__original is UNSAVED:
                return changed
            for k, v in self.__original.iteritems():
                if v != getattr(self, k):
                    changed[k] = v
            return changed
        cls.whats_changed = whats_changed

        # Ensure we are updating local attributes on model init
        def _post_init(sender, instance, **kwargs):
            _store_original(instance)
        post_init.connect(_post_init, sender=cls, weak=False)
        
        # Ensure we are updating local attributes on model save
        def save(self, *args, **kwargs):
            save._original(self, *args, **kwargs)
            _store_original(self)
        save._original = cls.save
        cls.save = save
        return cls
    return inner