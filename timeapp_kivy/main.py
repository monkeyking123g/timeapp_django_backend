# import tutte file.py
from db_conect import *
from screen_home import Windowferst
from screen_two import WindowSecond

from delete import SwipeToDeleteItemMonth, SwipeToDeleteItemTime
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivymd.app import MDApp
from datetime import datetime
from kivy.uix.screenmanager import  Screen
from kivy.uix.boxlayout import BoxLayout



class Content(BoxLayout):
   pass

class Windowfrie(Screen):
    pass



class Test(MDApp):
    dialog = None
    dialog_houre = None
    dialog_error = None
    date_now = datetime.now()

    def build(self):
        self.icon = "Logo.png"
        self.theme_cls.theme_style = "Light"
        
        return Builder.load_file('main.kv')

    def on_swipe_complete(self, instance):
        '''Delete widget and time of sql '''
        delete = delete_time(instance.id_tempo)
        self.root.ids.second.dada.remove_widget(instance)
        self.root.ids.md_list_all.remove_widget(instance)
        

    def remove_item(self, instance):
        '''Delete widget and month of sql '''
        self.root.ids.md_list.remove_widget(instance)

    def add_month(self):
        """Add total month """
        date_month = self.date_now.strftime('%m/%Y')
        totale = sum_total_time()
        post = post_totale(totale)
        get = get_totale()
      
        nam = 0
        for i in get:   
            nam = i['id']
            data = i["datetime_add"][:7]
        print(nam)
        self.root.ids.md_list.add_widget(
                SwipeToDeleteItemMonth(text=f'{str(nam)}.  {data} Totale  {str(totale)} ore', id_total_month=nam)
            )

    def restart_app(self, obj):
        self.dialog_error.dismiss()
        return self.on_start()

    def stop_app(self, obj):
        return self.stop()    

    def on_start(self):
        try:
            check = check_day_add_month()
            totale = get_totale()
            nam = 0
            for data in totale:
                nam += 1
                self.root.ids.md_list.add_widget(
                    SwipeToDeleteItemMonth(text=f'{str(nam)}.  {(data["datetime_add"][:7])} totale  {str(data["total_ore"])} ore', id_total_month=data['id'])
                )
            self.restart_screen_time()
             
        except:
            self.dialog_error = MDDialog(
                text="Oops! Nou internet connect!",
               radius=[20, 7, 20, 7],
                 buttons=[
                    MDFlatButton(
                        text="RESTART", text_color=self.theme_cls.primary_color,on_release=self.restart_app
                    ),
                    MDFlatButton(
                        text="EXIT", text_color=self.theme_cls.primary_color, on_release=self.stop_app
                    ),
                ],
            )
          
           # self.dialog_error.open()
    def restart_screen_time(self):
        # delete widget from screen 
        for i in  range(len(self.root.ids.md_list_all.children)):
            for widget in self.root.ids.md_list_all.children:
                self.root.ids.md_list_all.remove_widget(widget)

        # add widget from screen        
        time = get_time()
        nam = 0
        for data in time:
            nam += 1
            self.root.ids.md_list_all.add_widget(
                SwipeToDeleteItemTime(text=f'{str(nam)}.  {str(data["datetime_add"][:7])} ore  {str(data["ore_lavorative"])}', id_tempo=data['id'])
                )

    def trach(self, instance):
        '''Delete widget and month total from db'''
        delete = delete_totale(instance.id_total_month)
        self.root.ids.md_list.remove_widget(instance)
        

    def cancel_dialog(self, obj):
        self.dialog.dismiss()

    def cancel_dialog2(self, obj):
        self.dialog_houre.dismiss()

    def add_dialog(self, obj):
        """ Update time from sql and screen """
        try:
            date = self.root.ids.second.tol_bar.title
            ora =  float(self.dialog.content_cls.value.text)
            #update_request = requests.put(f'http://127.0.0.1:8000/time-detail/{str(self.id_widget)}', data={'ore_lavorative': ora})
            put_request = put_time(self.id_widget, ora)
            self.restart_screen_time()
            if date != "Data !":
                time = search_time(date)
                for i in  range(len(self.root.ids.second.dada.children)):
                    for widget in self.root.ids.second.dada.children:
                        self.root.ids.second.dada.remove_widget(widget)
                nam = 0
                for data_s in time:
                    nam += 1
                    self.root.ids.second.dada.add_widget(
                        SwipeToDeleteItemTime(text=f'{str(nam)}.  tempo aggiunto {data_s["ore_lavorative"]}', id_tempo=data_s['id'])
                    )
                
            self.dialog.dismiss()
        except:
            self.dialog.content_cls.value.text = "formato richiesta non corretto !"

    def show_confirmation_dialog(self, g):
        """Open dialog of update hours"""

        if not self.dialog:
            self.dialog = MDDialog(
                title="Agiorna la data:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color,on_release=self.cancel_dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.add_dialog
                    ),
                ],
            )
        ora =  self.dialog.content_cls.value.text
        self.id_widget = g.id_tempo
        self.dialog.open()

    def add_hours_for_day(self, obj):
        """ Add hours for day selected"""
        date = self.root.ids.second.tol_bar.title
        if date == "Data !":
            self.dialog_houre.content_cls.value.text = "non hai messo la data !"
        else:
            try: 
                ora =  float(self.dialog_houre.content_cls.value.text)
                #post = requests.post('http://127.0.0.1:8000/time', json={'ore_lavorative': ora, 'datetime_add': date})
                post = post_time(ora, date)
                date_post = search_time(date)
                id_nam = None
                time = None
                nam = 0
                for data in date_post:
                    nam += 1
                    id_nam = data['id']
                    time = data["ore_lavorative"]
                self.root.ids.second.dada.add_widget(
                    SwipeToDeleteItemTime(text=f'{str(nam)}.  tempo aggiunto {time}', id_tempo=id_nam)
                )
                self.dialog_houre.dismiss()
    
            except:
                self.dialog_houre.content_cls.value.text = "formato richiesta non corretto !"

            
         
    def show_confirmation_dialog2(self):
        ''' Open dialog from  "Agungi ore ". '''
       
        if not self.dialog_houre:
            self.dialog_houre = MDDialog(
                title="Agungi ore:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color,on_release=self.cancel_dialog2
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.add_hours_for_day
                    ),
                ],
            )
        self.dialog_houre.open()
    


if __name__ == '__main__':
    Test().run()
