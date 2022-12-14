# https://www.prefect.io/guide/blog/getting-started-prefect-2/

import random
from prefect import flow    # NEW **** 

def call_unreliable_api():
    choices = [{"data": 42}, "failure"]
    res = random.choice(choices)
    if res == "failure":
        raise Exception("Our unreliable service failed")
    else:
        return res

def augment_data(data: dict, msg: str):
    data["message"] = msg
    return data

def write_results_to_database(data: dict):
    print(f"Wrote {data} to database successfully!")
    return "Success!"

@flow   # NEW ****
def pipeline2(msg: str):
    api_result = call_unreliable_api()        
    augmented_data = augment_data(data=api_result, msg=msg)
    write_results_to_database(augmented_data)


pipeline2("Trying a flow!")