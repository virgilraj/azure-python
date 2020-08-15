import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
container_name = 'vraj-1197caff-ab18-4093-a7c2-e811406872f3'

def get_container():
    try:
        print("Azure Blob storage v12 - Python quickstart sample")
        # Quick start code goes here
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        #print(connect_str)

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        
        # Create a unique name for the container
        #container_name = 'vraj-'+str(uuid.uuid4())
        #Create the container 
        #container_client = blob_service_client.create_container(container_name)
        return blob_service_client
    except Exception as ex:
        print('Exception:')
        print(ex)

def upload_file():
    blob_service_client  = get_container()
    
    # Create a file in local data directory to upload and download
    local_path = "./data"
    local_file_name = "test1.pptx"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

def list_lobs_and_download():
    blob_service_client  = get_container()
    container_client = blob_service_client.get_container_client(container_name)
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
        download_file_path = os.path.join('./data', str.replace('test1.pptx' ,'.pptx', 'DOWNLOAD.pptx'))
        print("\nDownloading blob to \n\t" + download_file_path)

        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())

if __name__ == "__main__":
    list_lobs_and_download()