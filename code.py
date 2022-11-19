import sys
import datetime as dt
import sqlite3

from PyQt5 import QtCore, uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox, QTableWidgetItem


class MyWidget(QMainWindow):
    RED = QColor(255, 0, 0)
    PURPLE = QColor(85, 0, 127)
    GREY = QColor(170, 170, 170)
    GREEN = QColor(0, 255, 0)
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('orders.db',
                                    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.create_database()
        uic.loadUi('TaskPlanner.ui', self)  # Загружаем дизайн
        self.initUI()
        self.NewTask_btn.clicked.connect(self.create_task)
        self.NewElement_btn.clicked.connect(self.create_task)
        self.treeWidget.hideColumn(3)
        self.Done_btn.clicked.connect(self.ticked_task)
        self.bin_btn.clicked.connect(self.delete_task)
        self.ok_btn.pressed.connect(self.save_info_frame2)
        self.cancel_btn.pressed.connect(self.save_info_frame2)
        self.treeWidget.itemDoubleClicked.connect(self.show_frame2)
        self.resized.connect(self.change_size)
        self.not_done_btn.clicked.connect(self.not_ticked)
        self.hide_done.clicked.connect(self.hide_done_tasks)
        self.hide_inactive.clicked.connect(self.hide_inactive_tasks)
        self.report_btn.clicked.connect(self.show_frame3)
        self.show_done_tasks_btn.clicked.connect(self.show_report_done_tasks)
        self.close_btn.clicked.connect(self.close_frame3)
        self.task_structure = {}
        self.current_task = None
        self.hide_green_tasks = None
        self.hide_grey_tasks = None
        self.my_format = '%d.%m.%Y %H:%M'
        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.task_status_update)  # По истечении таймера запускается функция task_status_update
        self.timer.start(60000)  # Запуск таймера на 1 минуту
        self.task_status_update()
        self.frame2.hide()
        self.frame3.hide()

    def initUI(self):
        self.setWindowTitle('TaskPlanner')

    def resizeEvent(self, event):
        """
        Переопределение метода базового класса, добавление сигнала изменения размера основного окна.
        """
        self.resized.emit()
        return super(MyWidget, self).resizeEvent(event)

    def hide_inactive_tasks(self):
        """
        При нажатии на "Скрыть неактивные задачи" они становятся невидимыми
        (параметр self.hide_grey_tasks = True). Если при нажатии кнопки будущие задачи итак были
        скрыты, они снова становятся видимыми (параметр self.hide_grey_tasks = False)
        """
        if self.hide_grey_tasks:
            self.hide_grey_tasks = False
        else:
            self.hide_grey_tasks = True
        self.task_status_update()

    def hide_done_tasks(self):
        """
        При нажатии на "Скрыть выполненные задачи" они становятся невидимыми
        (параметр self.hide_green_tasks = True). Если при нажатии кнопки выполненные задачи итак были
        скрыты, они снова становятся видимыми (параметр self.hide_green_tasks = False).
        """
        if self.hide_green_tasks:
            self.hide_green_tasks = False
        else:
            self.hide_green_tasks = True
        self.task_status_update()

    def show_frame3(self):
        self.frame1.hide()
        self.frame3.show()
        self.start_done_task.setDateTime(dt.datetime.now())
        self.finish_done_task.setDateTime(dt.datetime.now())

    def close_frame3(self):
        self.frame3.hide()
        self.frame1.show()

    def show_report_done_tasks(self):
        try:
            start = dt.datetime.strptime(self.start_done_task.text(), self.my_format)
            finish = dt.datetime.strptime(self.finish_done_task.text(), self.my_format)
            tasks = self.cur.execute(
                '''SELECT tr.theme, tm.time_done FROM tree as tr, time as tm WHERE tr.id = tm.task_id AND tm.time_done >= ? AND tm.time_done <= ?''',
                (start, finish)).fetchall()
            self.done_tasks_table.setRowCount(0)
            for i, task in enumerate(tasks):
                self.done_tasks_table.setRowCount(self.done_tasks_table.rowCount() + 1)
                self.done_tasks_table.setItem(i, 0, QTableWidgetItem(task[0]))
                self.done_tasks_table.setItem(i, 1, QTableWidgetItem(
                    dt.datetime.strftime(task[1], self.my_format)))
            self.done_tasks_table.resizeColumnsToContents()
        except Exception as err:
            print(err)

    def not_ticked(self):
        """
        При отмене у задачи статуса "выполненной" функция not_ticked вызывает рекурсивную функцию
        delete_done_status от выбранной задачи и удаляет статус "выполненной" у этой задачи и ее
        предков (если они есть). После отрабатывания функции delete_done_status вызывается
        task_status_update(), чтобы обновить базу данных и дерево.
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            self.delete_done_status(task)
            self.task_status_update()
        except Exception as err:
            print(err)

    def delete_done_status(self, task):
        """
        Удаление у задачи статуса 'выполненная' и рекурсивный вызов функции от ее предка, если он
        был выполнен.
        """
        try:
            self.cur.execute('''UPDATE tree SET status=False WHERE id=?''', (task.text(3),))
            self.cur.execute('''DELETE FROM time WHERE task_id=?''', (task.text(3),))
            self.conn.commit()
            parent = task.parent()
            if parent:
                if self.cur.execute('''SELECT status FROM tree WHERE id=?''',
                                    (parent.text(3),)).fetchall():
                    self.delete_done_status(parent)
        except Exception as err:
            print(err)

    def change_size(self):
        """
        Изменение ширины первого столба в дереве, когда размер окна изменяется.
        """
        self.treeWidget.setColumnWidth(0, self.treeWidget.size().width() -
                                       self.treeWidget.columnWidth(1) * 2)

    def show_frame2(self, item):
        """
        Появление второго окна при двойном клике на задачу. Автоматическое заполнение формы данными
        из дерева и базы данных.
        """
        self.current_task = item
        self.frame2.show()
        self.frame1.hide()
        self.name_frame2.setText(self.current_task.text(0))
        self.start_frame2.setDateTime(
            dt.datetime.strptime(self.current_task.text(1), self.my_format))
        self.finish_frame2.setDateTime(
            dt.datetime.strptime(self.current_task.text(2), self.my_format))
        description = self.cur.execute('''SELECT description FROM tree WHERE id=?''',
                                       (self.current_task.text(3),)).fetchone()
        self.description_frame2.setText(description[0])

    def save_info_frame2(self):
        """
        Если во втором окне пользователь ответил да, после редактирования задачи, то дерево
        заполняется новой информацией и вызывается функция change_task. Если же пользователь ответил
        нет, то второе окно закрывается и возвращается главное окно без изменений.
        """
        try:
            if self.sender().text() == 'ОК':
                self.frame1.show()
                self.frame2.hide()
                print(self.name_frame2.text(), self.start_frame2.text(), self.finish_frame2.text(), self.description_frame2.toPlainText())
                print(self.current_task)
                self.current_task.setText(0, self.name_frame2.text())
                self.current_task.setText(1, self.start_frame2.text())
                self.current_task.setText(2, self.finish_frame2.text())
                self.cur.execute('''UPDATE tree SET description=? WHERE id=?''',
                                 (self.description_frame2.toPlainText(), self.current_task.text(3)))
                self.conn.commit()
                self.change_task(self.current_task)
            else:
                self.frame1.show()
                self.frame2.hide()
        except Exception as err:
            print(err)

    def create_task(self):
        """
        Если была нажата кнопка "Новый подэлемент", то к выбранной задаче добавляется подзадача,
        которая заполняется во втором и третьем столбце текущей датой и следующей датой
        соответственно (переменные start, finish). Даты в дереве преобразованы в строку.
        Новая подзадача сохраняется в базе данных со всеми данными из дерева, а потом четвертый
        столбец дерева (невидимый) заполняется id
        подзадачи из базы данных. Открытие второго окна для редактирования.
        Если пользователь кликнул на кнопку "Новая задача", то к qtreewidget добавляется задача,
        которая заполняется во втором и третьем столбце текущей датой и следующей датой
        соответственно (переменные start, finish). Даты в дереве преобразованы в строку.
        Новая задача сохраняется в базе данных со всеми данными из дерева, а потом четвертый
        столбец дерева (невидимый) заполняется id
        задачи из базы данных. Открытие второго окна для редактирования.
        """
        start = dt.datetime.today()
        finish = dt.datetime.today() + dt.timedelta(days=1)
        if self.sender().text() == 'Новый подэлемент':
            try:
                parent = self.treeWidget.selectedItems()[0]
                if parent:
                    child = QTreeWidgetItem(parent)
                    child.setText(0, 'Новый подэлемент')
                    child.setText(1, dt.datetime.strftime(start, self.my_format))
                    child.setText(2, dt.datetime.strftime(finish, self.my_format))
                    query = self.cur.execute('''INSERT INTO tree(theme, start, finish, parent_id, status) 
                        VALUES(?, ?, ?, ?, ?);''', (
                        child.text(0), start, finish, int(parent.text(3)), False))
                    child.setText(3, str(query.lastrowid))
                    self.conn.commit()
                    self.show_frame2(child)
            except Exception as err:
                print('Выберете задачу')
        elif self.sender().text() == 'Новая задача':
            root = QTreeWidgetItem(self.treeWidget)
            root.setText(0, 'Новая задача')
            root.setText(1, dt.datetime.strftime(start, self.my_format))
            root.setText(2, dt.datetime.strftime(finish, self.my_format))
            query = self.cur.execute(
                '''INSERT INTO tree(theme, start, finish, parent_id, status) 
                VALUES(?, ?, ?, ?, ?);''',
                (root.text(0), start, finish, None, False))
            root.setText(3, str(query.lastrowid))
            self.conn.commit()
            self.show_frame2(root)

    def change_task(self, item):
        """
        Редактирование базы данных изменением данных задач, полученных из второго окна.
        Преобразование дат из строки в объект datetime.
        """
        self.cur.execute('''UPDATE tree SET theme=?, start=?, finish=? WHERE id=?''',
                         (item.text(0), dt.datetime.strptime(item.text(1), self.my_format),
                          dt.datetime.strptime(item.text(2), self.my_format), int(item.text(3))))
        self.conn.commit()
        self.task_status_update()

    def ticked_task(self):
        """
        Вызов рекурсивной функции update_done_status от выбранной задачи при изменении ее
        статуса на "выполненную".
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            self.update_done_status(task)
        except Exception as err:
            print(err)

    def update_done_status(self, task):
        """
        Если у задачи есть потомки, то выполняется проверка, все ли ее подзадачи выполнены. Если нет,
        то высвечивается предупреждение, что не все подзадачи выполнены и функция ничего не
        возвращает. Если все подзадачи выполнены, то задача становится зеленой, в базе данных ее
        статус меняется на "выполненную". Если эта задача является подзадачей другой задачи, то
        вызывается функция all_children_done. Если функция вернула True, то высвечивается
        предложение отметить задачу выполненной. Если ответ да, то функция вызывается от этой задачи.
        """
        try:
            task_id = task.text(3)
            parent = task.parent()
            if task.childCount():
                if not self.all_children_done(task_id):
                    valid = QMessageBox.warning(
                        self, '', "Не все подзадачи выполнены",
                        QMessageBox.Ok)
                    return
            task.setForeground(0, MyWidget.GREEN)
            task.setForeground(1, MyWidget.GREEN)
            task.setForeground(2, MyWidget.GREEN)
            self.cur.execute('''UPDATE tree SET status=True WHERE id=?''', (task_id,))
            self.cur.execute('''INSERT INTO time(task_id, time_done) 
                        VALUES(?, ?);''', (task_id, dt.datetime.now()))
            self.conn.commit()
            if parent:
                if self.all_children_done(parent.text(3)):
                    valid = QMessageBox.question(
                        self, '', "Вы выполнили все подзадачи, отметить задачу выполненной?",
                        QMessageBox.Yes, QMessageBox.No)
                    if valid == QMessageBox.Yes:
                        self.update_done_status(parent)
        except Exception as err:
            print(err)

    def all_children_done(self, task_id):
        """
        Если функция нашла хотя бы одну задачу со статусом "невыполненная", то возвращается False,
        если же нет - True.
        """
        if self.cur.execute('''SELECT id FROM tree WHERE parent_id=? and status=?''',
                            (task_id, False)).fetchone():
            return False
        return True

    def task_status_update(self):
        """
        На основе данных из базы данных создается словарь с ключом-id задачи и значением-словаря,
        в котором ключи: название(значение-строка),
        начало срока (значение-объект datetime), конец срока (значение-объект datetime), id родителя
        (значение-число), дети (значение-список id подзадач), статус (значение-True/False) и описание
        (значение-строка).
        Дерево очищается и заполняется заново на основе словаря. idб начало и конец срока
        преобразуются в строку. Вызывается функция get_color с аргументами - статус, начало и конец
        срока. в полученный цвет окрашивается задача. В зависимости от значения переменных
        hide_green_tasks, hide_grey_tasks и цвета задача становится невидимой (или нет, если она не
        подошла ни под одно условие). Запускается рекурсивная функция add_children от id задачи и ее
        родителя. Запускается таймер на 1 минуту (в миллисекундах).
        """
        print('task_status_update')
        try:
            self.task_structure = {}
            tasks = self.cur.execute('''SELECT * FROM tree''').fetchall()
            self.treeWidget.clear()
            for task in tasks:
                self.task_structure[task[0]] = {'theme': task[1], 'start': task[2],
                                                'finish': task[3],
                                                'parent_id': task[4], 'children': [],
                                                'status': task[5], 'description': task[6]}
                if task[4]:
                    self.task_structure[task[4]]['children'].append(task[0])
            for taskid, task in self.task_structure.items():
                if not task['parent_id']:
                    root = QTreeWidgetItem(self.treeWidget)
                    root.setText(0, task['theme'])
                    root.setText(1, dt.datetime.strftime(task['start'], self.my_format))
                    root.setText(2, dt.datetime.strftime(task['finish'], self.my_format))
                    root.setText(3, str(taskid))
                    color = self.get_color(task['status'], task['start'], task['finish'])
                    for i in range(3):
                        root.setForeground(i, color)
                    if self.hide_green_tasks:
                        if self.task_structure[taskid]['status']:
                            root.setHidden(True)
                    if self.hide_grey_tasks:
                        if self.task_structure[taskid]['start'] > dt.datetime.now():
                            if self.task_structure[taskid]['finish'] > dt.datetime.now():
                                root.setHidden(True)
                    self.add_children(taskid, root)
            self.treeWidget.expandAll()
            self.timer.start(60000)
        except Exception as err:
            print(err)

    def add_children(self, taskid, parent):
        """
        Прохождение по списку "детей" из словаря для заданного ключа и добавление подзадач в дерево.
        Преобразование id, начала и конца срока в строку. Вызов функции get_color от статуса, начала
        и конца срока задачи, получение из нее цвета. В зависимости от значения переменных
        hide_green_tasks, hide_grey_tasks и цвета подзадача становится невидимой (или нет, если она
        не подошла ни под одно условие). Рекурсивный вызов функции от этой подзадачи и ее родителя.
        """
        for ch in self.task_structure[taskid]['children']:
            child_data = self.task_structure[ch]
            child = QTreeWidgetItem(parent)
            child.setText(0, child_data['theme'])
            child.setText(1, dt.datetime.strftime(child_data['start'], self.my_format))
            child.setText(2, dt.datetime.strftime(child_data['finish'], self.my_format))
            child.setText(3, str(ch))
            color = self.get_color(child_data['status'], child_data['start'],
                                   child_data['finish'])
            for i in range(3):
                child.setForeground(i, color)
            if self.hide_green_tasks:
                if self.task_structure[ch]['status']:
                    child.setHidden(True)
            if self.hide_grey_tasks:
                if self.task_structure[ch]['start'] > dt.datetime.now():
                    if self.task_structure[ch]['finish'] > dt.datetime.now():
                        child.setHidden(True)
            self.add_children(ch, child)

    def get_color(self, status, start, finish):
        """
        Если статус задачи True, то возвращается зеленый цвет(задача выполнена),
        если дата начала и конца срока
        задачи меньше сегоднешней даты, то возвращается красный цвет (задача просрочена). Если же
        дата начала срока меньше сегоднешней даты, а конец равен или больше, то возвращается
        фиолетовый цвет (задача активна). Если и начало, и конец срока больше сегоднешней даты, то
        возвращается серый цвет (задача неактивна).
        """
        if status:
            return MyWidget.GREEN
        if start <= dt.datetime.now():
            if finish < dt.datetime.now():
                return MyWidget.RED
            else:
                return MyWidget.PURPLE
        else:
            return MyWidget.GREY

    def delete_task(self):
        """
        Перед удалением задачи или подзадачи высвечивается вопрос с уточнением, точно ли
        пользователь хочет удалить задачу. Если у выбранной задачи есть родитель, то применяется
        removeChild, если нет - takeTopLevelItem. Удаление этой задачи со всеми ее элементами из
        базы данных.
        """
        try:
            task = self.treeWidget.selectedItems()[0]
            parent = task.parent()
            valid = QMessageBox.question(
                self, '', "Вы действительно хотите удалить задачу?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                self.cur.execute('''DELETE FROM tree WHERE id=?''', (task.text(3),))
                self.conn.commit()
                if parent:
                    parent.removeChild(task)
                else:
                    self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(task))
        except Exception as err:
            print('delete', err)

    def create_database(self):
        """
        Создание базы данных (название ее столбцов и принимаемые ими значения).
        """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tree (
    id          INTEGER   PRIMARY KEY AUTOINCREMENT,
    theme       TEXT      NOT NULL,
    start       timestamp,
    finish      timestamp,
    parent_id   INTEGER   REFERENCES tree (id) ON DELETE CASCADE,
    status      BOOLEAN   DEFAULT (False),
    description TEXT
);""")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS time (
    id          INTEGER   PRIMARY KEY AUTOINCREMENT,
    task_id   INTEGER  REFERENCES tree (id) ON DELETE CASCADE,
    time_done timestamp
);''')
        self.conn.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.showMaximized()
    sys.exit(app.exec_())
