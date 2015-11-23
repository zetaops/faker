__author__ = 'zekiye'


from .. import BaseProvider

class Provider(BaseProvider):
    classrooms = (
                     'A101', 'A102', 'A103', 'A104', 'A105', 'A106', 'A107', 'A108', 'A109', 'A110',
                     'A201', 'A202', 'A203', 'A204', 'A205', 'A206', 'A207', 'A208', 'A209', 'A210',
                     'A301', 'A302', 'A303', 'A304', 'A305', 'A306', 'A307', 'A308', 'A309', 'A310',
                     'A401', 'A402', 'A403', 'A404', 'A405', 'A406', 'A407', 'A408', 'A409', 'A410',
                     'A501', 'A502', 'A503', 'A504', 'A505', 'A506', 'A507', 'A508', 'A509', 'A510',
                     'M101', 'M102', 'M103', 'M104', 'M105', 'M106', 'M107', 'M108', 'M109', 'M110',
                     'M201', 'M202', 'M203', 'M204', 'M205', 'M206', 'M207', 'M208', 'M209', 'M210',
                     'M301', 'M302', 'M303', '3104', 'M305', 'M306', 'M307', 'M308', 'M309', 'M310',
                     'M401', 'M402', 'M403', 'M404', 'M405', 'M406', 'M407', 'M408', 'M409', 'M410',
                     'M501', 'M502', 'M503', 'M504', 'M505', 'M506', 'M507', 'M508', 'M509', 'M510',
                     'CZ101', 'CZ102', 'CZ103', 'CZ104', 'CZ105', 'CZ106', 'CZ107', 'CZ108' 'C101',
                     'C102', 'C103', 'C104', 'C105', 'C106', 'C107', 'C108', 'C201', 'C202', 'C203',
                     'C204', 'C205', 'C206', 'C207', 'C208', 'C301', 'C302', 'C303', 'C304', 'C305',
                     'C306', 'C307', 'C308', 'C401', 'C402', 'C403', 'C404', 'C405', 'C406', 'C407',
                     'C408', 'C501', 'C502', 'C503', 'C504', 'C505', 'C506', 'C507', 'C508', 'C601',
                     'C602', 'C603', 'C604', 'C605', 'C606', 'C607', 'C608'
                 )

    classroom_types = (

                        'Bilgisayar Laboratuarları', 'CAD Laboratuarları', 'Dikim Atölyesi', 'Elektronik Laboratuarı',
                        'Endüstriyel Tasarım El Aletleri Atölyesi', 'Endüstriyel Tasarım Model Maket Atölyesi',
                        'Fotoğraf Stüdyosu', 'Grafik Tasarım Laboratuarı', 'Kalıp Dikim Atölyesi', 'MAC Laboratuarları',
                        'Mikroişlemci Laboratuarı', 'Moda Tasarım Stüdyosu', 'Mütercim Tercümanlık Laboratuarı',
                        'Psikoloji Laboratuarları','Radyo Stüdyosu', 'Resim Atölyesi', 'Smart Class (Akıllı Sınıf)',
                        'Silent Study Kişisel Erişim Merkezi', 'Video-Audio G Kişisel Erişim Merkezi', 'Self Access Center',
                        'Simülasyon Laboratuarı', 'Tasarım Stüdyoları', 'Tekstil Arşivi', 'Tekstil Baskı Atölyesi'
                      )


    classroom_formats = ('{{bina}} {{kod}}')