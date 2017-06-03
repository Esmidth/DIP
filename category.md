# Digital Image Processing
### Python Practice with skimage, matplotlib, opencv
| number | practice content | function                                 |
| :----- | :--------------- | :--------------------------------------- |
| 1      | 环境安装与配置          | io.imread()                              |
| 2      | 图像的读取、显示与保存      | io.imshow() & cv2.imread()               |
| 3      | 图像像素的访问与裁剪       | img[:,:,:]                               |
| 4      | 图像数据类型和色彩空间的转换   | color.convert_colorspace(img,'RGB','HSV') |
| 5      | 图像的绘制            | plt.subplot() & plt.imshow()             |
| 6      | 图像的批量处理          | io.ImageCollection()                     |
| 7      | 图像的形变与缩放         | transform.resize() & transform.rescale() & transform.rotate() |
| 8      | 对比度与亮度调整         | exposure.adjust_gamma() & exposure.adjust_log() & exposure.is_low_contrast() & exposure.rescale_intensity() |
| 9      | 直方图绘制与直方图均衡      | np.histogram() & exposure.histogram() & plt.hist() & exposure.equalize_hist() |
| 10     | 图像的简单滤波          | filters.**() & feature.canny()           |
| 11     | 图形的自动阈值分割        | filters.threshold_**()                   |
| 12     | 基本图形绘制           | draw.**() & img[rr,cc] = [:,:,:]         |
| 13     | 基本形态学滤波          | sm.dilation() & sm.erosion() & sm.opening() & sm.closing() & sm.white_tophat() & sm.black_tophat() |
| 14     | 高级滤波             | sfr.autolevel() & sfr.bottomhat() & sfr.enhance_contrast() & sfr.entropy() & sfr.equalize() & str.gradient() |
| 15     | 霍夫线性变换           | st.hough_line() & st.probabilistic_hough_line() |
| 16     | 霍夫圆与椭圆变化         | transform.hough_circle() & transform.hough_ellipse() |
| 17     | 边缘与轮廓            | measure.find_contours() & measure.subdivide_polygon() & measure.approximate_polygon() |
| 18     | 高级形态学处理          | morphology.convex_hull_image() & morphology.convex_hull_object() & mearsure.regionprops() & measure.label() |
| 19     | 骨架提取和分水岭算法       |                                          |
