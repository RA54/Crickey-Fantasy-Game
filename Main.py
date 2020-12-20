from points_calculator import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from open import Ui_Dialog as Open  # importing open window dialogbox
from new import Ui_Dialog as New  # importing new window dialogbox
from neweva import Ui_MainWindow as Eva  # importing evaluate window

import sqlite3
import logging

fant = sqlite3.connect('fandatabase.db')  # connecting to database file(fandatabase.db)
fantcurs = fant.cursor()
logging.basicConfig(level=logging.INFO)

class Ui_MainWindow(object):
    def __init__(self):
        # INITIALISING WINDOWS
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

        # FILE OPENING MENU

    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

        # EVALUATE TEAM MENU

    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

    # NEW FILE MENU
    def file_new(self):
        self.newDialog.show()

    def setupUi(self, MainWindow):
        # INITIALISING POINTS AND COUNTS
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0

        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  # batsman nameslist
        self.c = []  # allrounder names list
        self.d = []  # wicketer names list
        self.list1 = []  # selectedplayer's list

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 230, 691, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.selectedplayers_lw = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.selectedplayers_lw.setObjectName("selectedplayers_lw")
        self.gridLayout.addWidget(self.selectedplayers_lw, 0, 4, 1, 1)
        self.availplayers_lw = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.availplayers_lw.setFlow(QtWidgets.QListView.TopToBottom)
        self.availplayers_lw.setLayoutMode(QtWidgets.QListView.Batched)
        self.availplayers_lw.setObjectName("availplayers_lw")
        self.gridLayout.addWidget(self.availplayers_lw, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 691, 141))
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 109, 691, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bat_rb = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout.addWidget(self.bat_rb)
        self.bow_rb = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.bow_rb.setObjectName("bow_rb")
        self.horizontalLayout.addWidget(self.bow_rb)
        self.wk_rb = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout.addWidget(self.wk_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout.addWidget(self.ar_rb)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 691, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bowlcount = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bowlcount.setObjectName("bowlcount")
        self.gridLayout_2.addWidget(self.bowlcount, 0, 1, 1, 1)
        self.alrcount = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.alrcount.setObjectName("alrcount")
        self.gridLayout_2.addWidget(self.alrcount, 0, 3, 1, 1)
        self.wicketcount = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.wicketcount.setObjectName("wicketcount")
        self.gridLayout_2.addWidget(self.wicketcount, 0, 2, 1, 1)
        self.batcount = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.batcount.setObjectName("batcount")
        self.gridLayout_2.addWidget(self.batcount, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 91, 16))
        self.label_2.setObjectName("label_2")
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(110, 210, 55, 16))
        self.points_available.setObjectName("points_available")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 210, 71, 16))
        self.label_8.setObjectName("label_8")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(500, 210, 55, 16))
        self.points_used.setObjectName("points_used")
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(160, 0, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.team_name.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name.setObjectName("team_name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 26))
        self.menubar.setObjectName("menubar")
        self.menu_Manage_Team = QtWidgets.QMenu(self.menubar)
        self.menu_Manage_Team.setObjectName("menu_Manage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_Manage_Team.addAction(self.actionNew_Team)
        self.menu_Manage_Team.addSeparator()
        self.menu_Manage_Team.addAction(self.actionOpen_Team)
        self.menu_Manage_Team.addSeparator()
        self.menu_Manage_Team.addAction(self.actionSave_Team)
        self.menu_Manage_Team.addSeparator()
        self.menu_Manage_Team.addAction(self.actionEvaluate_Team)
        self.menu_Manage_Team.addSeparator()
        self.menu_Manage_Team.addAction(self.actionExit)
        self.menu_Manage_Team.addSeparator()
        self.menubar.addAction(self.menu_Manage_Team.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # DOUBLE CLICK
        self.availplayers_lw.itemDoubleClicked.connect(self.removelist1)
        self.selectedplayers_lw.itemDoubleClicked.connect(self.removelist2)

        # -----stats of player
        self.stats = {}

        self.new_screen.savename.clicked.connect(self.namechange)

        # RADIOBUTTONS  CLICK
        self.bat_rb.clicked.connect(self.load_names)
        self.wk_rb.clicked.connect(self.load_names)
        self.bow_rb.clicked.connect(self.load_names)
        self.ar_rb.clicked.connect(self.load_names)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ">"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.bowlcount.setText(_translate("MainWindow", "Bowlers(Bow)  ##"))
        self.alrcount.setText(_translate("MainWindow", "Allrounders(AR) ##"))
        self.wicketcount.setText(_translate("MainWindow", "WicketKeeper(WK)  ##"))
        self.batcount.setText(_translate("MainWindow", "Batsmen(Bat)  ##"))
        self.label_2.setText(_translate("MainWindow", "Point Available"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.label_8.setText(_translate("MainWindow", "Point used"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.team_name.setText(_translate("MainWindow", " TEAM NAME "))
        self.menu_Manage_Team.setTitle(_translate("MainWindow", "    Manage Team"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))



    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT name FROM teams")
        l = fantcurs.fetchall()
        for i in l:
            logging.debug('team names',i)
            if i[0] == teamname:
                logging.debug('inder same name')
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText(self.tname)
            self.newDialog.close()

    # TO RESET ALL COUNTS AND LISTS
    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.selectedplayers_lw.clear()

        # SAVE TEAM MENU

    def file_save(self):
        if not self.error():  # IF THERE IS AN ERROR
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(' 😪Insufficient Players OR Points !!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
        elif self.error():  # IF NO ERROR
            try:
                fantcurs.execute("SELECT DISTINCT name FROM teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:  # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        logging.debug('Updating already there')
                        fantcurs.execute(
                            "DELETE  FROM teams WHERE name='" + self.team_name.text() + "';")  # DELETING TO UPDATE TEAM
            except:
                logging.debug('error')
            for i in range(self.selectedplayers_lw.count()):
                logging.debug('----addding--')
                logging.debug('teamnane: ',self.team_name.text())
                logging.debug('playername: ',self.list1[i])
                logging.debug('points: ', player_points[self.list1[i]])
                try:
                    fantcurs.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))


                except:
                    logging.debug('error in operation!')
            fant.commit()
            self.file_evaluate()
        else:
            logging.debug('---error in operation')

    # QUITING METHOD
    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText(' Bye 😙')
        msg.setWindowTitle("Fantasy Cricket")
        msg.exec_()
        logging.debug('exit')
        sys.exit()

    # ON RADIOBUTTONS CLICKED
    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT player,value from stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,value from stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,value from stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,value from stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.availplayers_lw.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.availplayers_lw.addItem(item)

    def removelist1(self, item):  # REMOVE FROM AVAILABLE PLAYERS AND ADD TO SELECTED PLAYERS
        self.conditions_1(item.text())
        self.availplayers_lw.takeItem(self.availplayers_lw.row(item))
        self.selectedplayers_lw.addItem(item.text())
        self.totalcount = self.selectedplayers_lw.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):  # Adding and Deducting respective points from points_calculator.py
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    def conditions_2(self, cat):  # Adding and Deducting respective poinrs from points_calculator.py
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.bowlcount.setText(str(self.bowlerscount))
        self.batcount.setText(str(self.batsmencount))
        self.alrcount.setText(str(self.alrdscount))
        self.wicketcount.setText(str(self.wicketerscount))

    def removelist2(self, item):  # REMOVE FROM SELECTED PLAYERS AND ADD TO AVAIALBLE PLAYERS
        self.selectedplayers_lw.takeItem(self.selectedplayers_lw.row(item))
        self.availplayers_lw.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.selectedplayers_lw.count()
        self.conditions_2(item.text())

    def openteam(self):  # upon open team selected
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT players from teams WHERE name= '" + teamname + "';")
        x = fantcurs.fetchall()
        score = []
        for i in x:
            fantcurs.execute("SELECT value from stats WHERE player='" + i[0] + "';")
            y = fantcurs.fetchone()
            score.append(y[0])
        logging.debug(score)
        sum = 0
        for i in score:
            sum += i
        self.selectedplayers_lw.clear()
        self.load_names()
        for i in x:
            self.selectedplayers_lw.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)

    def error(self):  # Handling and displaying error messages
        msg = QMessageBox()
        if self.avail_points <= 0:
            self.points_available.setText('0')
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough points!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Only 1 wicketkeeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        if self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No more than 11 players allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            logging.debug('available points',self.avail_points)
            return 0
        if self.totalcount < 11:
            return 0
        if self.wicketerscount < 1:
            return 0
        return 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
