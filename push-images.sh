#!/bin/bash

docker tag backend:latest public.ecr.aws/p2k6s0s6/backend:latest

docker push public.ecr.aws/p2k6s0s6/backend:latest