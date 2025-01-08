import re
import boto3
import os

class TagBedrockForMap:
    def __init__(self):
        region_name = os.getenv('AWS_REGION', 'us-east-1')
        self.bedrock_client = boto3.client("bedrock", region_name=region_name)

    # model_arn 有两种情况
    # 1. arn:aws:bedrock:us-east-1:55134xxxxxxxx:inference-profile/us.amazon.nova-pro-v1:0 (这是针对cross-region inference profile)
    # 2. arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0(这是针对基础模型)
    def create_inference_profile(self,profile_name, model_arn, tags):    
        """Create Inference Profile using base model ARN"""

        #check exists before create
        profile_response = self.get_inference_profile_by_name(profile_name)
        if profile_response:
            print("Inference profile already exists")
            raise Exception("Inference profile already exists")

        response = self.bedrock_client.create_inference_profile(
            inferenceProfileName=profile_name,
            modelSource={'copyFrom': model_arn},
            tags=tags
        )
        print("CreateInferenceProfile Response:", response['ResponseMetadata']['HTTPStatusCode']),
        print(f"{response}\n")
        return response       

    def get_inference_profile_by_name(self,profile_name):
        response = self.bedrock_client.list_inference_profiles(
            maxResults = 100,
            typeEquals = 'APPLICATION'
        )
        profile_response=''
        inferenceProfileSummaries = response['inferenceProfileSummaries']
        for inferenceProfileSummary in inferenceProfileSummaries:
            if inferenceProfileSummary['inferenceProfileName'] == profile_name:
                profile_response = self.bedrock_client.get_inference_profile(
                    inferenceProfileIdentifier=inferenceProfileSummary['inferenceProfileArn']
                )
                break
        return profile_response 

    def list_inference_profiles(self):

        return self.bedrock_client.list_inference_profiles()

    def delete_inference_profiles(self,profile_name):
        
        self.bedrock_client.delete_inference_profile(
            inferenceProfileIdentifier=profile_name)     

if __name__ == "__main__":
    TagBedrockForMap = TagBedrockForMap()
    model_arn = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-pro-v1:0"
    tags = [{'key': 'test', 'value': 'test'}]
    profile_name = "test-amazon-nova-pro-v1"
    response = TagBedrockForMap.create_inference_profile(profile_name,model_arn,tags)  
    print(response)
    model_inference_profile_arn = TagBedrockForMap.get_inference_profile_by_name(profile_name)["inferenceProfileArn"]
    print(model_inference_profile_arn)



    

    # Call Nova demo
    #response = self.bedrock_client.converse(
    #        modelId=model_inference_profile_arn,
    #        system=system_prompts,
    #        messages=[{'role': 'user', 'content': content}],
    #        inferenceConfig=self.inference_config,
    #        toolConfig=tool_config
    #    )
    
    #TagBedrockForMap.delete_inference_profiles("5ehdhz0gk52i")