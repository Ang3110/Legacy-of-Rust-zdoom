all: clean compress

clean:
	rm -f dist/LoR-zd.pk3

compress:
	cd src; \
	zip -r ../dist/LoR-zd.pk3 *; \
	cd ..;
