from apiclient import APIClient


class Client(APIClient):

    def regions(self):
        """Get a list of regions as Region instances.
        :return: List of Regions, Request
        :rtype: List, Request
        """

        json, res = self.all_regions()
        return [Region(self, **s) for s in json['regions']], res
    #regions()

    def sizes(self):
        """Get A list of sizes as Size instances
        :return: List of Sizes, Request
        :rtype: List, Request
        """

        json, res = self.all_sizes()
        return [Size(self, **s) for s in json['sizes']], res
    #sizes()

    def images(self):
        """Get A list of images as Image instances
        :return: List of Images, Request
        :rtype: List, Request
        """
        json, res = self.all_images()
        return [Image(self, **s) for s in json['images']], res
    #images()

    def ssh_keys(self):
        """Get A list of ssh keys as SSHKey instances
        :return: List of SSHKey, Request
        :rtype: List, Request
        """

        json, res = self.all_ssh_keys()
        return [SSHKey(self, **s) for s in json['ssh_keys']], res
    #ssh_keys()
#Client


class Water(object):
    """Docstring for Water """

    def __init__(self, client, id, name):
        """todo: to be defined """

        assert client, "No Client instance"
        assert id, "Size ID not specified."
        assert name, "Size Name not specified."

        self._client = client
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
        """This is intended to be shell friendly
        """
        return "{}:{}".format(self._name, self._id)
    #__repr__()
#Water


class Droplet(Water):
    """Docstring for Droplet """

    def __init__(self, client=None,
                 name=None, id=None, image_id=None,
                 size_id=None, event_id=None):
        """todo: to be defined """

    #__init__()

#Droplet


class Region(Water):
    pass
#Region


class Size(Water):
    pass
#Size


class Image(Water):
    """Docstring for Image """

    def __init__(self, client, id, name, distribution):
        """todo: to be defined """

        assert distribution, "Distribution Name not specified."
        super(Image, self).__init__(client, id, name)

        self._distro = distribution
    #__init__()

    def __repr__(self):
        """This is intended to be shell friendly
        """
        return "{}:{}:{}".format(self._name, self._distro, self._id)
    #__repr__()
#Image


class SSHKey(Water):
    pass
#SSHKey
