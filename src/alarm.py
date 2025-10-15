class Alarm:
    def __init__(self, alarm_type, threshold):
        self.alarm_type = alarm_type
        self.threshold = threshold

    def __str__(self):
        return f"{self.alarm_type} larm {self.threshold}%"

    def is_triggered(self, current_value):
        return current_value >= self.threshold


class AlarmManager:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm_type, threshold):
        new_alarm = Alarm(alarm_type, threshold)
        self.alarms.append(new_alarm)
        print(f"\nLarm för {alarm_type} satt till {threshold}%.")

    def list_alarms(self):
        if not self.alarms:
            print("\nInga larm är konfigurerade ännu.")
            return

        print("\n=== Aktiva larm ===")
        for alarm in sorted(self.alarms, key=lambda a: (a.alarm_type, a.threshold)):
            print(alarm)

    def check_alarms(self, monitor_data):
        for alarm in self.alarms:
            current_value = monitor_data.get(alarm.alarm_type, 0)
            if alarm.is_triggered(current_value):
                print(f"\n*** VARNING: {alarm.alarm_type}-användning "
                      f"överstiger {alarm.threshold}% ({current_value}%) ***")
