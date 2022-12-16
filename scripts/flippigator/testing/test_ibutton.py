import os
import time

import pytest
from termcolor import colored

from flippigator.case import BaseCase

os.system("color")


@pytest.mark.ibutton
class TestGpio(BaseCase):
    def test_ibutton_menu_negative(self, nav):
        nav.ibutton.go_into()
        menu = nav.get_menu_list()
        menu_ref = [
            "Read",
            "Saved",
            "Add Manually",
        ]
        assert menu == menu_ref, "iButton menu list is wrong"
        nav.go_to_main_screen()
