
def count_batteries_by_usage(cycles):
    low=0
    high=0
    med=0
    for i in cycles:
        if i <400:
            low=low+1
        elif (i>=400 and i<=919):
            med=med+1
        else:
            high=high+1
    return {
        "lowCount": low,
        "mediumCount": med,
        "highCount": high
        
    }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")
