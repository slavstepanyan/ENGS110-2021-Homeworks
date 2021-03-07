def main():
    N = int (input ("input width"))
    M = int (input ("input height"))

    row = 0
    while (row < M):
        if (row == 0 or row == (M-1)):
            print(N * "*", end = "\n")
        else:
            column = 0
            while (column < N):
                if (column == 0 or column == (N-1)):
                    print ("*", end = "")
                else:
                    print(" ", end = "")

                column +=1
            print (" ", end = "\n")
        row += 1

main()
