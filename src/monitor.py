import psutil

class Monitor:

    def __init__(self):
        pass

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        used_mb = round(mem.used / (1024 * 1024), 1)
        total_mb = round(mem.total / (1024 * 1024), 1)
        return mem.percent, used_mb, total_mb

    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        used_gb = round(disk.used / (1024 * 1024 * 1024), 1)
        total_gb = round(disk.total / (1024 * 1024 * 1024), 1)
        return disk.percent, used_gb, total_gb

    def show_system_status(self):
        cpu = self.get_cpu_usage()
        mem = self.get_memory_usage()
        disk = self.get_disk_usage()

        print("\n=== Systemstatus ===")
        print(f"CPU: {cpu}%")
        print(f"RAM: {mem[0]}% ({mem[1]} MB av {mem[2]} MB)")
        print(f"Disk: {disk[0]}% ({disk[1]} GB av {disk[2]} GB)")

    