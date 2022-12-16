import os
import time

import pytest
from termcolor import colored

from flippigator.case import BaseCase

os.system("color")


@pytest.mark.infrared
class TestInfrared(BaseCase):
    def test_infrared_menu_negative(self, nav):
        nav.infrared.go_into()
        menu = nav.get_menu_list()
        menu_ref = [
            "Universal Remotes",
            "Learn New Remote",
            "Saved Remotes",
            "Debug",
        ]
        assert menu == menu_ref, "Infrared menu list is wrong"
        nav.go_to_main_screen()
