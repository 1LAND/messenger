from kivymd.app import MDApp

from kivymd.uix.button import *
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager,SlideTransition as Transition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label

from kivy.core.window import Window

sys = {'mes':[],'connect':False}

class MainApp(MDApp):
    app_language = 'en'
    language = {'en':
            {
                'main_btn1':'Home','main_btn2':'Account','main_btn3':'Contacts','main_btn4':'Setting',
                'singIn_header':'Sing In','singIn_input1':'Login','singIn_input2':'Password','singIn_btn1':'Sing In','singIn_btn2':'Registration',
                'shat_input1':'Message',
                'setting_btn1_1':'Light','setting_btn1_2':'Dark','setting_btn2':'Colors app','setting_btn3':'Another account?','setting_btn4':'EN'
            },
            'rus':
            {
                'main_btn1':'Главный','main_btn2':'Аккаунт','main_btn3':'Контакты','main_btn4':'Настройки',
                'singIn_header':'Войти','singIn_input1':'Авторизоваться','singIn_input2':'Пароль','singIn_btn1':'Войти','singIn_btn2':'Регестрация',
                'shat_input1':'Сообщение',
                'setting_btn1_1':'Светло','setting_btn1_2':'Темно','setting_btn2':'Тема приложения','setting_btn3':'Другой аккаунт?','setting_btn4':'RUS'
            }
        }
    class SingInScreen(MDScreen):
        def on_sing_in(self):
            if (login := main.ids.front.children[1].children[0].children[-1].text) and (password := main.ids.front.children[1].children[0].children[-2].text):
                if login.strip() != '' and password.strip() != '':
                    if len(login)>5 and len(password)>8:
                        sys['login']=login
                        sys['password']=password             
                        main.ids.backdrop.open(0)
                        app.clear(main.ids.front,text=True)
                        return 0
            main.ids.front.children[1].children[0].children[-1].error = True
    class ShatScreen(MDScreen):
        def message(self,type:bool,message:str,**args) -> object:
            box,text = MDBoxLayout(padding='10dp'),MDLabel(adaptive_size=True,theme_text_color="Custom",text_color=[1,1,1,1])
            box.size_hint=(None,None)
            if type:
                box.md_bg_color=(.9, .5, .5, .9)
                box.radius=[12,12,0,12]
                box.pos_hint={'right':1}
            else:
                box.md_bg_color=app.theme_cls.primary_light if app.theme_cls.theme_style == "Dark" else app.theme_cls.primary_dark
                box.radius=[12,12,12,0]     
            box.width = len(message)*20+20
            box.height = text.height
            text.size_hint=[1,1]
            if box.width > (w := Window.width*.8): 
                box.width = w
                x = round((w-20)/20)/20
                box.height = box.height*x
            text.text = message    
            box.add_widget(text)
            if 'type' in args:
                return type
            sys['mes'].append(box)
            return box
        def create_message(self,type:bool,message:str):   
            if not message:
                return 0
            message_object = self.message(type,message)
            self.ids.box.add_widget(message_object)     
            self.ids.box.height = self.ids.box.height + message_object.height + 5
            self.ids.text_message.text = ''
    class SettingScreen(MDScreen):
        i = 0
        def theme_style_message(self):
            try:
                for i in range(len(sys['mes'])):
                    sys['mes'][i].md_bg_color = app.theme_cls.primary_light if app.theme_cls.theme_style == "Dark" else app.theme_cls.primary_dark
            except:
                pass        
        def theme_style(self):
            style=['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
            if self.i == len(style):
                self.i = 0
            app.theme_cls.primary_palette = style[self.i]
            self.i = self.i + 1
            self.theme_style_message()
        def swith_app_language(self):
            app.app_language = 'rus' if app.app_language == 'en' else 'en'
            #main.ids.backdrop.header_text = app.language['en']['singIn_header'] if  app.app_language == 'en' else app.language['rus']['singIn_header']
            main.ids.btn1.text = app.language['en']['main_btn1'] if  app.app_language == 'en' else app.language['rus']['main_btn1']
            main.ids.btn2.text = app.language['en']['main_btn2'] if  app.app_language == 'en' else app.language['rus']['main_btn2']
            main.ids.btn3.text = app.language['en']['main_btn3'] if  app.app_language == 'en' else app.language['rus']['main_btn3']
            main.ids.btn4.text = app.language['en']['main_btn4'] if  app.app_language == 'en' else app.language['rus']['main_btn4']
            singin.ids.login.hint_text = app.language['en']['singIn_input1'] if  app.app_language == 'en' else app.language['rus']['singIn_input1']
            singin.ids.password.hint_text = app.language['en']['singIn_input2'] if app.app_language == 'en' else app.language['rus']['singIn_input2']
            singin.ids.btn1.text = app.language['en']['singIn_btn1'] if app.app_language == 'en' else app.language['rus']['singIn_btn1']
            singin.ids.btn2.text = app.language['en']['singIn_btn2'] if app.app_language == 'en' else app.language['rus']['singIn_btn2'] +'*'
            shat.ids.text_message.hint_text = app.language['en']['shat_input1'] if app.app_language == 'en' else app.language['rus']['shat_input1']
            setting.ids.btn1.text = app.language['en']['setting_btn1_1'] if app.app_language == 'en' else app.language['rus']['setting_btn1_1']
            setting.ids.btn2.text = app.language['en']['setting_btn2'] if app.app_language == 'en' else app.language['rus']['setting_btn2']
            setting.ids.btn3.text = app.language['en']['setting_btn3'] if app.app_language == 'en' else app.language['rus']['setting_btn3']
            setting.ids.btn4.text = app.language['en']['setting_btn4'] if app.app_language == 'en' else app.language['rus']['setting_btn4']
    class ContactsScreen(MDScreen):
        #def swap_color(self):
        #    сontacts.ids.magnify.text_color = app.theme_cls.primary_dark if сontacts.ids.magnify.text_color != app.theme_cls.primary_dark else [1,1,1,1] if app.theme_cls.theme_style == "Dark" else [0,0,0,1]
        ...
    class MainScreen(MDScreen):
        pass
    back = None
    front = None
    def add(self,place:bool,item:str):
        if place:
            if item == 'setting' and self.back != item:
                self.clear(main.ids.back)
                main.ids.back.add_widget(setting)
                self.back = item
            elif item == 'сontacts' and self.back != item:
                self.clear(main.ids.back)
                main.ids.back.add_widget(сontacts)
                self.back = item    
            elif item == 'home' and self.back != item:
                self.clear(main.ids.back)
                #if sys['connect']:
                #    if data := client.recv(1024).decode('utf-8'):
                #        main.ids.back.add_widget(Label(text=data,md_bg_color=app.theme_cls.bg_dark))
                self.back = item 
            elif item == 'account' and self.back != item:
                self.clear(main.ids.back)    
        else:
            if item == 'shat' and self.front != item:
                self.clear(main.ids.front,text=True)
                main.ids.front.add_widget(shat)
                self.back = item
            elif item == 'singin' and self.front != item:
                self.clear(main.ids.front,text=True)
                main.ids.front.add_widget(MDScreen())
                main.ids.front.add_widget(singin)
                main.ids.front.add_widget(MDScreen())
                main.ids.backdrop.open(Window.height)
                main.ids.backdrop.header_text = app.language['en']['singIn_header'] if  app.app_language == 'en' else app.language['rus']['singIn_header']
                self.back = item    

    def build(self):
        global main,app,shat,setting,singin,сontacts
        app,main = self,MainApp.MainScreen(name='main')
        sm = ScreenManager(transition=Transition())
        shat,setting,singin,сontacts = self.ShatScreen(name='shat'),self.SettingScreen(name='setting'),self.SingInScreen(name='sing_in'),self.ContactsScreen(name='add')
        sm.add_widget(main)
        return sm
    def clear(self,box,text:bool=False):
        if text:
            main.ids.backdrop.header_text = ''
        for _ in range(len(box.children)):
            box.remove_widget(box.children[-1])

    def on_start(self):
        main.ids.backdrop.close()

if __name__ == '__main__':
    MainApp().run()