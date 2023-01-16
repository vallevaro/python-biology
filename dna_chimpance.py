# Import necessary libraries
import matplotlib.pyplot as plt

# Load the DNA sequence from a .txt file
with open("datasets/chimpanzee.txt") as f:
    sequence = f.read()

# Compute GC content
gc_content = (sequence.count("G") + sequence.count("C")) / len(sequence)

# Create a GC skew plot
gc_skew = []
window = 100
for i in range(0, len(sequence) - window, window):
    gc_count = (sequence[i:i+window].count("G") + sequence[i:i+window].count("C"))
    at_count = (sequence[i:i+window].count("A") + sequence[i:i+window].count("T"))
    gc_skew.append((gc_count - at_count) / (gc_count + at_count))

plt.plot(gc_skew)
plt.xlabel("Window Position (bp)")
plt.ylabel("GC Skew")
plt.title("GC Skew Plot")
plt.show()

# Create a codon usage plot
codon_counts = {}
for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    if codon in codon_counts:
        codon_counts[codon] += 1
    else:
        codon_counts[codon] = 1

plt.bar(codon_counts.keys(), codon_counts.values())
plt.xlabel("Codon")
plt.ylabel("Count")
plt.title("Codon Usage Plot")
plt.show()

# Print GC content
print("GC Content:", gc_content)
