# Turkish Translation of The Python Documentation

## Dokümantasyon Katkı Anlaşması

Bu proje gönüllü çevirmenler ve python-docs-tr ekibi iş birliğinde sürdürülmektedir. Bu anlaşma, çeviri sürecindeki tüm katılımcıların haklarını ve sorumluluklarını tanımlamaktadır. Projeyi GitHub ve diğer halka açık mecralarda yayınlayarak ve projeye katkı veya iyileştirme yaparak, katkılarınızı CC0 lisansı altında PSF'in kullanımına sunmuş olursunuz. Karşılığında, çeviri yaptığınız kısım için halka açık olarak övgü toplayabilirsiniz. Eğer çeviriniz PSF tarafından kabul edilirse, (eğer isterseniz) TRANSLATORS dosyasına isminizi ekleyerek bir yama gönderebilirsiniz. Yaptığınız katkı metinsel olmasa bile Python topluluğuna katılımınızı memnuniyetle karşılıyor ve herkesi katkı sağlamaya davet ediyoruz.

Çalışmanızı dokümantasyona dahil edilmek üzere PSF'e göndererek bu anlaşmayı kabul etmiş sayılırsınız.

## Çeviriye Katkıda Bulunmak

### Gereklilikler

- Bir [GitHub hesabı](https://github.com)
- Yüklü bir [Git](https://git-scm.com/) istemcisi
- ``.po`` dosyalarını düzenlemek için [poedit](https://poedit.net/) gibi bir program

### Adımlar

#### Projeye ilk başlarken

1. Projeyi GitHub üzerinden forklayın.
2. Forkladığınız projeyi bilgisayarınıza klonlayın.
   - ``git clone https://github.com/<kullaniciadi>/python-docs-tr.git``
3. Çevirmek istediğiniz dosyanın ismiyle bir branch oluşturun.
   - Örneğin, ``library/functions.po`` dosyasını çevirmek istiyorsanız, ``library-functions`` adında bir branch oluşturun.
   - ``git checkout -b library-functions``


#### Çalışma döngüsü

1. Doğru branchte olduğunuzdan emin olun.
   - ``git checkout library-functions``
2. Çevirmek istediğiniz dosyayı poedit ile açın.
3. Çevirilerinizi kaydedin.
4. Çevirilerinizi kendi forkunuzda kaydedin.
   - ``git add library/functions.po``
   - ``git commit -m "Çeviri tamamlandı."``
   - ``git push origin library-functions``