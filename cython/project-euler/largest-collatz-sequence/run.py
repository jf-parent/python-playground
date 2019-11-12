n = 1000000
candidate = 13
longest_seq = 10
while n > 13:
    print(n)
    nn = n
    nb_seq = 1
    while nn != 1:
        if nn % 2 == 0:
            nn = nn / 2
        else:
            nn = (3 * nn) + 1
        nb_seq += 1

    if nb_seq > longest_seq:
        candidate = n
        longest_seq = nb_seq

    n -= 1
print(candidate)
