import matplotlib.pyplot as plt
import random
plt.scatter(data_json_df_dedup_sorted['factulity']+ [random.random()*0.1 for i in range(len(data_json_df_dedup_sorted))], \
            data_json_df_dedup_sorted['zpp_score']+ [random.random()*0.01 for i in range(len(data_json_df_dedup_sorted))])

plt.title("Factuality vs ZCode++ score")
plt.xlabel("factulity")
plt.ylabel("zcode++ score")
plt.show()
