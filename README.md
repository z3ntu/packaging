# Packaging

## Debian

```bash
curl -L -o razergenie_0.9.90.orig.tar.gz https://github.com/z3ntu/RazerGenie/archive/main.tar.gz
tar xf razergenie_0.9.90.orig.tar.gz
cd RazerGenie-main
ln -s ../debian-packaging/razergenie/debian/ .
# Build binary package
debuild -i -us -uc -b
# Build source package
debuild -i -us -uc -S
```

Open-Build-Service wants `*.debian.tar.*`, `*.dsc` and `.orig.tar.*`, which are
the files for the source package
