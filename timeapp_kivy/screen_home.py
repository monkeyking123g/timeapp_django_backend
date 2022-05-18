from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDTimePicker
from datetime import datetime, date
from db_conect import post_time, sum_total_time 


class Windowferst(Screen):
    """Scermo home  for time"""
    def print_total(self):
        """Print total ore for month"""
        total = sum_total_time() # totale ore   
        # print total ore 
        self.tot.title = f'tempo totale {str(total)}'
       

    # return time
    def get_time(self, instance, time):
        '''add time dalle'''
        self.dalle.text = str(time)
        self.dalle_time = time
    
    # cancell
    def on_cancel(self,instance, time):
        self.dalle.text = "Cancel" 

    def show_time_picker(self, f1, f2):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=f1,time=f2)
        time_dialog.open()
    
    def show_time_picker_dalle(self):
        self.show_time_picker(self.on_cancel, self.get_time)
        
    
    def get_time_alle(self, instance, time):
        '''add time alle'''
        self.alle.text = str(time)
        self.alle_time = time
    
    # cancell
    def on_cancel_alle(self,instance, time):

        self.alle.text = "Cancel" 

    def show_time_picker_alle(self):
        self.show_time_picker(self.on_cancel_alle, self.get_time_alle)
    
    def calculate(self):
        try:  
            dalle = self.dalle_time
            alle = self.alle_time
            self.result.text = "confirm"
            result = datetime.combine(date.today(), alle) - datetime.combine(date.today(), dalle)
            # trasforiamo da secondi in ore 
            total = result.total_seconds() / 60**2
            # post = requests.post('http://127.0.0.1:8000/time', json={'ore_lavorative': total, 'datetime_add': str(datetime.now())})
            post = post_time(total, datetime.now()) 
                # aggiorna  tutto 
            totals = sum_total_time()    
            self.tot.title = f'tempo totale {str(totals)}'
            self.dalle.text = "Dalle ore"
            self.alle.text  = "Alle ore"

            self.dalle_time =  None 
            self.alle_time = None
        except:
             self.result.text = "Non hai messo ora!"
            


    def datate_now(self): 
        datetime_add = datetime.now() # date now 
        date_month = datetime_add.strftime('%m/%Y') # year and month
        return date_month
    