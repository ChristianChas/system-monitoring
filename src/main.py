from monitor import *
from alarm import AlarmManager
import time

# Klassen Menu hanterar användarens interaktion och programflödet
class Menu:
    def __init__(self):
        self.monitor = Monitor()
        self.alarm_manager = AlarmManager()

# Skriver ut huvudmenyn
    def display_menu(self):
        print("\n=== Systemövervakningsmeny ===")
        print("1. Visa systemstatus")
        print("2. Lägg till larm")
        print("3. Visa aktiva larm")
        print("4. Starta övervakningsläge")
        print("5. Avsluta")

# Huvudmetoden som kör menyloopen
    def run(self):
        while True:
            self.display_menu()
            try: 
                choice = int(input("Välj ett alternativ (1-5): "))

            except ValueError:  # Om användaren matar in något annat än en siffra
                print("Ogiltigt val. Försök igen.") 
                continue
            else: 
                match choice:
                    case 1:  # Alternativ 1: Visa systemstatus 
                        self.monitor.show_system_status()
                    case 2: # Alternativ 2: Lägg till larm
                        self.alarm_manager.display_alarm_menu()
                        sub_choice = input("Välj ett alternativ (1-4): ").strip()
                        if sub_choice == "4":  # Om användaren väljer 4 i alarm menyn -> gå tillbaka till huvudmeny
                            continue
                        mapping = {"1": "CPU", "2": "RAM", "3": "Disk"}
                        alarm_type = mapping.get(sub_choice)
                        if alarm_type is None:
                            print("Ogiltigt val. Återgår till huvudmenyn.") 
                            continue

                        threshold_input = input("Ange tröskelvärde (%): ").strip() # Användaren anger tröskelvärde (t.ex. 80%)
                        try:
                            threshold = int(threshold_input)
                            self.alarm_manager.add_alarm(alarm_type, threshold)
                        except ValueError:
                            print("\nFel: Tröskelvärdet måste vara ett heltal.")
                            continue
                    case 3:   # Alternativ 3: Visa alla aktiva larm
                        self.alarm_manager.list_alarms()
                    case 4: # Alternativ 4: Starta övervakningsläge 
                        try:
                            duration_input = input("Ange övervakningsduration (sekunder): ")
                            interval_input = input("Ange uppdateringsintervall (sekunder): ")
                            
                            duration = int(duration_input)
                            interval = int(interval_input)
                            
                            if duration <= 0 or interval <= 0: # Kontrollerar att värdena är logiska (inte 0 eller negativa)
                                print("\nFel: Duration och intervall måste vara 1 eller större än 1 sekund.")
                                continue
                                
                            start_time = time.time()
                            print(f"\nStartar övervakning i {duration} sekunder...") # Startar övervakningen
                            while time.time() - start_time < duration:
                                self.monitor.show_system_status()
                                monitor_data = {
                                    "CPU": self.monitor.get_cpu_usage(),
                                    "RAM": self.monitor.get_memory_usage()[0],
                                    "Disk": self.monitor.get_disk_usage()[0]
                                }
                                self.alarm_manager.check_alarms(monitor_data)
                                time.sleep(interval)
                            print("\nÖvervakning avslutad.")
                        except ValueError:   # Felhantering om användaren inte anger heltal
                            print("\nFel: Duration och intervall måste vara heltal.")
                            continue
                    case 5: # Alternativ 5: Avsluta programmet
                        print("Avslutar programmet.")
                        break
                    case _: # Om användaren skriver något annat än 1–5 
                        print("Ogiltigt val. Försök igen.")
if __name__ == "__main__": # Kör menyn om filen körs direkt
    menu = Menu()
    menu.run()