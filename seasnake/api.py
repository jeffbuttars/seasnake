from apiclient import APIClient


class Client(APIClient):

    def regions(self):
        """Get a list of regions as Region instances.
        :return: List of Regions
        :rtype: List
        """

        json, raw = self.all_regions()
        return [Region(self, **s) for s in json['regions']]
    #regions()
#Client


class Water(object):
    """Docstring for Water """

    def __init__(self, client=None):
        """todo: to be defined """

        self._client = client
        assert self._client, "No Client instance"
    #__init__()
#Water


class Droplet(Water):
    """Docstring for Droplet """

    def __init__(self, client=None,
                 name=None, id=None, image_id=None,
                 size_id=None, event_id=None):
        """todo: to be defined """

    #__init__()

#Droplet


class Region(object):
    """Docstring for Region """

    def __init__(self, client, id, name):
        """todo: to be defined """

        assert id, "Region ID not specified."
        assert name, "Region Name not specified."
        self._client = Client
        self._id = id
        self._name = name

    #__init__()

    @property
    def client(self):
        return self._client
    #client()

    @property
    def id(self):
        return self._id
    #id()

    @property
    def name(self):
        return self._name
    #name()

    def __repr__(self):
        return "Region '{}' : id {}".format(self._name, self._id)
    #__repr__()
#Region


class Size(object):
    """Docstring for Size """

    def __init__(self):
        """todo: to be defined """
        
    #__init__()
        
#Size


class Image(object):
    """Docstring for Image """

    def __init__(self):
        """todo: to be defined """
        
    #__init__()
        
#Image


class SSHKey(object):
    """Docstring for SSHKey """

    def __init__(self):
        """todo: to be defined """
        
    #__init__()
        
#SSHKey
