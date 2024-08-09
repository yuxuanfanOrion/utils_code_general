import json

def merge_json_files(file1, file2, output_file):
    # 读取第一个JSON文件
    with open(file1, 'r', encoding='utf-8') as f:
        data1 = json.load(f)

    # 读取第二个JSON文件
    with open(file2, 'r', encoding='utf-8') as f:
        data2 = json.load(f)

    # 确保两个文件有相同数量的项目
    assert len(data1) == len(data2), "两个JSON文件中的项目数量不匹配"

    # 合并数据
    merged_data = []
    for item1, item2 in zip(data1, data2):
        merged_item = item1.copy()  # 复制第一个文件的项目
        # 将output字段变为包含两个独立字符串的数组
        merged_item['output'] = [item1['output'], item2['output']]
        merged_data.append(merged_item)

    # 将合并后的数据写入新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

    print(f"合并完成，结果已保存到 {output_file}")

# 使用函数

file1_path = '/root/Machine-Mindset/datasets/behaviour/en/en_energy_introversion.json'
file2_path = '/root/Machine-Mindset/datasets/behaviour/en/en_energy_extraversion.json'

merged_json_path = './merged_output.json'

merge_json_files(file1_path, file2_path, merged_json_path)