#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#
# Imports
#
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import object
import sys
import xbmc

from resources.lib.dumpert_const import SEARCH_URL_PART_2, SEARCH_URL_PART_3, INITIAL_PAGE_NUMBER, LANGUAGE, \
    log, convertToUnicodeString


#
# Main class
#
class Main(object):
    #
    # Init
    #
    def __init__(self):
        # Get the command line arguments
        # Get the plugin url in plugin:// notation
        self.plugin_url = sys.argv[0]
        # Get the plugin handle as an integer number
        self.plugin_handle = int(sys.argv[1])

        # Get search term from user
        keyboard = xbmc.Keyboard('', LANGUAGE(30508))
        keyboard.doModal()

        if keyboard.isConfirmed():
            search_term = keyboard.getText()
            # If the user has entered nothing, we stop
            if search_term == "":
                sys.exit(0)
        else:
            # If the user cancels the input box, we stop
            sys.exit(0)

        sys.argv[2] = convertToUnicodeString(sys.argv[2])

        # Converting URL argument to proper query string like "https://post.dumpert.nl/api/v1.0/search/fiets/0/?order=date&media_type=all&app=www.dumpert.nl"
        sys.argv[2] = sys.argv[2] + search_term + SEARCH_URL_PART_2 + INITIAL_PAGE_NUMBER + SEARCH_URL_PART_3

        log("sys.argv[2]", sys.argv[2])

        import resources.lib.dumpert_json as plugin

        plugin.Main()
