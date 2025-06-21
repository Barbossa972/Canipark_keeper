from pathlib import Path
import numpy as np

def ranker(list_of_candidates: list[tuple]) -> list[tuple] :



    ratio_list = [(user[0], user[1]/(user[2] + 1)) for user in list_of_candidates]
    n = len(ratio_list)

    for i in range(n):

        already_sorted = True
        
        for j in range(n - i - 1):

            if ratio_list[j][1] < ratio_list[j + 1][1]:

                ratio_list[j], ratio_list[j  + 1] = ratio_list[j + 1], ratio_list[j]
                already_sorted = False

            elif ratio_list[j][1] == ratio_list[j + 1][1]:

                if np.random.random_sample() > 0.5:
                    ratio_list[j], ratio_list[j  + 1] = ratio_list[j + 1], ratio_list[j]
                    already_sorted = False

        if already_sorted:
            
            break

    return ratio_list


if __name__=='__main__':
    test_list = [(0, 3, 1), (16, 1, 1), (358, 3, 2), (1, 5, 0), (23, 7, 4), (19, 3, 1)]
    print(ranker(test_list))

