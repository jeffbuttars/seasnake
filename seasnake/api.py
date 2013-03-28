import logging
from apiclient import APIClient

logger = logging.getLogger('seasnake')


class Client(APIClient):

    def _res_to_obj(self, cls, key, json):
        return [cls(self, **s) for s in json[key]]
    #_res_to_obj()

    def regions(self):
        """Get a list of regions as Region instances.
        :return: List of Regions, Request
        :rtype: List, Request
        """

        json, res = self.all_regions()
        return self._res_to_obj(Region, 'regions', json), res
    #regions()

    def sizes(self):
        """Get A list of sizes as Size instances
        :return: List of Sizes, Request
        :rtype: List, Request
        """

        json, res = self.all_sizes()
        return self._res_to_obj(Size, 'sizes', json), res
    #sizes()

    def images(self):
        """Get A list of images as Image instances
        :return: List of Images, Request
        :rtype: List, Request
        """
        json, res = self.all_images()
        return self._res_to_obj(Image, 'images', json), res
    #images()

    def ssh_keys(self):
        """Get A list of ssh keys as SSHKey instances
        :return: List of SSHKey, Request
        :rtype: List, Request
        """

        json, res = self.all_ssh_keys()
        return self._res_to_obj(SSHKey, 'ssh_keys', json), res
    #ssh_keys()

    def droplets(self, fetch_related=True):
        """Get A list of Droplets for the client account

        :param fetch_related: Fetch related object information, Image, Size,
            etc.
        :type fetch_related: boolean
        :return: List of Droplet, Request
        :rtype: List, Request
        """

        json, res = self.get_active_droplets()

        logger.debug(json)

        drops = []

        for d in json['droplets']:
            d.update({'status': json['status'], 'fetch_related':fetch_related})
            logger.debug(d)
            drops.append(Droplet(self, **d))
        # end for d in json['droplets']

        # return [Droplet(self, **(s.update({'status': json['status'],
        #                                    'fetch_related':fetch_related})))
        #         for s in json['droplets']], res

        return drops, res
    #droplets()
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
        return "{} name:'{}', id:{}".format(self.__class__.__name__, self._name, self._id)
    #__repr__()
#Water


class Droplet(Water):
    """Docstring for Droplet """

    def __init__(self, client, id=None, name=None,
                 image_id=None, size_id=None,
                 event_id=None, region_id=None,
                 backups_active=None, ip_address=None,
                 status=None, fetch_related=False):

        super(Droplet, self).__init__(client, id, name)

        assert image_id, "No Image ID specified."
        assert size_id, "No Size ID specified."
        assert region_id, "No Region ID specified."
        assert status, "No Status specified."

        self._image_id = image_id
        self._size_id = size_id
        self._event_id = event_id
        self._region_id = region_id
        self._ip_address = ip_address or "N/A"
        self._status = status
        self._backups_active = backups_active or "N/A"
    #__init__()

    @classmethod
    def new(cls, client, name, image_id,
            size_id, region_id, ssh_key_ids=None):

        res, raw = client.new_droplet(name, size_id, image_id,
                                      region_id, ssh_key_ids=None)

        return Droplet(client, status=res['status'], **res['droplet'])
    #new()

    @classmethod
    def destroy(cls, client, id):
        return client.destroy_droplet(id)
    #destroy()

    def __repr__(self):
        """This is intended to be shell friendly
        """
        return "{} name:'{}', ip_address:{}, backups_active:{} id:{}".format(
            self.__class__.__name__, self._name, self._ip_address,
            self._backups_active, self._id)
    #__repr__()
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
        return "{} name:'{}', distro:'{}', id:{}".format(
            self.__class__.__name__, self._name, self._distro, self._id)
    #__repr__()
#Image


class SSHKey(Water):
    pass
#SSHKey
