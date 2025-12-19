from ward_class import Ward
from occupancy_utils import load_wards, save_wards, plot_occupancy

def main():
    print("Hospital Ward Occupancy System\n")

    # Step 1: Load data
    df = load_wards()

    # Step 2: Create Ward objects
    wards = [Ward(row['name'], row['total_beds'], row['occupied_beds']) for _, row in df.iterrows()]

    # Step 3: Display menu
    while True:
        print("\nMenu:")
        print("1. Admit a patient")
        print("2. Discharge a patient")
        print("3. View occupancy chart")
        print("4. Show ward details")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter ward name: ").capitalize()
            number = int(input("Number of patients to admit: "))
            for ward in wards:
                if ward.name == name:
                    ward.admit(number)

        elif choice == '2':
            name = input("Enter ward name: ").capitalize()
            number = int(input("Number of patients to discharge: "))
            for ward in wards:
                if ward.name == name:
                    ward.discharge(number)

        elif choice == '3':
            # Update DataFrame before plotting
            for i, ward in enumerate(wards):
                df.loc[i, 'occupied_beds'] = ward.occupied_beds
            plot_occupancy(df)

        elif choice == '4':
            print("\nWard Details:")
            for ward in wards:
                print(f"{ward.name}: {ward.occupied_beds}/{ward.total_beds} beds occupied "
                      f"({ward.get_occupancy_rate():.1f}%)")

        elif choice == '5':
            # Save and exit
            for i, ward in enumerate(wards):
                df.loc[i, 'occupied_beds'] = ward.occupied_beds
            save_wards(df)
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
