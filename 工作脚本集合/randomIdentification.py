import random
import string
import json

# 生成64位随机字符串 idType=2时适用
def generate_random_string(length=64):
    """生成一个指定长度的随机字符串"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# 生成64位随机整数，并转换为字符串 idType=3时适用
def generate_64bit_random_integer_as_string():
    """生成一个64位随机整数，并将其转换为字符串"""
    # 64位整数的范围是从0到2^64 - 1
    min_value = 0
    max_value = 2**64 - 1
    random_integer = random.randint(min_value, max_value)
    return str(random_integer)


def create_record():
    """创建一条包含随机identification的记录"""
    record = {
        "expKey": ["ab_arena_shy_tuan_entrance"],
        "identification": generate_64bit_random_integer_as_string(),
        "idType": 3  # 3表示user_id
    }
    return record


def main():
    num_records = 50000
    output_file = 'output_records.txt'

    with open(output_file, 'w') as file:
        for _ in range(num_records):
            record = create_record()
            json_record = json.dumps(record)
            file.write(json_record + '\n')


if __name__ == "__main__":
    main()