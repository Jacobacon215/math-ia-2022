import openpyxl, num2words, os, sys, math, itertools, gc, drawNumProbabilityCalculator, typing

# pn will be the probability of drawing n cards
# pn is the sum of the probabilities of each permutation of dice roll and landed zone that multiply to n
# This is another python file waiting to happen
# Need to find probabilities of zones before this is doable :)

def perms(num_a, num_b): # this is all ripped directly from the stackexchange answer to my question at https://stackoverflow.com/questions/75415051/how-to-check-for-repeated-yield-from-a-python-generator-function?noredirect=1#comment133067580_75415051
    res = []
    # A bit more efficient if we choose the indexes of the "minority" element
    if num_a < num_b:
        elem_sm, elem_lg = 'face', 'other'
        num_sm = num_a
    else:
        elem_sm, elem_lg = 'other', 'face'
        num_sm = num_b
    base_perm = [elem_lg] * (num_a + num_b)
    
    for c in itertools.combinations(range(num_a + num_b), num_sm):
        # c is the tuple of indexes that will be occupied by
        # the "minority" element
        perm = base_perm[:]
        for i in c:
            perm[i] = elem_sm
        res.append(perm)

    return res

class dice_roll_and_zone:
    def __init__(self, roll:int, zone:int) -> None:
        self.roll = roll
        self.zone = zone

        zone_prob = {2:0.038, 1:0.224, 0.5:0.258, 0.25:0.48}
        self.probability = 0.125 * zone_prob[self.zone]

        self.draw_number = int(self.roll * self.zone) if int(self.roll * self.zone) >= 1 else 1

        pass


if __name__ == "__main__":
    while True:

        list_of_dice_rolls_each_multiplied_by_a_zone = []

        roll_zone_dict = dict()

        for possible_roll in range(1,9):
            for possible_zone in [2, 1, 0.5, 0.25]:
                roll_zone_dict[f'roll{possible_roll}AndZone{possible_zone}'] = dice_roll_and_zone(roll=possible_roll, zone=possible_zone)
                # exec(f'roll{possible_roll}AndZone{possible_zone} = dice_roll_and_zone(roll=possible_roll, zone=possible_zone)')
                list_of_dice_rolls_each_multiplied_by_a_zone.append(roll_zone_dict[f'roll{possible_roll}AndZone{possible_zone}'])
                # exec(f'list_of_dice_rolls_each_multiplied_by_a_zone.append(roll{possible_roll}AndZone{possible_zone})')
                pass

        
        probability_dict = dict()

        for number in range(1,17):
            probability_dict[f'probabilityOf{number}'] = 0
            # exec(f'probabilityOf{(num2words.num2words(number)).capitalize} = 0')

        for combination in list_of_dice_rolls_each_multiplied_by_a_zone:
            probability_dict[f'probabilityOf{combination.draw_number}'] += combination.probability
            # exec(f'probabilityOf{combination.draw_number} += combination.probability')

        
        workbook = openpyxl.load_workbook(filename='Final_Roll_Probabilities.xlsx')
        worksheet = workbook['Face_Sheet']

        for col in worksheet.iter_cols(min_row=1, min_col=2, max_col=17, max_row=1):
            for cell in col:
                worksheet[f'{cell.column_letter}2'].value = probability_dict[f'probabilityOf{cell.value}']
                # exec(f'cell.value = probabilityOf{cell.value}')
                pass
            pass

        workbook.save('Final_Roll_Probabilities.xlsx')


        sys.exit()