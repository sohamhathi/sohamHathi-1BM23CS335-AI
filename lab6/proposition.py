print("Soham Hathi 1BM23CS335")
from itertools import product

def pl_true(sentence, model):
    if sentence == "A":
        return model["A"]
    elif sentence == "B":
        return model["B"]
    elif sentence == "C":
        return model["C"]
    elif sentence == "A_or_C":
        return model["A"] or model["C"]
    elif sentence == "B_or_not_C":
        return model["B"] or (not model["C"])
    elif sentence == "KB":
        return (model["A"] or model["C"]) and (model["B"] or (not model["C"]))
    elif sentence == "alpha":
       
        return model["alpha"]
    else:
        return False

def print_truth_table():
    print(f"{'A':<7} {'B':<7} {'C':<7} {'A∨C':<7} {'B∨¬C':<7} {'KB':<7} {'α':<7}")
    print("-"*50)
    
    all_rows = []
    for values in product([False, True], repeat=3):
        model = {"A": values[0], "B": values[1], "C": values[2]}
        
        
        model["A_or_C"] = pl_true("A_or_C", model)
        model["B_or_not_C"] = pl_true("B_or_not_C", model)
        model["KB"] = pl_true("KB", model)
        model["alpha"] = model["KB"]  
        
        all_rows.append(model)
        
        
        print(f"{str(model['A']).lower():<7} {str(model['B']).lower():<7} {str(model['C']).lower():<7} "
              f"{str(model['A_or_C']).lower():<7} {str(model['B_or_not_C']).lower():<7} "
              f"{str(model['KB']).lower():<7} {str(model['alpha']).lower():<7}")

    return all_rows

def tt_entails(all_rows):
    
    for model in all_rows:
        if model["KB"] and not model["alpha"]:
            return False
    return True

def main():
    all_rows = print_truth_table()
    entails = tt_entails(all_rows)
    print("\nDoes KB entail α? ", entails)

if __name__ == "__main__":
    main()
