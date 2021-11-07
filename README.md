# Tracking-a-Laser-pointer-with-Python-and-OpenCV
Tracking a Laser pointer with Python and OpenCV

Lazer Takip Sistemi

Pixel Tracking görüntü işleme tekniğiyle çalışan bir izleme sistemidir. Şu durumda lazer noktasını takip edebilen bu sistem bir bigisayara bağımlı olarak çalışır durumdadır. Kameradan alınan görüntüler Opencv ile Vs programında işlendikten sonra elde edilen veriler yazılım ile kontrol edilir, aynı şekilde kamera da bilgisayarla iletişimini USB port aracılığıyla yapar, görüntüler hazırlanan yazılımla alınır ve belli aralıklarda fotoğraflar çekilir. Fotoğraf içerisinde istenilen bir değerde görüntü aranmaya başlanır ve aranan değer bulunduğunda belirlenen koordinata kameranın odaklanması sağlanır. Bu işlemler belirli bir algoritma çerçevesinde gerçekleşir. Sistemin çalışma hızı (tepki hızı) burada önemli bir parametredir ve tasarlanan algoritma bu aşamada önem arzeder. 
OpenCV Kütüphanesi ile Görüntü İşleme
Görüntü işleme için kullanılan en popüler kütüphanelerden birisi OpenCV kütüphanesidir. Bu çalışma kapsamındaki örneklerin tamamı Python dili ile yazılmış ve Visual Studio Code ide’si kullanılmıştır. Öncelikle kütüphaneler import edilir. Şekil 1 de Editör penceresi nin şekli görülmektedir
.  
                                                         Şekil 1   Editör Penceceresi


                                   
Kameradan Görüntünün Alınması 

Kamera görüntüsünün opencv  içerisine alınması birkaç aşamadan ibarettir. Kamera daha önceden bilgisayara tanıtılmış olmalı başka bir deyişle driverlarının yüklenmiş olması gerekir. Bu sayede opencv kütüphanesi gerekli olan kamera bilgisine ulaşabilecektir. Kamera bilgisayara USB den bağlanabilir yada laptopunuzun kendi kamerası kullanılabilir çok önemli olmayan bir durumdur. OpenCV ile kameradan görüntü alabilmek için VideoCapture nesnesi oluşturulmalıdır. Bu nesneyi oluştururken parametre olarak cihaz indeksi ya da video dosyasının ismi gönderilir.


Kamera

Cihaz indeksi kameranın numarasını belirten bir sayıdır. Normal durumda bir bilgisayar üzerinde bir kamera olacağını varsayarsak parametre olarak 0 gönderebiliriz. Eğer cihazda 2 kamera varsa ve 2.kameradan görüntü almak istiyorsak o zaman 1 yazılması yeterli olacaktır.
Kameranın görüntüsünü almak için başlangıçta editöre şu komutlar yazılır.
lazer = cv2.VideoCapture(1)

lazer.set(cv2.CAP_PROP_FRAME_WIDTH,640)
lazer.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
while (1):
    

ret, frame = lazer.read()
hsvrenkdonusum = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

Bu komut ile kamera bilgisi alınmaya başlanır ancak görüntünün varlığından emin olmak için o görüntüye bakmak gereklidir bir başka deyişle görüntüyü açmak gereklidir. Bunun için ise;
cv2.imshow('Lazer Takip', frame)





komutu kullanılacaktır. Programı yazarken hafızaya alınan verilerin değişkenlere atılması gerektiği unutulmamalıdır. Şekil 2 de alınan kamera görüntüsü gösterilmiştir. 

 
Şekil 2
Görüntüden Resim Yakalama

Akıcı görüntü editör ekranına alındıktan sonra ara ara resimlerin alınması gerekir resim
çekme aralıkları tamamen algoritmayla alakalıdır. While döngüsü içinde görüntün sürekli alınması gerekir. Resim yakalamak için ;



while (1):


ret, frame = lazer.read()


komutu kullanılacaktır. Alınan resim bir değişkende saklanır. Resmin boyutları kameranın çözünürlüğüyle ilişki olduğu gibi bu durum opencv de ayarlanabilir. 640X480 resim formatı bu proje için uygundur.Bunun için;


lazer.set(cv2.CAP_PROP_FRAME_WIDTH,640)
lazer.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


komutu kullanılacaktır. Bu formatın daha yüksek olması tatbikî daha komplike sistemlerde avantaj sağlayacaktır. 


Resmin RGB tonlarıyla uğraşmak yerine siyah beyaz bir resim ile çalışmak daha uygun olacağından dolayı resmin formatında değişiklik yapmak gerekir, bunun için farlı bir değişkene RGB tonundaki resim siyah-beyaz olarak kaydedilecektir bunu;

    hsvrenkdonusum = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv2.threshold(gray, 250, 255, cv2.THRESH_B      INARY)

komutuyla yapıyoruz.. Resimleri görmek için ise ;
cv2.imshow('Lazer Takip', frame)
cv2.imshow('Lazer Takip', gray )
cv2.imshow('Lazer Takip', hsvrenkdonusum )

komutlarını kullanıyoruz. Resmin sayısal pixel değerlerini Debug modda görmemiz mümkünüdr. Bu sayede  resim üzerinde analiz yapma fırsatı elde ederiz. Bunu;
 
Şekil 3



Debug Modda ekranın sol tarafında Şekil 3’de görüldüğü şekilde inceleyebiliriz. Örnek olarak Frame matrisinin renk değerlerini,shape ile matrisin boyutlarını,max ve min değerleri ile en büyük ve en düşük renk aralıklarını görmek mümkün.

Resimden Pixel Değerlerinin Okuması 

Pixel değerlerinin her defasında kontrol edilmesi gereklidir çünkü aranan görüntünün nerde olduğu saptanacaktır. Bunun için öncelikle değerlerin resim içesinden okunup yer vektörünün oluşturulması gerekir. Pixel değerini ;

func(matris):

Fonksiyonu ile gerçekleştiriyoruz burada func; fonksiyon ismidir,komut değildir bu yüzden fonksiyon isminin ne olacağı önemsizdir. Parantez içindeki “matris” isimli değişken fonksiyona gönderilen matrisi temsil eder yani çekilen resim 640 x 480 pixel olduğundan oluşturula dizinin boyutu bu değerde olmalı ı ve bu değerlere ulaşmak için kullanılan değişkenler de;

matris.shape[0]
matris.shape[1]




Komutları ile matrisin genişlik ve yükseklik değerlerine ulaşabiliriz. shape[0] genişlik , shape[1] yükseklik değerlerini verir.

Bu duruma biraz daha ayrıntılı bakacak olursak; matris.shape[0], 640 değerine ulaşabilen yani 1 den 640 a kadar artabilen bir değişkeni matris.shape[1] ise 1 den 480 e kadar artan bir değişkeni temsil edecek ve matriste en yüksek değerlikli ışık renk değeri olan 255 beyaz noktasını arayacaktır  ancak artışlar belirli bir döngü içerisinde olacağından dolayı artım durumunun ve pozisyonunun ne şekilde olacağı tamamen tasarımcıya has bir özellikdir. Örneğin soladan sağa doğru bir tarama yapmak için oluşturulması gereken döngü tasarımı;






for ax in range(0,matris.shape[0],1):
for bx in range(0,matris.shape[1],1):
if (matris[ax][bx]) == 255:

say=say+1
return say

şeklinde olmalıdır. Bu döngü sayesinde matristeki renk değeri 255 e eşit olan pikseller elde edilir. Değer okunduktan sonra fonksiyon dışındaki while döngüsü içerinde iç içe for döngüsü oluşturulur. Burada elde ettiğimiz fotoğrafın yani frame değişkenini cvtColor fonksiyonu ile gray matris dediğimiz siyah beyaz matrise dönüştürmüştük. Elde edilen resmin matris değerlerine baktığınızda 0–255 arasında değerlerden oluştuğunu görüyoruz. Bazı durumlarda bu matrisin yalnızca 0 ve 255 değerlerinden oluşmasını isteyebiliriz . Böyle durumlarda threshold fonksiyonu kullanılmaktadır. 

    (thresh, blackAndWhiteFrame) = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

Oluşturulan yeni matris blackAndWhiteFrame adlı değişkene atanır böylelikle iki değer 
aralıklı yeni matris elde edilmiş olur.

array([[  0,   0,   0, ..., 255, 255, 255],
[  0,   0,   0, ..., 255, 255, 255],
[  0,   0,   0, ..., 255, 255, 255],
...,
[  0,   0,   0, ...,   0,   0,   0],
[  0,   0,   0, ...,   0,   0,   0],
[  0,   0,   0, ...,   0,   0,   0]], dtype=uint8)


Görüntümüzü eşikleme işlemine sokmadan önce görüntümüzün renk uzayını gri renk uzayına çevirmemiz gerekmektedir, fonksiyonun aldığı ilk girdi gri uzaydaki görüntümüzdür. İkinci girdi ise istediğimiz eşik değeridir, yani pixel değerlerini sınıflandırmak için kullanacağımız değerdir. Üçüncü girdi ise maksimum değerdir yani pixel değeri girdiğimiz eşik değerinden fazlaysa o pixele atanacak değerdir. Opencv kütüphanesi farkı eşikleme türlerini bize sunar, dördüncü parametre olarak da bu türlerden birisini yazarız. 







Oluşan blackAndWhiteFrame adlı yeni matris üzerinde for döngüsü ile tarama işlemi yapılır. Bu duruma biraz daha ayrıntılı bakacak olursak; blackAndWhiteFrame.shape[0], 640 değerine ulaşabilen yani 0 dan 640 a kadar 40 arlı olacak şekilde artabilen bir değişkeni blackAndWhiteFrame.shape[1] ise 0 dan 480 e kadar kadar 40 arlı olacak şekilde artan bir değişkeni temsil edecek. Matrisi 40 x 40’lık parçalara bölerek soldan sağa olacak şekilde arama yaparız.En yüksek yoğunluklu 40 x 40 lık matrisin bulunduğu yer ise aranan yerdir.Şu şekilde gerçekleştirilir;  



for i in range(0,blackAndWhiteFrame.shape[0],40): #satır
for j in range(0,blackAndWhiteFrame.shape[1],40): #sutun

matris=blackAndWhiteFrame[j:40+j,i:40+i]
beyazNoktaSayisi=func(matris)
if(beyazNoktaSayisi>=maxBeyazNoktaSayisi):
maxFrameCorners=[i,j,40+i,40+j]
maxBeyazNoktaSayisi=beyazNoktaSayisi



Burayı şu şekilde açıklayabiliriz; blackAndWhiteFrame adlı matrisi 40 x 40 olarak parçalara ayırıp matris adlı değişkene atadık.

matris=blackAndWhiteFrame[j:40+j,i:40+i]

func adlı fonksiyondan geri dönüş olarak aldığımız matris değerini beyazNoktaSayisi adlı değişkene atadık.Bu sayede en yüksek yoğunluk 40 x40 lık matrisi değişkende tuttuk.


beyazNoktaSayisi=func(matris)



Bu tasarımla resim içerisindeki tüm pixel değerleri elde edilebilir. Değer okundukdan sonra bir değişkende saklanır değeri görmek için değişkenin editör ekranına yazdırılması gerekir. 


Resmin Analiz Edilmesi 

Kameradan alınan görüntünün incelenmesi için analizin neye göre yapılacağına karar verilmesi önemli bir hususdur. Lazer takibi yapılan bu projede öncelikle lazerin zemin üzerinde bıraktığı iz analiz edilmiştir. Kameranın lazeri görmesi manuel olarak sağlanmış defalarca resim örneği alınmış ve renk değerleri kaydedilmiştir. Lazerin zemine veya kameranın lazer ve zemine olan uzaklıkları değerlendirilmiştir. Lazer ışığının ve ortam parlaklığının etkisinin çalışmayı büyük oranda etkilediği farkedilmiştir ve bu değerlerin belirli bir oranda olacağı düşünülerek tölerans değerleri uygun şekilde atanmıştır. Analiz python OpenCv kütüphanesi üzerinde yapılmıştır Şekil 4’de bir analiz örneği gösterilmektedir. 

 
Şekil 4
Matris üzerindeki beyaz renk piksellerinin daha iyi anlaşılması adına aşağıda benzer bir projenin matlab üzerinden alınmış ekran görüntüleri bulunmaktadır.
 
Şekil 5







 
Şekil 6

Hareketli görüntüden resim çektirildikten sonra elde edilen bu resme ayrıntılı olarak bakılması gereklidir. Resmin renk bileşenlerinin değerlerinin nasıl değiştiği analiz edilmelidir. Bunun için resme zoom yapıyoruz. Şekil 5
de resme zoom yapılmıştır, lazerin zemin üzerinde bıraktığı izin pembe ve beyaz tonlarda
olduğu, kırmızı bir halka içersinde beyaz bir bulutun olduğu açık olarak görülmektedir.



Örnek resme biraz ayrıntılı bakıldığında herbir pixel değerinin 3 bileşenden meydana geldiği
görülmektedir. Bu bileşenler resmin RGB kanallarını temsil ederler (Red Green Blue).
Resimde 3 kanalda birden veya herhangi bir kanalda çalışılmak isteniyorsa yazılımın o
şekilde oluşturulması gerekir. Bu proje için 3 kanalda birden çalışmak fazla bir önem
arzetmediğinden ya da alınan görüntünün çak hassa olmaması sebebiyle işimizi biraz daha
kolaylaştırıyoruz, kanalları tek boyuta indiriyoruz. Bunun için resmimizi siyah beyaz
yapmamız gerekecek.





 
Şekil 7


Konunun başında bahsedilmişti renkli resim siyah beyaz yapıldıktan
sonra siyah beyaz resim zoom edildiğinde alınan görüntünün durumu Şekil 6 de
görülmektedir. Resme biraz daha zoom yapıldığında Şekil 6 elde ediliyor. Sayıları daha iyi görebilmek için resme biraz daha yaklaşıyoruz ve Şekil 7yi elde ediyoruz. Bu aşamadan sonra lazerin izinin ne değerde olduğu kolayca anlaşılabilmektedir. Resme etraflı
bakıldığında ortalama lazer parlaklığı 250 nin üzerinde bir renk tonuna sahip o halde resim
içersinde aranması gereken değerin 250 nin üzerinde herhangi bir tonun bulunması gerektiği
yönün de olmalı. Maksimum değer 255 dir minumun değer ise 0 dır. 255 sayısı en parlak
rengi yani beyazı, 0 ise en mat rengi yani siyahı temsil eder. Lazeri bulmaya çalışırken bir
anlamda en parlak rengi bulmaya çalıştık. Yazılım oluştururken bir değişken oluşturulmalı ve
bu değişkene tolerans değeri olarak 250 değeri atanmalıdır ve herbir döngü içersinde de okunan pixel değerlerinin 250 den büyük veya küçük olup olmadıkları kontrol edilmelidir. Tolerans değeri ortama göre değişebilir daha önce bahsettiğim gibi ortam parlaklığı ve lazerin zemin üzerindeki parlaklığı örneklerden de görüldüğü gibi çok önemlidir. 




Yazılım içersinde tolerans değerinin sorgulanmasını biz zaten fonksiyon içinde su sekilde yapmıstık ;

if (matris[ax][bx]) >=250 or <=255:

Nokta Takibi

Bu aşamaya kadar noktanın hangi konumda olduğu belirlenmiş oldu bundan sonraki aşama
noktayı sürekli bir şekilde takip etmektir. Bu konuda bazı sıkıntılar yaşanmıyor değildir. Bu
tarz sıkıntılardan bir tanesi hız konusudur, sistem 640*480 = 307200 pixellik resmi hızlı bir
şekilde taramak sistemi yavaşlattığından ve ekranda görülen webcam görüntüsünde takipte yavaşlıklar ve takılmalar olduğundan birtakım çözüm metotlarına gidilmiştir. Burada iki seçenek söz konusudur birincisi işlemciyi
hızlandırmak ikincisi resim boyutunu azaltmak. Bu konuda tasarımcı kendine göre mimari
oluşturmalıdır.Proje sonunda nokta takibinin yavaşlığı sebebi ile kodda değişişiklikler yapılmaya gidildi ve kodun büyük bir kısmı değişti.Kodun şuan ki son hali işe şu şekildeydi;


import cv2
import numpy as np

lazer = cv2.VideoCapture(1)

lazer.set(cv2.CAP_PROP_FRAME_WIDTH,640)
lazer.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


def  func(matris):
say=0
for ax in range(0,matris.shape[0],1):
for bx in range(0,matris.shape[1],1):
if (matris[ax][bx]) >=250 or <=255:

say=say+1
return say





while (1):


    ret, frame = lazer.read()
    hsvrenkdonusum = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)


    lower_kırmızı = np.array([160, 100, 255])
    upper_kırmızı = np.array([179, 255, 255])
    maskeleme = cv2.inRange(hsvrenkdonusum, lower_kırmızı, upper_kırmızı)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(maskeleme)
    print("minimum val:",minVal)
    print("max value",maxVal)


    #cv2.circle(frame, maxLoc, 50, (60, 255, 100), 4, cv2.LINE_AA)
    
    cv2.imwrite("foto.jpg", frame)
    
    maxFrameCorners=[]
    maxBeyazNoktaSayisi=0
    for i in range(0,blackAndWhiteFrame.shape[0],40): #satır
        for j in range(0,blackAndWhiteFrame.shape[1],40): #sutun

            matris=blackAndWhiteFrame[j:40+j,i:40+i]
            beyazNoktaSayisi=func(matris)
            if(beyazNoktaSayisi>=maxBeyazNoktaSayisi):
                maxFrameCorners=[i,j,40+i,40+j]
                maxBeyazNoktaSayisi=beyazNoktaSayisi
            
    
    print("max Beyaz Nokta Sayisi-->",maxBeyazNoktaSayisi)




if cv2.waitKey(1) & 0xFF == ord('q'):
break
cv2.rectangle(frame, (maxFrameCorners[0],maxFrameCorners[1]), (maxFrameCorners[2],maxFrameCorners[3]), (60, 255, 100), 2)
cv2.imshow('Lazer Takip', frame)
cv2.imshow('Lazer ', blackAndWhiteFrame)




lazer.release()
cv2.destroyAllWindows()


Resim boyutunu kısaltmak için birçok tasarım yapılabileceği gibi farklı tarama yöntemleri de geliştirilebilir. Proje de soldan sağa tarama ve 3 er pixel atlatma metodu geliştirilmiştir. Bu şekilde x pozisyonunda resmin boyutu üçte birine düşmüştür ( 640 / 3 ) ve sistem 3 kat hız almıştır, aynı şekilde y pozisyonunda da 3 er pixel atlama gerçekleştirilmiş ( 480 / 3 ) ve sistem 3 kat daha hızlanarak toplamda 9 kat hız kazanmıştır. Lazer noktasının genişliği 3 pixel in üzerinde olduğu için (kameranın zemine uzaklığı önemlidir) 3 pixellik atlatmalar yapmak sistem de hiçbir probleme neden olmayacaktır. 

Nokta böylelikle hızlı birşekilde saptanır ve konumu belirlenir ancak bazen hassas çalışmamız gerekebilir ve daha çok hıza ihtiyacımız olabilir bu sebeplerden dolayı başka bir tasarıma daha ihtiyaç duyulmuştur. 




Buraya kadar yapılanlar 1, 4, 7, 10, 13. pixel atlama şeklinde oluyordu ancak 2. veya 3. pixeller bağzı durumlarda işe yarayacaktır ve kullanılması gerekiyordur. Sistemin bu duruma cevap verebilmesi için Resim Kesme metoduna gidilmiştir.


Resim Kesme Metodu (MATLAB KULLANANLAR İÇİN)


İstenilen değerdeki nokta saptandıktan sonra döngüden çıkılır ve bulunan nokta etrafı 40X40 pixel boyutunda kesilir kesilme işlemi noktanın konumuna göre farklı haller almaktadır bu konuya daha sonra değineceğim. Sistemin hızı son durumda 192 kat artmıştır. (640*480) / (40*40) = 192 dir. Arama işlemine kesilen nokta içerisinde devam edilir ve bu işlem bir pixel atlayarak gerçekleşir böylelikle tüm değerler elde edilmiş olur, nokta bulunduğunda tekrar başa dönülüp küçük kare içi aranmaya devam edilir. Küçük kare içerisindeki noktanın olmadığına karar verildiğinde döngü sistemden çıkıp resmi baştan taramaya başlar. Bu olay devamlı kendini tekrar eder. Küçük karenin hareket kararının verilmesini sağlayan kodlar aşağıdadır


 
Şekil 8





  if(blackAndWhiteFrame[satır][sutun])>250 and satır>40 and satır<440 :
        xx=satır
        deger=20
    elif (blackAndWhiteFrame[satır][sutun])>250 and satır>0 and satır<20:
        xx=satır 
        deger=20-satır
    elif (blackAndWhiteFrame[satır][sutun])>250  and satır>=20 and satır<40:
        xx=satır 
        deger=40-satır       
    elif (blackAndWhiteFrame[satır][sutun])>250  and (satır>440)and (satır<480):
     aa=satır-440
     xx=480-aa
     deger=20

    if(blackAndWhiteFrame[satır][sutun])>250 and sutun>40 and sutun<600 :
        yy=sutun
        deger=20
    if(blackAndWhiteFrame[satır][sutun])>250 and sutun>40 and sutun<600 and satır>0 and satır<40:
        yy=sutun
        deger=20
    elif (blackAndWhiteFrame[satır][sutun])>250 and sutun>20  and sutun<40:
     yy=sutun 
     deger=40-sutun
    elif (blackAndWhiteFrame[satır][sutun])>250  and (sutun>600)and (sutun<640):
     aa=sutun-600
     yy=640-aa
     deger=20




Şekil 8’de görülen küçük kare tüm resim içerisinde dolaşabilir. Bu tarz bir çözüm sistemi
oldukça hızlandırıyor, küçük kare lazer noktasını ortaya alacak şekilde odaklanır ve lazerin
takip ettiği yolu öğrenerek kayma eylemi gerçekleştirir.


Kayma işlemi her yönde olabilir, sağa sola yukarı aşağı çapraz her yönde ilerleyebilir ta ki
40X40 oranı bozuluncaya kadar. Oranın bozulmasından kastım noktanın 600. pixeli geçmesi
601 ve yukarısında olması ya da 39. pixelde olması ya da birbaşkası artık bu boyutlarda karenin kesilmesine olanak sağlamayacaktır. Bu durumun üstesinden
gelebilmek için yazılım tasarımına ekstra ilaveler yapmak gerekebilir.



Hareketli Çerçeve 


Hareketli nokta takibi başarıyla tamamlandı ve koordinat değerleri alınabildi bunlara ilaveten projeyi biraz görsel hale getirmek için lazer etrafına bir kare çizdirebilir ve bunu hareketlendirebiliriz. Şekil 9 da bir örneği verilmiştir.

 
Şekil 9





Hareketli çerçeve resmin her noktasına ulaşabilir özelliktedir yazılım bu mantıkta çalışır.

Koordinat Noktaları


Hareketli nokta takibi yaparken ekran üzerinde takip noktalarını kontrol edebilmek amacıyla koordinat noktalarını yazmak proje açısından iyi bir detay.Detaylı örnek Şekil 10’da gösterilmiştir.Ekranın sol üst köşe noktalanarının x ve y koordinatlarının 0 olduğunu bilmek gerekir yanı ekranın sol üst köşesi 0,0 noktasıdır.Bunu yazdırmak adına puttext() fonksiyonu yeterli bir araçtır.

 
Şekil 10

    cv2.putText(frame,str(yy),(yy+20,xx+50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2,cv2.LINE_4);
    cv2.putText(frame,",",(yy+80,xx+55),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2,cv2.LINE_8);
    cv2.putText(frame,str(xx),(yy+92,xx+50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2,cv2.LINE_8);



