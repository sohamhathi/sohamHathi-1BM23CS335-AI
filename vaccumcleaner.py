def vacuum_agent():
 
    state = {}
    state['A'] = int(input("Enter state of A (0 for clean, 1 for dirty): "))
    state['B'] = int(input("Enter state of B (0 for clean, 1 for dirty): "))
    location = input("Enter location (A or B): ").upper()

    cost = 0

    if state['A'] == 0 and state['B'] == 0:
        print("Turning vacuum off")
        print(f"Cost: {cost}")
        print(state)
        return

    if location == 'A':
        if state['A'] == 1:
            print("Cleaned A.")
            state['A'] = 0
            cost += 1
        print("Is A clean now? (0 if clean, 1 if dirty):", state['A'])
        print("Is B dirty? (0 if clean, 1 if dirty):", state['B'])
        if state['B'] == 1:
            print("Moving vacuum right")
            cost += 1
            print("Cleaned B.")
            state['B'] = 0
    elif location == 'B':
        if state['B'] == 1:
            print("Cleaned B.")
            state['B'] = 0
            cost += 1
        print("Is B clean now? (0 if clean, 1 if dirty):", state['B'])
        print("Is A dirty? (0 if clean, 1 if dirty):", state['A'])
        if state['A'] == 1:
            print("Moving vacuum left")
            cost += 1
            print("Cleaned A.")
            state['A'] = 0

    print(f"Cost: {cost}")
    print(state)



vacuum_agent()
