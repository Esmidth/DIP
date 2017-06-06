## Parameters & Data Structure

- Objects (list)：存储整个平面图像上各个区域（Segment）的信息

  - Seg (list) : 存储构成每个Segment中的各个点
    - Points (list): 存储每个点的坐标 (x,y)
      - 坐标 (int)

- Contents (list): 存储每个Segment所对应的内容 (Conetent) 

  - str

- Seps (list): 由从txt文件中读取的字符串分割而来，奇数内容为Coord，偶数内容为Contents

  - str

- image/img (np.ndarray): 图像

  ​