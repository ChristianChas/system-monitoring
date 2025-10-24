class Alarm: # Klassen Alarm representerar ett enskilt larm (t.ex. CPU, RAM eller Disk)
    def __init__(self, alarm_type, threshold):
        self.alarm_type = alarm_type # Sätter typ av larm (t.ex. "CPU") och tröskelvärde (procent)
        self.threshold = threshold

    def __str__(self): # Returnerar en läsbar text av larmet
        return f"{self.alarm_type} larm {self.threshold}%"

    def is_triggered(self, current_value): # Returnerar True om det aktuella värdet överskrider tröskeln vilket innebär att det larmas
        return current_value >= self.threshold


class AlarmManager: # Klassen AlarmManager hanterar flera larm t.ex. skapa, visa och kontrollera larm
    def __init__(self):
        self.alarms = [] 
    def display_alarm_menu(self):  # Skriver ut andra menyn för att skapa ett nytt larm
        print("\n=== Konfigurera alarm ===")
        print("1. CPU-användning")
        print("2. RAM-användning")
        print("3. Disk-användning")
        print("4. Tillbaka till huvudmenyn")

    def add_alarm(self, alarm_type, threshold):
        try:
            threshold = int(threshold)
            if not 1 <= threshold <= 100: # Säkerställer att värdet ligger mellan 1 och 100 %
                print("\nFel: Tröskelvärdet måste vara mellan 1 och 100%.")
                return
            new_alarm = Alarm(alarm_type, threshold) # Skapar nytt larm och lägger till i listan
            self.alarms.append(new_alarm)
            print(f"\nLarm för {alarm_type} satt till {threshold}%.")
        except ValueError: # Hanterar ogiltig inmatning (t.ex. bokstäver)
            print("\nFel: Tröskelvärdet måste vara ett heltal.")
            return

    def list_alarms(self): # Visar alla aktiva larm i sorterad ordning
        if not self.alarms:
            print("\nInga larm är konfigurerade ännu.")
            return

        print("\n=== Aktiva larm ===") 
        for alarm in sorted(self.alarms, key=lambda a: (a.alarm_type, a.threshold)): # Sorterar först på (CPU, RAM, Disk), sedan på tröskelvärde
            print(alarm.alarm_type + " larm med tröskelvärdet " + str(alarm.threshold) + "%")

    def check_alarms(self, monitor_data):  # Kontrollerar alla aktiva larm mot aktuella värden från systemet
        for alarm in self.alarms:
            current_value = monitor_data.get(alarm.alarm_type, 0)
            if alarm.is_triggered(current_value):
                print(f"\nVARNING: {alarm.alarm_type}-användning "
                      f"överstiger {alarm.threshold}% ({current_value}%)")