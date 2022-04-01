import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSlot
from random import randint
from threading import Thread
from time import sleep
from datetime import datetime,timedelta
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser


def run_server(path, username, password, n, days, check_old, fix_count):
    def instagram():
    #   функция входа в аккаунт инстаграма
        def login():
            sleep(randint(1, 5) / 10)
            username_input = browser.find_element_by_name('username')
            username_input.clear()
            username_input.send_keys(username)
            sleep(randint(1, 5) / 10)
            password_input = browser.find_element_by_name('password')
            password_input.clear()
            password_input.send_keys(password)
            sleep(randint(1, 5) / 10)
            password_input.send_keys(Keys.ENTER)

        EXE_PATH = r'chromedriver/chromedriver.exe'
        options = Options()
        if path:
            options.binary_location = path
        browser = webdriver.Chrome(options=options, executable_path=EXE_PATH)

        browser.get('https://www.instagram.com/')

        # ждем пока страница загрузится
        def autoDelay(flag, s, name, f):
            sleep(0.5)
            while flag:
                try:
                    if f == 'by_name':
                        browser.find_element_by_name(name)
                    elif f == 'by_tag_name':
                        browser.find_elements_by_tag_name(name)
                    elif f == 'by_xpath':
                        browser.find_element_by_xpath(name)
                    elif f == 'x':
                        pass
                    sleep(s)
                    break
                except Exception:
                    sleep(0.1)

        autoDelay(True, 0, 'username', 'by_name')
        login()
        sleep(4)
        try:
            username_input = browser.find_element_by_name('username')
            if username_input:
                login()
        except Exception:
            pass
            # Сохранить данные
            # autoDelay(True, 0, 'button', 'by_tag_name')
            # for x in browser.find_elements_by_tag_name('button'):
            # if x.get_attribute('innerText') == 'Сохранить данные':
            # x.click()
        print('Login confirmed')
        while thread1.is_alive():
            # ждем результат работы функции init()
            # результатом будет переменная de
            # global de-список старых подписчиков
            sleep(0.1)

        # Функция удаления
        print('del')
        def delite(name):
            try:
                flag = False
                profile_url = 'https://www.instagram.com/' + name
                browser.get(profile_url)
                autoDelay(True, 0.5, 'button', 'by_tag_name')
                try:
                    for x in browser.find_elements_by_tag_name('span'):
                        if x.get_attribute('aria-label') == 'Подписки':
                            x.click()
                            flag = True
                except Exception:
                    pass
                try:
                    for x in browser.find_elements_by_tag_name('button'):
                        if x.get_attribute('innerText') == 'Запрос отправлен':
                            x.click()
                            flag = True
                except Exception:
                    pass
                try:
                    un_link = browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/span')
                    un_link.click()
                    if un_link:
                        flag = True
                except Exception:
                    pass
                # подтверждаем отписку
                autoDelay(flag, 0, '/html/body/div[5]/div/div/div/div[3]/button[1]', 'by_xpath')
                print(name)
                accept = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
                accept.click()
            except Exception:
                pass

        # Удаляем старых
        de.reverse()
        for name in de:
            delite(name)

        # добавляем новых подписчиков в базу данных
        def new(name):
            date = datetime.now().__str__().split(' ')[0]
            with open('data/followers.txt', 'a') as f:
                f.write(name + ':' + date + '\n')

        # Функция подписки
        def follow(name):
            try:
                profile_url = 'https://www.instagram.com/' + name
                browser.get(profile_url)
                autoDelay(True, 0.5, 'button', 'by_tag_name')
                for b in browser.find_elements_by_tag_name('button'):
                    # if (b.get_attribute('innerText') == 'Подписаться в ответ' or b.get_attribute('innerText') == 'Подписаться') and b.location.get('y')<120:
                    if 'Подписаться' in b.get_attribute('innerText') and b.location.get('y') < 120:
                        b.click()
                        new(name)
            except Exception:
                pass

        # лайки
        def like():
            try:
                likes = []
                hrefs = []
                sleep(0.5)
                for link in browser.find_elements_by_tag_name('a'):
                    if '/p/' in link.get_attribute('href'):
                        hrefs.append(link)

                for i in range(randint(4, 5) if len(hrefs) > 4 else len(hrefs)):
                    likes.append(hrefs[i].get_attribute('href'))

                for m in likes:
                    browser.get(m)
                    sleep(0.5)
                    autoDelay(True, 0.2, 'svg', 'by_tag_name')
                    try:
                        for cl in browser.find_elements_by_tag_name('button'):
                            if '<svg aria-label="Нравится"' in cl.get_attribute('innerHTML'):
                                if 'width="24"' in cl.get_attribute('innerHTML'):
                                    cl.click()
                                    sleep(0.5)
                    except Exception:
                        pass

            except Exception:
                pass

        # подписываемся на новых
        print('new')
        [follow(x) for x in ne]
        count = n - c if n >= c else 0
        count = n if fix_count else count
        for i in range(count):
            name = ''
            browser.get('https://www.instagram.com/explore/people/suggested/')
            autoDelay(True, 2, 'a', 'by_tag_name')
            for x in browser.find_elements_by_tag_name('a'):
                name = x.get_attribute('innerText')
                if name == x.get_attribute('Title'):
                    if name not in use:
                        use.append(name)
                        follow(name)
                        print(i + 1, name)
                        like()
                        break

        browser.close()
        browser.quit()

    def init():
        print(datetime.now().__str__().split('.')[0])
        global c, de, use, ne
        d = {}
        de = []
        use = []
        ne = []

        with open('data/followers.txt') as f:
            a = f.readlines()

        with open('data/old.txt', "r") as f:
            [de.append(x) for x in f if check_old]

        for x in a:
            s = x.split(':')[1].strip()
            m = datetime(int(s.split('-')[0]), int(s.split('-')[1]), int(s.split('-')[2]))
            d.update({x.split(':')[0]: s})
            if m + timedelta(days=days) < datetime.now():
                de.append(x.split(':')[0])

        with open('data/old.txt', "r") as f:
            [use.append(x) for x in f]

        with open('data/old.txt', "a") as f:
            [f.write(x + '\n') for x in de]

        with open('data/new.txt', "r") as f:
            [ne.append(x) for x in f]

        with open('data/de.txt', "r") as f:
            [de.append(x) for x in f]

        with open('data/de.txt', "w") as f:
            pass

        with open('data/followers.txt', 'w') as f:
            for x in d:
                if not (x.split(':')[0] in de):
                    f.write(x + ':' + d.get(x) + '\n')
                    use.append(x)

        print('count of extra followers: ', len(d), ' old: ', len(de))
        c = len(d)


    thread1 = Thread(target=init)
    thread2 = Thread(target=instagram)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def start(path, username, password, n, days, time, check_old, fix_count):
    while True:
        try:
            run_server(path, username, password, n, days, check_old, fix_count)
        except Exception as e:
            print(e)
        print("Delay: "+str(time)+ "sec")
        for i in range(time):
            print(i)
            sleep(1)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Start', self)
        self.bp = QPushButton('   open', self)
        self.bm = QPushButton('>>', self)
        self.bs = QPushButton('💾', self)
        self.initUI()

    def initUI(self):
        data = []
        with open('data.bio', "r") as f:
            [data.append(x) for x in f]

        self.label_login =QLabel(self)
        self.label_login.setText("Login:")
        self.label_login.move(30, 23)

        self.label_pass = QLabel(self)
        self.label_pass.setText("Password:")
        self.label_pass.move(30, 55)

        self.label_e = QLabel(self)
        self.label_e.setText("* For advanced users only !")
        self.label_e.move(160, 290)

        self.label_d = QLabel(self)
        self.label_d.setText(" * Days before deletion:")
        self.label_d.move(30, 100)

        self.label_n = QLabel(self)
        self.label_n.setText(" * Number of followers:")
        self.label_n.move(30, 130)

        self.label_t = QLabel(self)
        self.label_t.setText(" * Interval in seconds:")
        self.label_t.move(30, 160)

        self.label_o = QLabel(self)
        self.label_o.setText(" * Check old followers:")
        self.label_o.move(30, 190)

        self.label_c = QLabel(self)
        self.label_c.setText("Path to chrome.exe:")
        self.label_c.move(30, 225)

        self.textbox_login = QLineEdit(self)
        self.textbox_login.move(100, 20)
        self.textbox_login.resize(180, 23)

        self.textbox_pass = QLineEdit(self)
        self.textbox_pass.move(100, 50)
        self.textbox_pass.resize(180, 23)

        self.textbox_d = QLineEdit(self)
        self.textbox_d.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.textbox_d.setText("2")
        self.textbox_d.move(150, 95)
        self.textbox_d.resize(50, 23)

        self.textbox_n = QLineEdit(self)
        self.textbox_n.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.textbox_n.setText("20")
        self.textbox_n.move(150, 125)
        self.textbox_n.resize(50, 23)

        self.textbox_t = QLineEdit(self)
        self.textbox_t.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.textbox_t.setText("3600")
        self.textbox_t.move(150, 155)
        self.textbox_t.resize(50, 23)

        self.checkbox_o = QCheckBox(self)
        self.checkbox_o.move(167, 190)

        self.textbox_path = QLineEdit(self)
        self.textbox_path.move(130, 220)
        self.textbox_path.resize(110, 23)

        self.bp.move(229, 219)
        self.bp.resize(50, 24)

        self.btn.setToolTip('Start!')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(115, 260)

        self.bs.setToolTip('Save')
        self.bs.resize(24, 24)
        self.bs.move(15, 260)

        self.bm.setToolTip('Get chromedriver')
        self.bm.resize(40,23)
        self.bm.move(250, 317)

        s = '<a href="https://chromedriver.storage.googleapis.com/index.html">&nbsp;Download the cromedriver' \
            ' of the same version <br>as your google chrome and replace it in the folder</a>'
        self.label_s = QLabel(self)
        self.label_s.setText(s)
        self.label_s.move(7, 315)

        self.textbox_login.setText(data[0])
        self.textbox_pass.setText(data[1])
        self.textbox_path.setText(data[2])

        self.setGeometry(700, 500, 300, 350)
        self.setWindowTitle('Instagram bot server')
        self.show()

        self.btn.clicked.connect(self.on_click)
        self.bs.clicked.connect(self.on_save)
        self.bp.clicked.connect(self.file_dialog)
        u='https://chromedriver.storage.googleapis.com/index.html'
        self.bm.clicked.connect(lambda: webbrowser.open(u))

    def file_dialog(self):
        f = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.textbox_path.setText(f)
        print('f')

    def on_click(self):
        #path= 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        path = self.textbox_path.text()
        username = self.textbox_login.text()
        password = self.textbox_pass.text()
        n = int(self.textbox_n.text())
        days = int(self.textbox_d.text())
        time = int(self.textbox_t.text())
        check_old = True if self.checkbox_o.checkState()==2 else False
        print(check_old)
        fix_count = True
        start(path, username, password, n, days, time, check_old, fix_count)

    def on_save(self):
        data = [self.textbox_login.text(), self.textbox_pass.text(), self.textbox_path.text()]
        with open('data.bio', "w") as f:
            [f.write(str(x)) for x in data]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()

    sys.exit(app.exec_())