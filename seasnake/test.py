#!/usr/bin/env python
# encoding: utf-8

from apiclient import APIClient
from pprint import pprint

CLIENT_ID = 'Z5rK4uhkl7calDsCK67eo'
API_KEY = 'hYAnyXKFYtESVzXq30JnP5hndoemQj9MwNSu7ILKx'


def main():
    cl = APIClient(CLIENT_ID, API_KEY)
    print(cl.get_doc())

    pprint(cl.get_active_droplets())
    pprint(cl.get_droplet(0))
    # pprint(cl.new_droplet(name, size_id, image_id, region_id))
    # pprint(cl.reboot_droplet(droplet_id))
    # pprint(cl.power_cycle_droplet(droplet_id))
    # pprint(cl.power_off_droplet(droplet_id))
# main()

if __name__ == '__main__':
    main()
