def all_numbers(array):
    for i in range(0, len(array)):
        if isinstance(array[i], int):
            print(array[i])
        elif isinstance(array[i], list):
            all_numbers(array[i])

print(all_numbers([
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8,
     [9, 10, 11,
      [12, 13, 14]
      ]
      ],
      [15, 16, 17, 18, 19,
       [20, 21, 22,
        [23, 24, 25, 
         [26, 27, 28, 29]
      ], 30, 31
], 32
], 33, ]))