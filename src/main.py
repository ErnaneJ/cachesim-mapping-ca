from simulator import simulate
from file_handler import clear_file, append_data_to_file
from report_data import reports_direct_and_fully_associative_mapping, report_associative_mapping_by_sets

def main():
  clear_file("./data/result.csv")
  append_data_to_file(f"./data/result.csv", 'mapping,num_sets,num_ways,block_size,hit_percent,miss_percent,rep_policy')
  
  cache_size = 4096 # (B)
  policies = ['FIFO', 'LRU', 'RR']

  for i in range(4): # => Direct with 8B, 16B, 32B and 64B blocks
    n = 8 * 2**i
    simulate('dm', cache_size//n, 1, n, 'LRU')

  for policy in policies: # => Associative per set with 2, 4, 8 and 16 ways
    for i in range(4):
        n = 8 * 2**i
        simulate('as', 4*cache_size//(n*n), n//4, n, policy)
  
  cache_size = 1024

  for policy in policies: # => Fully associative with 8B, 16B, 32B, and 64B blocks
    for i in range(4):
        n = 8 * 2**i
        simulate('fas', 1, cache_size//n, n, policy)

  reports_direct_and_fully_associative_mapping("Mapeamento direto","dm","LRU")
  reports_direct_and_fully_associative_mapping("Totalmente associativo (FIFO)","fa","FIFO")
  reports_direct_and_fully_associative_mapping("Totalmente associativo (LRU)","fa","LRU")
  reports_direct_and_fully_associative_mapping("Totalmente associativo (Aleatório)","fa","RR")

  report_associative_mapping_by_sets("Associativo por conjuntos (FIFO)","FIFO")
  report_associative_mapping_by_sets("Associativo por conjuntos (LRU)","LRU")
  report_associative_mapping_by_sets("Associativo por conjuntos (Aleatório)","RR")

main()