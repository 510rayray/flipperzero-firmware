import os
import time

import pytest
from termcolor import colored

from flippigator.case import BaseCase

os.system("color")


@pytest.mark.subghz
class TestSubGhz(BaseCase):
    def test_subghz_menu_negative(self, nav):
        nav.subghz.go_into()
        menu = nav.get_menu_list()
        menu_ref = [
            "Read",
            "Read RAW",
            "Saved",
            "Add Manually",
            "Frequency Analyzer",
            "Test",
        ]
        assert menu == menu_ref, "Sub-GHz menu list is wrong"
        nav.go_to_main_screen()
