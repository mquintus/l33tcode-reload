class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        First, we sort the cars by starting position.
        Second, we look at the car that progressed the most:
        We calculate the time when it arrives the goal and put it into a stack. 
        Three: we look at the previous car (n - 1): 
        - If it arrived before the first car (n), it would have been a fleet,
          in this case we pop the first car, and add the second car instead.
        - If it arrived after the first car, we just add the second car.
        Four (general):
        We look at car `i` and calculate when it passes the finish line.
        If there are other cars/fleets in the stack (i + 1, i + 2, ...),
        pop until time(i) > time(i+1)
        '''
        if len(position) < 2:
          return len(position)

        sortedCars = sorted(zip(position, speed))

        arriveStack = []

        for p, s in sortedCars[::-1]:
          arrivalTime = (target - p) / s
          #print("Car will arrive after ", arrivalTime, 'seconds')
          while len(arriveStack) > 0:
            arrivedFleet = arriveStack[-1]
            #print("Recent fleet will arrive after ", arrivedFleet, 'seconds')
            if arrivedFleet >= arrivalTime:
              #print("Pop")
              arriveStack.pop()
              arrivalTime = arrivedFleet
            else:
              break
          #print("New fleet will arrival time: after ", arrivalTime, 'seconds')
          arriveStack.append(arrivalTime)
          #print()

        
        return len(arriveStack)


# 12
# [10,8,0,5,3]
# [2,4,1,1,3]
# 10
# [3]
# [3]
# 100
# [0,2,4]
# [4,2,1]
# 750
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499]
# [23, 7, 12, 33, 6, 1, 4, 7, 32, 30, 6, 18, 31, 25, 1, 7, 23, 11, 17, 8, 31, 12, 13, 19, 37, 31, 32, 35, 39, 17, 21, 29, 32, 23, 14, 38, 30, 29, 13, 26, 20, 36, 38, 34, 2, 32, 4, 2, 8, 17, 26, 2, 20, 35, 15, 1, 23, 20, 11, 2, 33, 19, 19, 17, 12, 2, 28, 24, 15, 31, 5, 35, 32, 26, 7, 26, 9, 17, 10, 11, 19, 25, 12, 22, 27, 2, 23, 17, 2, 23, 35, 7, 13, 1, 25, 38, 20, 40, 33, 6, 32, 19, 10, 38, 4, 17, 7, 13, 40, 13, 19, 27, 10, 33, 39, 33, 15, 27, 26, 24, 21, 1, 2, 23, 35, 20, 11, 32, 31, 17, 36, 28, 1, 17, 23, 24, 23, 40, 3, 28, 13, 31, 3, 10, 7, 7, 17, 39, 6, 25, 20, 30, 35, 29, 36, 14, 25, 31, 27, 25, 25, 25, 25, 21, 24, 3, 14, 16, 22, 23, 15, 40, 24, 22, 15, 33, 13, 35, 38, 6, 27, 30, 31, 9, 11, 17, 12, 10, 6, 6, 14, 22, 4, 36, 8, 40, 16, 16, 2, 10, 33, 15, 10, 23, 7, 38, 14, 14, 24, 2, 10, 16, 2, 18, 8, 28, 1, 2, 28, 2, 11, 14, 34, 37, 30, 19, 33, 25, 30, 31, 12, 18, 36, 32, 39, 4, 19, 33, 25, 35, 33, 22, 5, 15, 18, 13, 14, 33, 19, 18, 8, 16, 31, 39, 5, 39, 24, 19, 20, 11, 40, 16, 30, 6, 30, 24, 32, 16, 6, 17, 16, 39, 2, 6, 7, 18, 27, 33, 34, 30, 20, 5, 5, 30, 2, 2, 36, 15, 3, 11, 36, 7, 25, 11, 11, 24, 10, 34, 32, 5, 39, 29, 6, 30, 26, 33, 18, 27, 31, 5, 21, 7, 16, 15, 33, 15, 4, 5, 21, 31, 14, 8, 26, 23, 13, 24, 26, 38, 22, 26, 19, 13, 32, 13, 40, 7, 31, 34, 39, 29, 38, 27, 10, 31, 27, 1, 2, 22, 19, 35, 25, 28, 11, 23, 22, 5, 33, 11, 19, 32, 1, 39, 24, 11, 28, 39, 17, 8, 12, 4, 25, 13, 40, 30, 10, 22, 30, 23, 39, 38, 11, 22, 28, 36, 25, 34, 33, 22, 1, 36, 37, 28, 20, 10, 4, 23, 37, 34, 19, 6, 38, 27, 14, 34, 21, 32, 29, 18, 16, 28, 21, 13, 6, 17, 23, 40, 37, 18, 2, 25, 35, 25, 1, 37, 1, 12, 7, 3, 22, 11, 21, 28, 37, 24, 33, 1, 5, 35, 39, 26, 1, 28, 31, 10, 27, 20, 36, 18, 37, 26, 3, 39, 30, 24, 13, 40, 21, 40, 3, 8, 8, 40, 12, 37, 18, 6, 24, 16, 25, 32, 39, 35, 37, 28, 20, 30, 5, 3, 27, 7, 8, 17, 37, 2, 17, 18, 7, 25, 6, 3, 13, 32, 9, 9, 7, 17, 39, 20, 16] 
