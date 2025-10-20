from monitor import *
from alarm import AlarmManager
import time

class Menu:
    def __init__(self):
        self.monitor = Monitor()
        self.alarm_manager = AlarmManager()

    def display_menu(self):
        print("\n=== Systemövervakningsmeny ===")
        print("1. Visa systemstatus")
        print("2. Lägg till larm")
        print("3. Visa aktiva larm")
        print("4. Starta övervakningsläge")
        print("5. Avsluta")

    def run(self):
        while True:
            self.display_menu()
            try: 
                choice = int(input("Välj ett alternativ (1-5): "))

            except ValueError:
                print("Ogiltigt val. Försök igen.")
                continue
            else: 
                match choice:
                    case 1:
                        self.monitor.show_system_status()
                    case 2:
                        self.alarm_manager.display_alarm_menu()
                        sub_choice = input("Välj ett alternativ (1-4): ").strip()
                        if sub_choice == "4":
                            continue
                        mapping = {"1": "CPU", "2": "RAM", "3": "Disk"}
                        alarm_type = mapping.get(sub_choice)
                        if alarm_type is None:
                            print("Ogiltigt val. Återgår till huvudmenyn.")
                            continue

                        threshold_input = input("Ange tröskelvärde (%): ").strip()
                        try:
                            threshold = int(threshold_input)
                            self.alarm_manager.add_alarm(alarm_type, threshold)
                        except ValueError:
                            print("\nFel: Tröskelvärdet måste vara ett heltal.")
                            continue
                    case 3:
                        self.alarm_manager.list_alarms()
                    case 4:
                        try:
                            duration_input = input("Ange övervakningsduration (sekunder): ")
                            interval_input = input("Ange uppdateringsintervall (sekunder): ")
                            
                            duration = int(duration_input)
                            interval = int(interval_input)
                            
                            if duration <= 0 or interval <= 0:
                                print("\nFel: Duration och intervall måste vara 1 eller större än 1 sekund.")
                                continue
                                
                            start_time = time.time()
                            print(f"\nStartar övervakning i {duration} sekunder...")
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
                        except ValueError:
                            print("\nFel: Duration och intervall måste vara heltal.")
                            continue
                    case 5:
                        print("Avslutar programmet.")
                        break
                    case _:
                        print("Ogiltigt val. Försök igen.")
if __name__ == "__main__":
    menu = Menu()
    menu.run()