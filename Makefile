test:
	python setup.py test

install:
	pip install .

uninstall:
	pip uninstall -y thingsboard-cli || echo "Seems not installed"

reinstall: uninstall install
update-project-layout:
	yo asc-python

swagger-codegen-cli.jar:
	wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.0/swagger-codegen-cli-2.2.0.jar -O swagger-codegen-cli.jar

generate-swagger-client: swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i swagger/thingsboard.json -l python -o thingsboard-client -D packageName=thingsboard_client -D packageVersion=2.3.1

install-swagger-client: generate-swagger-client
	cd thingsboard-client && python setup.py sdist && cd dist && pip install *.tar.gz



