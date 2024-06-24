import socket
import sys
import pyfiglet
from datetime import datetime


ascii_banner = pyfiglet.figlet_format("MEMENT0")
print(ascii_banner)

if len(sys.argv) != 2:
       print("usage: python portscanner.py <target>")
       sys.exit()

target = socket.gethostbyname(sys.argv[1])

print("-" * 50)
print("Sc4nn1ng T4rg3t: " + target)
print("Sc4nn1ng St4rt3d at:" + str(datetime.now()))
print("-" * 50)

try:
       for port in range (1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target,port))
            if result ==0:
                print("P0rT {} 1s 0p3n".format(port))
            s.close()

except KeyboardInterrupt:
        print ("\n3xit1ng Pr0gram!")
        sys.exit()
except socket.gaierror:
        print("\nH0stn4m3 C0uld N0t B3 R3s0lv3d!")
        sys.exit()
except socket.error:
        print("\nS3rv3r n0t r3sp0nd1ng!")
        sys.exit()


