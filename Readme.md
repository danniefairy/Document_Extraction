# Document Extraction

## Run the CI/CD
### Run ngrok
- **ngrok http 8080**
### Let Jenkins connect to Github
- Copy the url of the ngrok to the **Setting/Webhooks** as the format **https://<Jenkins user ID>:<Jenkins user token>@<Jenkins url>/job/<app name>/build?token=<app token on Jenkins>**

## Reference 
[Leveraging BERT for Extractive Text Summarization on Lectures](https://arxiv.org/abs/1906.04165)