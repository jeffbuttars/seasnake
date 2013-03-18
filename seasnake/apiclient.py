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

    """Droplets
    Droplets are Virtual Servers in the DigitalOcean Cloud. These are
    individual virtual server machines that you can login to, install your
    applications and software and are the basic computing servers. Droplets
    will have a certain amount of CPU cores,
    memory and disk associated with them.
    """
    def get_active_droplets(self):
        """Show All Active Droplets
        This method returns all active droplets that are currently running in
        your account. All available API information is
        presented for each droplet.

        Sample Return:
        {"status":"OK","droplets":[
            {"backups_active":null,"id":100823,"image_id":420,
                "name":"test222","region_id":1,
                "size_id":33,"status":"active"
                }
            ]}

        :return: status and droplet list
        :rtype: dictionary
        """

        res = self._get_json('/droplets')
        return res
    #get_active_droplets()

    def get_droplet(self, drop_id):
        """Show Droplet
        This method returns full information for a specific droplet ID that is
        passed in the URL.

        Sample Return:
        {"status":"OK","droplet":
            {"backups_active":null,"id":100823,"image_id":420,
            "name":"test222","region_id":1,"size_id":33,"status":"active"}
        }

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: status and droplet information
        :rtype: dictionary
        """

        res = self._get_json('/droplets/{}'.format(drop_id))
        return res
    #get_droplet()

    def new_droplet(self, name, size_id, image_id,
                    region_id, ssh_key_ids=None):
        """New Droplet
        This method allows you to create a new droplet. See the required
        parameters section below for an explanation of the variables that are
        needed to create a new droplet.

        Sample Return:
            {"status":"OK","droplet":
                {"id":100824,"name":"test","image_id":419,"size_id":32,
                    "event_id":7499
                }
            }

        :param name: Required, this is the name of the droplet - must be
            formatted by hostname rules
        :type name: string
        :param size_id: Required, this is the id of the size you would like the
            droplet created at
        :type size_id: int
        :param image_id: Required, this is the id of the image you would like
            the droplet created with
        :type image_id: int
        :param region_id: Required, this is the id of the region you would like
            your server in IE: US/Amsterdam
        :type region_id: int
        :param ssh_key_ids: Optional, comma separated list of ssh_key_ids that
            you would like to be added to the server
        :type ssh_key_ids: list of integers
        :return: event_id and status
        :rtype: dictionary
        """

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
        """Reboot Droplet
        This method allows you to reboot a droplet.
        This is the preferred method to use if a server is not responding.

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/reboot'.format(int(droplet_id)))
    #reboot_droplet()

    def power_cycle_droplet(self, droplet_id):
        """Power Cycle Droplet
        This method allows you to power cycle a droplet.
        This will turn off the droplet and then turn it back on.

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/power_cycle'.format(
            int(droplet_id)))
    #power_cycle_droplet()

    def shutdown_droplet(self, droplet_id):
        """Shut Down Droplet
        This method allows you to shutdown a running droplet.
        The droplet will remain in your account.

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/shutdown'.format(
            int(droplet_id)))
    #shutdown_droplet()

    def power_off_droplet(self, droplet_id):
        """Power Off
        This method allows you to poweroff a running droplet.
        The droplet will remain in your account.

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/power_off'.format(
            int(droplet_id)))
    #power_off_droplet()

    def power_on_droplet(self, droplet_id):
        """Power On
        This method allows you to poweron a powered off droplet.

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
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

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
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

        Sample Return:
            {"status":"OK","event_id":7501}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param size_id: Required, Numeric, this is the id of the size you would like the droplet to be resized to
        :type integer:
        :return: event_id and status
        :rtype: dictionary
        """
        return self._get_json('/droplets/{}/resize'.format(
            int(droplet_id)), {'size_id': size_id})
    #resize_droplet()

    def snapshot(self, droplet_id, name=''):
        """ Take a Snapshot
        This method allows you to take a snapshot of the running droplet,
        which can later be restored or used to create a new droplet from the
        same image. Please be aware this may cause a reboot.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param name: Optional, this is the name of the new snapshot you want to
            create. If not set, the snapshot name will default to date/time
        :type String:
        :return: event_id and status
        :rtype: dictionary
        """

        params = {}
        if name:
            params = {'name': name}

        return self._get_json('/droplets/{}/snapshot'.format(
            int(droplet_id)), params)
    #snapshot()

    def restore(self, droplet_id, image_id):
        """Restore Droplet
        This method allows you to restore a droplet with a previous image or
        snapshot. This will be a mirror copy of the image or snapshot to
        your droplet. Be sure you have backed up any necessary information
        prior to restore.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param image_id: Required, this is the id of the image you would like
            to use to restore your droplet with
        :type image_id: Integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/restore'.format(
            int(droplet_id)), {'image_id': image_id})
    #restore()

    def rebuild(self, droplet_id, image_id):
        """Rebuild Droplet
        This method allows you to reinstall a droplet with a default image.
        This is useful if you want to start again but retain the same 
        IP address for your droplet.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param image_id: image_id Required, this is the id of the image you would like to use to rebuild your droplet with
        :type image_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/rebuild'.format(
            int(droplet_id)), {'image_id': image_id})
    #rebuild()

    def enable_auto_backups(self, droplet_id, image_id):
        """Enable Automatic Backups
        This method enables automatic backups which run in the background
        daily to backup your droplet's data.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param image_id:  Required, this is the id of the image you would like
            to use to rebuild your droplet with
        :type image_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/enable_backups'.format(
            int(droplet_id)), {'image_id': image_id})
    #enable_auto_backups()

    def disable_auto_backups(self, droplet_id, image_id):
        """Disable Automatic Backups
        This method disables automatic backups from running to backup your
            droplet's data.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :param image_id: Required, this is the id of the image you would like
            to use to rebuild your droplet with
        :type image_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/disable_backups'.format(
            int(droplet_id)), {'image_id': image_id})
    #disable_auto_backups()

    def destroy_droplet(self, droplet_id):
        """Destroy Droplet
        This method destroys one of your droplets - this is irreversible.

        Sample Response:
            {"status":"OK","event_id":7504}

        :param droplet_id: Required, Integer, this is the id of your droplet
        :type droplet_id: integer
        :return: event_id and status
        :rtype: dictionary
        """

        return self._get_json('/droplets/{}/destroy'.format(
            int(droplet_id)), {'image_id': image_id})
    #destroy_droplet()

    """Regions
    Regions are different data center locations where you can create droplets.
    Different regions allow you to build physically diverse networks and ensure
    that if a single data center or region has a service problem, your other
    droplets are not affected. This enables highly available network
    environments and redundant droplets. Alternatively you may select a region
    based on global location to be as close as possible to your target
    visitors.
    """
    def all_regions(self):
        """All Regions
        This method will return all the available regions within the
        DigitalOcean cloud.

        Sample Response:
            {"status":"OK",
                "regions":[
                    {"id":1,"name":"New York 1"},
                    {"id":2,"name":"Amsterdam 1"}
                ]
            }


        :return: status and region listing
        :rtype: dictionary
        """

        return self._get_json('/regions')
    #all_regions()

    """Images
    Images are the basic building blocks of droplets. They contain the base
    Operating System and any additional software that has been bundled in.
    DigitalOcean provides a number of pre-built images of the most popular OS
    distributions. And users can take their own snapshots and use them as
    images to spin up new droplets.
    """

    def all_images(self, filter='global'):
        """All Images
        This method returns all the available images that can be accessed by
        your client ID. You will have access to all public images by default,
        and any snapshots or backups that you have created in your own account.

        Sample Response
        {"status":"OK","images":
            [{"id":429,"name":"Real Backup 10242011","distribution":"Ubuntu"},
            {"id":430,"name":"test233","distribution":"Ubuntu"},
            {"id":431,"name":"test888","distribution":"Ubuntu"},
            {"id":442,"name":"tesah22","distribution":"Ubuntu"},
            {"id":443,"name":"testah33","distribution":"Ubuntu"},
            {"id":444,"name":"testah44","distribution":"Ubuntu"},
            {"id":447,"name":"ahtest55","distribution":"Ubuntu"},
            {"id":448,"name":"ahtest66","distribution":"Ubuntu"},
            {"id":449,"name":"ahtest77","distribution":"Ubuntu"},
            {"id":458,"name":"Rails3-1Ruby1-9-2","distribution":"Ubuntu"},
            {"id":466,"name":"NYTD Backup 1-18-2012","distribution":"Ubuntu"},
            {"id":478,"name":"NLP Final","distribution":"Ubuntu"},
            {"id":540,"name":"API - Final","distribution":"Ubuntu"},
            {"id":577,"name":"test1-1","distribution":"Ubuntu"},
            {"id":578,"name":"alec snapshot1","distribution":"Ubuntu"}]}


        :param filter: Optional <global|my_images>
        :type filter: string
        :return: status and available image types listing
        :rtype: dictionary
        """

        return self._get_json('/images', {'filter': filter})
    #all_images()

    def show_image(self, image_id):
        """Show Image
        This method displays the attributes of an image.

        Sample Response:
            {"status":"OK",
                "image":{"id":429,"name":"Real Backup 10242011",
                    "distribution":"Ubuntu"
                }
            }

        :param image_id: Required, this is the id of the image you would like
            to use to rebuild your droplet with
        :type image_id: int
        :return: status
        :rtype: dictionary
        """

        return self._get_json('/images/{}'.format(image_id))
    #show_image()

    def destroy_image(self, image_id):
        """Destroy Image
        This method allows you to destroy an image. There is no way to restore
        a deleted image so be careful and ensure your data is
        properly backed up.

        Sample Response:
            {"status":"OK"}

        :param image_id: Required, this is the id of the image you would like to destroy
        :type image_id: integer
        :return: status
        :rtype: dictionary
        """

        return self._get_json('/images/{}/destroy'.format(image_id))
    #destroy_image()

    """SSH Keys
    SSH keys are public and private keys that allow a secure SSH connection to
    be established to a droplet without using a password.
    This automates login to the droplet - ensure that your private key is
    protected at all times. You only need to share your public key for access.
    """
    def all_ssh_keys(self):
        """All SSH Keys
        This method lists all the available public SSH keys in your account
        that can be added to a droplet.

        Sample Response:
            {"status":"OK","ssh_keys":[
                {"id":10,"name":"office-imac"},
                {"id":11,"name":"macbook-air"}]}

        :return: status and keys list
        :rtype: dictionary
        """

        return self._get_json('/ssh_keys')
    #all_ssh_keys()

    def show_ssh_key(self, ssh_key_id):
        """Show SSH Key
        This method shows a specific public SSH key in your account that can be
        added to a droplet.

        (The key in the response is broken to stay within PEP8 requirements.)
        Sample Response:
        {"status":"OK",
            "ssh_key":{"id":10,"name":"office-imac",
                "ssh_pub_key":"ssh-dss AHJASDBVY6723bgBVhusadkih238723kjLKFnbkj
                GFklaslkhfgBAFFHGBJbju8)H3hnNGjASGFkjgZn86ZCqk02NX3BTcMV4YI2I4/
                sebg8VnuebDn0XUbbmVrAq4YqGiobn86ZCqk02NX3BTcMp4QGmyL4/sebg8Vnus
                ytv93cA2PsXOxvbU0CdebDn0XUbbmVrAq4YqGiob48KzCT/NT6L6VoD5n+jSZvQ
                AAAIAspspAelh4bW5ncO5+CedFZPZn86ZCqk02NX3BTcMV4YIaSCO43Y+ghI2of
                4+E1TDJ1R9Znk9XJsald/U0u0uXwtyHXP2sommNWuAGtzp4QGmyL4/sebg8Vnus
                ytv93cA2PsXOxvbU0CdebDn0XUbbmVrAq4YqGiob48KzCT/NT6L6VoD5n+jSZfl
                FD684gdLsW1+gjVoFBk0MZWuGSXEQyIwlBRq/8jAAAAFQDrxI/h35BewJUmVjid
                8Qk1NprMvQAAAIAspspAelh4bW5ncO5+CedFZPZn86ZCqk02NX3BTcMV4YI2IEz
                b6R2vzZkjCTuZVy6dcH3ag6JlEfju67euWT5yMnT1I0Ow== me@office-imac"
            }
        }

        :param ssh_key_id: ssh key id number
        :type ssh_key_id: integer
        :return: status and key information
        :rtype: dictionary
        """

        return self._get_json('/ssh_keys/{}'.format(ssh_key_id))
    #show_ssh_key()

    def add_ssh_key(self, name, ssh_key_pub):
        """Add SSH Key
        This method allows you to add a new public SSH key to your account.

        (The key in the response is broken to stay within PEP8 requirements.)
        Sample Response:
        {"status":"OK",
            "ssh_key":{"id":47,"name":"my_key",
            "ssh_pub_key":"ssh-dss AAAAB3NzaC1kc3MAAACBAK5uLwicCrFEpaVKBzkWxC7R
            Qn+smg5ZQb5keh9RQKo8AszFTol5npgUAr0JWmqKIHv7nof0HndO86x9iIqNjq3vrz9
            CIVcFfZM7poKBJZ27Hv3v0fmSKfAc6eGdx8eM9UkZe1gzcLXK8UP2HaeY1Y4LlaHXS5
            tPi/dXooFVgiA7AAAAFQCQl6LZo/VYB9VgPEZzOmsmQevnswAAAIBCNKGsVP5eZ+IJk
            lXheUyzyuL75i04OOtEGW6MO5TymKMwTZlU9r4ukuwxty+T9Ot2LqlNRnLSPQUjb0vp
            lasZ8Ix45JOpRbuSvPovryn7rvS7//klu9hIkFAAQ/AZfGTw+696EjFBg4F5tN6MGMA
            6KrTQVLXeuYcZeRXwE5t5lwAAAIEAl2xYh098bozJUANQ82DiZznjHc5FW76Xm1apEq
            sZtVRFuh3V9nc7QNcBekhmHp5Z0sHthXCm1XqnFbkRCdFlX02NpgtNs7OcKpaJP47N8
            C+C/Yrf8qK/Wt3fExrL2ZLX5XD2tiotugSkwZJMW5Bv0mtjrNt0Q7P45rZjNNTag2c=
            user@host"
            }
        }

        :param name: Required, the name you want to give this SSH key.
        :type name: string
        :param ssh_key_pub: Required, the actual public SSH key.
        :type ssh_key_pub: string
        :return: status and key information
        :rtype: dictionary
        """

        return self._get_json('/ssh_keys/new',
                              {'name': name,
                               'ssh_key_pub': ssh_key_pub
                               }
                              )
    #add_ssh_key()

    def edit_ssh_key(self, ssh_key_id, ssh_key_pub):
        """Edit SSH Key
        This method allows you to modify an existing public SSH key in
        your account.

        Sample Response:
            Coming Soon..


        :param ssh_key_id: ssh key id number
        :type ssh_key_id: integer
        :param ssh_key_pub: Required, the actual public SSH key.
        :type ssh_key_pub: string
        :return: status and key information
        :rtype: dictionary
        """

        return self._get_json('/ssh_keys/{}/edit'.format(ssh_key_id),
                              {'ssh_key_pub': ssh_key_pub})
    #edit_ssh_key()

    def destroy_ssh_key(self, ssh_key_id):
        """Destroy SSH Key
        This method will delete the SSH key from your account.

        Sample Response:
            {"status":"OK"}

        :param ssh_key_id: ssh key id number
        :type ssh_key_id: integer
        :return: status
        :rtype: dictionary
        """

        pass
    #destroy_ssh_key()

    """
    Sizes
    Sizes indicate the amount of memory and processors that will be allocated
        to your droplet on creation.
    """
    def all_sizes(self):
        """All Sizes
        This method returns all the available sizes that can be used to
        create a droplet.

        Sample Response;
            {"status":"OK","sizes":[
                {"id":33,"name":"512MB"},
                {"id":34,"name":"1GB"},
                {"id":35,"name":"2GB"},
                {"id":36,"name":"4GB"},
                {"id":37,"name":"8GB"},
                {"id":38,"name":"16GB"}
                ]
            }

        :return: status and a list of available sizes
        :rtype: dictionary
        """

        pass
    #all_sizes()
#APIClient
