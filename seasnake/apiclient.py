import requests
import urllib


import logging

# Set up the logger
logger = logging.getLogger(__name__)
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(('%(asctime)s %(levelname)s:%(process)s'
                                   ' %(lineno)s:%(module)s:%(funcName)s()'
                                   ' %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)

CREDENTIAL_TMPL = "?client_id={}&api_key={}"
BASE_URL = 'https://api.digitalocean.com'


class APIClient(object):
    """Docstring for APIClient """

    def __init__(self, client_id, api_key):
        """todo: to be defined

        :param userid: arg description
        :type userid: type description
        :param api_key: arg description
        :type api_key: type description
        """

        self._client_id = client_id
        self._api_key = api_key

        self._cred = CREDENTIAL_TMPL.format(self._client_id, self._api_key)
        # self._base_url = BASE_URL + '/' + self._cred
    #__init__()

    def _get(self, path='', params={}):
        """todo: Docstring for _get

        :param path: arg description
        :type path: type description
        :return:
        :rtype:
        """

        url = BASE_URL + path + '/' + urllib.urlencode(params) + self._cred
        logger.debug("Requesting: %s", url)

        res = requests.get(url)

        if res.status_code != 200:
            raise Exception("Invalid status code")

        return res
    #_get()

    def _get_json(self, path='', params={}):
        res = self._get(path, params).json

        if res['status'] != 'OK':
            raise Exception("Status not OK\n{}".format(res))

        logger.debug("json: %s", res)
        return res
    #_get_json()

    def get_doc(self):
        """todo: Docstring for get_doc
        :return:
        :rtype:
        """

        res = self._get()
        return res.text
    #get_doc()

    def get_active_droplets(self):
        """todo: Docstring for get_active_droplets
        :return:
        :rtype:
        """

        res = self._get_json('/droplets')
        return res
    #get_active_droplets()

    def get_droplet(self, drop_id):
        """todo: Docstring for get_droplet

        :param drop_id: arg description
        :type drop_id: type description
        :return:
        :rtype:
        """

        res = self._get_json('/droplets/{}'.format(drop_id))
        return res
    #get_droplet()

    def new_droplet(self, name, size_id, image_id,
                    region_id, ssh_key_ids=None):
        params = {
            'name': str(name),
            'size_id': int(size_id),
            'image_id': int(image_id),
            'region_id': int(region_id),
        }
        if ssh_key_ids:
            params.update({'ssh_key_ids': ssh_key_ids})

        return self._get_json('/droplets/new', params)
    #new_droplet()

    def reboot_droplet(self, droplet_id):
        """

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/reboot'.format(int(droplet_id)))
    #reboot_droplet()

    def power_cycle_droplet(self, droplet_id):
        """

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/power_cycle'.format(
            int(droplet_id)))
    #power_cycle_droplet()

    def power_off_droplet(self, droplet_id):
        """Power Off
        This method allows you to poweroff a running droplet.
        The droplet will remain in your account.

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/power_off'.format(
            int(droplet_id)))
    #power_off_droplet()

    def power_on_droplet(self, droplet_id):
        """Power On
        This method allows you to poweron a powered off droplet.

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/power_on'.format(
            int(droplet_id)))
    #power_on_droplet()

    def password_reset(self, droplet_id):
        """Reset Root Password
        This method will reset the root password for a droplet.
        Please be aware that this will reboot the droplet to allow
        resetting the password.

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/password_reset'.format(
            int(droplet_id)))
    #reset_root_password()

    def resize_droplet(self, droplet_id, size_id):
        """ Resize Droplet
        This method allows you to resize a specific droplet to a different size.
        This will affect the number of processors and memory allocated
        to the droplet.

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :param size_id: Required, Numeric, this is the id of the size you would like the droplet to be resized to
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/resize'.format(
            int(droplet_id)), {'size_id': size_id})
    #resize_droplet()

    def snapshot(self, droplet_id, name):
        """ Take a Snapshot
        This method allows you to take a snapshot of the running droplet,
        which can later be restored or used to create a new droplet from the
        same image. Please be aware this may cause a reboot.

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type integer:
        :param name: Optional, this is the name of the new snapshot you want to create. If not set, the snapshot name will default to date/time
        :type String:
        :return: event_id and status
        :rtype: dictionary
        """
    
        pass
    #snapshot()
#APIClient
