from django.forms import ModelForm
from django import forms
from layanan.models import catalog, journal, repository

class catalogForm(forms.ModelForm):
    class Meta:
        model = catalog
        fields = '__all__'
            
        widgets = {
            'lokasi' : forms.Select({'class':'form-select', 'type':'text','name':'lokasi', 'id':'lokasi'}),
            'judul' : forms.TextInput({'class':'form-control', 'type':'text', 'name':'judul', 'placeholder':'Judul', 'id':'judul'}),
            'katalog_jurusan' : forms.Select({'class':'form-select', 'type':'text','name':'katalog_jurusan', 'id':'katalog_jurusan'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'text' ,'name':'penulis', 'placeholder':'Penulis', 'id':'penulis'}),
            'keyword' : forms.TextInput({'class':'form-control', 'type':'search' ,'name':'keyword', 'placeholder':'Keyword', 'id':'keyword'}),
            'jumlah_buku' : forms.NumberInput({'class':'form-control', 'type':'search', 'name':'jumlah_buku', 'placeholder':'Jumlah Buku', 'id':'jumlah_buku'}),
            'bahasa' : forms.Select({'class':'form-select', 'type':'search','name':'bahasa', 'id':'bahasa'}),
        }


class journalForm(forms.ModelForm):
    class Meta:
        model = journal
        fields = '__all__'

        widgets = {
            'judul_artikel' : forms.TextInput({'class':'form-control', 'type':'search','name':'judul_artikel', 'placeholder':'Judul Artikel'}),
            'judul_terbitan' : forms.TextInput({'class':'form-control', 'type':'search','name':'judul_terbitan', 'placeholder':'Judul Terbitan'}),
            'issn' : forms.NumberInput({'class':'form-control', 'type':'search','name':'issn', 'placeholder':'ISSN'}),
            'bahasa' : forms.Select({'class':'form-select', 'type':'search','name':'bahasa', 'placeholder':'Bahasa'}),
            'tempat_terbit' : forms.TextInput({'class':'form-control', 'type':'search','name':'tempat_terbit', 'placeholder':'Tempat Terbit'}),
            'tahun' : forms.NumberInput({'class':'form-control', 'type':'search','name':'tahun', 'placeholder':'Tahun'}),
            'volume' : forms.TextInput({'class':'form-control', 'type':'search','name':'volume', 'placeholder':'Volume'}),
            'penerbit' : forms.TextInput({'class':'form-control', 'type':'search','name':'penerbit', 'placeholder':'Penerbit'}),
            'frekuensi_penerbitan' : forms.TextInput({'class':'form-control', 'type':'search','name':'frekuensi_penerbitan', 'placeholder':'Frekuensi Penerbitan'}),
            'abstraksi' : forms.Textarea({'class':'form-control', 'type':'search','name':'abstraksi', 'placeholder':'Abstraksi'}),
            'terakreditasi' : forms.TextInput({'class':'form-control', 'type':'search','name':'terakreditasi', 'placeholder':'Terakreditasi'}),
            'kata_kunci' : forms.TextInput({'class':'form-control', 'type':'search','name':'kata_kunci', 'placeholder':'Keyword'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'search','name':'penulis', 'placeholder':'Penulis'}),
            'lokasi' : forms.Select({'class':'form-select', 'type':'search','name':'lokasi', 'placeholder':'Lokasi'}),
        }

class repositoryForm(forms.ModelForm):
    class Meta:
        model = repository
        fields = '__all__'

        widgets = {
            'jenis_penulisan' : forms.Select({'class':'form-select', 'type':'search','name':'jenis'}),
            'judul' : forms.TextInput({'class':'form-control', 'type':'search','name':'judul', 'placeholder':'Judul'}),
            'abstraksi' : forms.Textarea({'class':'form-control', 'type':'search','name':'abstraksi', 'placeholder':'Abstraksi'}),
            'pembimbing' : forms.TextInput({'class':'form-control', 'type':'search','name':'pembimbing', 'placeholder':'Pembimbing'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'search','name':'penulis', 'placeholder':'Penulis'}),
            'keyword' : forms.TextInput({'class':'form-control', 'type':'search','name':'keyword', 'placeholder':'Keyword'}),
            'lokasi' : forms.Select({'class':'form-select', 'type':'search','name':'lokasi', 'placeholder':'Lokasi'})    
        }

