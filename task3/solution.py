def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]


    combined_intervals = []

    pupil_intervals = intervals['pupil']
    for i in range(0, len(pupil_intervals), 2):
        start = pupil_intervals[i]
        end = pupil_intervals[i + 1]
        combined_intervals.append((start, end))


    tutor_intervals = intervals['tutor']
    for i in range(0, len(tutor_intervals), 2):
        start = tutor_intervals[i]
        end = tutor_intervals[i + 1]
        combined_intervals.append((start, end))

    sum_time = 0


    for start, end in combined_intervals:
        overlap_start = max(start, lesson_start)
        overlap_end = min(end, lesson_end)


        if overlap_start < overlap_end:
            sum_time += overlap_end - overlap_start

    return sum_time



tests = [
    {
        'intervals': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'intervals': {
            'lesson': [1594702800, 1594706400],
            'pupil': [
                1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                1594706524, 1594706524, 1594706579, 1594706641
            ],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]

#The final check-in
if __name__ == '__main__':
    for i in range(len(tests)):
        test = tests[i]
        test_answer = appearance(test['intervals'])


        if test_answer == test['answer']:
            print(f'Test  {i} passed!')
        else:

            print(f'ERROR {i}: got {test_answer}, expected {test['answer']}')
