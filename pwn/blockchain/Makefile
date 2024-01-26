.PHONY: all build package

all: build

build:
	docker build -f build.dockerfile . -t blockchainbuild
	docker run --rm -v $(CURDIR)/output:/output -t blockchainbuild cp target/release/libblockchain.so blockchain /output

package:
	-rm dist.tar
	cd .. && tar -czf blockchain/dist.tar \
		blockchain/chal/src \
		blockchain/chal/Cargo.toml \
		blockchain/chal/rbpf.diff \
		blockchain/output \
		blockchain/template/src \
		blockchain/template/Cargo.toml \
		blockchain/template/Makefile \
		blockchain/template/README.md \
		blockchain/Dockerfile

deploy:
	docker build . -t blockchain
	docker run --rm --privileged -p 1337:5000 -it blockchain