import base64

from django.db import models

class Foo(models.Model):
    _user = models.CharField(max_length=150)
    _data = models.BinaryField(
            blank=True)
    _path = models.CharField(max_length=1000)

    #def set_data(self, data):
    #    self._data = base64.encodestring(data)

    #def get_data(self):
    #    return base64.decodestring(self._data)

    #data = property(get_data, set_data)