"""
	Check the consumed RAM in real-time.
"""
import psutil
import time
import os
from psutil._common import bytes2human


mem_dict = dict(psutil.virtual_memory()._asdict())
max_mem = min_mem = mem_dict['used']/(1024 ** 2)

while True:
	try:
		os.system('clear')  # clear the terminal output

		mem_dict = dict(psutil.virtual_memory()._asdict())
		actual_mem = mem_dict['used']/(1024 ** 2)
		
		if actual_mem > max_mem:
			max_mem = actual_mem
		elif actual_mem < min_mem:
			min_mem = actual_mem
		else:
			pass

		print(f"RAM usage in MB:\n"
			  f"Actual: {actual_mem:.0f}\n"
			  f"Max: {max_mem:.0f}\n"
			  f"Min: {min_mem:.0f}")
		time.sleep(1)
	
	except KeyboardInterrupt:
		difference = max_mem - min_mem
		print(f"\nDifference: {difference:.0f} (MB)")
		exit()

