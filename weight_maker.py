import numpy as np
import json

f_name = 'prev_code/face_categ/faces.wts'
f_name_TEST = 'TEST_data.txt'


def test_read(file_name):
    # Opening JSON file
    f = open(file_name, )
    data = json.load(f)
    # Printing data
    #print(data)
    print(json.dumps(data, indent=4))

    #for i in data['emp_details']:
    #    print(i)
    f.close()


pic_size = 150  # 150x150 pixels

def test_write():
    data = {}
    data["Network"] = ""
    data["Layers"] = []

    ###############################
    #        Emotion Layer        #
    ###############################
    emotions = [
        {  # emotion 1 (happy)
            "Ri":0,
            "N": pic_size**2,
            "Si": list(range(0, pic_size**2)),                              # indices from 0 to 150^2
            "Wt": list(np.around(np.random.rand(pic_size**2), decimals=5))  # 150**2 random nums between
        },
        {  # emotion 2 (sad)
            "Ri": 1,
            "N": pic_size ** 2,
            "Si": list(range(0, pic_size ** 2)),                              # indices from 0 to 150^2
            "Wt": list(np.around(np.random.rand(pic_size ** 2), decimals=5))  # 150**2 random nums in [0,1)
        }
    ]

    emotion_projection_dict = {
        "From": "Input",
        "MetaData":{
            "GScale":"1"
        },
        "Rs": emotions
    }

    new_emotion_layer = {
        "Layer":"Emotion",
        "MetaData":{
            "ActMAvg":"0.15",
            "ActPAvg": "0.15"
        },
        "Prjns": [
            emotion_projection_dict
        ]
    }


    ###############################
    #         Input Layer         #
    ###############################
    projs_from_emo_to_all_nodes = []
    for i in range(150**2):
        entry = {
            "Ri": i,
            "N": 2,
            "Si": [0, 1],
            "Wt": list(np.around(np.random.rand(2), decimals=5))  # 2 random nums in [0,1)
        }
        projs_from_emo_to_all_nodes.append(entry)

    from_emotion_projection_dict = {
        "From": "Emotion",
        "MetaData": {
            "GScale":"1"
        },
        "Rs": projs_from_emo_to_all_nodes
    }

    new_input_layer = {
        "Layer": "Input",
        "MetaData": {
            "ActMAvg": "0.4857",
            "ActPAvg": "0.4857"
        },
        "Prjns": [
            from_emotion_projection_dict
        ]
    }

    # Append layers
    data["Layers"].append(new_input_layer)
    data["Layers"].append(new_emotion_layer)

    with open('TEST_data.wts', 'w') as outfile:
        json.dump(data, outfile)


test_write()
#test_read(f_name_TEST)

