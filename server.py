from random import randint
from threading import Thread
from time import sleep
from datetime import datetime,timedelta
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from settings import *


def run_server():
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
        options.binary_location = path
        browser = webdriver.Chrome(options=options, executable_path=EXE_PATH)
        browser.set_window_position(2000, 0)
        browser.set_window_size(900, 1000)

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
        for name in de:
            delite(name)


        # Функция подписки
        def follow(name):
            # добавляем новых подписчиков в базу данных
            def new(name):
                date = datetime.now().__str__().split(' ')[0]
                with open('data/followers.txt', 'a') as f:
                    f.write(name + ':' + date + '\n')
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

if __name__ == "__main__":
    while True:
        try:
            run_server()
        except Exception as e:
            print(e)
        print("Delay: 3600 sec")
        for i in range(3600):
            print(i)
            sleep(1)
