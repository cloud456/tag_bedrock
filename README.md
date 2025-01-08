## Introduction
这是一个用于为bedrock创建application inference profile的Python 代码，支持基础模型或跨域区域模型。通过inference profile,可以为bedrock 打上标签，对于bedrock的成本进行可观测。

## Setup

1. Clone and install dependencies:
```bash
git clone <repository-url>
cd tag_bedrock
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the script:
示例代码
```python
    TagBedrockForMap = TagBedrockForMap()
    model_arn = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0"
    tags = [{'key': 'test', 'value': 'test'}]
    profile_name = "test-amazon-nova-pro-v1"
    response = TagBedrockForMap.create_inference_profile(profile_name,model_arn,tags)  
    print(response)
    model_inference_profile_arn = TagBedrockForMap.get_inference_profile_by_name(profile_name)["inferenceProfileArn"]
    print(model_inference_profile_arn)

参数说明
- model_arn: 模型的ARN,支持基础模型或跨域区域模型
    - 基础模型: arn:aws:bedrock:<region>::foundation-model/<model_name>:<version>
    - 跨域区域模型: arn:aws:bedrock:<region>:<account_id>:inference-profile/<model_name>:<version>
- tags: 标签列表
- profile_name: inference profile名称

- model_inference_profile_arn: 返回的inference profile ARN,用于后续调用converse时的model_id 参数
```
