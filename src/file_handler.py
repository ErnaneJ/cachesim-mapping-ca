def clear_file(path):
  file = open(path, "w")
  file.write('')
  file.close()

def append_data_to_file(path, content):
  file = open(path, "a")
  file.write(content + "\n")
  file.close()

def read_reference_file(cache_simulator, path):
  reference_file = open(path, "r")

  for address in reference_file:
    address = int(address, 16)
    cache_simulator.load(address)

  reference_file.close()