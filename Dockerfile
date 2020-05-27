FROM ubuntu:18.04

LABEL maintainer="abdoul@test.com"

WORKDIR "/App"

RUN apt-get update && apt-get upgrade -y

# Expose port number
EXPOSE 8085

# Command
CMD ["/bin/bash"]

