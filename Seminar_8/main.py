from pathlib import Path

from get_from_user import get_from_user, read_json
from txt_to_json import txt_to_json

if __name__ == '__main__':
    txt_to_json(Path('../Seminar_7/result'))
    get_from_user(Path('../Seminar_8/data.json'))
    # print(type(read_json()))
