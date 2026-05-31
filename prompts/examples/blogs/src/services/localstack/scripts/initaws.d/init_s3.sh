#!/bin/bash

for bucket in files; do
  aws --endpoint-url=http://localstack:4566 s3 mb s3://$bucket && aws --endpoint-url=http://localstack:4566 s3api put-bucket-acl --bucket $bucket --acl public-read-write
done
