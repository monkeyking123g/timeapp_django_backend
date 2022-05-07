from db_conect import search_time
from delete import SwipeToDeleteItemTime
from kivymd.uix.picker import  MDDatePicker
from kivy.uix.screenmanager import Screen


class WindowSecond(Screen):

    def on_save(self, instance, value, date_range):

        data = value
        date_input = str(data)
        print(data)
        self.ids.tol_bar.title = date_input # print data for user 
        self.time_update(date_input)
       

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.ids.tol_bar.title = "Data !"
        
        for i in  range(len(self.ids.dada.children)):
            for widget in self.ids.dada.children:
                self.ids.dada.remove_widget(widget)


    def show_date_picker(self):
        """ Open date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    
    def time_update(self, date_input):
        #time = requests.get(f'http://127.0.0.1:8000/time-add/?search={date_input}').json() # get request date
        search = search_time(date_input)
        nam = 0
        for i in  range(len(self.ids.dada.children)):
            for widget in self.ids.dada.children:
                self.ids.dada.remove_widget(widget)

        for data_s in search:
            nam += 1
            self.ids.dada.add_widget(
                SwipeToDeleteItemTime(text=f'{str(nam)}.  tempo aggiunto {data_s["ore_lavorative"]}', id_tempo=data_s['id'])
                )

       
    
       

    
