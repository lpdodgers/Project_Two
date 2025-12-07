from PyQt6.QtWidgets import *
from Vote_Menu_GUI import *
import csv

class Logic(QMainWindow, Ui_GUI_Vote_Menu):
    def __init__(self) -> None:
        """
        Description: Initialize the main window,
        Creates a new list of used IDs,
        Creates the candidate list,
        Initializes the vote count,
        Links the buttons with their functions,
        Creates the csv file and labels inputs
        """
        super().__init__()
        self.setupUi(self)

        self.id_list = []
        self.cand_dict = {"SZA" : 0,
                          "Sabrina Carpenter" : 0,
                          "Timothee Chalamet" : 0,
                          "Kendrick Lamar" : 0,
                          "John Cena" : 0,
                          "Scarlett Johansson" : 0}
        self.lit = ""
        self.count = 0

        self.setWindowTitle("VOTE MENU")
        self.blank_label()
        self.blank_total()
        self.blank_id()

        self.Button_Submit.clicked.connect(self.vote)
        self.Button_exit.clicked.connect(self.exit)
        with(open("Voting Results.csv", "w+")) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Voter ID", "Candidate"])


    def vote(self) -> None:
        """
        Description: Gets voter id,
        Retrieves candidate,
        Ensures valid voter ID and candidate,
        Appends existing csv file,
        Calls confirmation,
        Handles Candidate/ID Errors through error calling
        """
        valid = self.vote_id()
        candidate = self.get_candidate()
        if valid and candidate != "":
            with(open("Voting Results.csv", "a+")) as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.get_id(), candidate])
            self.valid()
        else:
            if valid is False:
                self.prev_vote_error()
            elif candidate == "":
                self.candidate_error()
            else:
                self.invalid_error()

    def vote_id(self) -> bool | None:
        """
        Description: Sorts what kind of ID is being used
        :return: Type of vote id
        """
        id = self.get_id()
        if id is None:
            return None
        elif id in self.id_list:
            return False
        else:
            return True


    def get_id(self) -> int | None:
        """
        Description: Gets voter ID from user input (LineEdit),
        Passes along int if valid, returns None if not valid
        :return: The voter ID or None which will raise error
        """
        try:
            in_id = int(self.lineEdit_voter_id.text())
            if in_id <= 0:
                return None
            else:
                return in_id
        except ValueError:
            return None

    def get_candidate(self) -> str:
        """
        Description: Retrieves candidate name
        :return: User selected candidate
        """
        return str(self.dropBox_candidates.currentText())


    def invalid_error(self) -> None:
        """
        Description: Changes label to provide an error message for an invalid ID in red text
        """
        self.label_message.setStyleSheet("color: red")
        self.label_message.setText("Please enter a valid Voter ID")
        self.blank_id()

    def candidate_error(self) -> None:
        """
        Description: Changes label to provide an error message for an invalid candidate in red text
        """
        self.label_message.setStyleSheet("color: red")
        self.label_message.setText("Please select a valid Candidate")
        self.dropBox_candidates.setCurrentIndex(0)
        self.dropBox_candidates.hidePopup()

    def prev_vote_error(self) -> None:
        """
        Description: Changes label to provide an error message for an already used ID in red text
        """
        self.label_message.setStyleSheet("color: red")
        self.label_message.setText("ID has already voted")
        self.blank_id()


    def blank_id(self) -> None:
        """
        Description: Blanks out the lineEdit
        """
        self.lineEdit_voter_id.setText("")

    def blank_label(self) -> None:
        """
        Description: Blanks out the message label
        """
        self.label_message.setText("")

    def blank_total(self) -> None:
        """
        Description: Blanks out the total label
        """
        self.label_total.setText("")

    def blank_candidate(self) -> None:
        """
        Description: Blanks out the candidate drop menu,
        Sets the drop to the empty/first selection
        """
        self.dropBox_candidates.setCurrentIndex(0)
        self.dropBox_candidates.hidePopup()

    def valid(self) -> None:
        """
        Description: Adds vote to total candidate's vote,
        Updates the message label to display Candidate voted for in green,
        Stores ID used by voter,
        Updates total count of votes,
        Clears lineEdit and candidate list
        """
        self.cand_dict[self.get_candidate()] += 1
        self.label_message.setStyleSheet("color: green")
        self.label_message.setText(f"Voted for {self.get_candidate()}")
        self.id_list.append(self.get_id())
        self.count += 1
        self.blank_id()
        self.blank_candidate()

    def exit(self) -> None:
        """
        Description: Changes colour of total label to blue,
        Displays vote totals of all candidates,
        Hides all other inputs and labels except confirmation of vote and totals
        """
        self.label_total.setStyleSheet("color: blue")
        for i in self.cand_dict:
            self.lit += f'{i}: {self.cand_dict[i]}\n'
        self.label_total.setText(f"Total: {self.count}\n{self.lit}")
        self.Button_Submit.hide()
        self.label_voter_id.hide()
        self.lineEdit_voter_id.hide()
        self.Button_exit.hide()
        self.dropBox_candidates.hide()