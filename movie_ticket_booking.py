def book_seat(total_seats, booked_seats, seat_number):
    if seat_number in booked_seats:
        print(f"Seat {seat_number} is already booked.")
    elif seat_number > total_seats or seat_number < 1:
        print(f"Invalid seat number. Please choose a seat between 1 and {total_seats}.")
    else:
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} has been successfully booked.")
    return booked_seats

def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        print(f"Seat {seat_number} booking has been successfully canceled.")
    else:
        print(f"Seat {seat_number} was not booked.")
    return booked_seats

def available_seats(total_seats, booked_seats):
    available = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available

total_seats = 10
booked_seats = [2, 5, 7]

book_seat_number = 3  
cancel_seat_number = 5  
booked_seats = book_seat(total_seats, booked_seats, book_seat_number)

booked_seats = cancel_seat(booked_seats, cancel_seat_number)

available = available_seats(total_seats, booked_seats)

print(f"Available seats: {available}")
