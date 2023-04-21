# Python Dokümantasyonu Türkçe Çevirisi

[![discord](https://img.shields.io/badge/Discord-python--docs--tr-5865F2?style=for-the-badge&logo=Discord)](https://discord.gg/Af5z7JHshX) [![linkedin](https://img.shields.io/badge/LinkedIn-python--docs--tr-0A66C2?style=for-the-badge&logo=LinkedIn)](https://www.linkedin.com/company/python-docs-tr) [![gmail](https://img.shields.io/badge/GMail-python--docs--tr-EA4335?style=for-the-badge&logo=Gmail)](mailto:python.docs.tr@gmail.com)

## Dokümantasyon Katkı Anlaşması

Bu proje gönüllü çevirmenler ve python-docs-tr ekibi iş birliğinde sürdürülmektedir. Bu anlaşma, çeviri sürecindeki tüm katılımcıların haklarını ve sorumluluklarını tanımlamaktadır. Projeyi GitHub ve diğer halka açık mecralarda yayınlayarak ve projeye katkı veya iyileştirme yaparak, katkılarınızı CC0 lisansı altında PSF'in kullanımına sunmuş olursunuz. Karşılığında, çeviri yaptığınız kısım için halka açık olarak övgü toplayabilirsiniz. Eğer çeviriniz PSF tarafından kabul edilirse, (eğer isterseniz) [TRANSLATORS](TRANSLATORS) dosyasına isminizi ekleyerek bir yama gönderebilirsiniz. Yaptığınız katkı metinsel olmasa bile Python topluluğuna katılımınızı memnuniyetle karşılıyor ve herkesi katkı sağlamaya davet ediyoruz.

Çalışmanızı dokümantasyona dahil edilmek üzere PSF'e göndererek bu anlaşmayı kabul etmiş sayılırsınız.

## Çeviriye Katkıda Bulunmak

### Gereklilikler

- Bir [GitHub hesabı](https://github.com)
- Yüklü bir [Git](https://git-scm.com/) istemcisi
- ``.po`` dosyalarını düzenlemek için [poedit](https://poedit.net/) gibi bir program
- Yüklü bir Python ve ``pip`` versiyonu (en son stabil olan versiyon önerilir)

### Adımlar

#### Rezervasyon

Çeviri yapmak istediğiniz bir dosyaya rezervasyon oluşturmak için şu adımları izleyin:

1. `Issues > New Issue > Get started` düğmelerini takip ederek rezervasyon formunu açın.
2. foo/bar.po taslağını, çalışmak istediğiniz dosyanın yolu ile değiştirin.
   - Örnegin, "library/functions.po üzerinde çalışmak istiyorum".
3. Submit new issue düğmesine tıklayarak rezervasyonunuzu oluşturun ve çeviriyi üstlenin.

#### Projeye ilk başlarken

1. Projeyi GitHub üzerinden forklayın.
2. Forkladığınız projeyi bilgisayarınıza klonlayın.
   - ``git clone https://github.com/<kullaniciadi>/python-docs-tr.git``
3. Çevirmek istediğiniz dosyanın ismiyle bir branch oluşturun.
   - Örneğin, ``library/functions.po`` dosyasını çevirmek istiyorsanız, ``library-functions`` adında bir branch oluşturun.
   - ``git checkout -b library-functions``
4. Gerekli paketleri yükleyin.
   - ``python -m pip install --upgrade -r requirements.txt``
5. Syntax hatalarını commit öncesi otomatik kontrol eden ``pre-commit`` 'i kurun.
   - ``pre-commit install``


#### Çalışma döngüsü

1. Doğru branchte olduğunuzdan emin olun.
   - ``git checkout library-functions``
2. Çevirmek istediğiniz dosyayı poedit ile açın.
3. Çevirilerinizi yapın ve kaydedin.
4. Çevirilerinizi kendi forkunuza yükleyin.
   - ``git add library/functions.po``
   - ``git commit -m "Çeviri tamamlandı."``
   - ``git push origin library-functions``


#### Çeviri tamamlandıktan sonra

1. TRANSLATORS dosyasına isminizi ekleyin. (Çeviri kabul edilirse yaptığınız katkı için övgü toplayabilirsiniz.)
2. GitHub üzerinden çevirilerinizi göndermek için bir pull request oluşturun.
3. Çevirilerinizin kabul edilmesini bekleyin.
   - Bu süreçte çevirileriniz, uygunluğunu ve yazım hatalarını değerlendirmek için birkaç kişi tarafından incelenecektir.
   - İncelemenin sonucunda bazı değişiklikler yapmanız istenebilir.

### Dikkat Etmeniz Gerekenler

1. Çeviri yaparken yararlanabileceğiniz kaynaklar:
   - İmla kuralları ve Türkçe anlamlar: [Türk Dil Kurumu](https://sozluk.gov.tr/)
   - İngilizce-Türkçe terim çevirileri: [Bilkent Üniversitesi Bilişim Sözlüğü](http://cayfer.bilkent.edu.tr/~cayfer/bilisim-sozlugu/tbd-ing-trk-sozluk.htm)
   - İngilizce-Türkçe sözlük: [Tureng](https://tureng.com/en/turkish-english)
2. Çevirilerinizde terimlerin doğru kullanılmasına dikkat edin. Örneğin:
   - ``string`` ve ``str`` terimleri aynı şeyi temsil etmemektedir.
   - ``string`` terimi, Python'da metinleri temsil etmek için kullanılan bir veri tipi olup, ``str`` ise bu veri tipiyle ilgili fonksiyonlar ve metotlarda kullanılan bir kısaltmadır.
3. Çevirilerinizde bir terimin birden fazla çevirisi olması durumunda, önceki çevirilerde kullanılan çeviriyi kullanın.
   - Örneğin, ``string`` terimi için ``dize`` ve ``metin`` çevirileri kullanılmıştır. Bu durumda ``dize`` terimini tercih edin.
