from assembly_line_scheduling import assembly_line_scheduling

if __name__ == '__main__':
    a = [[7, 9, 3, 4, 8, 4],
         [8, 5, 6, 4, 5, 7]]
    t = [[2, 1, 1, 3, 4],
         [2, 1, 2, 2, 1]]
    e = [2, 4]
    x = [3, 2]

    time, path = assembly_line_scheduling(a, t, e, x)
    print(f"최소 시간: {time}")
    print(f"경로: {path}")