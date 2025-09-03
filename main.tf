# main.tf

# 1. 사용할 'Provider'를 선언합니다.
#    Provider는 Terraform이 제어할 대상(AWS, GCP, 로컬 파일 등)을 의미합니다.
#    여기서는 내 컴퓨터의 파일을 제어하는 'local' provider를 사용합니다.

terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.2.3" # 최신 버전은 공식 문서에서 확인하여 업데이트할 수 있습니다.
    }
  }
}

# 2. 만들고 싶은 'Resource'를 정의합니다.
#    "local_file" 타입의 리소스를 만들고, 코드 내에서 부를 이름은 "hello_file" 입니다.
resource "local_file" "hello_file" {
  # 파일의 내용은 "Hello, Terraform IaC!" 입니다.
  content  = "Hello, Terraform IaC!"
  # 파일의 이름은 "hello.txt" 입니다.
  filename = "${path.module}/hello.txt" # 프로젝트 폴더 내에 생성됩니다.
}