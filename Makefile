test:
	python setup.py test

install:
	pip install .

uninstall:
	pip uninstall -y thingsboard-cli || echo "Seems not installed"

reinstall: uninstall install
update-project-layout:
	yo asc-python

SWAGGER_VERSION=2.4.5
swagger-codegen-cli.jar:
	wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar -O swagger-codegen-cli.jar

generate-swagger-client: swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i swagger/thingsboard.json -l python -o thingsboard-client \
    -D projectName=thingsboard-client \
    -D appDescription='Thingsboard REST client (auto-generated from Swagger spec)' \
    -D packageName=thingsboard_client \
    -D packageVersion=2.3.1

install-swagger-client: generate-swagger-client
	cd thingsboard-client && python setup.py sdist && cd dist && pip install *.tar.gz



