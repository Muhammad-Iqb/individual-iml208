import tkinter as tk
from tkinter import messagebox

class GrabCarBookingSystem:
    def __init__(self):
        self.users = {}
        self.drivers = {}
        self.bookings = []

    def register_user(self, user_id, name, phone):
        if user_id in self.users:
            return f"User {user_id} already registered."
        self.users[user_id] = {
            'name': name,
            'phone': phone
        }
        return f"User {name} registered successfully."

    def register_driver(self, driver_id, name, car_model):
        if driver_id in self.drivers:
            return f"Driver {driver_id} already registered."
        self.drivers[driver_id] = {
            'name': name,
            'car_model': car_model,
            'is_available': True
        }
        return f"Driver {name} registered successfully."

    def book_ride(self, user_id, pickup_location, destination):
        if user_id not in self.users:
            return "User not registered."
        available_driver = next((driver_id for driver_id, details in self.drivers.items() if details['is_available']), None)
        if not available_driver:
            return "No drivers available at the moment."
        self.drivers[available_driver]['is_available'] = False
        booking_id = len(self.bookings) + 1
        self.bookings.append({
            'booking_id': booking_id,
            'user_id': user_id,
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


class GrabCarBookingSystemGUI:
    def __init__(self, root):
        self.system = GrabCarBookingSystem()

        self.root = root
        self.root.title("GrabCar Booking System")

        self.frame = tk.Frame(root)
        self.frame.pack()

        # Register User Section
        self.label_user_id = tk.Label(self.frame, text="User ID:")
        self.label_user_id.grid(row=0, column=0)
        self.entry_user_id = tk.Entry(self.frame)
        self.entry_user_id.grid(row=0, column=1)

        self.label_user_name = tk.Label(self.frame, text="User Name:")
        self.label_user_name.grid(row=1, column=0)
        self.entry_user_name = tk.Entry(self.frame)
        self.entry_user_name.grid(row=1, column=1)

        self.label_user_phone = tk.Label(self.frame, text="User Phone:")
        self.label_user_phone.grid(row=2, column=0)
        self.entry_user_phone = tk.Entry(self.frame)
        self.entry_user_phone.grid(row=2, column=1)

        self.button_register_user = tk.Button(self.frame, text="Register User", command=self.register_user)
        self.button_register_user.grid(row=3, column=0, columnspan=2)

        # Register Driver Section
        self.label_driver_id = tk.Label(self.frame, text="Driver ID:")
        self.label_driver_id.grid(row=4, column=0)
        self.entry_driver_id = tk.Entry(self.frame)
        self.entry_driver_id.grid(row=4, column=1)

        self.label_driver_name = tk.Label(self.frame, text="Driver Name:")
        self.label_driver_name.grid(row=5, column=0)
        self.entry_driver_name = tk.Entry(self.frame)
        self.entry_driver_name.grid(row=5, column=1)

        self.label_car_model = tk.Label(self.frame, text="Car Model:")
        self.label_car_model.grid(row=6, column=0)
        self.entry_car_model = tk.Entry(self.frame)
        self.entry_car_model.grid(row=6, column=1)

        self.button_register_driver = tk.Button(self.frame, text="Register Driver", command=self.register_driver)
        self.button_register_driver.grid(row=7, column=0, columnspan=2)

        # Book Ride Section
        self.label_user_id_book = tk.Label(self.frame, text="User ID (Book):")
        self.label_user_id_book.grid(row=8, column=0)
        self.entry_user_id_book = tk.Entry(self.frame)
        self.entry_user_id_book.grid(row=8, column=1)

        self.label_pickup_location = tk.Label(self.frame, text="Pickup Location:")
        self.label_pickup_location.grid(row=9, column=0)
        self.entry_pickup_location = tk.Entry(self.frame)
        self.entry_pickup_location.grid(row=9, column=1)

        self.label_destination = tk.Label(self.frame, text="Destination:")
        self.label_destination.grid(row=10, column=0)
        self.entry_destination = tk.Entry(self.frame)
        self.entry_destination.grid(row=10, column=1)

        self.button_book_ride = tk.Button(self.frame, text="Book Ride", command=self.book_ride)
        self.button_book_ride.grid(row=11, column=0, columnspan=2)

        # Complete Ride Section
        self.label_booking_id_complete = tk.Label(self.frame, text="Booking ID (Complete):")
        self.label_booking_id_complete.grid(row=12, column=0)
        self.entry_booking_id_complete = tk.Entry(self.frame)
        self.entry_booking_id_complete.grid(row=12, column=1)

        self.button_complete_ride = tk.Button(self.frame, text="Complete Ride", command=self.complete_ride)
        self.button_complete_ride.grid(row=13, column=0, columnspan=2)

        # Delete Booking Section
        self.label_booking_id_delete = tk.Label(self.frame, text="Booking ID (Delete):")
        self.label_booking_id_delete.grid(row=14, column=0)
        self.entry_booking_id_delete = tk.Entry(self.frame)
        self.entry_booking_id_delete.grid(row=14, column=1)

        self.button_delete_booking = tk.Button(self.frame, text="Delete Booking", command=self.delete_booking)
        self.button_delete_booking.grid(row=15, column=0, columnspan=2)

        # Show Bookings Section
        self.button_show_bookings = tk.Button(self.frame, text="Show Bookings", command=self.show_bookings)
        self.button_show_bookings.grid(row=16, column=0, columnspan=2)

        # Output Text Box
        self.text_output = tk.Text(self.frame, height=10, width=50)
        self.text_output.grid(row=17, column=0, columnspan=2)

    def register_user(self):
        user_id = self.entry_user_id.get()
        name = self.entry_user_name.get()
        phone = self.entry_user_phone.get()
        result = self.system.register_user(user_id, name, phone)
        self.text_output.insert(tk.END, result + "\n")

    def register_driver(self):
        driver_id = self.entry_driver_id.get()
        name = self.entry_driver_name.get()
        car_model = self.entry_car_model.get()
        result = self.system.register_driver(driver_id, name, car_model)
        self.text_output.insert(tk.END, result + "\n")

    def book_ride(self):
        user_id = self.entry_user_id_book.get()
        pickup_location = self.entry_pickup_location.get()
        destination = self.entry_destination.get()
        result = self.system.book_ride(user_id, pickup_location, destination)
        self.text_output.insert(tk.END, result + "\n")

    def complete_ride(self):
        booking_id = self.entry_booking_id_complete.get()
        result = self.system.complete_ride(int(booking_id))
        self.text_output.insert(tk.END, result + "\n")

    def delete_booking(self):
        booking_id = self.entry_booking_id_delete.get()
        result = self.system.delete_booking(int(booking_id))
        self.text_output.insert(tk.END, result + "\n")

    def show_bookings(self):
        bookings = self.system.show_bookings()
        if bookings:
            for booking in bookings:
                self.text_output.insert(tk.END, str(booking) + "\n")
        else:
            self.text_output.insert(tk.END, "No bookings available.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = GrabCarBookingSystemGUI(root)
    root.mainloop()
