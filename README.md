## Introduction
这是一个用于为bedrock创建application inference profile的Python 代码，支持Foundation Model或 cross-region inference。通过inference profile,可以为bedrock使用的模型打上标签，以对bedrock的成本进行可观测。

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
```

参数说明
- model_arn: 模型的ARN,支持Foundation Model或 cross-region inference
    - Foundation Model: arn:aws:bedrock:<region>::foundation-model/<model_name>:<version>
    - Cross-region Model: arn:aws:bedrock:<region>:<account_id>:inference-profile/<model_name>:<version>
- tags: 标签列表
- profile_name: inference profile名称

- model_inference_profile_arn: 返回的inference profile ARN,用于后续调用converse时的model_id 参数


3. 使用AWS CLI 创建inference profile
```bash
aws bedrock create-inference-profile --inference-profile-name <profile_name> --model-source copyFrom=<model_arn> --tags key=<key>,value=<value>
```

4. policy

在对模型进行调用时，请确保拥有以下权限

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["bedrock:InvokeModel*"],
      "Resource: [
          "arn:aws:bedrock:us-east-1:<account_id>:inference-profile/*",
          "arn:aws:bedrock:us-east-1::foundation-model/*",
          "arn:aws:bedrock:us-west-2::foundation-model/*"
      ]
    }
  ]
}
```


