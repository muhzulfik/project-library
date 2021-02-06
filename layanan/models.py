from django.db import models

from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class catalog(models.Model):

    LOKASI = (
                ('semua lokasi','Semua Lokasi'),
                ('perpustakaan ft','Perpustakaan FT'),
                ('perpustakaan fkip','Perpustakaan FKIP'),
                ('perpustakaan fk','Perpustakaan FK'),
                ('perpustakaan fisip','Perpustakaan FISIP'),
                ('perpustakaan ffs','Perpustakaan FFS'),
                ('perpustakaan feb','Perpustakaan FEB'),   
            )

    KATALOG_JURUSAN = (
                ('psikologi','Psikologi'),
                ('informatika','Informatika'),
                ('teknik mesin','Teknik Mesin'),
                ('teknik elektro','Teknik Elektro'),
                ('kedokteran','Kedokteran'),
                ('farmasi','Farmasi'),
                ('biologi','Biologi'),
                ('fisika','Fisika'),
                ('ekonomi','Ekonomi'),
                ('akuntansi','Akuntansi'),
                ('pendidikan guru sekolah dasar','Pendidikan Guru Sekolah Dasar'),
                ('sastra indonesia','Sasta Indonesia'),
                ('sastra inggris','Sastra Inggris'),
                ('ilmu politik','Ilmu Politik'),
            )

    BAHASA = (
        ('indonesia','Indonesia'),
        ('english','English')
    )

    lokasi = models.CharField(max_length=200, choices=LOKASI, default='semua lokasi')
    judul = models.TextField(blank=True)
    penulis = models.CharField(max_length=200, blank=True)
    katalog_jurusan = models.CharField(max_length=200, choices=KATALOG_JURUSAN, default='psikologi')
    keyword = models.TextField(null=True, blank=True)
    jumlah_buku = models.IntegerField()
    bahasa = models.CharField(max_length=200, null=True, choices=BAHASA, default='indonesia')

    def __str__(self):
        return "{}".format(self.judul)

class journal(models.Model):
    LOKASI = (
                ('semua lokasi','Semua Lokasi'),
                ('perpustakaan ft','Perpustakaan FT'),
                ('perpustakaan fkip','Perpustakaan FKIP'),
                ('perpustakaan fk','Perpustakaan FK'),
                ('perpustakaan fisip','Perpustakaan FISIP'),
                ('perpustakaan ffs','Perpustakaan FFS'),
                ('perpustakaan feb','Perpustakaan FEB'),   
            )

    BAHASA = (
        ('indonesia','Indonesia'),
        ('english','English')
    )

    judul_artikel   = models.TextField(blank=True)
    judul_terbitan  = models.TextField()
    issn            = models.IntegerField(blank=True)
    bahasa          = models.CharField(max_length=200, choices=BAHASA, default='indonesia')
    tempat_terbit   = models.CharField(max_length=200)
    tahun           = models.IntegerField()
    volume          = models.CharField(max_length=200)
    penerbit        = models.CharField(max_length=200)
    frekuensi_penerbitan = models.CharField(max_length=200)
    penulis         = models.CharField(max_length=200, blank=True)
    abstraksi       = models.TextField()
    kata_kunci      = models.TextField(blank=True)
    lokasi          = models.CharField(max_length=200, blank=True, choices=LOKASI, default='semua lokasi')
    terakreditasi   = models.CharField(max_length=200)
    slug            = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul_artikel)
        super().save()

    def get_absolute_url(self):
        return reverse('layanan:journal_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return "{}".format(self.judul_artikel)

class repository(models.Model):
    JENIS_PENULISAN = (
                ('semua penulisan', 'Semua Penulisan'),
                ('disertasi','Disertasi'),
                ('tesis','Tesis'),
                ('skripsi','Skripsi'),
            )

    LOKASI = (
                ('semua fakultas','Semua Fakultas'),
                ('ekonomi bisnis','Ekonomi dan Bisnis'),
                ('teknik','Teknik'),
                ('agama islam','Agama Islam'),
                ('psikologi','Psikologi'),
                ('kedokteran','Kedokteran'),
                ('keguruan','Keguruan dan Ilmu Pendidikan'),
                ('ilmu kesehatan','Ilmu Ilmu Kesehatan'),
                ('farmasi','Farmasi dan Sains'),
                ('sosial politik', 'Ilmu Sosial dan Ilmu Politik'),
                ('pascasarjana','Pascasarjana')  
            )

    judul           = models.TextField(blank=True)
    penulis         = models.CharField(max_length=200, blank=True)
    abstraksi       = models.TextField()
    keyword         = models.TextField(null=True, blank=True)
    pembimbing      = models.CharField(max_length=200)
    jenis_penulisan = models.CharField(max_length=200, choices=JENIS_PENULISAN, default='semua penulisan')
    lokasi          = models.CharField(max_length=200, choices=LOKASI, default='semua fakultas')
    slug            = models.SlugField(blank=True, editable=False)


    def __str__(self):
        return "{}".format(self.judul)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        return reverse('layanan:repository_detail', kwargs={'slug': self.slug})