# Streamlit Sample App for SAP

### [Blog Link](https://www.beex-inc.com/blog/webapp_for_sap_with_streamlit)

## Usage

```sh
# settings for docker image
IMAGE_NAME=sap-streamlit-app-sample 
LISTEN_PORT=8501                    

# sap connection
SAP_HOST=xxx.xxx.xxx.xxx # SAP Host
SAP_SYSNR=00             # SAP System Number
SAP_CLIENT=000           # SAP Client
SAP_USER=ddic            # SAP User
SAP_PASSWORD=*****       # SAP Password

# Build
docker build -t ${IMAGE_NAME} .

# Run
docker run -p ${LISTEN_PORT}:80 ${IMAGE_NAME} \
  --host ${SAP_HOST} \
  --sysnr ${SAP_SYSNR} \
  --client ${SAP_CLIENT} \
  --user ${SAP_USER} \
  --password ${SAP_PASSWORD}
```