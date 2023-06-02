from cachesim import Cache, MainMemory, CacheSimulator
from file_handler import append_data_to_file, read_reference_file

def simulate(mapping, num_sets, num_ways, block_size, replacement_policy):
  memory = MainMemory()

  cache = Cache(
    name=replacement_policy,
    sets=num_sets,
    ways=num_ways,
    cl_size=block_size,
    replacement_policy=replacement_policy.upper()
  )
  memory.load_to(cache)
  memory.store_from(cache)

  cache_simulator = CacheSimulator(cache, memory)
  for i in range(2):
    read_reference_file(cache_simulator, f"./data/reference-{i+1}.txt")
  cache_simulator.force_write_back()

  hit_percentage = 0.0
  error_percentage = 0.0

  for s in cache_simulator.stats():
    hit_percentage = s['HIT_count']/s['LOAD_count']
    error_percentage = s['MISS_count']/s['LOAD_count']
    break

  if num_sets == 1:
     append_data_to_file("./data/result.csv", f"fa,{num_sets},{num_ways},{block_size},{hit_percentage},{error_percentage},{replacement_policy}")
  elif num_ways == 1:
     append_data_to_file("./data/result.csv", f"dm,{num_sets},{num_ways},{block_size},{hit_percentage},{error_percentage},{replacement_policy}")
  else:
     append_data_to_file("./data/result.csv", f"fas,{num_sets},{num_ways},{block_size},{hit_percentage},{error_percentage},{replacement_policy}")