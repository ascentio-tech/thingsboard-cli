test:
	python setup.py test

install:
	pip install .

uninstall:
	pip uninstall -y thingsboard-cli || echo "Seems not installed"

reinstall: uninstall install
update-project-layout:
	yo asc-python

SWAGGER_VERSION=3.0.8
swagger-codegen-cli.jar:
	wget http://central.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar -O swagger-codegen-cli.jar

THINGSBOARD_VERSION=2.1.1
generate-swagger-client: swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i swagger/thingsboard.json -l python -o thingsboard-client \
    --additional-properties projectName=thingsboard-client,packageName=thingsboard_client,packageVersion=${THINGSBOARD_VERSION},appDescription='Thingsboard REST client (auto-generated from Swagger spec)'

install-swagger-client: generate-swagger-client
	cd thingsboard-client && python setup.py sdist && cd dist && pip install *.tar.gz



