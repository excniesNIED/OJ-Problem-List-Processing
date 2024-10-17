import os
import json
import re

def markdown_to_html(markdown):
    # 简单的Markdown到HTML转换
    markdown = markdown.replace("\n", "<br />")
    markdown = markdown.replace("### 【题目描述】", "<h3>题目描述</h3>")
    markdown = markdown.replace("### 【输入】", "<h3>输入</h3>")
    markdown = markdown.replace("### 【输出】", "<h3>输出</h3>")
    markdown = markdown.replace("### 【提示】", "<h3>提示</h3>")
    markdown = markdown.replace("### 【来源】", "<h3>来源</h3>")
    markdown = markdown.replace("### 【输入样例】", "<h3>输入样例</h3>")
    markdown = markdown.replace("### 【输出样例】", "<h3>输出样例</h3>")
    markdown = markdown.replace("```", "<pre>")
    return markdown

def generate_problem_json(directory):
    problem_json = {
        "display_id": "",
        "title": "",
        "description": {
            "format": "html",
            "value": ""
        },
        "tags": [
            "\u4e00\u672c\u901a"
        ],
        "input_description": {
            "format": "html",
            "value": ""
        },
        "output_description": {
            "format": "html",
            "value": ""
        },
        "test_case_score": [],
        "hint": {
            "format": "html",
            "value": ""
        },
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": [
            {
                "input": "",
                "output": ""
            }
        ],
        "template": {},
        "spj": None,
        "rule_type": "OI",
        "source": "SDNU \u673a\u5668\u4eba\u5b9e\u9a8c\u5ba4\u5728\u7ebf\u8bc4\u6d4b\u7cfb\u7edf http://127.0.0.1",
        "answers": []
    }

    # 获取子目录的数字
    dir_number = os.path.basename(directory)
    problem_json["display_id"] = f"SSOI-{dir_number}"
    problem_json["title"] = f"SSOI-{dir_number}"

    # 读取content.md文件
    content_md_path = os.path.join(directory, "content.md")
    with open(content_md_path, 'r', encoding='utf-8') as f:
        content_md = f.read()

    # 解析content.md文件
    sections = re.split(r"### \【(.*?)\】", content_md)
    sections = [markdown_to_html(section) for section in sections]

    problem_json["description"]["value"] = sections[2]
    problem_json["input_description"]["value"] = sections[4]
    problem_json["output_description"]["value"] = sections[6]
    problem_json["hint"]["value"] = sections[8]

    # 处理测试样例
    data_dir = os.path.join(directory, "data")
    test_cases = os.listdir(data_dir)
    in_files = sorted([f for f in test_cases if f.endswith(".in")])
    out_files = sorted([f for f in test_cases if f.endswith(".out")])

    if len(in_files) != len(out_files):
        raise ValueError("Number of input files does not match number of output files")

    score_per_case = 100 // len(in_files)
    for i in range(len(in_files)):
        problem_json["test_case_score"].append({
            "score": score_per_case,
            "input_name": in_files[i],
            "output_name": out_files[i]
        })

    # 写入problem.json文件
    output_path = os.path.join(directory, "problem.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(problem_json, f, ensure_ascii=False, indent=4)

def main():
    collections_dir = "C:\\User\\excnies\\Collections"
    for subdir in os.listdir(collections_dir):
        subdir_path = os.path.join(collections_dir, subdir)
        if os.path.isdir(subdir_path):
            generate_problem_json(subdir_path)

if __name__ == "__main__":
    main()