# Zoom erişilebilirlik iyileştirmeleri #

* Yazarlar: Mohamad Suliman, Eilana Benish
* [kararlı sürüm][1]ü indir
* NVDA uyumluluğu: 2018.4 - 2020.2

Bu eklenti, Zoom programının erişilebilirliğini arttıran özellikler
içermektedir. Toplantılar sırasında farklı olaylardan gelen uyarıları daha
kolay takip edebilmek için klavye kısayolları sağlar. Ayrıca, uzaktan
kontrol işlevinin daha erişilebilir hale getirilmesi gibi birçok farklı
iyileştirme içerir.

## Toplantı sırasında uyarıları kontrol etmek için klavye kısayolları

* NVDA + Shift + A: farklı bildirim uyarı modları arasında geçiş
  yapar. Aşağıdaki modlar kullanılabilir:

    * Tüm uyarıları bildir, tüm uyarıları bildirir.
    * Uyarıları bip sesiyle bildir, NVDA'nın Zoom'da görüntülenen her uyarı
      için kısa bir bip sesi çalar.
    * uyarıları bildirme,  NVDA hiçbir uyarıyı bildirmez.
    * Özel, sadece seçilen uyarılar bildirilir. Bu, eklentinin ayarlar
      iletişim kutusu kullanılarak veya bu işlev için atanmış klavye
      kısayolu kullanılarak yapılabilir.

Her bir uyarı türünün bildirimini açıp kapatmak için aşağıdaki kısayollar
kullanılabilir. Not: bu ayar, sadece özel mod seçiliyken etkilidir.

* NVDA + Ctrl + 1: Katılımcı Toplantıya Katıldı/Toplantıdan Ayrıldı
  (Yalnızca Toplantı Sahibi)
* NVDA + Ctrl + 2: Katılımcı Katıldı/Bekleme Odasından Ayrıldı (Yalnızca
  Toplantı Sahibi)
* NVDA + Ctrl + 3: Ses toplantı sahibi tarafından kapatıldı
* NVDA + Ctrl + 4: Video toplantı sahibi Tarafından Durduruldu
* NVDA + Ctrl + 5: Bir katılımcı tarafından ekran Paylaşımı
  Başlatıldı/Durduruldu
* NVDA + Ctrl + 6: Kayıt İzni Verildi/İptal Edildi
* NVDA + Ctrl + 7: Herkese Açık Toplantı İçi Sohbet mesajı Alındı
* NVDA + Ctrl + 8: Özel Toplantı İçi Sohbet mesajı Alındı
* NVDA + Ctrl + 9: Toplantı İçi Dosya Yüklemesi Tamamlandı
* NVDA + Ctrl + 0: Sunum izni Verildi/İptal Edildi
* NVDA + Shift + Ctrl + 1: Katılımcı Elini Kaldırdı/İndirdi (Yalnızca
  Toplantı Sahibi)
* NVDA + Shift + Ctrl + 2: Uzaktan Kontrol İzni Verildi/İptal Edildi
* NVDA + Shift + Ctrl + 3: IM sohbet mesajı alındı


Eklentinin istenen şekilde çalışması için Zoom erişilebilirlik
iyileştirmeleri ayarlarında tüm uyarı türlerini Bildir seçeneğinin işaretli
olduğuna emin olun. 

## Eklenti iletişim kutusunu açmak için klavye kısayolu:

NVDA + Z Eklenti iletişim kutusunu açar !

Bu iletişim kutusunu kullanarak şunları yapabilirsiniz:

* Bildirilen ve bildirilmeyen uyarıları görme,
* Bildirilmesini istediğiniz uyarı türlerini eçme,
* Uyarı bildirim modunu seçme,
* Özel değişiklikleri kaydetme.

## Uzaktan Kontrol

Uzaktan kontrol izni verildikten sonra, NVDA + O klavye kısayolu, uzaktan
kontrol ekranı ve kendi ekranınız arasında geçiş yapmanızı sağlar.

Diğer ekranı uzaktan kontrol edebilmek için odağın toplantı kontrollerinden
birinde olması gerektiğini unutmayın.

## Önemli:

Özel bildirim modu ayarı, şuanda sadece kullanıcı dili İngilizce olarak
ayarlandığında çalışmaktadır.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=zoom
