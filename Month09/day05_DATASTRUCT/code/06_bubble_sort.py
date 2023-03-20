

def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    bubble_sort(li)
    print(li)