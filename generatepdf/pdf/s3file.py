import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOiIzMTFkMWZlOC1lZDQwLTQ2ZDYtODQ4Zi1kYjdkODIyNTliOTMiLCJyb2xlIjoiYWRtaW4iLCJkZXZpY2VUb2tlbiI6InN0cmluZyIsImRldmljZVR5cGUiOiJzdHJpbmciLCJuYmYiOjE2ODI1OTAyODksImV4cCI6MTg0MDQ0MzA4OSwiaWF0IjoxNjgyNTkwMjg5fQ.1nKkJAoyVd_2vo_vP-4Mn2kRBHhLnPIIDOI82WY_B0s"

def upload_file(image_path):
    # url = 'https://staging-api.vivifyhealthcare.com/ImageUpload/DocUpload/'
    # url  = "http://invoicesappapi-prod.us-east-2.elasticbeanstalk.com/api/Management/UploadPdfFile"
    headers =  Imageheaders = {
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer {token}'
    }
    import PyPDF2

    pdfFileObj = open(image_path, 'rb')
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    files = {'UploadDoc': pdfFileObj}
    response = requests.post(url,files=files,headers=headers)
    print(response.status_code)
    imageurl = response.json()['Result']
   
    doc = (imageurl.items())
    for i in doc:
        url = (i[1])
        return url

    
# image_path = r"D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\Lifeeazy-HealthSummaryl.pdf"
# # image_path = r"D:\projects\New folder (2)\test.txt"
# upload_file(image_path=image_path)




# import boto3
# b_name = "ivin-pro-data-conversion"
# s3 = boto3.client("s3")
# b_res = s3.list_buckets()
# # for i in b_res['Buckets']:
#         # print(i)
# with open(r"C:\Users\anves\Pictures\as.png",'rb') as img:
#         s3.upload_fileobj(img,b_name,"testfile.jpg")
#
# s3.download_file(b_name,"testfile.jpg  ","download.jpg")
