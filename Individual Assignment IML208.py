class GrabCarBookingSystem:
    def __init__(self):
        self.users = {}
        self.drivers = {}
        self.bookings = []

    def register_user(self, name, phone):
        if phone in self.users:
            return f"User with phone number {phone} already registered."
        self.users[phone] = {
            'name': name,
            'phone': phone
        }
        return f"User {name} registered successfully with phone number {phone}."

    def register_driver(self, name, car_model):
        driver_id = len(self.drivers) + 1
        self.drivers[driver_id] = {
            'name': name,
            'car_model': car_model,
            'is_available': True
        }
        return f"Driver {name} registered successfully with Driver ID {driver_id}."

    def book_ride(self, phone, pickup_location, destination):
        if phone not in self.users:
            return "User not registered."
        available_driver = next((driver_id for driver_id, details in self.drivers.items() if details['is_available']), None)
        if not available_driver:
            return "No drivers available at the moment."
        self.drivers[available_driver]['is_available'] = False
        booking_id = len(self.bookings) + 1
        self.bookings.append({
            'booking_id': booking_id,
            'phone': phone,
            'driver_id': available_driver,
            'pickup_location': pickup_location,
            'destination': destination,
            'status': 'Ongoing'
        })
        return f"Ride booked successfully. Booking ID: {booking_id}, Driver: {self.drivers[available_driver]['name']}"

    def complete_ride(self, booking_id):
        for booking in self.bookings:
            if booking['booking_id'] == booking_id and booking['status'] == 'Ongoing':
                booking['status'] = 'Completed'
                self.drivers[booking['driver_id']]['is_available'] = True
                return f"Ride {booking_id} completed successfully."
        return "Invalid booking ID or ride already completed."

    def delete_booking(self, booking_id):
        for booking in self.bookings:
            if booking['booking_id'] == booking_id:
                self.bookings.remove(booking)
                self.drivers[booking['driver_id']]['is_available'] = True
                return f"Booking {booking_id} deleted successfully."
        return "Booking ID not found."

    def show_bookings(self):
        return self.bookings

def main():
    system = GrabCarBookingSystem()

    while True:
        print("\n=== GrabCar Booking System ===")
        print("1. Register User")
        print("2. Register Driver")
        print("3. Book Ride")
        print("4. Complete Ride")
        print("5. Delete Booking")
        print("6. Show Bookings")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            print(system.register_user(name, phone))

        elif choice == "2":
            name = input("Enter Name: ")
            car_model = input("Enter Car Model: ")
            print(system.register_driver(name, car_model))

        elif choice == "3":
            phone = input("Enter Phone Number: ")
            pickup_location = input("Enter Pickup Location: ")
            destination = input("Enter Destination: ")
            print(system.book_ride(phone, pickup_location, destination))

        elif choice == "4":
            booking_id = int(input("Enter Booking ID: "))
            print(system.complete_ride(booking_id))

        elif choice == "5":
            booking_id = int(input("Enter Booking ID to delete: "))
            print(system.delete_booking(booking_id))

        elif choice == "6":
            bookings = system.show_bookings()
            if bookings:
                for booking in bookings:
                    print(booking)
            else:
                print("No bookings available.")

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
