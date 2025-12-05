from PyQt6.QtWidgets import *
from Vote_Menu_GUI import *
import csv

class Logic(QMainWindow, Ui_GUI_Vote_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("VOTE MENU")

    def vote_id(self):
        id_list = []
        try:
            id = int(self.lineEdit_voter_id.text())
        except(ValueError):
            self.error()
            self.label_message.setText("Please enter a valid Voter ID")
            self.lineEdit_voter_id.setText("")
        if id in id_list:
            self.error()
            self.label_message.setText("ID already voted")
            self.lineEdit_voter_id.setText("")

    def vote(self):
        candidate = self.dropBox_candidates



    def error(self):
        self.label_message.setStyleSheet("color: red")