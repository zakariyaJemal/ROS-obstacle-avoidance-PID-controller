ROS Obstacle Avoidance ve PID Kontrol Projesi


1. Proje Amacı

Bu proje, ROS1 Noetic ortamında çalışan bir mobil robot için geliştirilmiştir. Amaç, robotun sensör verilerini kullanarak engellerden kaçınması ve PID kontrol algoritması ile daha stabil hareket etmesini sağlamaktır.



2. Kullanılan Sistem
ROS1 Noetic
Python 3
TurtleBot3 (simülasyon)
LaserScan sensörü (/scan)


3. Proje Yapısı

Proje iki ana dosyadan oluşmaktadır:

obstacle_avoid.py → Engel algılama ve hareket kontrolü
pid_controller.py → PID kontrol algoritması


4. Çalışma Mantığı

Robot sürekli olarak LiDAR sensöründen veri alır.

Engel Yoksa:

Robot ileri yönde hareket eder.

Engel Varsa:

Robot durur ve yön değiştirerek engelden kaçar.

PID Kontrol:

Robot ile hedef mesafe arasındaki hata hesaplanır ve bu hata kullanılarak daha düzgün yönlendirme sağlanır.



5. ROS Haberleşmesi
Abone Olunan Topic:
/scan
Yayınlanan Topic:
/cmd_vel


6. Çalıştırma Adımları

Terminalde sırasıyla:

ROS başlatılır:
roscore
Simülasyon çalıştırılır:
roslaunch turtlebot3_gazebo turtlebot3_world.launch
Proje çalıştırılır:
rosrun obstacle_avoidance_pid obstacle_avoid.py

7. Sonuç
Bu projede robot, sensör verilerini kullanarak engellerden kaçınabilmekte ve PID kontrol algoritması sayesinde daha stabil hareket etmektedi
