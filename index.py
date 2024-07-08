def solution(A):
    A.sort(reverse=True)
    rooms = 0
    current_room_size = 0
    for guest in A:
        if current_room_size + 1 > guest:
            rooms += 1
            current_room_size = 0
        current_room_size += 1
    return rooms + 1