import matplotlib.pyplot as plt

def reports_direct_and_fully_associative_mapping(title, mapping, rep_policy):
  data = pd.read_csv("./data/result.csv")
  
  df_mapping = data.query(f"mapping=='{mapping}' and rep_policy=='{rep_policy}'")
  df_mapping.reset_index(inplace=True)
  block_size_axis = df_mapping['block_size']
  hit_axis = df_mapping['hit_percent']
  miss_axis = df_mapping['miss_percent']

  fig, ax = plt.subplots()

  ax.scatter(block_size_axis,hit_axis)
  ax.scatter(block_size_axis,miss_axis)

  for i, txt in enumerate(hit_axis):
      ax.annotate(round(txt,2),(block_size_axis[i],hit_axis[i]))

  for i, txt in enumerate(miss_axis):
      ax.annotate(round(txt,2),(block_size_axis[i],miss_axis[i]))

  plt.title(f"{title}")
  plt.plot(block_size_axis, hit_axis, 'g', label="Acertos")
  plt.plot(block_size_axis, miss_axis, 'r', label="Falhas")
  plt.xlabel(f"Tamanho dos blocos da cache line (KB)")
  plt.ylabel("Percentual")
  plt.legend()

  plt.show()

def report_associative_mapping_by_sets(title,rep_policy):
    data = pd.read_csv("./data/result.csv")
    
    df_mapping = data.query(f"mapping=='fas' and rep_policy=='{str(rep_policy)}'")
    df_mapping.reset_index(inplace=True)
    num_ways_axis = df_mapping['num_ways']
    hit_axis = df_mapping['hit_percent']
    miss_axis = df_mapping['miss_percent']

    fig, ax = plt.subplots()

    ax.scatter(num_ways_axis,hit_axis)
    ax.scatter(num_ways_axis,miss_axis)

    for i, txt in enumerate(hit_axis):
        ax.annotate(round(txt,2),(num_ways_axis[i],hit_axis[i]))

    for i, txt in enumerate(miss_axis):
        ax.annotate(round(txt,2),(num_ways_axis[i],miss_axis[i]))

    plt.title(f"{title}")
    plt.plot(num_ways_axis, miss_axis, 'r', label="Falhas")
    plt.plot(num_ways_axis, hit_axis, 'g', label="Acertos")
    plt.xlabel(f"Número de vias")
    plt.ylabel("Percentual")
    plt.legend()

    plt.show()