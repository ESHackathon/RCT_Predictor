.PHONY: build test
default: build

build:
	docker build -t eshackathon/rct_predictor .

test:
	-rm -rf /tmp/i3-rct_predictor
	mkdir /tmp/i3-rct_predictor
	cp test.json /tmp/i3-rct_predictor/test.json
	docker run -e LANG=C.UTF-8 --volume /tmp/i3-rct_predictor:/app/work eshackathon/rct_predictor work/test.json  work/output.json
	@echo --- START OUTPUT ---
	@cat /tmp/i3-rct_predictor/output.json
	@echo --- END OUTPUT ---
	-rm -rf /tmp/i3-rct_predictor

shell:
	docker run -it --entrypoint=/bin/sh eshackathon/rct_predictor