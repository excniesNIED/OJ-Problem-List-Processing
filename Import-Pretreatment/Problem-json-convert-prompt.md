我有一个`problem.json`文件模板如下：

```json
{
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
    "test_case_score": [
        {
            "score": 50,
            "input_name": "1.in",
            "output_name": "1.out"
            "score": 50,
            "input_name": "2.in",
            "output_name": "2.out"
        },
    ],
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
    "spj": null,
    "rule_type": "OI",
    "source": "SDNU \u673a\u5668\u4eba\u5b9e\u9a8c\u5ba4\u5728\u7ebf\u8bc4\u6d4b\u7cfb\u7edf http://127.0.0.1",
    "answers": []
}
```

其中，这些项目保留默认值

```json
    "tags": [
        "\u4e00\u672c\u901a"
```

```json
   "time_limit": 1000,
    "memory_limit": 256,
```

```json
    "template": {},
    "spj": null,
    "rule_type": "OI",
    "source": "SDNU \u673a\u5668\u4eba\u5b9e\u9a8c\u5ba4\u5728\u7ebf\u8bc4\u6d4b\u7cfb\u7edf http://127.0.0.1",
    "answers": []
```

`description`、`input_description`、`output_description`、`test_case_score`、`hint`的`format`参数均为`HTML`

我有一个目录`Collections`，目录下有很多数字命名的子目录，每个子目录结构如下

```
C:\User\excnies\Collections\1212\
│
├── data\
│   ├── 1.in
│   ├── 1.out
│   ├── 2.in
│   └── 2.out
├── content.md
├── data.py
├── reference.yml
└── std.cpp
```

`display_id`的值为`SSOI-[子目录对应的数字]`，比如在`1212`子目录中，`display_id`的值为`SSOI-1212`

`title`的值为`SSOI-[子目录对应的数字]`，比如在`1212`子目录中，`title`的值为`SSOI-1212`

每个子目录中的content.md中包含以下内容

````markdown
### 【题目描述】

读入三个整数，按每个整数占8个字符的宽度，右对齐输出它们，按照格式要求依次输出三个整数，之间以一个空格分开。

### 【输入】

只有一行，包含三个整数，整数之间以一个空格分开。

### 【输出】

只有一行，按照格式要求依次输出三个整数，之间以一个空格分开。

### 【输入样例】

```
123456789 0 -1
```

### 【输出样例】

```
123456789       0      -1
```

### 【提示】

【数据规模】

30%数据：n\*m≤1000

100%数据：m,n≤1000


 ### 【来源】

 一本通在线评测 
````

将`### 【题目描述】`下的内容`读入三个整数，按每个整数占8个字符的宽度，右对齐输出它们，按照格式要求依次输出三个整数，之间以一个空格分开。`转换为HTML格式，将文字以Unicode编码填写到json文件的`description`下的`value`中：
```html
<p><span style=\"color: rgb(64, 70, 79);\">\u8bfb\u5165\u4e09\u4e2a\u6574\u6570\uff0c\u6309\u6bcf\u4e2a\u6574\u6570\u53608\u4e2a\u5b57\u7b26\u7684\u5bbd\u5ea6\uff0c\u53f3\u5bf9\u9f50\u8f93\u51fa\u5b83\u4eec\uff0c\u6309\u7167\u683c\u5f0f\u8981\u6c42\u4f9d\u6b21\u8f93\u51fa\u4e09\u4e2a\u6574\u6570\uff0c\u4e4b\u95f4\u4ee5\u4e00\u4e2a\u7a7a\u683c\u5206\u5f00\u3002</span><br /></p>
```

`### 【输入】`下的内容对应`input_description`下的`value`，`### 【输出】`下的内容对应`output_description`下的`value`，`### 【提示】`对应`hint`下的`value`，都需要转换为HTML。如果个别选项没有数据，`value`留空。

遍历子目录中`data`文件夹下的文件对应到json文件中的`test_case_score`，一组`.in`和`.out`文件对应一组测试样例。`input_name`和`output_name`包括所有`data`下的`.in`和`.out`文件。所有测试样例的分数`score`总和为100分（每组测试样例的分数为100除样例组的个数，保留整数）

        "test_case_score": [
            {
                "score": 50,
                "input_name": "1.in",
                "output_name": "1.out"
                "score": 50,
                "input_name": "2.in",
                "output_name": "2.out"
            },
        ],

写一个python脚本，为每个目录生成这个`problem.json`，生成在子目录下