def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
  n = len(arr)
  middle = n // 2

  if n <= 1:
    return arr
  
  left = merge_sort(arr[:middle])
  right = merge_sort(arr[middle:])

  return merge_two_lists(left, right)


def merge_two_lists(a, b):
  c = []
  i = j = 0

  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
  
  c += a[i:] + b[j:]

  return c


def insertion_sort(arr):
  n = len(arr)

  for i in range(1, n):
    j = i

    while j > 0 and arr[j-1] > arr[j]:
      arr[j - 1], arr[j] = arr[j], arr[j - 1]

      j -= 1


numbers = [94, 56, 32, 55, 344, 192, 4832, 2, 9, 0, 1]
# bubble_sort(numbers)
# print(numbers)

# print(merge_sort(numbers))
# print('')

# insertion_sort(numbers)
# print(numbers)