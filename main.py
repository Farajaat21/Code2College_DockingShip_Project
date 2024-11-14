# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function

    
    
    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below
def find_available_bays(ship_size, arrival_time,departure_time ):
    
    available_bays = []

    for bay in db.docking_bays:
        
        if bay['size'] == ship_size:
            if available_schedule(bay,arrival_time,departure_time):
                available_bays.append(bay)
    return available_bays

def available_schedule(bay, arrival_time, departure_time):
    for scheduled in bay['schedule']:
        schedule_arrival_time, schedule_departure_time, _=scheduled
        
        if arrival_time < schedule_departure_time and departure_time > schedule_arrival_time:
            return False
    return True
def assigning_ships(incoming_ships):
    for ships in incoming_ships:
        ship_size = ships['size']
        arrival_time = ships['arrival_time']
        departure_time = ships['departure_time']
        available_bays = find_available_bays(ship_size, arrival_time,departure_time)
        
        if available_bays:
            found_ship = available_bays[0]
            
            found_ship['schedule'].append((arrival_time, departure_time, ships['ship_name']))
        else:
            print(f"No bays were found for ship: {ships['ship_name']}. Try again later")

def main():
    print_docking_bays()
    print_incoming_ships()
    
    for ship in db.incoming_ships:
        ship_size = ship['size']
        arrival_time = ship['arrival_time']
        departure_time = ship['departure_time']
        available_bays = find_available_bays(ship_size, arrival_time, departure_time)
        print()
        print(f"available bay for ship {ship['ship_name']} Size: {ship_size}")
        print('----------------------------------------------------')
        
        if available_bays:
            for bays in available_bays:
                print(f"bay {bays['bay_id']} Size {bays['size']}")
        else:
            print(f"No bays were found for {ship['ship_name']}. Try again later")
if __name__ == "__main__":
    main()
