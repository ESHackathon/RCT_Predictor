.PHONY: build test
default: build

build:
	docker build -t jivasquez/rct_predictor .

test:
	-rm -rf /tmp/i3-rct_predictor
	mkdir /tmp/i3-rct_predictor
	cp test.tsv /tmp/i3-rct_predictor/test.tsv
	docker run --volume /tmp/i3-rct_predictor:/app/work jivasquez/rct_predictor test.tsv >output.tsv
	@echo --- START OUTPUT ---
	@cat /tmp/i3-rct_predictor/output.json
	@echo --- END OUTPUT ---
	-rm -rf /tmp/i3-rct_predictor

shell:
	docker run -it --entrypoint=/bin/sh jivasquez/rct_predictor
