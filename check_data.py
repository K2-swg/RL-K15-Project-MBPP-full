from datasets import load_dataset

ds = load_dataset("google-research-datasets/mbpp", "full")
print(ds)

for split_name in ds.keys():
    split = ds[split_name]
    print("=" * 60)
    print("SPLIT:", split_name, "| примеров:", len(split))
    for i in range(min(3, len(split))):
        row = split[i]
        print("-" * 40)
        print("task_id:", row.get("task_id"))
        print("text:", row.get("text"))
        for t in row.get("test_list", []):
            print("   ", t)