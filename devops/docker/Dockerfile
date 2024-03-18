FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# Install dependencies
RUN yum update -y && \
 yum install -y httpd && \
 yum install -y python && \
 yum install -y git && \
 yum install -y sudo

EXPOSE 80