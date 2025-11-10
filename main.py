import matplotlib.pyplot as plt
import numpy as np
 
# === Fill in your measured query times here (in milliseconds) ===
# Example data — replace with your actual EXPLAIN ANALYZE results
distances = [500, 1000, 2000]        # in meters
dijkstra_times = [45.2, 63.8, 120.5] # e.g., from EXPLAIN ANALYZE Total runtime
astar_times = [38.4, 52.1, 95.7]     # e.g., from EXPLAIN ANALYZE Total runtime
 
# === Plot configuration ===
plt.figure(figsize=(8, 5))
x = np.arange(len(distances))
width = 0.35
 
plt.bar(x - width/2, dijkstra_times, width, label="Dijkstra", alpha=0.8)
plt.bar(x + width/2, astar_times, width, label="A*", alpha=0.8)
 
# === Labels and design ===
plt.xticks(x, [f"{d} m" for d in distances])
plt.ylabel("Execution Time (ms)")
plt.xlabel("Query Distance")
plt.title("Performance Comparison: Dijkstra vs A*")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
 
# === Save & show ===
plt.savefig("routing_performance_comparison.png", dpi=300)
plt.show()