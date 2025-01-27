# File Formats

## JSON

### Advantages

* Her bir satırın metadatası kendi içinde
  * Schema flexibility
  * Sparse representation.
* Nested/Complex typelara izin var.
* Human readable.
* XML e göre daha az yer tutuyor.
* Satır bazlı sorgularda hızlı

### Disadvantages

* Anahtar/Colon isimleri tekrar ediyor. Depolama verimsiz.
* Attribute/anahtar bazlı gittiğimizde performans kötü.
* Text based olduğu için parsing verimsizlik ?!?
* No type forcing.

## Fix Length

## Advantages

* Fast offset based parsing
* Prevent memory/disk fragmentation (SLAB allocators)
* Human readable.
* Satır bazlı sorgularda hızlı

## Disadvantages

* Redundant space usage
* No type forcing.
* Text based olduğu için parsing verimsizlik ?!?
* No metadata information.
* Nested/Complex typelara izin yok.
* Colon bazlı sorgularda hızlı
* Schema evaluation (type resizing) çok zor.
* Yeni alan sadece sona eklenebiliyor.


