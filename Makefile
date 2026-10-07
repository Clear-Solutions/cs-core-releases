.PHONY: setup check security
setup:
	python3 tools/install_tools.py
check:
	python3 tools/check_release.py
	python3 -m compileall -q tools
security: setup
	work/bin/gitleaks git --redact --exit-code 1
	work/bin/actionlint
