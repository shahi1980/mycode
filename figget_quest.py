#!/usr/bin/env python3

import json

    json_file = '{"category": "General Knowledge","type": "multiple","difficulty": "easy","question":"What machine element is located                 in the center of fidget spinners?","correct_answer": "Bearings","incorrect_answers": ["Axles","Gears","Belts"]}'
    data = json.loads(json_file)
    print(data)
    print(data['question'])
