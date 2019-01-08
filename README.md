# rest-deploy
DOCKER 실행

호스트쉘> docker run -ti \
    -e AWS_PROFILE=zappa \
    -v $(pwd):/var/task \
    -v ~/ .aws/:root/.aws \
    --rm myzappa
