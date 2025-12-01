from PyQt6.QtWidgets import QMainWindow

from Vote_Menu_GUI import *
from candidate_menu_gui import *
import csv

class Logic(Ui_GUI_Vote_Menu, Ui_Dialog_Candidate_Menu):
    def __init__(self):
        Ui_GUI_Vote_Menu.__init__(self)
        Ui_Dialog_Candidate_Menu.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("VOTE MENU")

    def vote(self):
        in_label = str(self.line_v_x.text().strip()).lower()

        if in_label is not None:
            if in_label == "x":
                ##Close window
                pass
            elif in_label == "v":
                ##Close Vote_menu
                ##Open Candidate_Menu
                pass