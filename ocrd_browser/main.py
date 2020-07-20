#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from pathlib import Path

BASE_PATH = Path(__file__).absolute().parent.parent
RESOURCE_FILE_NAME = "resources/ocrd-browser.gresource"


def main(arguments):
    from application import OcrdBrowserApplication
    app = OcrdBrowserApplication()
    app.run(arguments)



def install_excepthook():
    """ Make sure we exit when an unhandled exception occurs. """
    old_hook = sys.excepthook
    def new_hook(etype, evalue, etb):
        old_hook(etype, evalue, etb)
        while Gtk.main_level():
            Gtk.main_quit()
        sys.exit()
    sys.excepthook = new_hook




if __name__ == "__main__":
    resources = Gio.resource_load(str(BASE_PATH / RESOURCE_FILE_NAME))
    Gio.resources_register(resources)
    install_excepthook()
    sys.exit(main(sys.argv))