from PyQt6.QtWidgets import *
from Vote_Menu_GUI import *
import csv

class Logic(QMainWindow, Ui_GUI_Vote_Menu):
    id_list = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("VOTE MENU")
        self.blank_label()
        self.blank_total()
        self.blank_id()


    def vote_id(self):
        id = self.get_id()
        if id in self.id_list:
            self.error()
            self.label_message.setText("ID already voted")
            self.blank_id()
        else:
            self.id_list.append(id)

    def vote(self):
        self.vote_id()
        candidate = self.dropBox_candidates
        if candidate is not None:
            with(open("Voting Results.csv", "a+")) as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.get_id(), candidate])
            self.label_message.setText(f"Voted for {candidate}")

    def get_id(self):
        try:
            id = int(self.lineEdit_voter_id.text())
        except(ValueError):
            self.error()
            self.label_message.setText("Please enter a valid Voter ID")
            self.blank_id()


    def error(self):
        self.label_message.setStyleSheet("color: red")

    def blank_id(self):
        self.lineEdit_voter_id.setText("")
    def blank_label(self):
        self.label_message.setText("")
    def blank_total(self):
        self.label_total.setText("")