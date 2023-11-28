import os
import re

class Minecraft:
    def __init__(self, base_command = "/usr/local/bin/msm") -> None:
        self.base_command = base_command

    def run_command(self, command:str) -> str:
        return os.popen(f"{self.base_command} {command}").read()
    
    def list_all_servers(self) -> list:
        result = self.run_command("server list").split("/n")

        filtered = list(filter(lambda x: x != "", result))
        def format(row):
            reg_status = "(\[.*\])"
            reg_server_name = "(\".*\")"
            reg_message = "(\..*\.)"

            status = re.search(reg_status, row).group()
            server_name = re.search(reg_server_name, row).group()
            message = re.search(reg_message, row).group()

            return {
                "status": status[1:len(status) - 1],
                "serverName": server_name[1:len(server_name) - 1],
                "message": message[2:len(message) - 1]
            }

        return [format(x) for x in filtered]
    
    def start_server(self, server_name: str) -> bool:
        result = self.run_command(f"{server_name} start")

        print(result)

        return True
    
    def stop_server(self, server_name: str, force = False) -> bool:
        now = "now"
        empty = ""

        result = self.run_command(f"{server_name} stop {now if force else empty}")

        print(result)

        return True
    
    def restart_server(self, server_name:str, force = False) -> bool:
        now = "now"
        empty = ""

        result = self.run_command(f"{server_name} restart {now if force else empty}")

        print(result)
        return True
    
    def server_status(self, server_name) -> str:
        return self.run_command(f"{server_name} status")
